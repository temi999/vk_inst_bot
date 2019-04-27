import requests
import csv
import constants as cs


base_url= f'https://api.vk.com/method/friends.get?access_token={cs.access_token}' \
    f'&user_id={cs.user_id}&fields=connections&v={cs.api_version}'


response = requests.get(base_url,
                        params={
                            'access_token': cs.access_token,
                            'user_id': cs.user_id,
                            'fields': 'connections',
                            'v': cs.api_version
                        })

friends = response.json()['response']['items']
for friend in friends:
    try:
        print(friend['first_name'], friend['last_name'], friend['instagram'])
    except:
        pass
