import httpx
import asyncio
from bs4 import BeautifulSoup as bs


async def bin_scrape(binov: int):
    url = 'https://binov.net/'
    if len(binov) < 6:
        return {"status": False, "error": "INVALID DATA PROVIDED 6 DIGITS REQUIRED"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url,
                                  data={
                                      'BIN': binov[:6],
                                      'BANK': 1,
                                      'COUNTRY': 1,
                                  })
            soup = bs(r, features='lxml')
            k = soup.find('table', width="900px")

            data = {}
            data["status"] = True
            data["bin"] = binov[:6]
            data["brand"] = k.findAll('td')[7].get_text()
            data["bank"] = k.findAll('td')[8].get_text()
            data["type"] = k.findAll('td')[9].get_text()
            data["level"] = k.findAll('td')[10].get_text()
            data["country"] = k.findAll('td')[11].get_text()
            return data
    except Exception as e:
        return {"status": False, "error": e}
