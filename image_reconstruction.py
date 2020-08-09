import matplotlib.pyplot as plt
import scipy.fftpack as fp
import numpy as np
from skimage.color import rgb2gray
from skimage.io import imread, imshow, show
import matplotlib.pylab as pylab
from PIL import Image

def generate_gray_and_resize(image_file, width, height, title):
    image_data = Image.open(image_file)
    image_data_resized = image_data.resize((width, height))
    image_data = rgb2gray(np.array(image_data))
    image_data_resized = rgb2gray(np.array(image_data_resized))
    f, axes = plt.subplots(1,2)
    f.suptitle(title)
    axes[0].imshow(image_data, cmap = "gray")
    axes[0].title.set_text("Original Image")
    axes[1].imshow(image_data_resized, cmap = "gray")
    axes[1].title.set_text("Resized Image")
    plt.show(f)
    f.savefig("results/"+title + ".jpg")
    return image_data_resized

def generate_spectrum(image_data, title):
    image_spectrum = np.fft.fftshift(np.fft.fft2(image_data))
    image_mag = np.abs(image_spectrum)

    image_magnitude = np.log(np.abs(image_spectrum))
    image_phase = np.angle(image_spectrum)
    f, axes = plt.subplots(1,2)
    f.suptitle(title)
    axes[0].imshow(image_magnitude, cmap = "gray")
    axes[0].title.set_text("Spectrum Magnitude")
    axes[1].imshow(image_phase, cmap = "gray")
    axes[1].title.set_text("Spectrum Phase")
    plt.show(f)
    f.savefig("results/"+title + ".jpg")
    return image_mag, image_magnitude, image_phase

def reconstruct_images(magnitude_data, phase_data):
    reconstruction = np.multiply(magnitude_data, np.exp(1j*phase_data))
    reconstructed_image = np.real(np.fft.ifft2(reconstruction))
    return reconstructed_image

clock = generate_gray_and_resize("clock.jpg",800,800, "Clock")
snow = generate_gray_and_resize("valley.jpeg", 800, 800, "Snow")

clock_mag, clock_magnitude, clock_phase =  generate_spectrum(clock, "Spectrum information of Clock")
snow_mag, snow_magnitude, snow_phase = generate_spectrum(snow, "Spectrum information of Snow")

magAphaseB = reconstruct_images(clock_mag, snow_phase)
magBphaseA = reconstruct_images(snow_mag, clock_phase)

figure, images = plt.subplots(1,2)
images[0].imshow(magAphaseB, cmap = "gray")
images[0].title.set_text("Magnitude Clock + Phase Snow")
images[1].imshow(magBphaseA, cmap = "gray")
images[1].title.set_text("Magnitude Snow + Phase Clock")
figure.suptitle("Reconstructed Images")
plt.show(figure)
figure.savefig("results/Reconstructed Images.jpg")