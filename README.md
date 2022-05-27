# binchk-api
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fxbinner18%2Fbinchk-api)

# Note:
## If not running on vercel please upgrade sanic to latest version.

# Usage:
https://binchk-api.vercel.app/{6digitbin}
response example below
success
`{"status":true,"bin":"510805","brand":"MASTERCARD","bank":"CAPITAL ONE BANK (USA), NATIONAL ASSOCIATION","type":"DEBIT","level":"ENHANCED","country":"UNITED STATES"}`

failure
`{"status":false,"e":"error reason"}`
