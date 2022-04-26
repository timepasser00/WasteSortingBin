import RPi.GPIO as GPIO
import time
import dump
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
def rotateMotor(rotation,reverse=False):
    for i in range(rotation):
        for halfstep in range(8):
            for pin in range(4):
                if reverse:
                    GPIO.output(control_pins[pin], halfstep_seq[7-halfstep][pin])
                else:
                    GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0010)
def clk():
    for i in range(128):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0010)

    # time.sleep(1)

def antiClk():
    for i in range(128):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[7-halfstep][pin])
            time.sleep(0.0010)


def sync_motor():
    print("Type steps to be rotated(-ve for anti and 0 for exit)")
    while True:
        val = int(input())
        if val==0:
            break
        else:
            if val<0:
                rotateMotor(-1*val,True)
            else:
                rotateMotor(val)

#sync_motor()

def run(type):
    wasteType = type #input()

    quarter_steps = int(520/4)
    rotation_degree = 0
    if wasteType == "cardboard" or wasteType == "paper":
        rotation_degree = quarter_steps
        """clk()
        time.sleep(1)
        dump.start()
        antiClk()"""
    elif wasteType == "plastic":
        rotation_degree = 2*quarter_steps
        """clk()
        clk()
        time.sleep(1)
        import dump
        antiClk()
        antiClk()"""
    elif wasteType == "metal":
        rotation_degree = quarter_steps*3
        """for i in range(3):
            clk()
        time.sleep(1)
        import dump
        for i in range(3):
            antiClk()"""
    rotateMotor(rotation_degree)
    dump.start()
    time.sleep(1)
    rotateMotor(rotation_degree,True)
    # GPIO.cleanup()


# type = input()   
# run(type)
# sync_motor()
# # dump.start()
# GPIO.cleanup()


