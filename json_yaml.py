class converter:
    def json_to_yaml(json_file_name, yaml_file_name):
        open(json_file_name, "r") as data:
        json_data = json.load(data)
        open(outfile, "w") as output:
        yaml.dump(json_data, output)
        
    def yaml_to_json(yaml_file_name, json_name_file):
        open(yaml_file_name, "r") as data:
        yaml_data = json.load(data)
        open(outfile, "w") as output:
        yaml.dump(yaml_data, output)


converter.
