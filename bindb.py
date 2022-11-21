import httpx
import flag
import asyncio
import random
import re
import pycountry


def gen(first_6: int, mm: int=None, yy: int=None, cvv: int=None):
    BIN = 15-len(str(first_6))
    card_no = [int(i) for i in str(first_6)]  # To find the checksum digit on
    card_num = [int(i) for i in str(first_6)]  # Actual account number
    seventh_15 = random.sample(range(BIN), BIN)  # Acc no (9 digits)
    for i in seventh_15:
        card_no.append(i)
        card_num.append(i)
    for t in range(0, 15, 2): 
        # odd position digits
        card_no[t] = card_no[t] * 2
    for i in range(len(card_no)):
        if card_no[i] > 9:  # deduct 9 from numbers greater than 9
            card_no[i] -= 9
    s = sum(card_no)
    mod = s % 10
    check_sum = 0 if mod == 0 else (10 - mod)
    card_num.append(check_sum)
    card_num = [str(i) for i in card_num]
    cc = ''.join(card_num)
    if mm is None:
        mm = random.randint(1, 12)
    if len(str(mm)) < 2:
        mm = f'0{mm}'
    else:
        mm = mm
    if yy is None:
        yy = random.randint(2023, 2028)
    else:
        yy = yy
    if cvv is None:
        cvv = random.randint(000, 999)
    if len(str(cvv)) <= 2:
        cvv = 999
    else:
        cvv = cvv
    return f'{cc}|{mm}|{yy}|{cvv}'


async def bin_scrape(binov: int):
    CC = gen(binov[:6])
    CCN, M, Y, CVV = CC.split('|')
    url = f'https://api.worldpay.com/v1/tokens'
    try:
        headers = {"user-agent": "Mozilla/5.0 (Linux; Android 10; vivo 1806) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                   "accept": "application/json",
                   "content-type": "application/json",
                   "accept-language": "en-US,en;q=0.9"
                   }
        payload = {
            "paymentMethod": {
                "name": "Nikhil Rai",
                "cardNumber": CCN,
                "expiryMonth": M[1:],
                "expiryYear": Y,
                "cvc": CVV,
                "type": "Card",
                "issueNumber": 1
            },
            "clientKey": "L_C_9d85db71-21f3-46e0-9a25-9cbc3b68466d"
        }
        async with httpx.AsyncClient(headers=headers) as client:
            r = await client.post(url, json=payload)
            
            code = re.search(r'"countryCode":"([^"]+)', r.text)[1]
            Type = re.search(r'"cardType":"([^"]+)', r.text)[1]
            issuer = re.search(r'"cardIssuer":"([^"]+)', r.text)[1]
            prepaid = re.search(r'"prepaid":([^}]+)', r.text)[1]
            scheme = re.search(r'"cardProductTypeDescNonContactless":"([^"]+)', r.text)[1]
            country = pycountry.countries.get(alpha_2=code)
            
            data = {}
            data["status"] = True
            data["bin"] = binov[:6]
            data["type"] = Type
            data["bank"] = issuer
            data["scheme"] = scheme
            data["country"] = country.name
            data["code"] = code
            data["flag"] = flag.flag(code)

            return data
    except Exception as e:
        return {"status": False, "error": e}
