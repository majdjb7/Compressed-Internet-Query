"""
Names: Majd Jaber, ID: 208488692
"""

import os
import pandas as pd
import shutil
import string
import struct
import sys
from operator import itemgetter
import csv
import stat

import errno
import re


# Function that creates lists of alphabetical tokens database, saving the tokens in each text
def create_alphabetical_database(text, review_counter, a_dict):
    exists = False  # Variable that checks if word is already in the dictionary
    create_new = False
    # Here we make all words lowercase, then separate them
    text2 = text.lower()
    text2.translate(string.punctuation)
    regex = r'\w+'

    word_list = re.findall(regex, text2)

    for each_word in word_list:
        new_word = each_word[0:25]

        w_frequency = 0  # The overall word frequency
        appear_in_review = 0  # Represents frequency of word in each individual review
        appearances = []  # Will contain all review IDs and frequency of the word for each review
        for all_words in range(len(a_dict)):
            # If this product is already in dictionary or not, we determine here and assign boolean to it
            if new_word == a_dict[all_words]["word"]:
                exists = True
                break
            else:
                exists = False

        # If the word isn't saved in our dictionary
        if not exists:
            w_frequency += 1
            appear_in_review += 1

            per_review = (review_counter, appear_in_review)


            appearances.append(per_review)

            item = {'word': new_word,
                    'frequency': w_frequency,
                    'Appearances (ReviewId, Frequency)': appearances}
            a_dict.append(item)
        # IF the word is in the dictionary
        elif exists:
            appear_in_review += 1
            per_review = (review_counter, appear_in_review)

            length = len(list(a_dict[all_words]["Appearances (ReviewId, Frequency)"]))

            a_dict[all_words]["frequency"] += 1

            change = a_dict[all_words]["Appearances (ReviewId, Frequency)"][length - 1]
            if change[0] == review_counter:
                y = list(change)
                y[1] += 1
                appear_in_review += 1
                change = tuple(y)
                a_dict[all_words]["Appearances (ReviewId, Frequency)"][length - 1] = change
                appear_in_review +=1
            else:
                appearances.append(per_review)
                a_dict[all_words]["Appearances (ReviewId, Frequency)"] += appearances
        else:
            pass

#Function that counts the total size of tokens from all the texts
def token_counter(counter, text2):
    temp = 0
    text2.translate(string.punctuation)
    regex = r'\w+'
    word_list = re.findall(regex, text2)

    for each_word in word_list:
        temp += 1
    return temp


#Create the first file, our general database for all features relating to the product ID
def create_general_review_database(dictionary, dir2):
    data = pd.DataFrame(dictionary)

    # ----------------------------------------------------------------------------------------------------------- #
    # ---------------- Here we set the path of the directory for this file and all following files ----------------
    # Parent Directories
    parent_dir = os.getcwd()


    # Path
    path = os.path.join(parent_dir, dir2)

    if os.path.exists(path):  # If path exists already, delete it and create new one
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)

    # ----------------------------------------------------------------------------------------------------------- #
    data.to_csv(path + r'\All_Data.csv', index=False)


# Function that creates our third file (database) containing only total sum of reviews, and total token size
def create_special_database(dictionary, dir2):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir2)
    data = pd.DataFrame(dictionary)
    data.to_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv', index=False)


# Function that creates our fourth file (database) containing product IDs and all the reviews belonging to each one
def create_product_review_database(dictionary, dir4):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir4)
    data = pd.DataFrame(dictionary)
    data.to_csv(path + r'\ProductIDs_and_Reviews.csv', index=False)


def create_file_alphabetical(dictionary2, dir2):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir2)
    data2 = pd.DataFrame(dictionary2)
    data2.to_csv(path + r'\token_dictionary.csv', index=False)


# This function checks for a common prefix in the 9-in-10 front coding dictionary and returns new word with prefix #
def check_prefix(first_word, normal_word):
    prefix = 0
    common = ''
    for i in range(len(normal_word)):
     #####   print(normal_word[0:i+1])
        if len(normal_word) < len(first_word):
            if normal_word[0:i+1] == first_word[0:i+1]:
                common = first_word[0:i+1]
        else:
            if first_word[0:i+1] == normal_word[0:i+1]:
                common = normal_word[0:i+1]

    prefix = len(common)
    new_normal = normal_word[0+prefix: len(normal_word)]
    """
    print("First Word: ", first_word, " Normal word: ", normal_word, "COMMON IS: ", common)
    print("NEW NORMAL: ", new_normal, "PREFIX IS: ", prefix)
    """
    return new_normal, prefix


