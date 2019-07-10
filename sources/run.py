from sources.pull import Pull

newPull = Pull()
newPull.getHtml()
newPull.parseForOld()
newPull.fillCars()
newPull.checkForNew()
newPull.saveCars()
print(newPull.getNewCars())