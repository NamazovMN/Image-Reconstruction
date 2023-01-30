import argparse
import os


def set_configuration() -> argparse.Namespace:
    """
    Function is used to collect all required information from the user. In case user will not specify some information
    default values will be utilized
    :return: Namespace object for all required parameters
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--width', required=False, type=int, default=500,
                        help='Specifies desired width of the first image')
    parser.add_argument('--height', required=False, type=int, default=500,
                        help='Specifies desired width of the first image')
    parser.add_argument('--data_dir', required=False, type=str, default='data',
                        help='Specifies path to the first image')
    parser.add_argument('--combinations', required=False, type=int, default=[0, 1], nargs='+',
                        help='Specifies path to the second image')
    parser.add_argument('--out_dir', required=False, type=str, default='results',
                        help='Specifies output directory where process results will be saved')

    return parser.parse_args()


def get_parameters() -> dict:
    """
    Function collects user-defined parameters and add output directory to the parameters dictionary
    :return: required parameters for the project
    """
    configuration = dict()
    parameters = set_configuration()
    for argument in vars(parameters):
        configuration[argument] = getattr(parameters, argument)
    check_dir('results')
    configuration['output_dir'] = 'results'
    return configuration


def reconstruct_combination(parameters, image_results):
    """
    Function is used to check whether provided combination is valid or not. Then collects combinations and return
    required information for images
    :param parameters: required parameters for the project
    :param image_results:
    :return:
    """
    result_dict = dict()
    for idx, image_choice in enumerate(parameters['combinations']):
        if image_choice > len(image_results) - 1:
            raise IndexError('Choice must be within the range of the dataset. If there are maximum 35 data, maximal'
                             'choice can be 34')
        current_dict = {data: info for data, info in image_results[f'image_{image_choice}'].items()}
        current_dict['choice'] = image_choice
        result_dict[idx] = current_dict
    return result_dict


def check_dir(directory: str) -> None:
    """
    Function is used to check existence of the requested directory. In case it does not exist, it will be created.
    :param directory: requested path, which existence will be checked
    :return: None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
