import urllib.request, json, time, simplekml



while True:
    # some JSON:
    with urllib.request.urlopen("http://127.0.0.1:56781/mavlink/") as url:
        y = json.load(url)
    # parse x:




    kml = simplekml.Kml()
    pnt = kml.newpoint(name="Aircraft", description="Generic aircraft",
                    coords=[(y["GPS_RAW_INT"]["msg"]["lon"] * 0.0000001, y["GPS_RAW_INT"]["msg"]["lat"] * 0.0000001, y["GPS_RAW_INT"]["msg"]["alt"] * 0.001) ])  # lon, lat optional height
    pnt.altitudemode = simplekml.AltitudeMode.relativetoground

    kml.save("pyout.kml")




    time.sleep (1)











 



