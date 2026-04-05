import requests
import threading
url_target=input("Enter a URL:\n")

#third_level_domains=["mail", "dev", "admin", "test", "api", "staging", "vpn", "portal", "remote", "beta"]
# If you wish to hardcode the list of subdomains and not read from a different file, you should comment out
# the " with open("third-level-domains.txt", "r") as third_lvl_domains: " and then create a list with all the required subdomains.

def scanning(subdomain):
    url = f"https://{subdomain.strip()}.{url_target}"
    try:
        result = requests.get(url, timeout=5, allow_redirects=False)
        if result.status_code == 200 or result.status_code == 403:
            print(f"SERVER FOUND! {url}. Status Code: {result.status_code}")
            with open("Found Servers.txt", "a") as found_servers:
                found_servers.write(f"SERVER FOUND! {url}. Status Code: {result.status_code}\n")
        elif result.status_code == 301 or result.status_code == 302:
            print(f"SERVER FOUND, BUT REDIRECTIONS ARE EXPECTED! {url}. Status Code: {result.status_code}")
    except:
        print(f"[DEAD] {url}.")

with open("third-level-domains.txt", "r") as third_lvl_domains:
    for third_level_dom in third_lvl_domains:
        scan = threading.Thread(target=scanning, args=(third_level_dom.strip(),))
        scan.start()
