# hairpinbend_collision_avoidance_yolov8
This project aims to prevent vehicle collisions at dangerous hairpin bends by detecting trucks in real-time using YOLOv8 object detection models. The system gives priority to heavy vehicles by controlling traffic lights intelligently through an ESP32 microcontroller, ensuring safe, automated traffic flow without manual supervision.
# how to work with code 
I have given 4 code in this repository<br> 
**1)truckdetect(img).ipynb** ==>  so this code basicaly does truck detection in a picture .you can run this code in google colab<br>
**2)truckdetect(vid).ipynb** ==>  this code detect truck in a video. you can run this  in google colab and once the code is runned the processed video will be downloaded in your PC in mp4 format where we can see the detected trucks.<br>
**3)tuck.py** ==> this is the code that is to be used for real time implementation of the system. in this code we use two camera modules and detect the truck,and based on the truck we give signals to the both side of the road in haipin bends. it can be runned in vs code .if little modifications are made can be runned in raspberry pi.<br>
**4)truckdetectesp.ino** ==> this code will be dumped in the Esp32 controller that i am using in this project to control the traffic light via serial communication . if you are using it in raspberry pi you dont need this part just configure the gpio pins in truck.py and run it.<br>
# pictorial representation of the project
![Image](https://github.com/user-attachments/assets/47eda52b-1a2e-4d90-bdd9-1fff4c6fb1bc)
# Real timemodel setup
