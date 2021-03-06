# put your code here.
import sys 

def count_words_in_file(filename):
    file = open(filename)
   
    dict_word_count = {}
    for line in file: 
        line = line.split(" ")
        for word_ in line:
            word_ = word_.lower().strip().replace(',', "").replace(".", "").replace(";", "").replace("?", "")
            dict_word_count[word_] = dict_word_count.get(word_, 0) + 1
    

      
    for key, value in dict_word_count.items():
        print(f'{key} {value}')
    # number of unique words
    print(len(dict_word_count.keys()))


if __name__ == '__main__':
    file_name = sys.argv[1]
    count_words_in_file(file_name)
