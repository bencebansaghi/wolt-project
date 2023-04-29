from flask import Flask, request, jsonify
import math
from datetime import datetime

app = Flask(__name__)


def order_surcharge(cart_value):  # Returns the difference to 10€, if the order is under it
    if cart_value < 1000:
        diff_to_10 = 1000 - cart_value
        return diff_to_10
    return 0


def distance_charge(distance):
    base_charge = 200  # delivery fee for the first 1000 meters is 2€
    if distance <= 1000:
        return base_charge
    else:
        charge = math.ceil((distance - 1000) / 500) * 100
        return charge + base_charge


def items_surcharge(number_of_items):
    surcharge = 0
    if number_of_items > 4:
        surcharge += (number_of_items - 4) * 50
    if number_of_items > 12:
        surcharge += 120
    return surcharge


def friday_rush_multiplier(time, delivery_fee):
    time_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
    if int(time_datetime.strftime("%w")) == 5:  # is it friday
        if 15 < int(time_datetime.strftime("%H")) < 20:  # is it between 3-7 PM
            return delivery_fee * 1.2
    return delivery_fee


@app.route("/<request_json>", methods=["POST"])
def calculate_total_fee(request_json):
    requested_data_dict = request.json

    values_int_dict = {
        "cart_value": int(),
        "delivery_distance": int(),
        "number_of_items": int()
    }
    for name in values_int_dict:
        if name in requested_data_dict:  # check if the given values are in the request
            try:
                values_int_dict[name] = int(requested_data_dict[name])  # add to the dict in int
            except Exception as ex:
                return jsonify(f"Error in {name}: {ex}")
        else:
            return jsonify(f"{name} missing from request")

    try:
        delivery_time = requested_data_dict["time"]
        datetime.strptime(delivery_time, "%Y-%m-%dT%H:%M:%S%z")

    except Exception as ex:
        return jsonify(f"Error in time: " + str(ex))

    if values_int_dict["cart_value"] >= 10000:
        return jsonify({"delivery_fee": 0})  # return 0e as delivery fee if order over 100€
    delivery_fee_initial = order_surcharge(values_int_dict["cart_value"]) \
                           + items_surcharge(values_int_dict["number_of_items"]) \
                           + distance_charge(values_int_dict["delivery_distance"])  # Those that need to be added

    delivery_fee_final = friday_rush_multiplier(delivery_time, delivery_fee_initial)  # final multiplication
    if delivery_fee_final > 1500:  # max delivery fee is 15€
        delivery_fee_final = 1500

    return jsonify({"delivery_fee": delivery_fee_final})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
