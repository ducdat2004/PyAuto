import requests
headers = {
    "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE2OTMxODEyMTgsImV4cCI6MTcyNDcxNzIxOCwibmJmIjoxNjkzMTgxMjE4LCJqdGkiOiJ0M09zQVFnVmdMU0tNWjFTIiwic3ViIjo5NjkzNSwicHJ2IjoiYjkxMjc5OTc4ZjExYWE3YmM1NjcwNDg3ZmZmMDFlMjI4MjUzZmU0OCJ9.iMp7lBVI4SecDuY3KfPDVrWxn1-CyofFjJ2wie87Z88",
    "Content-Type" : "application/json;charset=utf-8",
    'authority': 'gateway.golike.net',
    'method': 'GET',
    'path': '/api/tiktok-account',
    'scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://app.golike.net',
    'Referer': 'https://app.golike.net/',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'T': 'VFZSWk5VMTZSVFJOVkdONlRXYzlQUT09'
}
params = {
    'account_id' : '428157',
    'ads_id': '786358',
    'async': 'true',
    'data': 'null'
}
d = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, params=params)
print(d.json())