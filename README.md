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
- [Download, Install, and Run](#download,-install,-and-run)
- [License](#license)


## Project Overview

Many job application forms are hosted on a subdomain of greenhouse.io. However, the process of filling out forms on greenhouse.io can be unnecessarily time-consuming and tedious. Job applicants must manually type out their personal information for each application. Unfortunately, it is not possible to save this information because applicants cannot create accounts on greenhouse.io (only recruiters can). 

This project is an attempt to automate the process of filling out these greenhouse.io forms. Instructions for downloading and running the Python script are included below.



## Requirements

The installation instructions are for machines running macOS (e.g. MacBook, MacBook Pro, iMac, etc.). This project has not been tested on devices running other operating systems, but the script should be able to work after making some minor modifications.


## Download, Install, and Run

Here is a step-by-step guide for downloading, installing, and running this project. This is meant to be a set of exhaustive instructions to allow anyone to use this project, regardless of experience with Terminal or running code.


### Download

On this page, click the arrow on the green "Code" button towards the top-right, and click "Download .zip". You will then be prompted on where you would like to save the project. Next, open the project in an IDE. I recommend opening the project in Visual Studio Code, which you can download [here](https://code.visualstudio.com) by following the instructions on that page.


### Set Up config.yml File

After opening the project in Visual Studio Code (or any other IDE), rename the `template.yml` file to `config.yml` by hitting the control key and clicking simultaneously (control + click). Then, fill in the appropriate values between each pair of double-quotes as you would for the actual form (first name, last name, etc.). Note that values for drop-down menus must match an exact value as it appears in the form. 


### Install Necessary Packages

This project uses [Python 3](https://www.python.org/downloads/), along with two third-party modules: `Selenium` and `PyYAML`. To install these two modules, first click and drag upwards from the blue bar at the bottom of the Visual Studio Code window to bring up the Terminal. In the Terminal, type the following commands (wait until the first one is completed before typing the next command):
`pip3 install selenium`
`pip3 install pyyaml`

The `Selenium` module allows us to automate the filling out of web forms, and the `PyYAML` module allows us to use YAML files in our Python project.


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


### Run

Now that the `config.yml` file has been updated, we can now run the script. In Visual Studio Code (or your IDE of choice), open the `script.py` file, and then click the "Run" button in the top-right corner (it should be a right-facing triangle icon that looks like a "Play" button). A new window will automatically open in your browser of choice, and then the form should automatically populate with the values from your `config.yml` file. 

If you attempt to interact with the new window while using Safari, you may encounter a pop-up that asks whether you want to continue running the automated session. In this case, click "Stop Session" so that you can manually submit the form. 

<i>Note that the form is not automatically submitted so that you have a chance to review it before submission.</i>


## License

This project is released under the MIT license. 
