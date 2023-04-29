import requests

res = requests.post(
    'http://localhost:8080/order',
    json=
    {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
)
if res.ok:
    print(res.json())
