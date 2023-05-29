import json


def de_bridge_keys_data():
    dictionary = open('/Users/annaskvortsova/PycharmProjects/deBridge/keys_de_bridge.json').read()
    nets = json.loads(dictionary)
    return nets
