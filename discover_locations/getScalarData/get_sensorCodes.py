import onc
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("ONC_TOKEN")

def main():

    # Create ONC client using the SDK
    my_onc = onc.ONC(token)

    params = {
        "locationCode": "FGPD",
        "deviceCategoryCode": "CTD",
        "sensorCategoryCodes": "",
        "dateFrom": "2024-08-05T12:00:00.000Z",
        "dateTo" : "2024-08-05T13:00:00.000Z"
    }

    result = my_onc.getSensorCategoryCodes(params)

    if result and isinstance(result, list):
        for i, sensor in enumerate(result):
            print(f"Sensor # {i+1}")
            print(f"propertyCode: {sensor.get("propertyCode")}")
            print(f"sensorCategoryCode: {sensor.get("sensorCategoryCode")}")
            print(f"sensorCode: {sensor.get("sensorCode")}")
            print(f"sensorName: {sensor.get("sensorName")}")
            print(f"unitOfMeasure: {sensor.get("unitOfMeasure")}")
            print(f"")
    else:
        print("no result")


if __name__ == "__main__":
    main()
