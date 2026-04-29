import os
import asyncio

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

from config import MEROSS_EMAIL, MEROSS_PASSWORD


async def main():
    http_api_client = await MerossHttpClient.async_from_user_password(
        email=MEROSS_EMAIL, 
        password=MEROSS_PASSWORD, 
        api_base_url="https://iot.meross.com"
    )

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Discover devices.
    await manager.async_device_discovery()
    meross_devices = manager.find_devices()

    print("Found the following Meross devices:")
    for dev in meross_devices:
        print(f"- {dev.name} ({dev.type}): {dev.online_status}")

    manager.close()
    await http_api_client.async_logout()


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())