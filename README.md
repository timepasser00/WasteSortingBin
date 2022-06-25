# WasteSortingBin
The Bin automatically stores the waste classified as cardboard,metal and plastic.

# File info

live.py is the code always running on the rasperry pi.

test_img.py contains the code to capture the image of the waste dumped.

motorControl.py contains the code to rotate the pole, so that waste can be dumped in right bin.

my_pred.py contains the code with a pre-trained model, which helps to predict the waste category.

dump.py contains code to rotate the container containing the waste. 


# Basic Internal Working.

live.py is running in an infinite loop, getting data from IR sensor. When the user dumps the waste , IR senses and starts prediction process. 

my_pred.py , using the test_img.py clicks the picture of the waste, then a a pre-trained model predicts the waste type. Based on the waste motorControl.py rotates 
by a pre-difined angle. It then activate the dump.py to dump the waste. After that motorControl.py rotates the same angle in anti Clockwise direction to return to it's intial position.




