import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]

mongodb_host = config_env['MONGODB_HOST']
mongodb_port = int(config_env['MONGODB_PORT'])
mongodb_username = config_env['MONGODB_USERNAME']
mongodb_password = config_env['MONGODB_PASSWORD']
# mongodb_uri = f"mongodb://192.168.0.120:{config_env['MONGODB_PORT']}"
