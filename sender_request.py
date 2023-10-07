import data
import Configuration
import requests


def post_order(body_orders):
    return requests.post(Configuration.URL_SERVER + Configuration.CREATE_ORDER,
                         json=body_orders,
                         headers=data.headers)
response = post_order(data.body_orders)
print(response.status_code)
print(response.json())

track_order = response.json()["track"]

def get_treck_order(track_order):
    return requests.get(Configuration.URL_SERVER + Configuration.GET_ORDER_TRACK,
                        params={"t": track_order})
response = get_treck_order(track_order)
print(response.status_code)
print(response.json())
