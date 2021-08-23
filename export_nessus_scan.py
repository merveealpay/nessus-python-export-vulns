import requests
import os
from dotenv import load_dotenv
from typing import List, Dict, Any
from urllib.parse import urljoin

load_dotenv()

access_key = os.environ.get("ACCESS_KEY")
secret_key = os.environ.get("SECRET_KEY")
scan_url = os.environ.get("SCAN_URL", default="https://127.0.0.1:8834/scans")


def send(url: str, method: str = "GET", verify: bool = False) -> Dict[str, Any]:
    header = {"X-ApiKeys": f"accessKey={access_key}; secretKey={secret_key}"}
    response = requests.request(method, url=url, headers=header, verify=verify)
    if not response.ok:
        return {}
    return response.json()


def get_vulns() -> None:
    """Get Vulnerabilities.

    scans: list of nessus scan ids
        example [{"id": 1}]

    vulnerabilities: vulnerability list of scan id
    example [{"vuln_name"..}]

    """

    vuln_list = []

    result = send(scan_url)
    if not result:
        return

    scans: List[Dict[str, int]] = result.get("scans", [])

    for scan in scans:
        scan_detail_url = urljoin(scan_url, str(scan["id"]))
        scan_detail_result = send(url=scan_detail_url)

        if not scan_detail_result:
            continue

        vulnerabilities: List[Dict[str, Any]] = scan_detail_result.get("vulnerabilities", [])

        vuln_list.extend(vulnerabilities)

    for vuln in vuln_list:
        print(f'vuln_name: {vuln["plugin_name"]} ----- severity: {vuln["severity"]}')