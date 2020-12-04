import os
import requests
from MainPy import settings
from MainPy.settings import PROXY_URL
from OrmMongodbRepository import OrmRepository

""" This class is for handle extra methods for other classes """


class Tools:

    # download file from url net
    @staticmethod
    def download_file(url):
        print(url)
        if url == 'None':
            return bytes('null'.encode())
        elif url == "null":
            return bytes('null'.encode())
        else:
            proxy_dict = {
                "http": "http://" + PROXY_URL,
                "https": "https://" + PROXY_URL,
            }
            img = requests.get(url, proxies=proxy_dict, verify=False)
            return img.content


    # save file on drive with get bytes and address
    @staticmethod
    def save_file(bytes, media_address):
        if media_address is not None:
            file_name = media_address.split('/')[-1].split('.')[0]
            file_ext = '.' + media_address.split('.')[-1]
            write_file = open(os.path.join(settings.BASE_DIR, "tweeter_crawler" + "\\" + file_name + file_ext), 'wb')
            write_file.write(bytes)
            write_file.close()

    # find from mongodb and save bytes with using of method save_file and save as images
    @staticmethod
    def save_images(key, value):
        for image in OrmRepository.OrmRepository.find(key, value):
            Tools.save_file(image.binary_file, image.media)
            print("image save shod!!!!!!!")
        return {"state": "save shod!!!"}
