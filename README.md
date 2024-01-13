# Hogwarts Characters
#### Video Demo:  <https://youtu.be/rZ113j4YSuw>
#### Description
This project is a part of the final project for the cs50 Python course at Harvard. The project is designed to interact with an API that contains characters from the Harry Potter story. The goal is to extract specific information such as name, house, and year of birth from the API data. The extracted data is then processed to eliminate incomplete or empty records. The cleaned data is stored in a CSV file with fields for first name, last name, house, and age.

The project includes 4 functions in addition to the main function:
1. Function for retrieving the API data
2. Function for searching characters by name
3. Function for validating command line arguments
4. Function for calculating age based on the current date and time

Additionally, there is a test_project.py file to validate the functionality of these functions.

## Installation and Usage
To run the project, make sure you have project.py and test_project.py in your project root directory. You'll also find this README.md file and a requirements.txt for library installation instructions.

#### Installation
1. Install the required libraries specified in requirements.txt:

bash
   pip install -r requirements.txt


#### Usage
- Use the following command to run the project and store the data in a CSV file named wizards.csv (or a name of your choice, but it should be a CSV file):

bash
  python project.py wizards.csv


- To run the tests, execute the following command after installing pytest:

bash
  pytest test_project.py


Note: Python should be installed in your system before running the project or tests.

## Future Improvements
Potential future enhancements for the project include:
- Building a visual frontend
- Improving search functionality for all fields

## Contact Information
- YouTube Channel: [Link to the video demo](https://youtu.be/rZ113j4YSuw)
- Name: Elham Hosseini
- Email: xxfaveen6@gmail.com

## Acknowledgements
Special thanks to Harvard's cs50 Python course for the knowledge and inspiration to develop this project.
