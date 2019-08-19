# curl https://api.robinhood.com/challenge/053dc3f1-661f-40fe-9d40-667dc3f25ed9/respond/ -H "Content-Type: application/json" -d  '{"response":"467910"}'
# https://github.com/Jamonek/Robinhood
# https://github.com/Jamonek/Robinhood/issues/176


# This one works for getting challenge
# curl -v https://api.robinhood.com/oauth2/token/  -H "Content-Type: application/json" -d '{"password": {password}, "username": {username}, "grant_type": "password", "client_id": "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS", "expires_in": "86400", "scope": "internal", "device_token": "29106c90-e38d-42e5-9dee-2ac86c46656f", "challenge_type": "sms"}'