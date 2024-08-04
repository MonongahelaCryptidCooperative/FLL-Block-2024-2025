# FLL-Block-2024-2025
FLL Block Code 2024-2025

We wanted to share a project we worked on for first lego league. One of the things our FLL team did in past years was to use the Lego Bluetooth remotes to control our robot while we were developing new attachments for our robot as well as mission strategies. This allowed for a rapid development cycle as we didn't have to worry about coding. We also used the remote code to take measurements so we did not have to "guess and check" when programming the robot. Previously we did this in text Pybricks python. However Pybricks recently released a block interface. They also added Xbox controller support. This is better than using the Lego Bluetooth controllers as it allows for analog inputs vs the binary inputs on the Lego controllers. We want novice teams to be able to have the same advantages as more advanced teams so we created this starter pack to get people started who want to try out Pybricks/alternative firmware for FLL.

Included here is some example code to show how to use Pybricks for FLL. For one thing Pybricks does not have a user interface to select programs. Included is a user interface so you can move between programs by selecting the right/left buttons on the hub. The Center button 

Included are 3 example programs "S" "T" and "C"

S = Drive in Square
T = Drive in Triangle 
C = Drive in Circle

Any single character/number can be used as a program label and thus hundereds of programs are possible. Additionbal conditionals can be added. The number of programs will be limited by the storage space on the Spike hub. The order of the programs is dependent on the order of the entries in the "PROGRAM_LIST". Again hopefully the examples make it clear how to accomplish this. 


The remote mode for XBOX is currenlty loaded and accessed by selecting the program "R"

The left joystick makes the robot go fowards/backwards

The right joystick turns

The right trigger controls the right motor, pushing down the right bumper and the right trigger reverses the right motor. This is done via analog inputs so fine control is possible.

The left trigger controls the left attachment motor in a similar manner.

The "a" button is very cool. It prints off how far the robot drove/turned and how far the attachment motors moved. These values can be used to directly program the FLL robot and eliminated "guessing and checking" or having to use a ruler to figure out how far to make the robot drive/turn/move an attachment, etc.

The "x" button exits teleop mode

SETTINGS THAT WILL NEED TO BE CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

In the hub block you will have to set which direction your hub is facing. Front is the axis of the usb port, top is the screen. Unless you also have a vertically oriented hub design these values will be wrong. YOU WILL LIKELY HAVE TO CHANGE THESE VALUES Examples: For the Advanced driving base front-axis = y, top axis = z for example. Documentation can be found on Pybrick's website: https://docs.pybricks.com/en/stable/signaltypes.html#robotframe

You also have to give the drivebase class the layout/dimensions of your robot. It needs both the wheel spacing of the contact area (in mm) and wheel diameter (in mm). This is how the drivebase module is able to do accurate driving commands. MEDIUM SPIKE WHEELS ARE 56 mm LARGE SPIKE WHEELS ARE 88 mm. You can look up the dimensions of other wheels at http://www.wheels.sariel.pl/. Technic holes are spaced 8 mm apart so you can either count the holes or use a ruler to determine your wheel spacing. Remember you are measuring where the wheels touch. So either measure that, or measure from the inside of one wheel to the outside of the other.

Enjoy! Please contact us with any questions! Please credit our team (FTC team 23247 the Monongahela Cryptid Cooperative) and our coder (Julian Huss) if our code is used.
