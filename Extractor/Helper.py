from Extractor.Download import Download
from Extractor.Logger import Logging
from Extractor.Scrapper import ImageScrapperClass

logger_obj = Logging('Advance Image Downloader')  # Creating a custom based logger
logger_obj.initialize_logger()  # Instantiating the logger object


class HelperClass:

    def helper_image(self, search_query, no_images, req_id):
        """
        this helper method responsible for calling the respective methods for inserting the images into the database
        :param search_query: Search query given by user
        :param no_images: Number of images to download
        :param req_id: Unique request ID of the user
        """
        try:

            # Initializing the image_scrapper for web scrapping
            image_scrapper = ImageScrapperClass(no_images)

            # Opening the URL provided in the Chrome tab
            image_scrapper.get_request(search_query)

            # Storing the URL
            image_scrapper.fetch_thumbnails(req_id)

            self.helper_download(search_query, req_id)

        except Exception as e:
            logger_obj.print_log('(HelperClass.py(helper_image) - Something went wrong ' + str(e), 'exception')

            # Deleting the URL and files which are inserted/created
            self.helper_delete(str(req_id))
            raise Exception(e)

    @staticmethod
    def helper_delete(req_id):
        """
        This helper method is responsible for calling the methods to delete the files after some amount of time
        :param req_id: Unique request ID
        """
        try:
            logger_obj.print_log('Deleting operation started', 'info')

            # Deleting the files from the system
            Download.delete_file(req_id)

            logger_obj.print_log('All the files are deleted', 'info')

        except Exception as e:
            logger_obj.print_log('(HelperClass.py(helper_delete) - Something went wrong ' + str(e), 'exception')
            raise Exception(e)

    @staticmethod
    def helper_download(search_query, req_id):
        """
        This helper method is responsible for calling the methods to download the images over an internet
        :param search_query: Search query of the user
        :param req_id: Unique request ID
        """
        try:
            logger_obj.print_log('Inside the download function', 'info')

            # Creating the download class object for performing download operations
            download_obj = Download()

            str_req_id = str(req_id)

            # Creating directory for saving images
            Download.create_dir(str_req_id)
            logger_obj.print_log('Directory is created', 'info')

            # Downloading Images
            download_obj.download_images(search_query, str_req_id)
            logger_obj.print_log('Images are downloaded over the internet', 'info')

            # Creating a zip file
            Download.create_zip(str_req_id)
            logger_obj.print_log('Zip file is created', 'info')

        except Exception as e:
            logger_obj.print_log('(Helper.py(helper_dowload)) - Something went wrong You are not allowed to access',
                                 'exception')
            raise Exception(e)
