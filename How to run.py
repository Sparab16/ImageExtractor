from flask import Flask
from flask_cors import cross_origin
from ImageExtractor.Extractor import ImageExtractorClass
import datetime
import threading
import time
import os

app = Flask(__name__)


class ThreadClass:

    def __init__(self, req_id, time_to_sleep, ):
        self.req_id = str(req_id)
        self.time_to_sleep = time_to_sleep
        self.thread = threading.Thread(target=self.sleep)
        self.thread.start()

    def sleep(self):
        try:
            # Sleep for the given time
            time.sleep(self.time_to_sleep)

            # Wait until the zip file is not ready
            while not os.path.exists(self.req_id + '_zipfile.zip'):
                print('File not exists')
                time.sleep(5)

            print('File exists now')
            time.sleep(30)

            # Deleting the file after 10 seconds
            ImageExtractorClass.delete_file(self.req_id)
            print('Files are deleted')
        except Exception as e:
            print(e)


# Home page route
@app.route('/', methods=['GET'])
@cross_origin()
def index():
    try:

        # Creating the object of ImageExtractorClass
        image_extractor = ImageExtractorClass()

        # Current datetime
        current = datetime.datetime.now()

        # The scheduled datetime
        date_inserted = current + datetime.timedelta(minutes=5)

        date_str = str(date_inserted.year) + '-' + str(date_inserted.month) + '-' + str(date_inserted.day)
        time_str = str(date_inserted.hour) + ':' + str(date_inserted.minute)

        req_id, time_to_sleep = image_extractor.schedule_job('some_sample_query', date_str, time_str, 54)

        # Time to sleep the thread
        time_to_sleep = current + datetime.timedelta(seconds=time_to_sleep)
        total_seconds_sleep = time_to_sleep - datetime.datetime.now()

        # Total seconds to sleep the thread
        total_seconds_sleep = int(total_seconds_sleep.total_seconds())

        ThreadClass(req_id, total_seconds_sleep)

        return '<h1> req id is ' + str(req_id) + ' and time_to_sleep is ' + str(total_seconds_sleep) + ' seconds</h1>'

    except Exception as e:
        return "<h1> Error is " + str(e) + "</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run()