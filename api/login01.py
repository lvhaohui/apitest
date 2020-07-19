import requests,unittest,logging
#
# = requests.Session()

def login_api(username,password):
      url = "http://192.168.1.160:5000/login"
      data = {"username": username, "password": password}
      headers = {"Content-Type": "application/json"}

      r = requests.post(url, json=data, headers=headers)
      a = r.headers["Set-Cookie"]
      
      return r









