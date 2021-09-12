from distutils.core import setup
setup(
  name = 'Extractor',
  packages = ['Extractor'],
  version = '1.0',
  license='MIT',
  description = 'Extractor library is useful to help the user download any kind of Images at any date and time over the internet. These images will get downloaded as a job and then let user know that the images have been downloaded.',
  author = 'Shreyas Parab',
  author_email = 'shreyas.parab16@gmail.com',
  url = 'https://github.com/Sparab16/Extractor',
  download_url = 'https://github.com/Sparab16/Extractor/archive/refs/tags/v1.0.tar.gz',
  keywords = ['Python', 'Selenium', 'Flask', 'Scheduling', 'Extract', 'Image Extract'],   # Keywords that define your package best
  install_requires=[
          'apscheduler',
          'configparser',
          'python-dateutil'
          'requests',
          'selenium',
          'urllib3',
          'webdriver-manager',
          'zipp'
          ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)