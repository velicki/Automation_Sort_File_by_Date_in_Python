# Sort File by Date

The "Sort File by Date" project is a Python-based automation tool designed to simplify the process of managing and sorting files based on their modification dates. This project is particularly useful for tasks involving a large volume of files with varying modification dates.

___________________________________________________

# WHAT I HAVE LEARNED?


While developing the "Sort File by Date" script, I gained valuable insights and learned important lessons that enhanced my understanding of file management, automation, and Python programming. Here's what I learned:

1. File Handling: Working on this project provided me with practical experience in file handling operations using Python. I learned how to read file paths, check modification dates, and move files between directories programmatically.

2. Date Formatting: Understanding how to format dates in Python was essential for creating destination folders named by modification date (%Y-%m-%d). I learned how to utilize Python's datetime module to format dates according to specific requirements.

3. Folder Creation: Automating the creation of destination folders based on modification dates taught me how to interact with the file system using Python. I gained experience in dynamically creating folders and managing directory structures within a script.

4. Conditional Logic: Implementing conditional logic to check if destination folders exist and create them if necessary improved my understanding of control flow in Python. I learned how to use if statements and logical operators to make decisions based on certain conditions.

5. File Movement: Developing the functionality to move files to the appropriate destination folders based on their modification dates honed my skills in file manipulation. I learned how to use Python's shutil module to perform file operations such as moving files between directories.

6. Error Handling: Implementing error handling mechanisms to handle potential exceptions, such as file not found errors or permission issues, enhanced the robustness of the script. I learned how to use try-except blocks to gracefully handle errors and prevent script crashes.

7. Analytics Calculation: Calculating and displaying analytics at the end of the sorting process provided me with insights into data analysis and reporting in Python. I learned how to aggregate and analyze data to derive meaningful insights and present them in a structured format.

8. Project Organization: Structuring the script into modular functions and organizing code logically improved code readability and maintainability. I learned the importance of code organization and the benefits of breaking down complex tasks into smaller, more manageable components.

Overall, developing the "Sort File by Date" script was a rewarding learning experience that allowed me to apply Python programming concepts to solve real-world problems related to file management and automation. It equipped me with practical skills that are valuable for future projects and helped me become a more proficient Python developer.
___________________________________________________


# Features:


Folder Path Input: The program prompts the user to input the folder path where the files to be sorted are located.

Destination Folder Input: Users can specify the destination folder where they want to move and organize the files.

Automatic Folder Creation: Inside the desired destination folder, the script automatically creates destination folders named by modification date (%Y-%m-%d) if they don't already exist.

File Movement: The script moves each file to the corresponding destination folder based on its modification date.

Analytics: At the end of the process, the script provides analytics such as:
    Number of created folders
    Number of files moved into the folders
    Number of files in the folder with the most files
    Average number of files per folder

___________________________________________________


# Usage:


-Run the script sort_file_by_date.py.

-Enter the folder path where the files to be sorted are located.

-Specify the destination folder where you want to move and organize the files.

-The script will create destination folders based on modification dates and move the files accordingly.

-After completion, the script will display analytics summarizing the sorting process.

___________________________________________________


# Dependencies:


This project requires Python 3.x to run. There are no additional dependencies or external libraries required.

___________________________________________________


# Disclaimer:


This tool is provided as-is, without any warranties or guarantees. Users are advised to use caution when running automation scripts and ensure that they understand the implications of file manipulation actions.