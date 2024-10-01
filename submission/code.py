import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

max = 255
colorOption = 0
while True:
    inp = input("\nSelect an option: 1, 2, 3, or q to quit. ")
    try:
        # Check if number is an integer
        if type(int(inp)) == int:
            # Check if the integer is in range
            if 0 < int(inp) <= 3:
                colorOption = int(inp)
                print("Running option", inp)
            else:
                print("Number out of range.")
                continue
    # If integer check fails:
    except:
        # Check if inp is the quit string
        if inp == "q":
            print("Exiting program.")
            break
         # else, freak out
        else:
            print("Invalid input, try again.")
            continue

    while max > 0:
        for i in range(10):
            if colorOption == 1:
                cp.pixels[i] = (max, 0, 0) 
            elif colorOption == 2:
                cp.pixels[i] = (0, max, 0) 
            elif colorOption == 3:
                cp.pixels[i] = (0, 0, max) 
        cp.pixels.show()
        time.sleep(0.003)

        max = max - 1
    # Reset max after execution value
    max = 255