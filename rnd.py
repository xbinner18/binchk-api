import httpx
from bs4 import BeautifulSoup as bs


async def rnd_scrape():
    url = 'https://fakepersongenerator.com/Index/generate'
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            soup = bs(r, features='html.parser')
            k = soup.findAll('b')
            m = k[0].get_text()
            f = m.split()[0]
            l = m.split()[2]
            add = k[6].get_text().split(',')

            data = {}
            data["status"] = True
            data["first"] = f
            data["last"] = l
            data["gender"] = k[1].get_text()
            data["race"] = k[2].get_text()
            data["dob"] = k[3].get_text()
            data["age"] = k[4].get_text()
            data["street"] = k[5].get_text()
            data["city"] = add[0]
            data["state"] = add[1][:-4].strip()
            data["st"] = add[1][-4:][1:3]
            data["zip"] = add[2].strip()
            data["phone"] = k[8].get_text()
            data["country"] = 'United States'
            data["code"] = 'US'
            return data
    except Exception as e:
        return {"status": False, "error": e}
