import os
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize


class ReadImage:
    def __init__(self, config_parameters: dict):
        """
        Method is initializer of the class
        :param config_parameters: required parameters for the project
        """
        self.configuration = config_parameters

    def get_image(self, image_path: str) -> np.array:
        """
        Method is used for getting the image, transform it into gray-scale and resize to the desired dimension
        :param image_path: path to the requested image
        :return: np array in shape of desired dimensions
        """
        image = imread(image_path)
        gray_image = rgb2gray(image)
        return resize(gray_image, (self.configuration[f'width'], self.configuration[f'height']))

    def compute_mag_phase(self, image_path: str) -> np.array:
        """
        Method is used to compute spectrum, magnitude and phase information of the requested image
        :param image_path: path to the requested image
        :return: dictionary that contains required information for the requested image
        """
        image = self.get_image(image_path)
        spectrum = np.fft.fftshift(np.fft.fft2(image))
        magnitude = np.abs(spectrum)
        image_magnitude = np.log(magnitude)
        image_phase = np.angle(spectrum)
        return {'spectrum_magnitude': magnitude, 'magnitude': image_magnitude, 'phase': image_phase}

    def collect_images(self) -> dict:
        """
        Method is used to combine all processes in one body
        :return: dictionary of all images' information in the dataset
        """
        image_results = dict()
        for idx, each_image in enumerate(os.listdir(self.configuration['data_dir'])):
            image_path = os.path.join(self.configuration['data_dir'], each_image)
            image_results[f'image_{idx}'] = self.compute_mag_phase(image_path)
        return image_results
