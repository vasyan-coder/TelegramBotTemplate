from config_data.config import load_config


config = load_config('<путь к файлу .env>')

bot_token = config.tg_bot.token
super_admin = config.tg_bot.admin_ids[0]
