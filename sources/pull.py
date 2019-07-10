from urllib import request
import ast


class Pull:
    def __init__(self):
        self.areNew = False
        self.mystr = ""
        self.cars = []


    def getHtml(self):
        """Writes craiglist html to file named stored.
        """
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
        """Parses through the HTML from stored and
        turns it into the needed data. Data stored in out.
        """
        outText = open("out", "w")
        inText = open("stored", "r")
        d = inText.readline()
        count = 0
        while (count < 1212):
            d = inText.readline()
            count += 1
        while (d != "" and d.find("search-legend bottom") == -1):
            if d.find("http") != -1:
                almostUrl = d
                d = inText.readline()
                price = d
                outText.write(almostUrl)
                outText.write(price)
            if d.find("time class") != -1:
                time = d
                outText.write(time)
            d = inText.readline()
        outText.close()
        inText.close()

    def fillCars(self):
        """Takes the data from out and puts
        it into self.cars, a list of all current
        cars for sale.
        """
        price = 0
        title = ""
        link = ""
        time = ""

        outText = open("out", "r")
        d = outText.readline()
        while (d != ""):
            link = d[d.find('href="')+6: d.rfind('" class')]
            d = outText.readline()
            price = d[d.find('price">')+7: d.find("</")]
            d = outText.readline()
            time = d[d.find('title="')+7:d.rfind('"')]
            d = outText.readline()
            title = d[d.find('hdrlnk">')+8: d.rfind("</")]
            self.cars.append([title, price, time, link])
            d = outText.readline()
            d = outText.readline()
        outText.close()



    def saveCars(self):
        """"Writes the self.cars to a file called oldDic.
        """
        oldDic = open("oldDic", "r+")
        for x in self.cars:
            oldDic.write(str(x) + "\n")

        oldDic.close()


    def checkForNew(self):
        """Compares oldDic to self.cars to identify
        new advertisements, created since the last compile.
        """
        oldDic = open("oldDic", "r+")
        newCars = open("newCars", "w")
        newCars.truncate()
        oldCars = []

        d = oldDic.readline()

        while d != "":
            try:
                d = d[0:d.find("\n")]
                d = ast.literal_eval(d)
                oldCars.append(d)
                d = oldDic.readline()
            except Exception:
                d = oldDic.readline()

        size = len(oldCars)

        self.cars = self.cars[:(size-len(self.cars))]
        if len(self.cars) == 0:
            self.areNew = False
        else:
            self.areNew = True

        newCars.write(str(self.cars))
        newCars.close()
        oldDic.close()

    def getNewCars(self):
        """"returns the new car list.
        """
        if self.areNew:
            return self.cars
        else:
            return "No new cars, sorry!"

    def getAreNew(self):
        """returns bool areNew.
        """
        return self.areNew













