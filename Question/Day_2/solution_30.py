import subprocess
import time

def show_notification(title, message):
    subprocess.run(["notify-send", title, message, "-t", "10000"])

def main():
    while True:
        show_notification("Please drink water", "Water is beneficial for your health!")
        time.sleep(3600)  

if __name__ == "__main__":
    main()
