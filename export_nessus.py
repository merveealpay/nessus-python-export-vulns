import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_vulns():
    access_key = os.environ.get('access_key')
    secret_key = os.environ.get('secret_key')
    header = {"X-ApiKeys": "accessKey={}; secretKey={}".format(access_key, secret_key)}
    url = "https://127.0.0.1:8834/scans"
    result = requests.get(url=url, headers=header, verify=False)
    data = result.json()
    for scan in data["scans"]:
        url = url + "/" + str(scan["id"])
        scan_result = requests.get(url=url, headers=header, verify=False)
        vuln_list = scan_result.json()['vulnerabilities']

    for vuln in vuln_list:
        print("vuln_name: " + vuln['plugin_name'] + " ----- severity: " + str(vuln['severity']))


get_vulns()
