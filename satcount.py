import urllib.request, json



while True:
    # some JSON:
    with urllib.request.urlopen("http://127.0.0.1:56781/mavlink/") as url:
        y = json.load(url)
    # parse x:


    # the result is a Python dictionary:
    print(y["GPS_RAW_INT"]["msg"]["satellites_visible"])
