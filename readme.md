# WoltAPI by Bence Bansaghi

# Introduction

This API is used to calculate the total delivery fee for orders by given parameters. The API has to be called via standard HTTP POST requests. The request should contain a json object, the answer is also in json format.

Written in Python 3.10 on 22/01/2023.

Contains the following Python scripts:
<br>**woltAPI.py**: the API, with a local server run command at the end
<br>**request.py**: an example request sent from python
<br>**test.py**: a test for all possible types of errors

The following Python packages are used:
<br>For the API: *flask, math, datetime*
<br>For the API calls: *requests*

## Usage (Windows environment)

Unzip all the files to an empty folder from the ZIP.

### Requirements
Python 3.10 (or compatible versions) with the required packages listed above installed.

### Run the server
Run the **woltAPI.py** file (eg. py woltAPI.py). The server will await POST requests on localhost, port 8080.

### Call the API
While the server is running, run the **request.py** file to send the default request to the server.

The API can be used by including the following parameters in json format in the body of the request:

<br>"cart_value": the value of the cart, given in integer format
<br>"delivery_distance": the delivery distance, given in integer format
<br>"number_of_items": the number of items in cart, given in integer format
<br>"time": the time of the order, given in string format, with formatting "%Y-%m-%dT%H:%M:%S%z"

## Testing
### Run tests
While the server is running, run the **test.py** file using Python. It will run several POST requests to the API, and checks whether the calculation is performed. The tests contain both positive and negative tests. For negative tests *FAIL* expected, it is a successful test (*PASS*).
To send any desired parameters for delivery fee calculation, modify the json content of request.py, or send corresponding json via POST request from your favourite web browser or curl.

### Error codes
- Necessary field missing: \<field> missing from request
- Required integer value not given as an integer:  Error in \<field>: invalid literal for int() with base 10: \<value type>
- Required string value not given as a string:  Error in time: strptime() argument 1 must be str, not \<value type>
- Order time not given in the required format: Error in time: time data \<value> does not match format '%Y-%m-%dT%H:%M:%S%z'