import webbrowser
import time


pages = list(input('Input page urls, divided by commas:\n').split(','))
interval = int(input('Input interval of delay between showing pages (sec):\t'))

for page in pages:
    webbrowser.open(page)
    time.sleep(interval)