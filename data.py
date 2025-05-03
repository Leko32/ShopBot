import json
from pathlib import Path

DATA_FILE = Path("product_data.json")
DEFAULT_DATA = {
    "flonq_30": "flonq_30 нет в наличии",
    "solana_30": "solana_30 нет в наличии",
    "hqd_10": "hqd_10 нет в наличии",
    "hqd_30": "hqd_30 нет в наличии",
    "elfliq_10": "elfliq_10 нет в наличии",
    "elfliq_30": "elfliq_30 нет в наличии",
    "anarchia": "anarchia нет в наличии",
    "elix_10": "elix_10 нет в наличии",
    "elix_30": "elix_30 нет в наличии",
    "chaser_black_5": "chaser_black_5 нет в наличии",
    "chaser_lux_5": "chaser_lux_5 нет в наличии",
    "chaser_black_6_5": "chaser_black_6_5 нет в наличии",
    "chaser_lux_6_5": "chaser_lux_6_5 нет в наличии",
    "lost_mary": "lost_mary нет в наличии",
    "elf_x": "elf_x нет в наличии",
    "minican_4": "minican_4 нет в наличии",
    "xros_mini": "xros_mini нет в наличии",
    "xros_3_mini": "xros_3_mini нет в наличии",
    "xros_4_mini": "xros_4_mini нет в наличии",
    "xros_pro": "xros_pro нет в наличии",
    "cuba_40": "cuba_40 нет в наличии",
    "cuba_150": "cuba_150 нет в наличии",
}


def load_product_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            # если формат старый — автоконвертируем
            if all(isinstance(v, str) for v in raw_data.values()):
                converted = {
                    key: {"text": value, "photo": None}
                    for key, value in raw_data.items()
                }
                save_product_data(converted)
                return converted
            return raw_data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_product_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
