from File_writer import File_writer
from Process_file import ProcessFile

"""
Program Name: Lab7.py (Group 5 project)
Course: IT3883/Section W01
Student Name: Vongai Kwenda, Crystal Misko, Opeyemi Faronbi.
Assignment Number: Lab7
Due Date: 12/05/2023
"""


# ************* Code by Crystal Misko **************
if __name__ == "__main__":
    # classes instances.
    process_file = ProcessFile()
    file_writer = File_writer()

    # Read the content of the President Washington Inaugural Speech text file.
    try:
        words = process_file.read_file('President_Washington_Inaugural_Speech.txt')
        print("The file content was successfully read.")
    except Exception as e:
        print(f"Error: {e}")

    # Extract the next word after 'the'.
    next_word = process_file.extract_next_word(words)

    # Adds the extracted word to the extracted_words list.
    file_writer.add_to_list(next_word)

    # Write the list to a file.
    try:
        file_writer.write_to_file('Extracted_words_after_the.txt')
        print("Extracted words was successfully written to 'Extracted_words_after_the.txt'")
    except Exception as e:
        print(f"Error: {e}")
