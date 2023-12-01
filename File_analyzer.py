class File_analyzer:
    def extract_next_word(self, text):  # Extracts the next word after 'the'.
        words = text.split()
        # Get the index of 'the' in the text file then return it as a list.
        the_word = [i for i, word in enumerate(words) if word.lower() == 'the']
        extracted_word = []
        for index in the_word:  # Loop through the index and save the next word after the index.
            if index + 1 < len(words):
                extracted_word.append(words[index + 1])

        return extracted_word
