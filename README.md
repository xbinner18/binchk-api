# binchk-api
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fxbinner18%2Fbinchk-api)

# Note:
## If not running on vercel please upgrade sanic to latest version.

# Usage:
https://binchk-api.vercel.app/bin={6digitbin}
response example below
success
`{"status":true,"bin":"510805","brand":"MASTERCARD","type":"DEBIT","level":"STANDARD","bank":"CAPITAL ONE BANK (USA), N.A.","url":"------","phone":"800-955-7070","country":"UNITED STATES","code":"US","flag":"\ud83c\uddfa\ud83c\uddf8","currency":"USD"}`

failure
`{"status":false,"e":"error reason"}`

https://binchk-api.vercel.app/ua to get a rnd firefox android 10-12 useragent with latest browser build...
