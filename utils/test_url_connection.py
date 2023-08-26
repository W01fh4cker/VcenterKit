import requests
import urllib3
urllib3.disable_warnings()

def test_url_connection(url):
    try:
        requests.get(url, verify=False, allow_redirects=False)
        return 1
    except Exception as e:
        return 0