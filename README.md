# Extractor

Extractor library is useful to help the user download any kind of Images at any date and time over the internet. These images will get downloaded as a job and then let user know that the images have been downloaded.

## Appendix

There are often a times, we need bunch images to work. We can consider the example such as training the Machine learning model over the Cat and Dog images or having those hundreds of beautiful desktop/mobile wallpaper on our laptop with just single click. In such scenario’s we need hundreds of images right away. This problem can be solved using the Extractor Library. The following use cases can be implemented: 
  
## Features

- Upto 2000 images on single click
- Cross platform

## Run Locally

### To download the Extractor, either fork this github repo or simply use Pypi via pip.

```bash
$ pip install ImageExtractor
```

### Code Demonstration

```python

from flask import Flask
from flask_cors import cross_origin
from ImageExtractor.Extractor import ImageExtractorClass
import datetime
import threading
import time
import os

app = Flask(__name__)


class ThreadClass:

    def __init__(self, req_id, time_to_sleep,):
        self.req_id = str(req_id)
        self.time_to_sleep = time_to_sleep
        self.thread = threading.Thread(target = self.sleep)
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
@app.route('/', methods = ['GET'])
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
        
        return '<h1> req id is ' + str(req_id) +' and time_to_sleep is ' + str(total_seconds_sleep) + ' seconds</h1>'

    except Exception as e:
        return "<h1> Error is " + str(e) + "</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()

```
And you are ready to go! At this point, at the given date and time, the images will start downloading.
  
## <center>Usage

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

<li> Fork the repo
<li> Create a new branch

```bash
 git checkout -b new-feature
```
<li> Make the appropriate changes in the file
<li> Commit your changes

```bash
git commit -am "New feature added"
```

<li> Push to the branch

```bash
git push origin new-feature
```

<li> Create a pull request

### Bug/Feature Request
If you find any bug or have some idea about a new feature that can be implemented, you can either open an issue <a href='https://github.com/Sparab16/Extractor/issues' target="_blank">here</a> or you can directly mail us at advance-image-downloader@gmail.com.

Please include the sample queries and their corresponding results.

## <center>Tech Stack

### Project is built with:-

**Client:** 
- <a href='python.org' target="_blank">Python </a>
</a>
  
**Server:** 
- <a href='https://flask.palletsprojects.com/en/2.0.x/' target="_blank">Flask</a>
- <a href='https://www.selenium.dev/' target="_blank">Selenium</a>


  
## Authors

- [@Shreyas](https://github.com/Sparab16)
- [@Harshad](https://github.com/harshad5498)
  
## Optimizations

<li>Since the upto 2000 images are supported the filesize can get very large. That's why we have used the zip functionality to reduce the file size.</li>
<li>It is scalable as many users can request for images at the same time.</li>


## Feedback

If you have any feedback, please reach out to us at advance-image-downloader@gmail.com

  
## FAQ

#### Do user have to wait until images get downloaded?

Ans - No. User can simply submit the job and continue doing other tasks. Once the task ends zip file will get created at the user's end.

#### How much images can be downloaded at single go?

Ans - Upto 2000 images can be downloaded at single time. If more required we can simple submit the query again.


## Documentation

[High level design documentation](Docs/Advance_Image_Generator-HLD.pdf)<br>

[Low level design documentation](Docs/Advance_Image_Generator-LLD.pdf)<br>

[Wireframe](Docs/Advance-Image-Downloader_Wireframe.pdf)<br>

[Architecture](Docs/Advance_Image_Downloader-Architecture.pdf)

## License
MIT License

Copyright (c) [2021] [Shreyas Parab]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Thanks for reading out till the end. Hello, I'm Shreyas! 👨🏼‍💻
  
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shrey16/)

  