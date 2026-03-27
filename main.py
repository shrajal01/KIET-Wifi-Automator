import requests
import time


LOGIN_URL = "http://172.16.16.16:8090/login.xml" 
EMAIL_ID = "enter your username"
PASSWORD = "enter the password"

def kiet_wifi_login():
    
    payload = {
        "mode": "191",
        "username": EMAIL_ID,
        "password": PASSWORD,
        "a": int(time.time() * 1000), 
        "productname": "Sophos"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    print(f"[*] Attempting login for: {EMAIL_ID}")
    
    try:
        
        response = requests.post(LOGIN_URL, data=payload, headers=headers, timeout=10)
        
        
        if response.status_code == 200:
            if "status=\"live\"" in response.text.lower() or "successful" in response.text.lower():
                print("[\u2705] LOGIN SUCCESSFUL! Internet enjoy karo.")
            else:
                print("[!] Request sent, but check if password is correct.")
                
        else:
            print(f"[-] Gateway error. Status code: {response.status_code}")

    except Exception as e:
        print(f"[\u274C] Error connecting to 172.16.16.16: {e}")

if __name__ == "__main__":
    kiet_wifi_login()