# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file_open = open("./story.txt","r")
    read_file_content = file_open.read()

    print(read_file_content(filename))
    #return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    t_split = text.split
    print(t_split)
    return {"as": 10, "would": 20}