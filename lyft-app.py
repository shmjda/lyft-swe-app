# -------- Lyft Apprenticeship application -----------
# Please write a small web application in Python/Ruby/Node. The application only needs to do the following:
# Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
# Return a JSON object with the key “return_string” and a string containing every third letter from the original string.

# -------- Example ----------
# If you POST
# {"string_to_cut": "iamyourlyftdriver"}
# it will return:
# {"return_string": "muydv"}
# Note: To see expected behavior you can test against a current working example with the command:
# curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/test', methods=["POST"])
# this function should retrieve the submitted string and from that, create a new_string with every 3rd letter and return a JSON object with that string.
# RETURN: JSON object  {"return_string": new_string}
def cut_string():
    # retrieve the string_to_cut from the POST request
    json_data = {"string_to_cut": request.json["string_to_cut"]}

    # cut the string from json_data to pull only every 3rd letter of the string submitted by using string slicing
    input_string = json_data["string_to_cut"]
    return_string = ""
    for i in range(2, len(input_string), 3):
        return_string += input_string[i]

    # store result with key in dict and return
    return_string_json = {"return_string": return_string}

    return return_string_json


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
    # app.jinja_env.auto_reload = True

# in all honesty I didn't have enough time to do this, but I think this is roughly how it works
# a quick plug for my portfolio, available at selamawit.com/portfolio