def calc_bytes_total_len(val1_len, val2_len, val3_len, val4_len):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0

    if val4_len == 1:
        x4 = 0
    elif val4_len == 2:
        x4 = 1
    elif val4_len == 3:
        x4 = 2
    elif val4_len == 4:
        x4 = 3

    if val3_len == 1:
        x3 = 0
    elif val3_len == 2:
        x3 = 4
    elif val3_len == 3:
        x3 = 8
    elif val2_len == 4:
        x3 = 12

    if val2_len == 1:
        x2 = 0
    elif val2_len == 2:
        x2 = 16
    elif val2_len == 3:
        x2 = 32
    elif val2_len == 4:
        x2 = 48

    if val1_len == 1:
        x1 = 00
    elif val1_len == 2:
        x1 = 64
    elif val1_len == 3:
        x1 = 128
    elif val1_len == 4:
        x1 = 192

    total_length = x1+x2+x3+x4

    return total_length


def create_text_file(sorted_dic, word_list_with_pl, dir):
    # print(word_list_with_pl)
    all_string = ''
    str_ptr = 0
    term1 = {}
    term2 = {}
    term3 = {}
    term4 = {}
    term5 = {}
    term6 = {}
    term7 = {}
    term8 = {}
    term9 = {}
    term10 = {}

    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir)
    completeName = (path + r'\text.dic')
    input = ''
    block_array = []
    counter = 0
    for words in range(len(sorted_dic)):
        for get_pl in range(len(word_list_with_pl)):
            if sorted_dic[words]['word'] == word_list_with_pl[get_pl]['word']:
                word_pl = word_list_with_pl[get_pl]['Posting-List']

        freq_in_file = sorted_dic[words]['freq_in_files']
        counter += 1
        temp = sorted_dic[words]['word']
        #print("WORD: ", temp, "FREQ IN FILE: ", freq_in_file, " GAPS: ", sorted_dic[words]['Appearances (ReviewId, Frequency)'])
        if (counter % 10) == 1:  # If the first word
            temp_first = sorted_dic[words]['word']
            input += temp_first
            term1 = {'freq': freq_in_file,
                        'post-ptr': word_pl,
                         'length': len(temp)}
        elif (counter % 10) != 1:  # Coding rest of the words
            new_word, prefix = check_prefix(temp_first, temp)
            if (counter % 10) == 2:
                if words != len(sorted_dic)-1:
                    term2 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term2 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 3:
                if words != len(sorted_dic)-1:
                    term3 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term3 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 4:
                if words != len(sorted_dic)-1:
                    term4 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term4 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 5:
                if words != len(sorted_dic)-1:
                    term5 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term5 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 6:
                if words != len(sorted_dic)-1:
                    term6 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term6 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 7:
                if words != len(sorted_dic)-1:
                    term7 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term7 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 8:
                if words != len(sorted_dic)-1:
                    term8 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term8 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 9:
                if words != len(sorted_dic)-1:
                    term9 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                             'length': len(temp),
                              'prefix': prefix}
                else:
                    term9 = {'freq': freq_in_file,
                             'post-ptr': word_pl,
                              'prefix': prefix}
            elif (counter % 10) == 0:
                term10 = {'freq': freq_in_file,
                         'post-ptr': word_pl,
                          'prefix': prefix}
            if words == len(sorted_dic)-1 and (len(sorted_dic) % 10) != 0:
            #    print(new_word)
                #input += new_word  #ADDED THIS LAST
            #    print("IN:", input)

                # Each block contains string size, string, and each term's length + prefix
                block = {'str_ptr': str_ptr,
                               'string': input,
                               'term1': term1,
                               'term2': term2,
                               'term3': term3,
                               'term4': term4,
                               'term5': term5,
                               'term6': term6,
                               'term7': term7,
                               'term8': term8,
                               'term9': term9,
                               'term10': term10}
                block_array.append(block)
                str_ptr += len(input)

            input += new_word
            if(counter % 10) == 0:  # After the 10th word in the coding
                block = {'str_ptr': str_ptr,
                               'string': input,
                               'term1': term1,
                               'term2': term2,
                               'term3': term3,
                               'term4': term4,
                               'term5': term5,
                               'term6': term6,
                               'term7': term7,
                               'term8': term8,
                               'term9': term9,
                               'term10': term10}
                block_array.append(block)
                str_ptr += len(input)
                term2 = {}
                term3 = {}
                term4 = {}
                term5 = {}
                term6 = {}
                term7 = {}
                term8 = {}
                term9 = {}
                term10 = {}

            #    all_string += input
                input = ''
    for i in range(len(block_array)):
        each = list(block_array[i].values())
        all_string += each[1]


    with open(completeName, "wb") as f:
        # Write size of whole string (dictionary size)
        all_str_len = len(all_string)
        all_str_len_in_bytes = all_str_len.to_bytes(4, 'big')  # bytes for overall string length
        f.write(all_str_len_in_bytes)  # write size of string

        # Encode and write string
        arr = bytes(all_string, 'utf-8')
        f.write(arr)

        for i in range(len(block_array)):
            for j in block_array[i].items():
                # first 4 bytes of the block containing 'string pointer'
                if i != len(block_array)-1:
                    if j[0] == 'str_ptr':
                        str_ptr_byte = j[1].to_bytes(4, 'big')
                        f.write(str_ptr_byte)
                    elif j[0] == 'term1':
                        freq_byte = j[1]['freq'].to_bytes(4, 'big')
                        post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                        len_byte = j[1]['length'].to_bytes(1, 'big')
                        f.write(freq_byte)
                        f.write(post_ptr_byte)
                        f.write(len_byte)
                    elif j[0] == 'term2' or j[0] == 'term3' or j[0] == 'term4' or j[0] == 'term5' or j[0] == 'term6' or \
                            j[0] == 'term7' or j[0] == 'term8' or j[0] == 'term9':
                        freq_byte = j[1]['freq'].to_bytes(4, 'big')
                        post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                        len_byte = j[1]['length'].to_bytes(1, 'big')
                        prefix_byte = j[1]['prefix'].to_bytes(1, 'big')
                        f.write(freq_byte)
                        f.write(post_ptr_byte)
                        f.write(len_byte)
                        f.write(prefix_byte)
                    elif j[0] == 'term10':
                        freq_byte = j[1]['freq'].to_bytes(4, 'big')
                        post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                        prefix_byte = j[1]['prefix'].to_bytes(1, 'big')
                        f.write(freq_byte)
                        f.write(post_ptr_byte)
                        f.write(prefix_byte)
                else:  # if at end of last block, and it contains less than 10 string
                    if j[0] == 'str_ptr':
                        str_ptr_byte = j[1].to_bytes(4, 'big')
                        f.write(str_ptr_byte)
                    elif j[0] == 'term1':
                        freq_byte = j[1]['freq'].to_bytes(4, 'big')
                        post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                        len_byte = j[1]['length'].to_bytes(1, 'big')
                        f.write(freq_byte)
                        f.write(post_ptr_byte)
                        f.write(len_byte)
                    elif j[0] == 'term2' or j[0] == 'term3' or j[0] == 'term4' or j[0] == 'term5' or j[0] == 'term6' or \
                            j[0] == 'term7' or j[0] == 'term8' or j[0] == 'term9' or j[0] == 'term10':
                        if bool(j[1]) is not False:
                            if len(j[1]) == 4:
                                freq_byte = j[1]['freq'].to_bytes(4, 'big')
                                post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                                len_byte = j[1]['length'].to_bytes(1, 'big')
                                prefix_byte = j[1]['prefix'].to_bytes(1, 'big')
                                f.write(freq_byte)
                                f.write(post_ptr_byte)
                                f.write(len_byte)
                                f.write(prefix_byte)
                            else:  # If its the last word in the dictionary, it has no length
                                freq_byte = j[1]['freq'].to_bytes(4, 'big')
                                post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                                prefix_byte = j[1]['prefix'].to_bytes(1, 'big')
                                f.write(freq_byte)
                                f.write(post_ptr_byte)
                                f.write(prefix_byte)
                    elif j[0] == 'term10':
                        freq_byte = j[1]['freq'].to_bytes(4, 'big')
                        post_ptr_byte = j[1]['post-ptr'].to_bytes(4, 'big')
                        prefix_byte = j[1]['prefix'].to_bytes(1, 'big')
                        f.write(freq_byte)
                        f.write(post_ptr_byte)
                        f.write(prefix_byte)
                # 4 bytes of for the frequency
                # 4 bytes for pointer to posting list
                # 1 byte for length of this word (all words get a length except for the last one)
                # 1 byte for the prefix (all words get a prefix except the first one)



