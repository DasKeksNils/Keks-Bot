import urllib.request


def download(link):
    dw = urllib.request.urlretrieve(link, "picture.jpg")
    return dw
