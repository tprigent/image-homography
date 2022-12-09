# Homography on image

This simple code has been developed during the PIV (Image Processing) course @[IST Lisboa](https://tecnico.ulisboa.pt/).

The aim is to determine the homography between a sheet distorted by perspective and a view from above.
The homography is determined manually, without using OpenCV. However, OpenCV is used for display purposes and to apply 
the homography once determined.

## Algorithm

The first part consists in getting the 4 key points of the sheet. These coordinates will be considered as being part of
the *initial picture* frame.

Then, we declare our *final frame*, by choosing (for example) the size of the input image. Hence, the sheet will fill the entire 
output image.

The mathematical part follows. We build the correpondance point matrix A for each point as below.

Then, the homography h is given by solving $Ah=0$. The SVD algorithm is then used to get the result 
(the last column of V gives the best result).
We get the desired form H by reshaping h to a $3x3$ matrix.

OpenCV is again used to apply the homography, and write the output image.

## Results
The 4 points have been places at the 4 corners of the iPad, here is the result:

| **Input image** | **Output image** |
|:---------------:|:----------------:|
|                 |                  |
