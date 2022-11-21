# binchk-api
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fxbinner18%2Fbinchk-api)

# Note:
## If not running on vercel please upgrade sanic to latest version.

# Usage:
https://binchk-api.vercel.app/bin={6digitbin}
response example below
success
`{'status': True, 'bin': '403833', 'type': 'VISA_CORPORATE_DEBIT', 'bank': 'GREEN DOT BANK DBA BONNEVILLE BANK', 'scheme': 'Visa Debit Com', 'country': 'United States', 'code': 'US', 'flag': '🇺🇸'}`

failure
`{"status":false,"e":"error reason"}`

https://binchk-api.vercel.app/ua to get a rnd firefox android 10-12 useragent with latest browser build.
https://binchk-api.vercel.app/rnd to get rnd us person data..
