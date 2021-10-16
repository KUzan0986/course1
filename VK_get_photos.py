import requests
import json
import copy


class MyVk:
    def __init__(self, count=1, user=None):
        with open("VK_token", encoding="UTF-8") as token:
            self.token = token.readline().strip()
        self.root_url = "https://api.vk.com/method/"
        self.user = user
        self.vers = "5.131"
        self.json_main = []
        self.count = count
        self._get_photos_urls()
        self._save_json()

    def _get_photos_urls(self):
        if not self.user:
            user = "64810636"
        else:
            user = self.user
        url = self.root_url + "photos.get"
        params = {"access_token": self.token,
                  "v": self.vers,
                  "owner_id": f"{user}",
                  "album_id": "profile",
                  "rev": 1,
                  "count": self.count,
                  "extended": 1
                  }
        request = requests.get(url=url, params=params)
        # pprint(request.json())
        items = request.json()['response']['items']
        for photo in items:
            name_file = str(photo['likes']['count']) + ".jpeg"
            url_photo = photo['sizes'][-1]['url']
            size_photo = photo['sizes'][-1]['type']
            for j in self.json_main:
                if j['file_name'] == name_file:
                    name_file = name_file[0:len(name_file) - 5] + " " + str(photo['date']) + ".jpeg"
            self.json_main.append({"file_name": name_file, "size": size_photo, "url": url_photo})
        return self.json_main

    def _save_json(self):
        json_save = copy.deepcopy(self.json_main)
        for i in json_save:
            del i["url"]
        with open("result_json.json", "w") as file:
            json.dump(json_save, file, indent=4)
