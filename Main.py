from File_writer import File_writer
from Process_file import Process_file
from File_analyzer import File_analyzer

if __name__ == "__main__":
    # classes instances.
    process_file = Process_file()
    string_analyzer = File_analyzer()
    file_writer = File_writer()

    # Read the content of the President Washington Inaugural Speech text file.
    try:
        words = process_file.read_file('President_Washington_Inaugural_Speech.txt')
        print("The file content was successfully read.")
    except Exception as e:
        print(f"Error: {e}")

    # Extract the next word after 'the'.
    next_word = string_analyzer.extract_next_word(words)

    # Adds the extracted word to the extracted_words list.
    file_writer.add_to_list(next_word)

    # Write the list to a file.
    try:
        file_writer.write_to_file('Extracted_words_after_the.txt')
        print("Extracted words was successfully written to 'Extracted_words_after_the.txt'")
    except Exception as e:
        print(f"Error: {e}")
