<div align="center">
  <a href="https://github.com/jmlackner/LOAFR">
    <img src="https://github.com/jmlackner/LOAFR/blob/main/loafr.jpg"
         alt="Logfile Analysis Framework Logo">
  </a>
<h3 align="center">Logfile Analysis Framework (LOAFR)</h3>
  <p align="center">
    A central framework for log analysis, testing, and validation.
  </p>
</div>

# LOAFR - Log Analysis Framework

## Overview
LOAFR (Log Analysis Framework) is a Python-based software system designed to facilitate log file analysis. It enables users to perform various operations like searching, sorting, and filtering log entries efficiently.

## Getting Started
Follow these steps to execute the LOAFR system on your local machine.

### Prerequisites
- Install the latest version of Python, if it is not already installed on your computer. You can [download Python here](https://www.python.org/downloads/).
- To check if you already have Python installed, open a command line terminal and enter `python --version`. In order to use LOAFR, you should see output containing: `Python 3.x.x` where the x's can be any number.

### Installation

#### From GitHub
**NOTE** The LOAFR GitHub repository is currently private.
1. Clone or download the LOAFR repository to your local machine.

#### From a Compressed File
1. After downloading the compressed LOAFR file, extract the contents of the .zip file to a convenient location on your computer.
2. Once the extraction of the file contents is complete, you will be able to use LOAFR.

### Usage
1. Open a terminal or command prompt and navigate to the directory in which you have downloaded LOAFR.
2. Run the following command to execute LOAFR: `python loafr.py` or `python3 loafr.py`
3. LOAFR 0.2 only supports an interactive command line interface mode. Follow the on-screen instructions to interact with the system.

### Walkthrough Example

LOAFR is useful for test engineers to quickly find relevant information in log files. Imagine you are a test engineer looking for potential errors that may have been logged by your system. You know these errors are logged with a "WARN" tag, but you need to quickly get a list of all errors and don't want to manually go through the log files. Your current log file may look like this:

![image](https://github.com/jmlackner/LOAFR/blob/main/docs/example_log.png)

Once you have LOAFR set up on your computer, you can launch LOAFR using the `python loafr.py` command from the directory LOAFR is installed in.

![image](https://github.com/jmlackner/LOAFR/blob/main/docs/step01.png)

LOAFR will prompt you for the information it needs. Here, we search a log file for all log entries that contain the "WARN" tag:

![image](https://github.com/jmlackner/LOAFR/blob/main/docs/step02.png)

This conveniently saves all log entries with a "WARN" tag to an output log file, helping the test engineer in their analysis.

![image](https://github.com/jmlackner/LOAFR/blob/main/docs/step03.png)

## Log File Anlysis

Version 0.2 of LOAFR offers six different anlysis functions, which can be used by themselves or in sequence in order to perform advanced log file analysis. Currently, the only version of LOAFR that is implemented is an interactive command line interface. You can follow the prompts given after running LOAFR in order to use the log file analysis functions.

### Search

- Search for specific keywords in log files.
- **Function Name:** SEARCH
- **Arguments:** A comma-separated list of case-sensitive keywords to search for.
- **Output:** A log file with only the entries of the input file that contain one or more of the keywords. If no entries are found in the input log files that match any of the search keywords, the output will be empty.

### After

- Contextual analysis function, used to find log entries starting from a log entry that matches a condition.
- **Function Name:** AFTER
- **Arguments:** \[EQUALITY OPERATOR\] \[VALUE\], where EQUALITY OPERATOR can be any of the following: less than (<), less than or equal to (<=), equal to (==), greater than or equal to (>=), greater than (>), or not equal to (!=). VALUE is the value that the log entry should be checked against in order to determine whether or not the current and subsequent entries should be included in the output. VALUE must be a number.
- **Output:** A log file with only the entries of the input file that occur after a log value matches the AFTER function value, including the log entry that matches the condition. NOTE: If the condition is never met, the output will be empty.

### Before

- Contextual analysis function, used to find log entries up to a log entry that matches a condition.
- **Function Name:** BEFORE
- **Arguments:** \[EQUALITY OPERATOR\] \[VALUE\], where EQUALITY OPERATOR can be any of the following: less than (<), less than or equal to (<=), equal to (==), greater than or equal to (>=), greater than (>), or not equal to (!=). VALUE is the value that the log entry should be checked against in order to determine whether or not the subsequent entries should be excluded in the output. VALUE must be a number.
- **Output:** A log file with only the entries of the input file that occur before a log value matches the BEFORE function value, excluding the log entry that matches the condition. NOTE: If the condition is never met, all entries from the input log file(s) will be included in the output.

### Sort

- Sort log entries based on specified columns.
- **Function Name:** SORT
- **Arguments:** \[COLUMN\] \[DIRECTION\] = asc, where COLUM is the column to be sorted by. DIRECTION is ascending by default, but also takes the value "desc" to reverse the order
- **Output:** A log file with only the entries of the input file that occur with COLUMN sorted in DIRECTION.

### Count

- Count the number of log entries that contain a keyword.
- **Function Name:** COUNT
- **Arguments** \[KEYWORD\], where KEYWORD is the word that should be searched for in log entries and used to determine if that log entry should be included in the count.
- **Output:** The number of log entries that contain the given keyword.

### High-and-Low ("HNL")

- Get log file entries starting when a log value dips below a given low value, and ending when the log value returns to another value. Used for tracking down log entries indicating a user is in a hypoglycemic state.
- **Function Name:** HNL
- **Arguments:** \[EVENT_TYPE\], \[HIGH\], \[LOW\] - a comma-separated string where EVENT_TYPE is the event type that high-low values should be checked for. Output of log entries begins when the value for a log entry of type EVENT_TYPE dips below LOW, and finishes when the value returns to HIGH.
- **Output:** The set of log entries between the low and high values, including entries that might not belong to the given EVENT_TYPE.
- **Note:** EVENT_TYPE is only used to determine when the high and low values should be used to indicate the beginning and end point for outputting log entries.

## Update History

### 0.2
- Added the ability the find the start time, end time, and duration between events that are 
  triggered by high and low values. For example, users can identify periods of hypoglycemia (HNL function).
- Added the ability to count the number of rows in a log file, or log analysis file, where a
  keyword appears (COUNT function).
- Added the ability to select log file entries occuring before and/or after a log entry that meets a user-defined equality or inequality condition (AFTER and BEFORE functions).

### 0.1
- Initial release.
- Added support for searching a log file for one or more keywords.

## Interactive Demo/Video Tutorial

An interactive demo or video tutorial showcasing LOAFR's capabilities is planned for future release.

## Credits

- The LOAFR bread logo is used, freely under the Unsplash License, from https://unsplash.com/photos/baked-bread-beside-knife-on-wooden-board-NYRuUS8iNWc
