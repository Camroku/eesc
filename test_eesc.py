from eesc import *

addEasterEgg("1000", "-", "7", "Oshiete")
# English, default.
runCalc()
print("")
# Turkish.
runCalc("tr")
print("")
# English, but not default.
runCalc("en")