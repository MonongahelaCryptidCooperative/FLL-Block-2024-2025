"""
File needed along with the BlockMain.py file. Holds various functions that are
difficult to do in the block code. Of note multitasking will not work with this 
code but multitasking/async isn't really required for FLL
"""
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController, 

#Global Controller Variable
CONTROLLER = None

#Functions to select the next/prior programs
def prior_program(active, prog_list):
    "Selects the prior program"
    active = (active - 1) % len(prog_list)
    return active

def next_program(active, prog_list):
    "Selects the next program"
    active = (active + 1) % len(prog_list)
    return active


# Lanch the XBOX Controller RC Mode.
def launch_XBOX(hub:PrimeHub, drivebase:DriveBase, left_attach:Motor, right_attach:Motor, remote_speed:int = 200, remote_turn:int = 100, 
    remote_accel:int = 1000, remote_turn_accel:int = 1000, attach_speed:int = 500):
    "Function to go into RC mode with XBOX controller"
    #Connect to controller if not yet connected)
    hub.light.blink(Color.RED, [ 200, 200])
    global CONTROLLER
    if CONTROLLER == None:
        CONTROLLER = XboxController()

    # Local variables that are used in this function
    left_stick = 0
    right_stick = 0
    left_trigger = 0
    right_trigger = 0 

    # Zero out the odometry and attachment motors
    drivebase.reset()
    left_attach.reset_angle(0)
    right_attach.reset_angle(0)

    # Override the drivebase values to make it easier to control
    drivebase.settings(remote_speed, remote_accel, remote_turn, remote_turn_accel)
    # Turn on Gyro
    drivebase.use_gyro(True)

    ### Main Controller Loop
    while True:
        hub.light.on(Color.BLUE)
        if Button.A in CONTROLLER.buttons.pressed():
            # If the A button is pressed print off to the console:
            # how far the robot drove,
            # how much it turned,
            # how far the attachment motors were moved
            # then reset all of these measurements
            print(drivebase.distance(), ' mm driven')
            print(drivebase.angle(), ' degrees turned')
            print(left_attach.angle(), ' degrees left attachment')
            print(right_attach.angle(), ' degrees right attachment')
            left_attach.reset_angle(0)
            right_attach.reset_angle(0)
            drivebase.reset()
            CONTROLLER.rumble(50, 400)
            hub.speaker.beep(500, 200)
        elif Button.X in CONTROLLER.buttons.pressed():
            # X exits RC mode and allows a new program to be selected
            drivebase.use_gyro(False)
            CONTROLLER.rumble(50, 400)
            hub.speaker.beep(500, 200)
            break
        # If neither the A/X buttons pressed see if their are stick/trigger inputs
        else:
            left_stick = convert_stick_input(CONTROLLER.joystick_left()[1])
            right_stick = convert_stick_input(CONTROLLER.joystick_right()[0])
            left_trigger = convert_stick_input(CONTROLLER.triggers()[0])
            right_trigger = convert_stick_input(CONTROLLER.triggers()[1])


            # If left/right stick input make the robot move
            if left_stick != 0 or right_stick != 0:
                drivebase.drive(left_stick * remote_speed, right_stick * remote_turn)
            # Else stop the robot
            else:
                drivebase.brake()


            # If left trigger input make the attachment move
            if left_trigger != 0:
                if Button.LB in CONTROLLER.buttons.pressed():
                    # Control the Left attachment motor
                    # Left trigger = Left motor forward
                    # Left trigger + Left bumper  = Left motor backwards
                    left_attach.run(left_trigger * attach_speed * -1)
                else:
                    left_attach.run(left_trigger * attach_speed)
            # Else stop the left attachment.
            else:
                left_attach.brake()


            # If Right trigger input make the attachment move
            if right_trigger != 0:
                if Button.RB in CONTROLLER.buttons.pressed():
                    # Control the Right attachment motor
                    # Right trigger = right motor forward
                    # Right trigger + right bumper  = right motor backwards
                    right_attach.run(right_trigger * attach_speed * -1)
                else:
                    right_attach.run(right_trigger * attach_speed)
            # Else stop the right attachment.
            else:
                right_attach.brake()
        wait(10)


