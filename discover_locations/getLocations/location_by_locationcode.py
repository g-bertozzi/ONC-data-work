import onc
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")
"""
returns metdata for a location given it's location code
"""

def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    # Get location for specific location code
    params = {
    "locationCode": "BACAX",
    }
    result = my_onc.getLocations(params)
    

# Check and extract the first result
    if result and isinstance(result, list) and len(result) > 0:
        location = result[0]
        print("\nLocation Metadata\n")

        # Print labeled fields
        print(f"Location Code       : {location.get('locationCode')}")
        print(f"Location Name       : {location.get('locationName')}")
        print(f"Description         : {location.get('description')}")
        print(f"Latitude            : {location.get('lat')}")
        print(f"Longitude           : {location.get('lon')}")
        print(f"Depth (m)           : {location.get('depth')}")
        print(f"Deployments         : {location.get('deployments')}")
        print(f"Has Device Data     : {location.get('hasDeviceData')}")
        print(f"Has Property Data   : {location.get('hasPropertyData')}")
        print(f"Data Search URL     : {location.get('dataSearchURL')}")

        # Nested bounding box
        bbox = location.get("bbox", {})
        print("\nBounding Box:")
        print(f"  Min Latitude      : {bbox.get('minLat')}")
        print(f"  Max Latitude      : {bbox.get('maxLat')}")
        print(f"  Min Longitude     : {bbox.get('minLon')}")
        print(f"  Max Longitude     : {bbox.get('maxLon')}")
        print(f"  Min Depth (m)     : {bbox.get('minDepth')}")
        print(f"  Max Depth (m)     : {bbox.get('maxDepth')}")

    else:
        print("No location data found or invalid format.")

if __name__ == "__main__":
    main()