import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name="ImageExtractor",
    author="Shreyas Parab",
    version = '1.2.1',
    author_email="shreyas.parab16@gmail.com",
    description="ImageExtractor library is useful to help the user download any kind of Images at any date and time over the internet. These images will get downloaded as a job and then let user know that the images have been downloaded.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sparab16/Extractor",
    download_url="https://github.com/Sparab16/Extractor/archive/refs/tags/v1.1.tar.gz",
    packages=['ImageExtractor'],
    package_data={'': ['**/*.py']},
    keywords = ['Python', 'Selenium', 'Flask', 'Scheduling', 'Extract', 'Image Extract'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[
        'apscheduler',
        'configparser',
        'python-dateutil',
        'requests',
        'selenium',
        'urllib3',
        'webdriver-manager',
        'zipp'
    ],
    python_requires='>=3.6',
)