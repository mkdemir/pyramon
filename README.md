# PYRAMON

PYRAMON is a powerful tool for performance testing and query analysis in MongoDB databases. It is designed to evaluate the performance of your database and analyze queries in it.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Installation

1. Install and configure MongoDB.
   * For more information on MongoDB installation, please refer to its documentation.
2. Clone the Pyramon repository:
   * git clone [https://github.com/mkdemir/pyramon.git](https://github.com/mkdemir/pyramon.git)
3. Install the dependencies:
   * Windows - PowerShell: Run the following command to install Pyramon on Windows using PowerShell
   `.\setup_powershell.ps1 -PythonVersion "3.11" -EnvName "venv" -RequirementsFile ".\requirements.txt"`
      - PythonVersion specifies the Python version to be installed.
      - EnvName specifies the name of the virtual environment to be created.
      - RequirementsFile specifies the path to the requirements file that contains the dependencies.
   * Linux/Unix - Shell script: Run the following command to install Pyramon on Linux/Unix using a shell script
   `./setup_linux.sh`

## Usage

1. Navigate to the `pyramon/src/` directory in your terminal.
2. Enter the necessary information into your .env file.
3. Run the command `../venv/bin/python3 main.py` to start the script.
4. The script will start running and retrieving information from MongoDB.
5. When the script finishes, it will stop execution.
6. You can find the files containing the information under the **data/data_log/** folder.

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the **MIT License** - see the **[LICENSE](https://github.com/mkdemir/pyramon/blob/main/LICENSE)** file for details.