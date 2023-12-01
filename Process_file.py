# ************* Code by Vongai Kwenda **************
# class to process file
class ProcessFile:
    # Created a read file method to read president speech file and return it as string
    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            content = file.read()  # content is a string
        # return file content
        return content

    # Method to analyze the string.
    # This extract_next_word method is for taking string as input and splitting to words
    def extract_next_word(self, text):
        words = text.split()  # split string into words and storing it in words list
        next_words = []  # list created
        for i in range(len(words) - 1):
            # so words that come after the word "the" are extracted
            if words[i].lower() == "the":  # .lower() used to make comparison case-insensitive
                next_word = words[i + 1]  # temporarily stores each word that comes after "the"
                #  stored in next_words list
                next_words.append(next_word)
        # return next_words list
        return next_words
