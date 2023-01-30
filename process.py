import os

import numpy as np
from matplotlib import pyplot as plt


class GetImageProcess:
    """
    Class is used for collecting images according to the provided parameters, process and plot the results
    """

    def __init__(self, config_parameters: dict, images_data: dict):
        """
        Method is initializer of the class
        :param config_parameters: required parameters for the project
        """
        self.configuration = config_parameters
        self.images_data = images_data

    @staticmethod
    def reconstruct(phase_data: np.array, magnitude_data: np.array) -> np.array:
        """
        Method is used to reconstruct image according to magnitude and phase information
        :param phase_data: phase data of the image
        :param magnitude_data: magnitude data of the image
        :return: reconstructed image in form of numpy array
        """
        reconstruction = np.multiply(magnitude_data, np.exp(1j * phase_data))
        reconstructed_image = np.real(np.fft.ifft2(reconstruction))
        return reconstructed_image

    def plot_combinations(self, image1: np.array, image2: np.array, information: str, image_name: str) -> None:
        """
        Method is used to plot provided two images in one figure along with the provided information
        :param image1: the first image
        :param image2: the second image
        :param information: information about the figure
        :param image_name: specifies image name to save the image into the output directory
        :return: None
        """
        file_name = os.path.join(self.configuration['output_dir'], f'{image_name}.png')
        f, axes = plt.subplots(1, 2)
        f.suptitle(information)
        axes[0].imshow(image1, cmap="gray")
        axes[0].title.set_text("(a)")
        axes[1].imshow(image2, cmap="gray")
        axes[1].title.set_text("(b)")
        plt.plot()
        plt.savefig(file_name)
        plt.show()

    def process(self) -> None:
        """
        Method is used as main function of the object which combines all process
        :return: None
        """

        self.plot_combinations(
            self.images_data[0]['magnitude'], self.images_data[0]['phase'],
            f'Spectrum Magnitude (a) and Spectrum Phase(b) for Image {self.images_data[0]["choice"]}',
            f'mag_phase_{self.images_data[0]["choice"]}'
        )
        self.plot_combinations(
            self.images_data[1]['magnitude'], self.images_data[1]['phase'],
            f'Spectrum Magnitude (a) and Spectrum Phase(b) for Image {self.images_data[1]["choice"]}',
            f'mag_phase_{self.images_data[1]["choice"]}'
        )
        reconstruction_01 = self.reconstruct(self.images_data[0]['phase'], self.images_data[1]['spectrum_magnitude'])
        reconstruction_10 = self.reconstruct(self.images_data[1]['phase'], self.images_data[0]['spectrum_magnitude'])
        self.plot_combinations(reconstruction_01, reconstruction_10, 'SM 1 and SP 2 (a) and SM 2 and SP 1 (b)',
                               'reconstruction_result_{self.images_data[0]["choice"]}_{self.images_data[1]["choice"]}')
