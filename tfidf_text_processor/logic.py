#!/usr/bin/env python

from numpy import log10
import pandas as pd

file_name = "text.txt"

def read_words(file):
        words = file.read().replace("\n"," ").replace(",","").replace(".","").replace(";","").replace("--", ' ').replace('\"', '').lower()
        return filter(lambda a: a != '', words.split(" "))


def create_df(words_multydict):
    words = words_multydict['words'] 
    tf = words_multydict['tf'] 
    idf = words_multydict['idf'] 
    # s1 = pd.Series(words.items())
    df = pd.DataFrame(words_multydict)

    # df = pd.DataFrame(columns = ['word', 'tf', 'idf'])
    # df['word'] = words
    # df['tf'] = tf.values()
    # df['idf'] = idf.values()
    return df


def count_words(words):
    words_count = {'TOTAL_WORDS': 0}
    for word in words:
        if not word in  words_count:
            words_count[word] = 1
        else:
            words_count[word] +=1
        words_count['TOTAL_WORDS'] +=1
    return words_count


def words_get_freq(words_count):
    words_parameters = dict()
    for word in words_count.keys():
        words_parameters[word] = words_count[word]/words_count['TOTAL_WORDS']
    return words_parameters


def count_files_for_word(words, words_file_count):
    for word in words:
        if not word in words_file_count.keys():
            words_file_count[word] = 1
        else:
            words_file_count[word] +=1
    return words_file_count


def main(file_array : dict, file_id : int = 0):
    file_id = int( file_id)
    docks = 0
    words_file_count = dict()
    words_multydict = dict()
    
    for file in file_array.keys():
        docks += 1
        words = read_words(file_array[file])
        words_count = count_words(words)
        words_tf = words_get_freq(words_count)
        words_file_count = count_files_for_word(words_count.keys(), words_file_count)
        words_multydict[file] = {'words': words_count, 'tf': words_tf} 

    words_global_idf = dict()

    for word in words_file_count.keys():
        words_global_idf[word] = log10(docks/words_file_count[word])
        # words_global_idf[word] = docks/words_file_count[word]

    for file in words_multydict.keys(): 
        words_local_idf= dict()
        for word in words_multydict[file]['words'].keys():
           words_local_idf[word] = words_global_idf[word] 
        words_multydict[file] = {'words': words_multydict[file]['words'], 'tf': words_multydict[file]['tf'], 'idf': words_local_idf} 
    return create_df(words_multydict[file_id])



def file_handle(file_array):
    new_dict = {}
    for file in range(len(file_array)):
        f = open(file_array(file), 'r')
        new_dict[file] = f
    main(new_dict)





if __name__ == "__main__":
    print(main([file_name,'text2.txt']).head(20))







