# RealmEye-Character-Delogger
RealmEye Character Delogger is a Python script that automatically sets your character(s) on your RealmEye as "Dead". 

Want to keep your RealmEye page fully public, but don't want characters and fame history to update? 

## Requirements

- Python 3.x or higher installed. You can download it from [here](https://www.python.org/downloads/).
-RealmEye Profile. You can obtain a password to your RealmEye by messagin [MrEyeball](https://www.realmeye.com/mreyeball) in-game.

## Installation

1. Clone the repository or download the script directly.

    ```bash
    git clone https://github.com/WhaleOTE/Steam-Status-Tracker.git
    ```

2. Install the necessary dependencies using pip.

    ```bash
    pip install requests
    ```

    ## Configuration

Before running the script, you need to edit the code to include your RealmEye Username, Password, and characters to automatically remove. Follow the steps below:

1. Open the script file `REdelog.py` in a text editor.

2. Locate the following lines and replace the placeholder values with your RealmEye username and password:

    ```python
    username = "yourusername"
    password = "yourpassword"

    character_ids = {
    784: "Priest",
    782: "Wizard",
}
    ```

## How to Run

Open command prompt and navigate to the directory where the script is located. Then, run the following command:

```bash
python REdelog.py
```

If `python` isn't recognized, try `py` instead. The script will start monitoring the status of the Steam IDs and will log the data in the specified log files. You can stop the script at any time by pressing `Ctrl + C` in the terminal.
