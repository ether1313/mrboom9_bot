import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8304481697:AAGZN7VNPj65y71Z5JqBEMPVNx6liVS4Qak")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/MRBOOM9AUS")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://mrboom9.com/RFMRBOOMTLGBOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://mrboom9.com/RFMRBOOMTLGBOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Mrboom9 Promo Bot"
BOT_DESCRIPTION = "Mrboom9 Marketing Assistant - Provides latest promotions and event information"
