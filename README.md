# Homography on image

This simple code has been developed during the PIV (Image Processing) course @[IST Lisboa](https://tecnico.ulisboa.pt/).

The aim is to determine the homography between a sheet distorted by perspective and a view from above.
The homography is determined manually, without using OpenCV. However, OpenCV is used for display purposes and to apply 
the homography once determined.

## Algorithm

The first part consists in getting the 4 key points of the sheet. These coordinates will be considered as being part of
the *initial picture* frame.

Then, we declare our *final frame*, by choosing the size of the input image (example here, should fit the sheet format). Hence, the sheet will fill the entire 
output image.

The mathematical part follows. We build the correpondance point matrix $A$ for each point as below:

<img width="375" alt="A matrix" src="https://user-images.githubusercontent.com/14911193/206594293-f27e6af6-38c7-4fa8-8391-79e6def5ca1f.png">


Then, the homography h is given by solving $Ah=0$. The SVD algorithm is then used to get the result 
(the last column of V gives the best result).
We get the desired form H by reshaping $h$ to a $3x3$ matrix.

OpenCV is again used to apply the homography, and write the output image.

## Results
The 4 points have been places at the 4 corners of the iPad, here is the result:

| **Input image** | **Output image** |
|:---------------:|:----------------:|
| ![Image](https://user-images.githubusercontent.com/14911193/206594007-3165bf4c-c32b-4520-938b-b420da945fff.jpeg) |![res-Image](https://user-images.githubusercontent.com/14911193/206594045-8bfd4e7f-46cf-4f4d-a05c-dfe48b3653dd.jpeg)|