def create_text_pl(sorted_dict, dir):

        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, dir)
        input = ''
        pl_array = []
        pl_array2 = []
        gaps = ()
        counter = 0
        for words in range(len(sorted_dict)):
            temp = sorted_dict[words]['Appearances (ReviewId, Frequency)']
          ##  print("old: ", temp)
          ##  print(len(temp))

            for x in range(0, len(temp)):
                if x == 0:
                    gaps = ()
                    num = temp[x]
                    gaps = gaps + (num,)
                    num2 = temp[x + 1]
                    gaps = gaps + (num2,)
                if x >= 2:
                    if x % 2 != 0:
                        num = temp[x]
                    elif x % 2 == 0:
                        num = abs(temp[x] - temp[x-2])
                    gaps = gaps + (num,)

            if len(gaps) % 4 != 0:
                gaps = gaps + (0, 0)
            block = {'word': sorted_dict[words]['word'],
                        'Gaps': gaps}

            pl_array.append(block)



        total_length = 0
        val1 = 0
        val2 = 0
        val3 = 0
        val4 = 0
        val1_len = 0
        val2_len = 0
        val3_len = 0
        val4_len = 0

        post_list_counter = 0

        completeName = (path + r'\text.pl')

        with open(completeName, "wb") as f:

            for x in range(len(pl_array)):
                token_gaps = pl_array[x]['Gaps']
                same_word = pl_array[x]['word']

                block_new = {'word': same_word,
                             'Gaps': gaps,
                             'Posting-List': post_list_counter}

                pl_array2.append(block_new)

            #    print("WORD: ", same_word)
            #    print("Posting_List: ", post_list_counter)

                fill_len = len(token_gaps)

                for y in range(len((pl_array[x]['Gaps']))):
                    val = pl_array[x]['Gaps'][y]
                    if val <= 255:
                        byte_len = 1  # use one byte
                    elif val >= 256 and val <= 65535:  # use two bytes
                        byte_len = 2
                    elif val >= 65536 and val < 16777216:  # use three bytes
                        byte_len = 3
                    elif val >= 16777216:  # use four bytes
                        byte_len = 4

                    if y % 4 == 0:
                        total_length = 0
                        val1 = val
                        val1_len = byte_len
                    if y % 4 == 1:
                        val2 = val
                        val2_len = byte_len
                    if y % 4 == 2:
                        val3 = val
                        val3_len = byte_len
                    if y % 4 == 3:
                        val4 = val
                        val4_len = byte_len
                    if val <= 255:
                        byte_len = 1  # use one byte (?)


                    # When at our 4th term, which means we saved the first 4 values, we write them as bytes
                    if (y % 4) == 3:
                        total_length = calc_bytes_total_len(val1_len, val2_len, val3_len, val4_len)

                        yy_length = total_length.to_bytes(1, 'big')
                        yy1 = val1.to_bytes(val1_len, 'big')
                        yy2 = val2.to_bytes(val2_len, 'big')
                        yy3 = val3.to_bytes(val3_len, 'big')
                        yy4 = val4.to_bytes(val4_len, 'big')

                        f.write(yy_length)
                        f.write(yy1)
                        f.write(yy2)
                        f.write(yy3)
                        f.write(yy4)

                        post_list_counter += 1 + val1_len + val2_len + val3_len + val4_len
        return(pl_array2)