def convert_stick_input(stick):
    "Eliminate Stick Drift"
    # Convert the input from the xbox controller
    # from -100 to 100 to -1 to 1. Also change small
    # values to 0 to eliminate stick drift. Rescales the
    # inputs appropriately
    if -7 <= stick <= 7:
        # Return 0 to eliminate  stick drift
        return 0
    elif 7 > stick:
        # Rescale positive (right turning input) given that 0  to  7 = 0
        return (stick - 7) / 93
    else:
        # Rescale negative (left turning input) given that 0 to -7 = 0
        return (stick + 7) / 93



# Lanch the Lego Controller RC Mode.
def launch_LegoRemote(hub:PrimeHub, drivebase:DriveBase, left_attach:Motor, right_attach:Motor, remote_speed:int = 200, remote_turn:int = 100, 
    remote_accel:int = 1000, remote_turn_accel:int = 1000, attach_speed:int = 500):
    "Function to go into RC mode with Lego Bluetooth Remote controller"
    #Connect to controller if not yet connected)
    hub.light.blink(Color.RED, [ 200, 200])
    global CONTROLLER
    if CONTROLLER == None:
        CONTROLLER = Remote()

    # Zero out the odometry and attachment motors
    drivebase.reset()
    left_attach.reset_angle(0)
    right_attach.reset_angle(0)

    # Override the drivebase values to make it easier to control
    drivebase.settings(remote_speed, remote_accel, remote_turn, remote_turn_accel)
    # Turn on Gyro
    drivebase.use_gyro(True)
    ### Main Controller Loop
    while True:
        turn = 0 
        straight = 0
        hub.light.on(Color.BLUE)
        buttons = CONTROLLER.buttons.pressed()
        if Button.CENTER in buttons:
            # If the center button is pressed print off:
            # how far the robot drove,
            # how much it turned,
            # how far the attachment motors were moved
            # then reset all of these measurements
            print(drivebase.distance(), ' mm driven')
            print(drivebase.angle(), ' degrees turned')
            print(left_attach.angle(), ' degrees left attachment')
            print(right_attach.angle(), ' degrees right attachment')
            left_attach.reset_angle(0)
            right_attach.reset_angle(0)
            drivebase.reset()
            hub.speaker.beep(500, 200)
        elif Button.LEFT in buttons and Button.RIGHT in buttons:
            drivebase.brake()
            left_attach.brake()
            right_attach.brake()
            hub.speaker.beep(500, 500)
            break
        else:
            #Right attachment
            if Button.LEFT in buttons:
                if Button.RIGHT_PLUS in buttons:
                    right_attach.run(attach_speed)
                elif Button.RIGHT_MINUS in buttons:
                    right_attach.run(-attach_speed)
                else:
                    right_attach.brake()
            # Left Attachment
            elif Button.RIGHT in buttons:
                if Button.LEFT_PLUS in buttons:
                    left_attach.run(attach_speed)
                elif Button.LEFT_MINUS in buttons:
                    left_attach.run(-attach_speed)
                else:
                    left_attach.brake()

            # Code to move the robot
            else: 
                if Button.LEFT_PLUS in buttons:
                        straight = remote_speed
                elif Button.LEFT_MINUS in buttons:
                        straight = -remote_speed
                else:
                    pass
                if Button.RIGHT_PLUS in buttons:
                        turn = remote_turn
                elif Button.RIGHT_MINUS in buttons:
                        turn = -remote_turn
                else:
                    pass
                if straight != 0 or turn != 0:
                    drivebase.drive(straight, turn)
                else: 
                    drivebase.brake()
