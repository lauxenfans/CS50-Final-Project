import pyautogui
import time

def take_screenshot(output_file="screenshot.png"):
    # Wait for a moment to switch to the desired window or screen
    time.sleep(3)

    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the specified file
    screenshot.save(output_file)
    print(f"Screenshot saved as {output_file}")

# Call the function to take a screenshot (you can provide a custom filename if needed)
take_screenshot()