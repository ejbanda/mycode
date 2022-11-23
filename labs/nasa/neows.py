#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def dateEntry():
    print("Enter a date: ")

    year = input('Enter Year (YYYY):\n>')
    month = input('Enter Month (MM):\n>')
    day = input('Enter Day (DD):\n>')
    dateString = year + "-" + month + "-" + day
    return dateString

def askEnd():
    choice = input("Would you like to enter a end date? (y/n)\n>")
    if choice.lower().strip() == 'n':
        return False
    return True


# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"


    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    #print(neodata)
    print('Custom date range')
    start = dateEntry()
    endStatus = askEnd()
    if endStatus:
        end = dateEntry()
    dateReq = NEOURL + start + '&' + end + '&' + nasacreds
    data = requests.get(dateReq).json()
    print(data)


if __name__ == "__main__":
    main()

