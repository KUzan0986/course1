from pprint import pprint
import requests

class MyVk:
    def __init__(self):
        with open("VK_token", encoding="UTF-8") as token:
            self.token = token.readline().strip()
        self.root_url = "https://api.vk.com/method/"
        self.vers = "5.131"

    def get_photos(self):
        url = self.root_url + "photos.get"
        params = {"access_token": self.token,
                  "v": self.vers,
                  "owner_id": "64810636",
                  "album_id": "profile",
                  "rev": 1,
                  "count": 2
                  }
        request = requests.get(url=url, params=params)

        for i in range(len(request.json()['response']['items'])):
            url_to_get = request.json()['response']['items'][i]['sizes'][-1]['url']
            img_data = requests.get(url_to_get).content
            print(url_to_get)


        # #pprint(request.json()['response']['items'][i]['sizes'][-1]['url'])

        #print(len(request.json()['response']['items']))


getter_VK = MyVk()
getter_VK.get_photos()