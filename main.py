from utilities import *
from process import GetImageProcess
from read_process import ReadImage


def __main__():
    """
    Main function to perform all processes
    :return:
    """
    parameters = get_parameters()
    image_reader = ReadImage(parameters)
    images = image_reader.collect_images()
    images_data = reconstruct_combination(parameters, images)
    process_images = GetImageProcess(parameters, images_data)
    process_images.process()


if __name__ == '__main__':
    __main__()
