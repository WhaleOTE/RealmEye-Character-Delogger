
![REdelog](https://github.com/WhaleOTE/RealmEye-Character-Delogger/assets/148757860/0263473a-98d8-475d-b0ef-5d0b593da7a0)

# RealmEye-Character-Delogger
RealmEye Character Delogger is a Python script that automatically sets your character(s) on your RealmEye Page as "Dead" every minute.

    1. Sends a login POST request to RealmEye
    2. Logs the session cookie that is provided when you login to RealmEye
    3. Sends a delete character POST request to RealmEye using the session cookie
    4. Repeats every minute for 60 iterations (1 hour)
    5. Sends a logout POST request to RealmEye using your current session cookie for verification
    6. Sends another login POST request to RealmEye and repeats
    
Want to keep your RealmEye page fully public, but don't want your characters and fame history to update? 

## Requirements

- Python 3.x or higher installed. You can download it from [here](https://www.python.org/downloads/).
- RealmEye Profile. You can obtain a password to your RealmEye by messaging [MrEyeball](https://www.realmeye.com/mreyeball) in-game.

## Installation

1. Clone the repository or download the script directly.

    ```bash
    git clone https://github.com/WhaleOTE/RealmEye-Character-Delogger.git
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
    
3. Here is a list of all character IDs. Add them to the current list above to include more characters. By default, the script will remove your Priest and Wizard from your RealmEye

    ```python
    768: "Rogue",
    775: "Archer",
    782: "Wizard",
    784: "Priest",
    785: "Samurai",
    796: "Bard",
    797: "Warrior",
    798: "Knight",
    799: "Paladin",
    800: "Assassin",
    801: "Necromancer",
    802: "Huntress",
    803: "Mystic",
    804: "Trickster",
    805: "Sorcerer",
    806: "Ninja",
    817: "Summoner",
    818: "Kensei",
    ```



## How to Run

Open command prompt and navigate to the directory where the script is located. Then, run the following command:

```bash
python REdelog.py
```

If `python` isn't recognized, try `py` instead. The script will automatically set your character(s) on your RealmEye Page as "Dead" every minute.
