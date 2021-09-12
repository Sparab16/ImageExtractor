# <center>Extractor

Extractor library is useful to help the user download any kind of Images at any date and time over the internet. These images will get downloaded as a job and then let user know that the images have been downloaded.

## <center>Appendix

There are often a times, we need bunch images to work. We can consider the example such as training the Machine learning model over the Cat and Dog images or having those hundreds of beautiful desktop/mobile wallpaper on our laptop with just single click. In such scenario’s we need hundreds of images right away. This problem can be solved using the Extractor Library. The following use cases can be implemented: 
  
## <center>Features

- Upto 2000 images on single click
- Cross platform

## <center>Run Locally

### To download the Extractor, either fork this github repo or simply use Pypi via pip.

```bash
pip install ImageExtractor
```

### Using it

```python
from ImageExtractor.Extractor import ImageExtractorClass

image_extractor = ImageExtractorClass()
image_extractor.schedule_job('sample_search_query', 'YY-MM-DD', 'HH:MM', 100)

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

  