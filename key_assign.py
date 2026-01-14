import serial  # serial port communication
import pyautogui  # to control mouse/keyboard

# set port and baud rate, change as needed
arduino = serial.Serial('COM5', 9600)
print("working")
while True:
    if arduino.in_waiting > 0:  # wait for arduino to be inactive
        
        # receive command decoded by arduino
        code = arduino.readline().decode().strip()

        if code == "FORWARD":  # advance slide
            pyautogui.press('right')  # right arrow
        elif code == "BACKWARD":  # go back slide
            pyautogui.press('left')  # left arrow
        elif code == "1":
            pyautogui.press('home')  # go to first slide
        elif code == "2":
            pyautogui.press('end')  # go to last slide
        elif code == "MODE":
            pyautogui.press("f5")   # enter presentation mode
        elif code == "POWER":
            pyautogui.press("esc")  # exit presentation mode
        # Add more buttons for other functions (scalability)