def keyboardInput(caption, datatype, errormessage, defaultvalue=None):
    value = None
    isErrorInput = True
    while (isErrorInput):
        try:
            value = input(caption)
            if (defaultvalue == None):
                value = datatype(value)
            else:
                if (value == ""):
                    value = defaultvalue
                else:
                    value = datatype(value)
        except:
            print(errormessage)
        else:
            isErrorInput = False
    return value

if __name__ == '__main__':
    principle = keyboardInput("Principle Amount: ", int, "Principle Amount must be Integer")
    period = keyboardInput("Period in Years: ", int, "Period must be Integer")
    rate = keyboardInput("Rate in Percentage: ", float, "Rate must be float")
    interest = (principle * period * rate) / 100
    print("Interest Amount:", interest)