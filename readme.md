# Banking System Template

To run:

- Install requirements by running command `pip install -r requirements.txt`
- Rename env.yaml.template to env.yaml and fill out your db credentials (this is done so that your credentials are not leaked.)
- Run `python main.py init-db` to create a database with some fake data. (You need to have the schema/database created and the user table not yet created.)

Note: This example app stores passwords insecurely. To store passwords securly, take a look at https://stackoverflow.com/questions/12042724/securely-storing-passwords-for-use-in-python-script.
