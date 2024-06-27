# Dictionary Search Application
Find word forms or get the definition of a word.
## For Users
- Download and Start: Download the program.exe file and start using the application immediately.
- Getting Help: Type `help` in the program to get started.
## For Developers
- Download the Source Code: Download the `source.py` file.
- Setup Instructions:
  + Install Python and an IDE: Ensure Python is installed on your system, including PyPI. Install an IDE (such as [Thonny IDE](https://thonny.org/)) for editing the source code.
  + Install Required Libraries: Open Command Prompt (CMD) and run the following command to install necessary libraries:
```
pip install beautifulsoup4 requests lxml
```
After completing these steps, you can begin developing the program.
- Compiling to an Executable File:
  + Install PyInstaller: Open Command Prompt (CMD) and run the following command:
  ```
  pip install pyinstaller
  ```
  + Compile the Source Code: Use the following command to compile the source code into an executable file:
  ```
  pyinstaller --onefile <path/to/source.py>
  ```
The executable file will be located in the `<working_dir>/dist/` directory. The `<working_dir>` is the path where you run the command from; it must be the path you see before you type a command.
