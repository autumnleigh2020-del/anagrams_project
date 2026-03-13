import sys

def load(file):
    """Open a text file & return a list of lower case strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.")
        sys.exit(1)