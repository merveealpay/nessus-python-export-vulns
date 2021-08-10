import requests
import subprocess

def nessus_request():
    access_key =
    secret_key =
    header = {"X-ApiKeys": "accessKey={}; secretKey={}".format(access_key, secret_key)}
    url = "https://127.0.0.1:8834/scans"
    result = requests.get(url=url, headers=header, verify=False)
    data = result.json()
    for i in data["scans"]:
        scan_id = i["id"]
        url = url + "/" + str(i["id"])
        result = requests.get(url=url, headers=header, verify=False)
        for i in result.json()["hosts"]:
            try:
                IP = i['hostname']
                host_id = i['host_id']
                print(IP)
                print(host_id)
                print("================")
                url = url + "/hosts/" + str(host_id) + "/plugins/11936"
                vuln = requests.get(url=url, headers=header, verify=False)
                plugin_output = vuln.json()['outputs'][0]['plugin_output']
                print(plugin_output)
                if "Windows" in plugin_output:
                    output = str(IP) +"\n"
                    file = open("windows.txt", "w")
                    file.write(output)
                    file.close()

                file = open("windows.txt", "r")
                ip_list = file.read()
                file.close()

                if not str(IP) in ip_list:
                    data = str(IP) + "\n"
                    file = open("windows.txt", "a")
                    file.write(data)
                    file.close()


            except:
                pass



nessus_request()
