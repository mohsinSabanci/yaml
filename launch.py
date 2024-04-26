# app.py
import yaml

# Load configuration from YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Print the configuration
print("Application Name:", config['app']['name'])
print("Version:", config['app']['version'])
print("Description:", config['app']['description'])
