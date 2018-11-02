import requests 
  
# api-endpoint 
URL = "https://api.github.com/users/biyichen/repos"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
  
for element in data:
 print("Name:%s" %(element['name']))
