**Appium Automated Mobile Testing** 

**Description:**

> This project demonstrates automated mobile testing using Appium with Python. It focuses on testing the Android ApiDemos application, showcasing how to automate various user interactions like swipes, scrolls, and navigation.

**Table of Contents:**

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Configuration](#configuration)
* [Usage](#usage)
* [Testing Scenarios](#testing-scenarios)
* [Folder Structure](#folder-structure)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

**About the Project:**

> This project provides a set of automated tests for the Android ApiDemos application using Appium and Python. The tests cover essential user interactions, including:
>
> * Navigation between app screens.
> * Swipe gestures.
> * Scroll actions.
> * Verification of element interactions.
>
> The project is designed to be a learning resource for those new to Appium and mobile test automation.

**Getting Started:**

**Prerequisites:**

> Before you begin, ensure you have the following installed:
>
> * Python (3.7 or later)
> * Android SDK and Android Studio
> * Appium Server (2.0 or later)
> * Node.js and npm (if installing Appium via npm)
> * An Android emulator or a real Android device

**Installation:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Muthoni69/adb_project
    cd <your_project_directory>
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```
3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    (Create a `requirements.txt` file with `selenium` and `Appium-Python-Client` inside)
4.  **Install Appium Server:**
    ```bash
    npm install -g appium@latest #If using npm
    ```

**Configuration:**

1.  **Set up your Android emulator or connect your real device.**
2.  **Start the Appium server:**
    ```bash
    appium
    ```
3.  **Update the `android_setup.py` file with your device and app details:**
    * `deviceName`
    * `appPackage`
    * `appActivity`
    * `app` path

**Usage:**

> To run the tests, execute the following command:
>
> ```bash
> python swipe_actions.py # or scroll_actions.py
> ```
>
> This will execute the automated tests defined in the Python scripts.

**Testing Scenarios:**

> The project includes tests for the following scenarios:
>
> * Swiping left to right and right to left within a gallery.
> * Navigating to specific screens within the ApiDemos app.

**Folder Structure:**

```
apidemos/
├── android_setup.py     # Appium driver setup and common methods
├── swipe_actions.py     # Test scripts for swipe gestures
├── scroll_actions.py    # Test scripts for scroll actions
├── requirements.txt     # Python dependencies
└── README.md
```


