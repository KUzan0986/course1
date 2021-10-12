import requests
import VK_get_photos
from pprint import pprint

class YaUploader:
    def __init__(self):
        with open("YA_disk_token", encoding="UTF-8") as token:
            self.token = token.readline().strip()

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def ya_upload(self, json_vk):  # метод через post

        ya_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._get_headers()
        #self.chek_path(path)
        count = 0
        for i in json_vk:
            count += 1
            print(f"загружаем {count} из {len(json_vk)}")
            params = {
                "path": f"/test/{i['file_name']}",
                "url": i["url"]
            }
            result = requests.post(url=ya_url, headers=headers, params=params)

    def chek_path(self, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self._get_headers()
        params = {
            "path": f"/{path}"
        }
        result = requests.put(url=url, headers=headers, params=params)
        result.raise_for_status()


vk_loader = VK_get_photos.MyVk()
ya_uploader = YaUploader()
ya_uploader.ya_upload(vk_loader.json_main)