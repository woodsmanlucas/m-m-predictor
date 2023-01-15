# m-m-predictor

This project is real simple computer vision at the moment. The goal is to find M&M's within an image.

![M and M prediction](current_best_ouput.png)

This is my current best output for the project. Notice I still need to implement non-maximum supression so there isn't 20 hits per M&M.

The files in this repo that I'm mostly working with are M_and_Ms.ipynb and Sliding_window.ipynb. I've also been using Split_Images_into_photos to generate more data from large images. 

Server.py and Test.py was some of my tinkering with getting a version of the model in the M and M's file deployed to Heroku. I'll probably eventually update this and use the code I wrote in the sliding windows file.

The object localization file was for finding a single M&M and I had it slightly working
