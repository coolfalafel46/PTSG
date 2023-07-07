import requests
a=requests.get("https://gist.githubusercontent.com/FexinShifter/821845203c24ad3d6d527471e5b4a9e7/raw/fcee0d0c84736a67031ee9664d48a41573225a4d/101%2525",stream=True)



file=open("101.ini","wb")
file.write(a.content)
file.close()