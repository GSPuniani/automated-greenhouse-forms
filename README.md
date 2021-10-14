<h1 align="center">Automated greenhouse.io Forms</h1>

<p align="center">
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/GSPuniani/automated-greenhouse-forms" />
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/GSPuniani/automated-greenhouse-forms" />
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/GSPuniani/automated-greenhouse-forms" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/GSPuniani/automated-greenhouse-forms" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/GSPuniani/automated-greenhouse-forms" />
</p>


- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)


## Project Overview

Many job application forms are hosted on a subdomain of greenhouse.io. However, the process of filling out forms on greenhouse.io can be unnecessarily time-consuming and tedious. Job applicants must manually type out their personal information for each application. Unfortunately, it is not possible to save this information because applicants cannot create accounts on greenhouse.io (only recruiters can). 

This project is an attempt to automate the process of filling out these greenhouse.io forms. Instructions for downloading and running the Python script are included below.



## Requirements

The installation instructions are for machines running macOS (e.g. MacBook, MacBook Pro, iMac, etc.). This project has not been tested on devices running other operating systems, but the script should be able to work after making some minor modifications.


## Download, Install, and Run

Here is a step-by-step guide for downloading, installing, and running this project. This is meant to be a set of exhaustive instructions to allow anyone to use this project, regardless of experience with Terminal or running code.

### Download

### Set Up .env File

### Change Browser

There are currently three options for your browser choice: Safari, Chrome, and Firefox. You can run the script as is if you want to use Firefox, since it is the default option. If you would prefer to use Safari or Chrome, follow the respective instructions below.

#### Safari

- Uncomment this line: `browser = webdriver.Safari()`. (Uncommenting a line means removing the hashtag and empty space from its immediate left.) 
- Comment out this line: `browser = webdriver.Firefox()`. (Commenting out a line means adding a hashtag to its immediate left.)
- Open a Safari window, click on the "Develop" in the menu bar at the top, and make sure that the option for "Allow Remote Automation" has a checkmark next to it. You can click on it to enable it if the check mark is absent.
    -  Note: If your menu bar does not have a "Develop" menu between "Bookmarks" and "Window", then you can enable it by clicking on the "Safari" menu, opening "Preferences", selecting the "Advanced" tab on the far-right, and then clicking the checkbox at the bottom to "Show Develop menu in menu bar".


#### Chrome

- Uncomment this line: `browser = webdriver.Chrome()`. (Uncommenting a line means removing the hashtag and empty space from its immediate left.) 
- Comment out this line: `browser = webdriver.Firefox()`. (Commenting out a line means adding a hashtag to its immediate left.)
- Download the appropriate version of ChromeDriver by finding the one that matches your system [here](https://chromedriver.chromium.org/downloads).
    - Unless you feel comfortable modifying the `chromedriver_location` line of the script, you should save the downloaded file in your Downloads folder. 
- In the `.env` file that you set up earlier, change the value for `USER` to match your username for logging on to your machine. If you are unsure what your username is, then click the Apple logo on the far-left of the menu bar at the top of the screen, and look for the name at the bottom of the menu immediately to the right of "Log Out". 


### Run

## License

This project is released under the MIT license. 
