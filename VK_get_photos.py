from pprint import pprint
import requests


class MyVk:
    def __init__(self):
        with open("VK_token", encoding="UTF-8") as token:
            self.token = token.readline().strip()
        self.root_url = "https://api.vk.com/method/"
        self.vers = "5.131"
        self.json_main = []
        self._get_photos_urls()

    def _get_photos_urls(self):
        user = "64810636"
        url = self.root_url + "photos.get"
        params = {"access_token": self.token,
                  "v": self.vers,
                  "owner_id": f"{user}",
                  "album_id": "profile",
                  "rev": 1,
                  "count": 5,
                  "extended": 1
                  }
        request = requests.get(url=url, params=params)
        # pprint(request.json())
        for i in range(len(request.json()['response']['items'])):
            name_file = str(request.json()['response']['items'][i]['likes']['count']) + ".jpeg"
            url_photo = request.json()['response']['items'][i]['sizes'][-1]['url']
            size_photo = request.json()['response']['items'][i]['sizes'][-1]['type']
            for j in self.json_main:
                if j['file_name'] == name_file:
                    name_file = name_file[0:len(name_file) - 5] + " " + str(
                        request.json()['response']['items'][i]['date']) + ".jpeg"
            self.json_main.append({"file_name": name_file, "size": size_photo, "url": url_photo})
        return self.json_main

