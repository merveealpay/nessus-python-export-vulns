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
        vuln_list = result.json()['vulnerabilities']

    for item in vuln_list:
        print("vuln_name: " + item['plugin_name'] + " ----- severity: " + str(item['severity']))

    for i in result.json()["hosts"]:
        try:
            IP = i['hostname']
            host_id = i['host_id']
            print("================")
            url = url + "/hosts/" + str(host_id) + "/plugins/11936"
            vuln = requests.get(url=url, headers=header, verify=False)
            plugin_output = vuln.json()['outputs'][0]['plugin_output']
            os = plugin_output.split('\n')
            print(os[1] + " ---------- host: " + IP)

        except:
            pass


nessus_request()

