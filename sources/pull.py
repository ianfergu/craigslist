from urllib import request


class Pull:
    def __init__(self):
        self.areNew = False
        self.mystr = ""
        self.cars = {}


    def getHtml(self):
        try:
            url = request.urlopen("https://raleigh.craigslist.org/search/cto?search_distance=100&postal=27516&max_price=4000&auto_transmission=1")
            mybytes = url.read()

            self.mystr = str(mybytes.decode("utf8"))
            url.close()

            storedToCompare = open("stored", "wb")
            storedToCompare.write(mybytes)
            storedToCompare.close()
        except Exception:
            print("failed to read url")

    def parseForOld(self):
        outText = open("out", "w")
        inText = open("stored", "r")
        d = inText.readline()
        count = 0
        while (count < 1212):
            d = inText.readline()
            count += 1
        while (d != ""):
            if d.find("http") != -1:
                almostUrl = d
                d = inText.readline()
                while (d.find("price") == -1):
                    d =inText.readline()
                price = d
                outText.write(almostUrl)
                outText.write(price)
            d = inText.readline()
        outText.close()
        inText.close()

    def fillCars(self):
        price = 0
        title = ""
        time = ""
        link = ""

        outText = open("out", "r")
        d = outText.readline()
        while (d != ""):
            d.find("href=")




