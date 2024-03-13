import urllib.request, json, time



while True:
    # some JSON:
    with urllib.request.urlopen("http://127.0.0.1:56781/mavlink/") as url:
        y = json.load(url)
    # parse x:


    # the result is a Python dictionary:
    print(y["GPS_RAW_INT"]["msg"]["lat"] * 0.0000001, y["GPS_RAW_INT"]["msg"]["lon"] * 0.0000001)

    time.sleep (1)
