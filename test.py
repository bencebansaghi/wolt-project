import requests


def send_request(test_data):
    return requests.post(
        "http://localhost:8080/order",
        json=test_data)


def test(test_data, desired_output):
    got_output = send_request(test_data).json()
    if desired_output in got_output:
        print("PASS! -- " + str(got_output) + "\n")
    else:
        print("FAIL! -- " + str(got_output) + "\n")


try:
    print("Test: correct input fields")
    correct_data = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
    test(correct_data, "delivery_fee")

    print("Test: correct input fields with extra fields")
    correct_data_unused_fields = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z",
        "something": 53,
        "unrelevant": "stringtype"
    }
    test(correct_data_unused_fields, "delivery_fee")

    print("Test: necessary fields missing")
    data_point_missing = {
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
    test(data_point_missing, "missing from request")

    print("Test: int value type incorrect")
    value_type_incorrect = {
        "cart_value": "string",
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021-10-12T13:00:00Z"
    }
    test(value_type_incorrect, "invalid literal for int() with base 10:")

    print("Test: string value type incorrect")
    value_type_incorrect = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": {"something": 8, "another": 9}
    }
    test(value_type_incorrect, "Error in time: strptime() argument 1 must be str")

    print("Test: time in wrong format")
    time_in_wrong_format = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2021:10:12T13-00-00Z"  # ":" replaced with "-" and vice versa
    }
    test(time_in_wrong_format,
         "does not match format '%Y-%m-%dT%H:%M:%S%z'")

except Exception as error:
    print(f"Error occurred: ", error)