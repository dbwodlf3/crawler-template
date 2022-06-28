import requests
# curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/20"
# curl "https://api.twitter.com/2/users/by/username/$USERNAME" -H "Authorization: Bearer $ACCESS_TOKEN"

def getCurl(url, headers=None):
    return requests.get(url=url, headers=headers)
    