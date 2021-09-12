import uuid

from ImageExtractor.Scheduler import ScheduleJob
from ImageExtractor.Logger import Logging
from ImageExtractor.Download import Download

# Configuring the logger
logger_obj = Logging('Advance Image Downloader')  # Creating a custom based logger
logger_obj.initialize_logger()  # Instantiating the logger object


class ImageExtractorClass:
    @staticmethod
    def schedule_job(search_query, date, time, no_images):
        try:
            is_valid, error = validate_inputs(search_query, date, time, no_images)
            if is_valid:
                # Creating the unique ID for the request generated
                req_id = uuid.uuid4()
                # Creating a object for the scheduler
                schedule_job = ScheduleJob()
                # Adding the job in the scheduler
                schedule_job.insert_request(search_query, date, time, int(no_images), req_id)
                logger_obj.print_log('Schedule is added for adding the job in queue', 'info')
                return req_id, no_images
            else:
                logger_obj.print_log('(Extractor.py) - Something went wrong ' + error, 'exception')
                raise Exception(error)
        except Exception as e:
            print(e)

    @staticmethod
    def delete_file(req_id):
        try:
            Download.delete_file(req_id)
        except Exception as e:
            print(e)


def validate_inputs(search_query, date, time, no_images):
    """
    Function is responsible for validating the inputs given by the user
    :param search_query: search term by the user
    :param date: Date for scheduling the job
    :param time: Time for scheduling the job
    :param no_images: No of images given by the user
    :return: Boolean if the input's are valid
    """
    try:
        # Checking if the queries passed are empty
        if search_query != '' and date != '' and time != '' and no_images != '':

            no_images = int(no_images)  # Converting into integer for further processing
            # Number of images should be in between 1 and 500
            if 1 <= no_images <= 2000:
                return True, None
            else:
                logger_obj.print_log(
                    '(Extractor.py (validate_inputs)) - Something went wrong. No of images must be in '
                    'between 1 and 2000',
                    'exception')
                return False, 'No of images must be in between 1 and 500'
        else:
            logger_obj.print_log(
                '(Extractor.py (validate_inputs)) - Something went wrong. One of the inputs is empty',
                'exception')
            return False, 'One of inputs is empty'

    except Exception as e:
        raise Exception(e)
