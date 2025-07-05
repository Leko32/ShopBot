# Vape Shop Telegram Bot

This is a **Telegram bot** designed for a **vape shop**. The bot allows users to browse and choose from various vape products, including e-liquids, vapes, and disposable vapes. It also features an **admin panel** with elevated privileges for managing the product assortment, as well as enabling or disabling buttons for specific products.

## Features

### 🛒 **Product Categories:**

* **E-liquids**: Browse different flavors of e-liquids.
* **Vapes**: Explore various vape devices.
* **Disposable Vapes**: Choose from a range of disposable vapes.

### 🔐 **Admin Features:**

* **Update Assortment**: Admins can add, remove, or update products in the catalog.
* **Enable/Disable Buttons**: Admins can enable or disable product buttons dynamically, allowing for greater control over the user interface and available products.

### 🧑‍💻 **Commands for Admins:**

* `/add_item <product_name> <price>`: Add a new product to the catalog.
* `/remove_item <product_name>`: Remove a product from the catalog.
* `/enable_button <product_name>`: Enable the button for a specific product.
* `/disable_button <product_name>`: Disable the button for a specific product.

## Setup

### 1. **Clone the repository:**

```bash
git clone https://github.com/Leko32/ShopBot.git
```

### 2. **Install dependencies:**

Make sure you have **Python 3.x** installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### 3. **Set up the bot:**

* Create a `.env` file and set your **Bot Token**.
* Example:

  ```env
  TELEGRAM_API_TOKEN=your_telegram_bot_api_token
  ```

### 4. **Run the bot:**

```bash
python main.py
```

Your bot should now be up and running! 🎉

---

## Folder Structure

```
/VapeShopBot
│
├── main.py         # Main script to run the bot
├── handlers.py     # Handlers for bot commands
├── keyboards.py    # Inline keyboards and buttons
├── admin_handlers.py  # Handlers for admin commands
├── .env            # Environment variables (contains bot token)
├── requirements.txt  # List of required Python packages
├── README.md       # This file
└── .gitignore      # Git ignore file (to keep .env and other sensitive data safe)
```

## How It Works

The bot allows customers to view products and make selections. For admins, special commands are available to manage the catalog, including the ability to enable/disable products and update their details.

### Example User Interaction:

1. User sends a message like "Show me vapes", and the bot replies with a list of available vapes.
2. User selects a product to see more details or purchase it.
3. Admin uses the `/update text`, `/off button`, or `/on_button` commands to manage the product catalog.

### Example Admin Interaction:

* `/update Vape 1000ml 300`
* `/off anarchia`
* `/on anarchia`

---

## Contributing

Feel free to fork this repo and submit pull requests for improvements or new features. If you find any bugs or issues, please report them in the **Issues** section.

---

### 🚀 Let your customers vape with ease! Happy coding! 😎

---
