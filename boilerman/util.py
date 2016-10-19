from sys import stdout, exit

def prompt(text):
    """Writes a prompt message and returns the user's answer"""
    stdout.write(text)
    return input()
    
def load_file_as_str(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except IOError as ex:
        exit("Template file %s not found!" % path)