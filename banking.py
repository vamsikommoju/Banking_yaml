import yaml
import pprint

file_path = 'banking.yml'

with open(file_path,'r') as file:
    try:
        data = yaml.safe_load(file)
        print(type(data))
        pprint.pprint(data)
    except yaml.YamlError as exc:
        print(exc)