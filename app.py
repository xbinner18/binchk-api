# import asyncio
# import uvloop
from sanic import Sanic
from sanic.response import json, html
from bindb import bin_scrape

app = Sanic('binchk-app')


INDEX = f'''
    <html>
        <body>
            <h1>BIN CHK API!</h1>
            <h3>Up-to-date Better Then bins.su</h3>
            <h6>©Copyright by <a href="https://t.me/Xbinner69">Nitin</a></h6>
            <h6>Source code: <a href="https://github.com/xbinner18/binchk-api">github.com/Nitin181/binchk-api</a></h6>
        </body>
    </html>
    '''


@app.route('/')
async def wlc_handler(request):
    return html(INDEX)


@app.route('/<query>')
async def index(request, query):
    return json(await bin_scrape(query))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
