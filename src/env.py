import yaml

with open('env.yaml', 'r') as f:
    env_vars = yaml.safe_load(f)

HOST = env_vars['host']
USERNAME = env_vars['username']
PASSWORD = env_vars['password']
DB_NAME = env_vars['db_name']
