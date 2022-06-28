import requests
# curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/20"
# curl "https://api.twitter.com/2/users/by/username/$USERNAME" -H "Authorization: Bearer $ACCESS_TOKEN"

def getTwitById(bearerToken, id):
    headers = {
        "Authorization": "Bearer {}".format(bearerToken)
    }

    return requests.get(url="https://api.twitter.com/2/tweets/{}".format(id), headers=headers)