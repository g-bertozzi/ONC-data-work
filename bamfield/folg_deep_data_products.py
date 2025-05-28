from datetime import datetime, timedelta
import onc
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")
"""
"""

def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    # Define parameters (query window: June 1, 2021 from 00:00 to 01:00 UTC)
    params = {
        "locationCode": "FGPD",
        "deviceCategoryCode": "CTD",

    }

    data_products = my_onc.getDataProducts()

    if data_products and isinstance(data_products, list):
        print(f"Total data products: {len(data_products)}\n")

        for i, product in enumerate(data_products):
            print(f"Data Product #{i + 1}")
            print(f"  Code              : {product.get('dataProductCode')}")
            print(f"  Name              : {product.get('dataProductName')}")
            print(f"  Extension         : {product.get('extension')}")
            print(f"  Help Document     : {product.get('helpDocument')}")
            print(f"  Has Device Data   : {product.get('hasDeviceData')}")
            print(f"  Has Property Data : {product.get('hasPropertyData')}")
            print(f"  Options : {product.get('hasPropertyData')}")            
            print("-" * 60)
    else:
        print("No data products found or invalid response format.")



if __name__ == "__main__":
    main()
