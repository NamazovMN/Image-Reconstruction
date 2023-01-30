# Image-Reconstruction
The project involves 2 main steps, such as making chosen images grey-scale and reconstruction of new image using the magnitude and phase information of images.

# Details

## image_reconstruction.py

_**The program has been done by running this exact file. This code file does 2 main proccesses.**_

  > **_Making two images grey-scale_**
  
  > **_Generating new image using magnitude information of one image and phase information of another._**
  
 ## Input images
 
 **_Clock and Valley images have been used for this purpose. However, you can use any other 2 images in order to have different results._**
 
 ## Results
 
 **_The folder is used to contain the results of the images, such as magnitude and phase information of all images and reconstructed image._**
 
 ## How to test?
  In order to test the project you can follow the steps that are given: 
* Initially, you need to pull the project into your local machine; 
* Then, you should run the following snippet to install all required dependencies: 
  ```python
  python main.py -r requirements.txt
* You can add as much as images into your data folder, so that only combination of two images will be used for reconstruction, which should be provided by you.
* Now you are all set to run the following snippet 
  ```python
  python main.py --combinations 0 1
  
**_Best Regards_**

**_Mahammad Namazov_**
