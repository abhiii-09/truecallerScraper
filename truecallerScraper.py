import requests
import json
import csv

data_file = open("data.txt", "a+", encoding="utf-8")
# json_file = open("jsonData.json", "w")

with open("numbers.csv", encoding="utf-8-sig") as csv_file:
  csv_reader = csv.reader(csv_file)

  for row in csv_reader:
        number = row

        # def dataExtractor(start, end):
        url = f"https://search5-noneu.truecaller.com/search?countryCode=in&q={number[0]}"
        payload={}
        headers = {
          'authority': 'search5-noneu.truecaller.com',
          'accept': 'gzip',
          'authorization': 'Bearer a1i0v--UA5Axz-BF7c9PPA4OIyfZRu0ZAStNW8PRLXOXO6HJQfq5fHK3I61pvB_8',
          'user-agent': 'Truecaller/11.76.6 (Android;9)',
          'sec-gpc': '1',
          'origin': 'https://www.truecaller.com',
          'sec-fetch-site': 'same-site',
          'sec-fetch-mode': 'cors',
          'sec-fetch-dest': 'empty',
          'referer': 'https://www.truecaller.com/',
          'accept-language': 'en-US,en;q=0.9'

        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        if(len(json.loads(response.text))):
          name = data["name"]
          phone = data["phones"][0]["e164"]
          address = data["addresses"][0]["address"]
          email = data["email"]["email"]
          data_file.write("\n")
          data_file.write("Name: ")
          data_file.write(name)
          data_file.write("\n")
          data_file.write("Phone: ")
          data_file.write(phone)
          data_file.write("\n")
          data_file.write("Address: ")
          data_file.write(address)
          data_file.write("\n")
          data_file.write("Email: ")
          data_file.write(email)
          data_file.write("\n")
          print("Name: ", name)
          print("Phone: ", phone)
          print("Address: ", address)
          print("Email: ", email)
          print("\n")
          # json.dump(data[0], json_file, indent=4)

