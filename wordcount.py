# put your code here.
"""
Defines a function to input .txt file and outputs word counts in file.
"""

# define function, with file
def count_words(filename):
    """Open a file and count how many times each space-separated word occurs in the file. 
    Print the counts to the screen. """

    # create empty list and dictionary
    all_words = []
    word_count = {}

    # open .txt file
    txt_file = open(filename)
     #get separate words in the file
     # take text file and strip out spaces
    
    for line in txt_file:
        split_line = line.rstrip().split(' ')
        #  print(split_line)
        for word in split_line:
            all_words.append(word)
    # print(all_words) 

    for word in all_words:
        word_count[word] = word_count.get(word , 0) + 1

    #print(word_count) 

def print_dict(word_count)
    for word, count in word_count.item():
    print(word, count)

# Call the function with this text file
count_words('test.txt')
