import requests

def nessus_request():
    access_key =
    secret_key =
    header = {"X-ApiKeys": "accessKey={}; secretKey={}".format(access_key, secret_key)}
    url = "https://127.0.0.1:8834/scans"
    result = requests.get(url=url, headers=header, verify=False)
    data = result.json()
    for i in data["scans"]:
        url = url + "/" + str(i["id"])
        result = requests.get(url=url, headers=header, verify=False)
        print(result.json())

nessus_request()
