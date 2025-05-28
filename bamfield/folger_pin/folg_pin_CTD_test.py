from datetime import datetime, timedelta
import onc
import json
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")
"""
Fetches scalar data using the ONC Python SDK for a given location, device category,
property, and time window — prints results to console.
"""

def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    params = {
        "locationCode": "FGPPN",
        "deviceCategoryCode": "CTD",
        "sensorCategoryCodes": "temperature",
        "dateFrom": "2024-08-05T12:00:00.000Z",
        "dateTo" : "2024-08-05T12:02:00.000Z"
    }

    result = my_onc.getScalardata(params)

    script_dir = Path(__file__).parent.resolve()
    output_file = script_dir / "pin_output.json"
   
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("JSON data written to 'locations_output.json'")

if __name__ == "__main__":
    main()