"""
        byte = f.read(1)
        while(byte):
            byte = f.read(1)
            print(byte)
            print(int.from_bytes(byte, byteorder='big'))
"""

       # f.close()  # to change file access modes

def create_product_pl(rev_gaps_dic, dir):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir)

    prod_post_list_counter = 0
    new_rev_gaps_with_pl = []
    completeName = (path + r'\prod.pl')

    with open(completeName, "wb") as f:

        for x in range(len(rev_gaps_dic)):
            rev_gaps = rev_gaps_dic[x]['rev_ct']

            block_new = {'Products': rev_gaps_dic[x]['Products'],
                         'rev_ct': rev_gaps_dic[x]['rev_ct'],
                         'Posting-List': prod_post_list_counter}
            new_rev_gaps_with_pl.append(block_new)


            fill_len = len(rev_gaps)

            for y in range(len((rev_gaps_dic[x]['rev_ct']))):
                counter = 0
                val = rev_gaps_dic[x]['rev_ct'][y]
               # print("VAL: ", val)
                if val <= 255:
                    byte_len = 1  # use one byte
                elif val >= 256 and val <= 65535:  # use two bytes
                    byte_len = 2
                elif val >= 65536 and val < 16777216:  # use three bytes
                    byte_len = 3
                elif val >= 16777216:  # use four bytes
                    byte_len = 4

                if y % 4 == 0:
                    total_length = 0
                    val1 = val
                    val1_len = byte_len
                if y % 4 == 1:
                    val2 = val
                    val2_len = byte_len
                if y % 4 == 2:
                    val3 = val
                    val3_len = byte_len
                if y % 4 == 3:
                    val4 = val
                    val4_len = byte_len
                if val <= 255:
                    byte_len = 1  # use one byte (?)

                counter = y  # When counter is 3, which means we saved the first 4 values, we write them as bytes
                if (y % 4) == 3:
                    total_length = calc_bytes_total_len(val1_len, val2_len, val3_len, val4_len)

                    yy_length = total_length.to_bytes(total_length, 'big') # only thing i changed last!!!!!!
                    yy_length = total_length.to_bytes(byte_len, 'big')

                    #    print(total_length)
                    yy1 = val1.to_bytes(val1_len, 'big')
                    yy2 = val2.to_bytes(val2_len, 'big')
                    yy3 = val3.to_bytes(val3_len, 'big')
                    yy4 = val4.to_bytes(val4_len, 'big')

                    f.write(yy_length)
                    f.write(yy1)
                    f.write(yy2)
                    f.write(yy3)
                    f.write(yy4)

                    prod_post_list_counter += 1 + val1_len + val2_len + val3_len + val4_len
    return new_rev_gaps_with_pl


