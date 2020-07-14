# put your code here.
import sys 
from collections import Counter

def count_words_in_file(filename):
    file = open(filename)
    f = file.read()
    # clean some punctuation
    f = f.replace("\n", " ").replace("'", " ").replace("(", " ").replace(")", " ").replace(":", "")
    f = f.replace(";", " ").replace("_", "").replace(".", " ").replace(",", " ").replace("-", " ").split(" ")
    # make it lower case, clean more punctuation
    f_cleaned = [word.lower().replace("?", "").replace("!", "").replace('"', "") for word in f]
    # make a Counter object
    dict_word = Counter(f_cleaned)
    # sort by word count using most common method
    # print(dict_word.most_common()[:100])
    # sort by either value, individually
    sorted_dict = sorted(dict_word.items(), key = lambda x: x[1], reverse=True)
    
    values_set = set(dict_word.values())
    new_sorted_dict = {}
    
    for value in sorted(list(values_set), reverse=True):
        same_value = []
        for key in dict_word.keys():
            if dict_word[key] == value:

                same_value.append(new_sorted_dict.get(value, key))
                same_value.sort()
        new_sorted_dict[value] = new_sorted_dict.get(value, same_value)
        for word in same_value:
            print(f"{word} {value}")
        
    return(dict_word)
    
    

if __name__ == '__main__':
    file_name = sys.argv[1]
    count_words_in_file(file_name)
