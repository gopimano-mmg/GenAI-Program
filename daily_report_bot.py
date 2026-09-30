import pyautogui
import time
from datetime import datetime
from openpyxl import Workbook
import os

today = datetime.now()
date_time = today.strftime("%Y-%m-%d %H:%M:%S")
date_for_file = today.strftime("%Y-%m-%d")

website_url = "https://www.google.com/search?q=weather+today"
fetched_data = "Weather information checked from browser"
comment = "Good for daily status report"

# Open Chrome
pyautogui.hotkey("win", "s")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)

# Go to website
pyautogui.write(website_url)
pyautogui.press("enter")
time.sleep(5)

# Create Excel file
file_name = f"daily_report_{date_for_file}.xlsx"

workbook = Workbook()
sheet = workbook.active
sheet.title = "Daily Report"

sheet.append(["Date & Time", "Fetched Data", "Comment"])
sheet.append([date_time, fetched_data, comment])

workbook.save(file_name)

# Open Excel file
os.startfile(file_name)
time.sleep(5)

# Take screenshot
screenshot_name = f"daily_report_screenshot_{date_for_file}.png"
screenshot = pyautogui.screenshot()
screenshot.save(screenshot_name)

print("Daily report created successfully.")
print("Excel file:", file_name)
print("Screenshot:", screenshot_name)