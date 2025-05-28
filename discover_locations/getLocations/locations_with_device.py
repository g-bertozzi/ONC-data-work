import onc
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")
"""
Get all locations with instruments of a specific device category, 
including and below a location in the Oceans 3.0 Data Search Tree
"""

# all locations in folgers passage with CTDs

def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    # FGP
    # deviceCategoryCode=CTD

    params = {
        "locationCode": "FGP",
        "includeChildren": "true",
        "deviceCategoryCode": "CTD"
    }

    result = my_onc.getLocations(params)

    if result and isinstance(result, list) and len(result) > 0:
        print(f"Total locations returned under 'NEP': {len(result)}\n")
        for i, location in enumerate(result):
            print(f"Location #{i+1}")
            print(f"  Location Code     : {location.get('locationCode')}")
            print(f"  Location Name     : {location.get('locationName')}")
            print(f"  Description       : {location.get('description', 'No description')}")
            print(f"  Depth (m)         : {location.get('depth')}")
            print(f"  Latitude          : {location.get('lat')}")
            print(f"  Longitude         : {location.get('lon')}")
            print(f"  Deployments       : {location.get('deployments')}")
            print(f"  Has Device Data   : {location.get('hasDeviceData')}")
            print(f"  Has Property Data : {location.get('hasPropertyData')}")
            print(f"  Data Search URL   : {location.get('dataSearchURL')}")
            print("-" * 50)
    else:
        print("No locations found or invalid response format.")



if __name__ == "__main__":
    main()