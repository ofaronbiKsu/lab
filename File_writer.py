# ************* Code by Opeyemi Faronbi **************

class File_writer:
    def __init__(self):
        self.extracted_words = []

    def add_to_list(self, word):
        self.extracted_words.extend(word)

    def write_to_file(self, file_name):  # Write to new file.
        with open(file_name, 'w') as file:
            for word in self.extracted_words:
                # Removes ', and .' after the word and capitalized it.
                format_word = word.strip(",.").capitalize()
                file.write(format_word + '\n')
