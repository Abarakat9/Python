# This program will display the heat index given a temperature and
# relative humidity.
# @Ahmad Barakat

def main():
    T_MIN = 80
    T_MAX = 110
    RH_MIN = 40
    RH_MAX = 100

    # initiate value
    T = T_MIN - 1
    while T < T_MIN or T > T_MAX:
        T = int(input(F"Fahrenheit Temperature ({T_MIN} - {T_MAX}): "))
    
    RH = RH_MIN - 1
    while RH < RH_MIN or RH > RH_MAX:
        RH = int(input(F"Relative Humidity ({RH_MIN} - {RH_MAX}): "))
    
    # Calc Heat Index if both T and RH are valid
    HI = getHeatIndex(T, RH)
    print(f"\nHeat Index: {HI} degrees")


# getHeatIndex takes temperature and relative humidity into the heat index
# formula to calculate the perceived temperature.
# @param T: temperature in Fahrenheit.
# @param RH: relative humidity.
# @return Heat Index is rounded to 1 decimal place.
def getHeatIndex(T, RH):
    
    # Heat index formula
    HI = (-42.379 + 2.04901523*T + 10.14333127*RH
        - .22475541*T*RH - .00683783*T*T
        - .05481717*RH*RH + .00122874*T*T*RH
        + .00085282*T*RH*RH - .00000199*T*T*RH*RH)

    # round to one decimal place
    return round(HI, 1)

main()