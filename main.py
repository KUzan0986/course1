import VK_get_photos
import YA_disk_loader


def get_number(none_allowd = False):
    while True:
        try:
            stri = int(input("введите запрашиваемое число"))
        except ValueError:
            if none_allowd:
                return None
            print("вы ввели не число")
        else:
            return stri


def main():
    print("введите ID пользователя или оставьте поле пустым")
    user_ID = get_number(none_allowd=True)
    path = input("введите название папки, куда сохранить")
    print("введите количество фотографий")
    count = get_number()
    vk_photos = VK_get_photos.MyVk(count=count, user=user_ID)
    ya_upload = YA_disk_loader.YaUploader(path=path)
    ya_upload.ya_upload(vk_photos.json_main)
    input()


main()
