from datetime import datetime, timedelta
import onc
import json
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")


def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    # check temp at CTD
    CTD_params = {
        "locationCode": "FGPPN",
        "deviceCategoryCode": "CTD",
        "sensorCategoryCodes": "temperature",
        "dateFrom": "2024-08-05T12:00:00.000Z",
        "dateTo" : "2024-08-05T12:02:00.000Z"
    }
    
    # check temp at Acoustic Doppler Current Profiler 2 MHzc
    mount_params = {
        "locationCode": "FGPPN",
        "deviceCategoryCode": "ADCP600KHZ",
        "sensorCategoryCodes": "temperature",
        "dateFrom": "2024-08-05T12:00:00.000Z",
        "dateTo" : "2024-08-05T12:02:00.000Z"
    }
    


    CTD_result = my_onc.getScalardata(CTD_params)
    mount_result = my_onc.getScalardata(mount_params)


    print(f"CTD Temperature Data at Foglers Deep: {CTD_result["sensorData"][0]["data"]["values"]}")
    print(f"Acoustic Temperature Data at Foglers Deep: {mount_result["sensorData"][0]["data"]["values"]}")


if __name__ == "__main__":
    main()
