#coding=utf-8
import requests
import webbrowser

#data = {'firstname': '莫烦', 'lastname': 's'}
#r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=data)
#print(r.text)

#login in
#payload = {'username': 'Morvan', 'password': 'password'}
#r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
#print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


#r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
#print(r.text)

# Hey Morvan! Looks like you're still logged into the site!

#payload = {'username': 'Morvan', 'password': 'password'}
#r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
#print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


#r = requests.get('http://pythonscraping.com/pages/cookies/welcome.php', cookies=r.cookies)
#print(r.text)

session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


#r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
#print(r.text)