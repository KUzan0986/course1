import requests
from pprint import pprint


class YaUploader:
    def __init__(self, path="test"):
        with open("YA_disk_token", encoding="UTF-8") as token:
            self.token = token.readline().strip()
        self.path = path

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def ya_upload(self, json_vk):  # метод через post

        ya_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._get_headers()
        self._chek_path(self.path)
        count = 0
        for i in json_vk:
            count += 1
            print(f"загружаем {count} из {len(json_vk)}")
            params = {
                "path": f"/{self.path}/{i['file_name']}",
                "url": i["url"]
            }
            print("выполняю запрос")

            result = requests.post(url=ya_url, headers=headers, params=params)
            print("результат запроса", result, "\n")

    def _chek_path(self, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self._get_headers()
        slitter = path.split("/")
        count = 0
        for i in slitter:
            count += 1
            stri = ""
            for j in range(count):
                stri = stri + slitter[j] + "/"
            stri = stri[0:len(stri)-1]
            params = {
                "path": f"/{stri}"
            }
            result = requests.put(url=url, headers=headers, params=params)
            pprint(result.json())
