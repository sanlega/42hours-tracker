# 42Hours Tracker

42Hours Tracker is a Python script that calculates the total number of hours a student has spent at the 42 school using the 42 Intranet API. It uses the student's login name and retrieves their location statistics to determine the total time spent at the school.
## Prerequisites

To run this script, you need to have Python installed on your machine. The script has the following dependencies:
- requests

You can install them using pip:

```
Copy code
pip install -r requirements.txt
```


## Setup 
1. Obtain your `client_id` and `client_secret` from the 42 Intranet API. 
2. The `tokens.json` file is already included in the repo. Edit the file with the following content:

```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret"
}
```



Replace `your_client_id` and `your_client_secret` with the actual values obtained in step 1.
## Usage

To run the script, navigate to the repository directory in your terminal and run the following command:

```python
python main.py
```



The script will prompt you to enter the login of the student you want to target. After entering the login, the script will display the total hours spent by the student.
## Files

The repository contains the following files: 
- `main.py`: The main script to calculate the total hours a student has spent at the 42 school. 
- `token_generator.py`: A helper script to generate the access token required to access the 42 Intranet API. 
- `tokens.json`: A JSON file containing your API credentials. Edit this file with your own credentials before running the script. 
- `requirements.txt`: A list of required Python packages that can be installed using pip.
## Future Updates

We are constantly working to improve the 42Hours Tracker. In the future, we plan to:
- Convert the script into a web application for easier access and usage.
- Create a leaderboard to display the top users with the most hours spent at the school, promoting student engagement and attendance.
- Improve the accuracy of the tracking algorithm to cover more than just the last 4 months, providing a more comprehensive view of the student's time spent at the school.

