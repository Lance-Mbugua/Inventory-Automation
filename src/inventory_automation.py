import pandas as pd
from datetime import datetime

# Load inventory data from CSV (or Excel)
def load_inventory(file_path='data/inventory.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

# Update inventory based on sales or restock
def update_inventory(df, product_id, quantity_change, action="sale"):
    if product_id not in df['Product_ID'].values:
        print(f"Error: Product ID {product_id} not found.")
        return df
    if action == "sale":
        df.loc[df['Product_ID'] == product_id, 'Quantity'] -= quantity_change
    elif action == "restock":
        df.loc[df['Product_ID'] == product_id, 'Quantity'] += quantity_change
    df['Quantity'] = df['Quantity'].clip(lower=0)
    return df

# Generate low-stock alerts
def check_low_stock(df, threshold=10):
    low_stock = df[df['Quantity'] <= threshold][['Product_Name', 'Quantity']]
    return low_stock

# Save updated inventory to CSV
def save_inventory(df, file_path='data/inventory.csv'):
    df.to_csv(file_path, index=False)

def main():
    # Load inventory
    df = load_inventory()
    if df is None:
        return

    # Simulate a sale
    print("Updating inventory for sale of 5 Stainless Steel Pans...")
    df = update_inventory(df, product_id="K123", quantity_change=5, action="sale")
    print("Updated Inventory:")
    print(df)

    # Simulate a restock
    print("\nRestocking 10 Ceramic Knives...")
    df = update_inventory(df, product_id="K124", quantity_change=10, action="restock")
    print("Updated Inventory:")
    print(df)

    # Check for low stock
    low_stock = check_low_stock(df)
    if not low_stock.empty:
        print("\nLow Stock Alert:")
        print(low_stock)
    else:
        print("\nNo low stock items.")

    # Save updated inventory
    save_inventory(df)
    print(f"\nInventory saved to data/inventory.csv")

if __name__ == "__main__":
    main()
