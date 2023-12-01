class Process_file:
    def read_file(self, file_name):  # reads the file.
        with open(file_name, 'r') as file:
            file_content = file.read()
        return file_content
