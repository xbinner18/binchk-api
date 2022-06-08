import httpx
import re
from bs4 import BeautifulSoup as bs


async def bin_scrape(binovt):
    url = 'https://binov.net/'
    x = re.sub(r'[^0-9]', '', binovt)
    if len(x) < 6:
        return {"status": False, "error": "INVALID DATA PROVIDED 6 DIGITS REQUIRED"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url,
                                  data={
                                      'BIN': x[:6],
                                      'BANK': 1,
                                      'COUNTRY': 1,
                                  })
            soup = bs(r, features='lxml')
            k = soup.find('table', width="900px")

            data = {}
            data["status"] = True
            data["bin"] = x[:6]
            data["brand"] = k.findAll('td')[7].get_text()
            data["bank"] = k.findAll('td')[8].get_text()
            data["type"] = k.findAll('td')[9].get_text()
            data["level"] = k.findAll('td')[10].get_text()
            data["country"] = k.findAll('td')[11].get_text()
            return data
    except Exception as e:
        return {"status": False, "error": e}
