import os
import requests
import urllib3
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv
from imgurpython import ImgurClient


urllib3.disable_warnings()


def fetch_image_links_spacex_last_launch():
    get_url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(get_url)
    response.raise_for_status()
    images_links = response.json()['links']['flickr']['original']
    return images_links


def download_images_spacex_last_launch(images_links):
    for image_number, image_link in enumerate(images_links):
        response = requests.get(image_link)
        response.raise_for_status()
        with open(f'{file_path}/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)
        print(f'spacex_{image_number}.jpg')


def get_hubble_images_id():
    payload = {'page': 'all', 'collection_name': 'printshop'}
    response = requests.get(
        'http://hubblesite.org/api/v3/images', params=payload)
    response.raise_for_status()
    image_files_descriptions = response.json()
    images_id = []
    for image in image_files_descriptions:
        images_id.append(image['id'])
    return images_id


def download_hubble_images_link(image_id):
    get_url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(get_url)
    response.raise_for_status()
    image_files_descriptions = response.json()['image_files']
    image_link = image_files_descriptions[-1]['file_url']
    return image_link


def download_hubble_images(file_path, image_link, image_id, image_exten):
    response = requests.get(f'http:{image_link}', verify=False)
    response.raise_for_status()
    with open(f'{file_path}/{image_id}{image_exten}', 'wb') as file:
        file.write(response.content)
        print(f'{image_id}{image_exten}')


def edit_images(file_path, edited_images_path):
    images = os.listdir(file_path)
    for image_number, image in enumerate(images):
        image = Image.open(f'{file_path}/{image}')
        image.thumbnail((1080, 1080))
        image.save(f'{edited_images_path}/{image_number}.jpg', format="JPEG")
        print(f'{image_number}.jpg')


def upload_images(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    upload_images = os.listdir(edited_images_path)
    for image_number, image in enumerate(upload_images):
        with open(f'{edited_images_path}/{image}', "r") as file:
            caption = file.read()
        pic = f'{edited_images_path}/{image}'
        bot.upload_photo(pic, caption=caption)
        print('Upload: ' + image_number)


def get_imgur_token(client_id, client_secret):
    payload = {'client_id': client_id, 'client_secret': client_secret}
    response = requests.post(
        f'https://api.imgur.com/oauth2/token',
        json=payload
    )
    response.raise_for_status()
    response_data = response.json()
    print(response_data)

 #   credentials = client.authorize(
 #       'TOKEN OBTAINED FROM AUTHORIZATION', 'token')
 #   client.set_user_auth(
 #       credentials['access_token'], credentials['refresh_token'])

 #   print("Authentication successful! Here are the details:")
 #   print("   Access token:  {0}".format(credentials['access_token']))
 #   print("   Refresh token: {0}".format(credentials['refresh_token']))

 #   return client


def imgur_images_upload(client_id, client_secret, access_token, refresh_token):
    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('token')


if __name__ == '__main__':
    file_path = 'd:/CODING/DEVMAN/Auto_Instagramm_Post/images'
    edited_images_path = 'd:/CODING/DEVMAN/Auto_Instagramm_Post/edited_images'
    os.makedirs(file_path, exist_ok=True)
    os.makedirs(edited_images_path, exist_ok=True)

#    images_links = fetch_image_links_spacex_last_launch()
#    download_images_spacex_last_launch(images_links)

#    images_id = get_hubble_images_id()
#    for image_id in images_id:
#        image_link = download_hubble_images_link(image_id)
#        name_link, image_exten = os.path.splitext(image_link)
#        download_hubble_images(file_path, image_link, image_id, image_exten)

#    edit_images(file_path, edited_images_path)

    load_dotenv()
#   username = os.getenv('USERNAME')
#   password = os.getenv('PASSWORD')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
 #  upload_images(username, password)
    get_imgur_token(client_id, client_secret)
