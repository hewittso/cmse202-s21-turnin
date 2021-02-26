from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self,im1_filename,im2_filename):
        '''
        Load_images method so that it takes two image filenames as inputs, loads the FITS files, and stores the image array data as attributes of the Observer class.
        '''
        hdu_list = fits.open(self.im1_filename)
        im1_filename_data = hdu_list[0].data
        hdu_list = fits.open(self.im2_filename)
        im2_filename_data = hdu_list[0].data
        a_dict= {self.im1_filename: im1_filename_data , self.im2_filename: im2_filename_data}
        return a_dict

    
        '''
    Define a new method called calc_stats for the Observer class that prints the mean and standard deviation of both images. Make sure that the print statements indicate which image the values correspond to by using the filename attributes that are stored when the Observer is initialized.
    '''
    def calc_stats(self):
        keys= a_dict.keys()
        keys_list= list(a_dict)
        values = a_dict.values()
        values_list = list(values)
        for x in values:
            print('Stdev', keys_list[x],":", np.std(x))
            print('Mean',keys_list[x],":",np.mean(x))
            
        '''
       Finish the make_composite method so that it creates a 3D NumPy array that represents a 2D image and it's corresponding RGB values. As a reminder, the Red, Green, and Blue channels should be defined in the following ways:

The red channel should be defined as
1.5×I filter image arrayThe maximum of the R filter image array
 
The green channel should be based on the average pixels values, speficially defined as
(I filter image array+R filter image array)/2The maximum of the R filter image array
 
The blue channel should be defined as
R filter image arrayThe maximum of the R filter image array
'''

    
    def make_composite(self):
        '''
        creates a 3D NumPy array that represents a 2D image and it's corresponding RGB values.
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_filename_data.shape[0],self.im1_filename_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_filename_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_filename_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        #green channel
        rgb[:,:,0] = ((self.im2_filename_data.astype("float")+ self.im1_filename_data.astype("float")))/(2*norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        #blue channel
        rgb[:,:,0] = 1.5 * (self.im1_filename_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        
        