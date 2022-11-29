#!/usr/bin/python3

import requests

url = "http://localhost:2224/"
def main():
    count = 0
    while True:
        res = requests.get(f"{url}fast")
        if res.status_code == 200:
            count += 1
            print("The count is " + str(count))

if __name__ == "__main__":
    main()

