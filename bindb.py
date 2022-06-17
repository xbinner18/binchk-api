import httpx
import flag
from bs4 import BeautifulSoup as bs


async def bin_scrape(binov: int):
    url = f'https://bincheck.io/details/{binov}'
    if len(binov) < 6:
        return {"status": False, "error": "INVALID DATA PROVIDED 6 DIGITS REQUIRED"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            soup = bs(r, features='html.parser')
            k = soup.findAll('td', width="65%")

            data = {}
            data["status"] = True
            data["bin"] = binov[:6]
            data["brand"] = k[0].get_text()
            data["type"] = k[1].get_text().strip()
            data["level"] = k[2].get_text().strip()
            data["bank"] = k[3].get_text().strip()
            data["url"] = k[4].get_text().strip()
            data["phone"] = k[5].get_text().strip()
            data["country"] = k[6].get_text().strip()
            data["code"] = k[8].get_text().strip()
            data["flag"] = flag.flag(k[8].get_text())
            data["currency"] = k[10].get_text().strip()
            return data
    except Exception as e:
        return {"status": False, "error": e}
