import requests
import time

BLYNK_TOKEN = "vVCkGIbnKLdtTKsB3qM0raXXj1BU-Jnl"
GET_URL = "https://blynk.cloud/external/api/get"

def getStatus():
    status=0
    try:
        url = f"{GET_URL}?token={BLYNK_TOKEN}&V1"
        response = requests.get(url)

        status = response.text.strip()

        if status == "POLE CONDUCTING":
            print("⚠️ Pole is Conducting")
            status=1
        elif status == "POLE SAFE":
            print("✅ Pole is Safe")
            status=0
        else:
            print("No data received from Blynk")

    except Exception as e:
        print("Error:", e)

    time.sleep(1)
    return status
    

# status=getStatus()
# print("status ",status)