import base64
import hashlib
import hmac
from datetime import datetime

api_key = 'dba090cea9a94af09406c4f57cd0e554'
api_secret = 'eIu6blt8VgrJx8ROYs6EOruXKZMDEudZgDDvbWmhTyg='
current_time = datetime.utcnow()
formatted_time = current_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
http_uri = '/pro/564e27553efe4c97930e65f468ccc019/v1/data-deal-admin/advertisingSpace/queryAdvertisingSpaceConfig'
http_method = 'GET'

params = "adsenseNumber=3&adsenseChannel=0"

signing_string = http_method + "\n" + http_uri + "\n" + "" + "\n" + api_key + "\n" + formatted_time + "\n" + ""

secret = bytes(api_secret, 'utf-8')
message = bytes(signing_string, 'utf-8')

hash = hmac.new(secret, message, hashlib.sha256)

# to lowercase base64
if __name__ == '__main__':
    print(formatted_time)
    print(base64.b64encode(hash.digest()))

