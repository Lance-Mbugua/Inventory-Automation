# Inventory Automation System

A Python-based system to automate inventory tracking for an e-commerce kitchen products store. This project uses CSV (or Excel) for real-time inventory monitoring and generates low-stock alerts.

## Features
- Automates inventory updates for sales and restocks.
- Integrates with CSV/Excel for data storage.
- Generates alerts for low-stock items (threshold: 10 units).

## Technologies
- Python 3.8+
- pandas
- CSV (or Excel)

## Setup
1. Clone the repository:
    git clone https://github.com/Lance-Mbugua/Inventory-Automation.git

2. Install dependencies:
bash

pip install -r requirements.txt

3. Ensure data/inventory.csv is in the data/ folder.

Run the script:
bash

python src/inventory_automation.py

Usage
Modify inventory_automation.py to update product IDs and quantities.

Check data/inventory.csv for updated inventory.

Low-stock alerts are printed to the console.

Project Structure
src/inventory_automation.py: Main Python script.

data/inventory.csv: Sample inventory data.

requirements.txt: Python dependencies.

Example Output

Updating inventory for sale of 5 Stainless Steel Pans...
Updated Inventory:
  Product_ID       Product_Name  Quantity  Price
0      K123  Stainless Steel Pan       15  29.99
1      K124      Ceramic Knife       15  19.99
2      K125  Wooden Cutting Board      30  14.99
3      K126   Glass Mixing Bowl       10  24.99

Low Stock Alert:
        Product_Name  Quantity
1      Ceramic Knife       15
3   Glass Mixing Bowl       10

License
MIT License



