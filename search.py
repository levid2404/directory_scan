import requests

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'


def dirhunt(url, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            directory = line.strip()
            full_url = url + '/' + directory
            response = requests.get(full_url)
            if response.status_code == 200:
                print(GREEN + f"Found directory: {full_url}" + RESET)
            if response.status_code == 404:
                print(RED + f"{full_url} Not found" + RESET)

hostname = input("Enter Host Domain (incuding https://):")
wordlist = input("Enter wordlist:  ")
dirhunt(hostname, wordlist)