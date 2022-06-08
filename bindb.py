import httpx
from bs4 import BeautifulSoup as bs


async def bin_scrape(binovt):
    url = 'https://binov.net/'
    if len(binovt) < 6:
        return {"status": False, "error": "INVALID DATA PROVIDED 6 DIGITS REQUIRED"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(url,
                                  data={
                                      'BIN': binovt[:6],
                                      'BANK': 1,
                                      'COUNTRY': 1,
                                  })
            soup = bs(r, features='lxml')
            k = soup.find('table', width="900px")
            al = k.findAll('td')

            data = {}
            data["status"] = True
            data["bin"] = binovt[:6]
            data["brand"] = al[7].get_text()
            data["bank"] = al[8].get_text()
            data["type"] = al[9].get_text()
            data["level"] = al[10].get_text()
            data["country"] = al[11].get_text()
            return data
    except Exception as e:
        return {"status": False, "error": e}
