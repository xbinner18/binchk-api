from sanic import Sanic
from sanic.response import json, html
from bindb import bin_scrape
from ua import ua_scrape

app = Sanic('binchk-app')


INDEX = '''
    <html>
        <body>
            <h1>BIN CHK API!</h1>
            <h3>Stable bin Database</h3>
            <h3>Example to use: https://binchk-api.vercel.app/bin=510805<h3>
            <h6>©Copyright by <a href="https://t.me/Xbinner69">Nitin</a></h6>
            <h6>Source code: <a href="https://github.com/xbinner18/binchk-api">github.com/Nitin181/binchk-api</a></h6>
        </body>
    </html>
    '''


@app.route('/')
async def index(request):
    return html(INDEX)


@app.route('/bin=<query>')
async def binn(request, query):
    return json(await bin_scrape(query))


@app.route('/ua')
async def rndua(request):
    return json(await ua_scrape())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