class CompressedIndexWriter:
    def __init__(self, inputFile, dir):
        self.dir = dir
        number_of_reviews = 0
        token_size_of_reviews = 0

        pIDFind = 0
        helpFind = 0
        scoreFind = 0
        textFind = 0
        review_counter = 0
        dictionary = []  # Dictionary will contain the list of all products/reviews and their infos
        dictionary2 = []  # Special dictionary that holds total number of reviews and total token size
        dictionary3 = []  # Dictionary containing product IDs and all the reviews belonging to each one
        # Initialize all the alphabetical dictionaries where each one
        token_dict = []
        rev_ct = ()
        # -- Open file, loop over each line, identify the key variables and save them into a dictionary, close file
        read_file = open(inputFile, "r")         # opening the text file



        # Loop that goes over each line
        for line in read_file:
            # reading each word
            for word in line.split():
                if pIDFind == 1:  # When we identified the productID
                    review_counter += 1  # We start the 1st review with 1, and then increment accordingly

                    product_id = word
                    pIDFind -= 1
                    """
                    HERE WE TRY TO CREATE FILE 4 (for product IDs and all the reviews numbers relating to them)
                    """
                    exists = False


                    for dic_items in dictionary3:
                        if product_id in dic_items.values():
                            exists = True
                            for s in range(len(dictionary3)):
                                # If this product is already in dictionary
                                if product_id == dictionary3[s]["Products"]:
                                    rev_ct = rev_ct + (review_counter,)
                                    dictionary3[s]["ReviewIDs"] += ', ' + str(review_counter)
                                    dictionary3[s]['rev_ct'] = rev_ct
                                    # exists = True
                        else:
                            exists = False
                    if exists == False:
                        rev_ct = ()
                        rev_ct = rev_ct + (review_counter,)
                        item2 = {'Products': product_id,
                                 'ReviewIDs': str(review_counter),
                                 'rev_ct': rev_ct}

                        dictionary3.append(item2)


                if word == "product/productId:":  # Helps us identify the productID
                    pIDFind += 1

                if helpFind == 1:  # When we identified the helpfulness
                    helpfulness = word
                    helpFind -= 1
                if word == "review/helpfulness:":  # Helps us identify the helpfulness
                    helpFind += 1

                if scoreFind == 1:  # When we identified the score
                    score = word
                    scoreFind -= 1
                if word == "review/score:":  # Helps us identify the score
                    scoreFind += 1

                if textFind == 1:  # When we identified the text
                    text = line[len(delete):len(line)].lstrip()


                    token_size_of_reviews += token_counter(token_size_of_reviews, text)

                # --------------------------------------------------------------------------------------------------- #
                # Call to function that creates lists of alphabetical tokens database

                    create_alphabetical_database(text, review_counter, token_dict)

                # --------------------------------------------------------------------------------------------------- #
                    textFind -= 1
                    """We add all the info to the dictionary after we have found the text, since it means
                    we have found all the other variables we were looking for (end of review)"""
                    # We temporarily copy the info to "item" since its the only way to append to the dictionary
                    item = {'review_num': review_counter,
                           'productId': product_id,
                           'helpfulness': helpfulness,
                           'score': score,
                           'text': text}
                    dictionary.append(item)
                if word == "review/text:":  # Helps us identify the text
                    delete = word
                    textFind += 1
        read_file.close()
        # ----------------------------------------------------------------------------------------------------------- #
        # Create the first file, our general database for all features relating to the product ID
        create_general_review_database(dictionary, dir)

        # -------------------------------  Here we create our second file ------------------------------------------- #
        number_of_reviews = review_counter  # Total number of reviews
        item = {'total_reviews': number_of_reviews,
                'token_size': token_size_of_reviews}
        dictionary2.append(item)
        # Call function that creates the third file
        create_special_database(dictionary2, dir)
        # ----------------------------------------------------------------------------------------------------------- #

        # This part of the code takes the dictionary and sorts it alphabetically
        words_alone = []
        new_dic = {}
        for all_words in range(len(token_dict)):
            new_dic[all_words] = token_dict[all_words]

        for num, table in new_dic.items():
            for i in table.items():
                if i[0] == 'word':
                    words_alone.append(i[1])

        words_alone.sort()
        sorted_dict = []

        for i in range(len(words_alone)):
            for j in range(len(token_dict)):
                if words_alone[i] == token_dict[j]['word']:
                    # We copy the appearances from list to a tuple since we were asked to change in forum
                    appearance = ()
                    for k in range(len(token_dict[j]['Appearances (ReviewId, Frequency)'])):
                        for h in range(len(token_dict[j]['Appearances (ReviewId, Frequency)'][k])):
                            appearance = appearance + (token_dict[j]['Appearances (ReviewId, Frequency)'][k][h],)

                    item = {'word': words_alone[i],
                            'frequency': token_dict[j]['frequency'],
                            'Appearances (ReviewId, Frequency)': appearance,
                            'freq_in_files': int(len(appearance)/2)}
                    sorted_dict.append(item)

        # WONT NEED LATER
        create_file_alphabetical(sorted_dict, dir)

        word_list_with_pl = create_text_pl(sorted_dict, dir)

        create_text_file(sorted_dict, word_list_with_pl, dir)

        review_gaps = ()
        prods_dict = []
        for element in range(len(dictionary3)):
        #####    print("OLD: ", dictionary3[element]['rev_ct'])
            for x in range(len(dictionary3[element]['rev_ct'])):
                if x == 0:
                    review_gaps = ()
                    add_rev = dictionary3[element]['rev_ct'][x]
                    review_gaps = review_gaps + (add_rev,)
                if x > 0:
                    if x < len(dictionary3[element]['rev_ct'])-1:
                        add_rev = abs(dictionary3[element]['rev_ct'][x+1] - dictionary3[element]['rev_ct'][x])
                        review_gaps = review_gaps + (add_rev,)
                    if x == len(dictionary3[element]['rev_ct'])-1:
                        add_rev = abs(dictionary3[element]['rev_ct'][x] - dictionary3[element]['rev_ct'][x-1])
                        review_gaps = review_gaps + (add_rev,)
            # Here we make all review counters divisible by 4
            if len(review_gaps) % 4 != 0:
                if len(review_gaps) % 4 == 1:
                    review_gaps = review_gaps + (0, 0, 0, )
                elif len(review_gaps) % 4 == 2:
                    review_gaps = review_gaps + (0, 0, )
                elif len(review_gaps) % 4 == 3:
                    review_gaps = review_gaps + (0, )

            new_item = {'Products': dictionary3[element]['Products'],
                     'rev_ct': review_gaps}

            prods_dict.append(new_item)

        prod_list_with_pl = create_product_pl(prods_dict, dir)
        # -------------------------------  Here we create our third file ------------------------------------------- #
        # Call function that creates the third file
        create_product_review_database(prod_list_with_pl, dir)
        # HERE IT WAS 'dictionary3' in Exercise 1
        #    print(dictionary3)

        # ----------------------------------------------------------------------------------------------------------- #

    def removeIndex(self, dir):
       # path_del = os.path.dirname(os.path.abspath(dir))  # Get the path of directory we want to delete
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)

        if os.path.exists(path):  # If path exists already, delete it and create new one


            for file in os.scandir(path):
                os.remove(file)

            directory = os.listdir(path)  # Check if directory is empty

            try:  # We will try to delete the empty directory (after we remove all files in it)
                if len(path) == 0:
                    os.rmdir(path)
                else:
                    shutil.rmtree(path)
            except OSError as e:
                print("Error: %s : %s" % (path, e.strerror))
