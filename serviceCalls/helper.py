import json
import os


def de_bridge_keys_data():
    project = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('deBridge'))))
    base_dir = os.getenv('GITHUB_WORKSPACE', project)
    file_path = os.path.join(base_dir, 'keys_de_bridge.json')
    dictionary = open(file_path).read()
    nets = json.loads(dictionary)
    return nets
