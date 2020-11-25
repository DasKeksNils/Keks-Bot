import urllib.request


def download(link):
    dw = urllib.request.urlretrieve(url=link, filename="picture.jpg")
    return dw
