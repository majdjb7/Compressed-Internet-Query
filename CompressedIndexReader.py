"""
Names: Majd Jaber, ID: 208488692
       Saed Jaber, ID: 208480632
"""

import pandas as pd
import os
import string
import re


# Changes 4 bytes of hex to an int
def hex_to_int_for_one(string_size):
    first_size = hex(string_size[0])

    first_in_hex = str(first_size[2:len(first_size)])

    str1 = first_in_hex

    length_of_str_dic = int(str1, 16)
    return length_of_str_dic


# Changes 4 bytes of hex to an int
def hex_to_int_for_four(string_size):
    first_size = hex(string_size[0])
    second_size = hex(string_size[1])
    third_size = hex(string_size[2])
    fourth_size = hex(string_size[3])

    first_in_hex = str(first_size[2:len(first_size)])
    if len(first_in_hex) == 1:
        first_in_hex = '0' + first_in_hex
    second_in_hex = str(second_size[2:len(second_size)])
    if len(second_in_hex) == 1:
        second_in_hex = '0' + second_in_hex
    third_in_hex = str(third_size[2:len(third_size)])
    if len(third_in_hex) == 1:
        third_in_hex = '0' + third_in_hex
    fourth_in_hex = str(fourth_size[2:len(fourth_size)])
    if len(fourth_in_hex) == 1:
        fourth_in_hex = '0' + fourth_in_hex

    first_in_hex += second_in_hex
    first_in_hex += third_in_hex
    first_in_hex += fourth_in_hex
    str1 = first_in_hex

    length_of_str_dic = int(str1, 16)
    return length_of_str_dic

#def function_that_check():


def get_the_words(new_block_arr):
    new_dictionary = []

    for i in range(len(new_block_arr)):
        if i != len(new_block_arr)-1:
            str = new_block_arr[i]['string']
        #    print(str)
            #########################################################################################################
            leng1 = new_block_arr[i]['term1']['length']
            word = str[0:leng1]
            freq = new_block_arr[i]['term1']['freq']
            post_ptr = new_block_arr[i]['term1']['post_ptr']
            block = {'word': word,
                     'frequency': freq,
                     'post_ptr': post_ptr
                     }
        #    print("WORD1: ", word)
            new_dictionary.append(block)
            # wintertch (prefix:wi...........len:5)
            #working (prefix: work, len 7)
            #########################################################################################################
            leng2 = new_block_arr[i]['term2']['length']
            prefix2 = new_block_arr[i]['term2']['prefix']
            word2 = str[0:prefix2]
            word2 = word2 + str[leng1:leng1+(leng2-prefix2)]
        #    print("WORD2: ", word2)
            freq2 = new_block_arr[i]['term2']['freq']
            post_ptr2 = new_block_arr[i]['term2']['post_ptr']
            block = {'word': word2,
                     'frequency': freq2,
                     'post_ptr': post_ptr2
                     }
            new_dictionary.append(block)

            leng2_real = leng2 - prefix2

            new_leng = leng1+leng2_real
            #########################################################################################################
            leng3 = new_block_arr[i]['term3']['length']
            prefix3 = new_block_arr[i]['term3']['prefix']
            word3 = str[0:prefix3]
            word3 = word3 + str[new_leng:new_leng+(leng3-prefix3)]
        #    print("WORD3: ", word3)
            freq3 = new_block_arr[i]['term3']['freq']
            post_ptr3 = new_block_arr[i]['term3']['post_ptr']
            block = {'word': word3,
                     'frequency': freq3,
                     'post_ptr': post_ptr3
                     }
            new_dictionary.append(block)

            leng3_real = leng3 - prefix3
            new_leng = leng1+leng2_real+leng3_real
            #########################################################################################################
            leng4 = new_block_arr[i]['term4']['length']
            prefix4 = new_block_arr[i]['term4']['prefix']
            word4 = str[0:prefix4]
            word4 = word4 + str[new_leng:new_leng+(leng4-prefix4)]
        #    print("WORD4: ", word4)
            freq4 = new_block_arr[i]['term4']['freq']
            post_ptr4 = new_block_arr[i]['term4']['post_ptr']
            block = {'word': word4,
                     'frequency': freq4,
                     'post_ptr': post_ptr4
                     }
            new_dictionary.append(block)

            leng4_real = leng4 - prefix4
            new_leng = leng1+leng2_real+leng3_real+leng4_real
            #########################################################################################################
            leng5 = new_block_arr[i]['term5']['length']
            prefix5 = new_block_arr[i]['term5']['prefix']
            word5 = str[0:prefix5]
            word5 = word5 + str[new_leng:new_leng+(leng5-prefix5)]
        #    print("WORD5: ", word5)
            freq5 = new_block_arr[i]['term5']['freq']
            post_ptr5 = new_block_arr[i]['term5']['post_ptr']
            block = {'word': word5,
                     'frequency': freq5,
                     'post_ptr': post_ptr5
                     }
            new_dictionary.append(block)

            leng5_real = leng5 - prefix5
            new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real
            #########################################################################################################
            leng6 = new_block_arr[i]['term6']['length']
            prefix6 = new_block_arr[i]['term6']['prefix']
            word6 = str[0:prefix6]
            word6 = word6 + str[new_leng:new_leng+(leng6-prefix6)]
        #    print("WORD6: ", word6)
            freq6 = new_block_arr[i]['term6']['freq']
            post_ptr6 = new_block_arr[i]['term6']['post_ptr']
            block = {'word': word6,
                     'frequency': freq6,
                     'post_ptr': post_ptr6
                     }
            new_dictionary.append(block)

            leng6_real = leng6 - prefix6
            new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real
            #########################################################################################################
            leng7 = new_block_arr[i]['term7']['length']
            prefix7 = new_block_arr[i]['term7']['prefix']
            word7 = str[0:prefix7]
            word7 = word7 + str[new_leng:new_leng+(leng7-prefix7)]
        #    print("WORD7: ", word7)
            freq7 = new_block_arr[i]['term7']['freq']
            post_ptr7 = new_block_arr[i]['term7']['post_ptr']
            block = {'word': word7,
                     'frequency': freq7,
                     'post_ptr': post_ptr7
                     }
            new_dictionary.append(block)

            leng7_real = leng7 - prefix7
            new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real+leng7_real
            #########################################################################################################
            leng8 = new_block_arr[i]['term8']['length']
            prefix8 = new_block_arr[i]['term8']['prefix']
            word8 = str[0:prefix8]
            word8 = word8 + str[new_leng:new_leng+(leng8-prefix8)]
        #    print("WORD8: ", word8)
            freq8 = new_block_arr[i]['term8']['freq']
            post_ptr8 = new_block_arr[i]['term8']['post_ptr']
            block = {'word': word8,
                     'frequency': freq8,
                     'post_ptr': post_ptr8
                     }
            new_dictionary.append(block)

            leng8_real = leng8 - prefix8
            new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real+leng7_real+leng8_real
            #########################################################################################################
            leng9 = new_block_arr[i]['term9']['length']
            prefix9 = new_block_arr[i]['term9']['prefix']
            word9 = str[0:prefix9]
            word9 = word9 + str[new_leng:new_leng+(leng9-prefix9)]
        #    print("WORD9: ", word9)
            freq9 = new_block_arr[i]['term9']['freq']
            post_ptr9 = new_block_arr[i]['term9']['post_ptr']
            block = {'word': word9,
                     'frequency': freq9,
                     'post_ptr': post_ptr9
                     }
            new_dictionary.append(block)

            leng9_real = leng9 - prefix9
            new_leng = leng1 + leng2_real + leng3_real + leng4_real + leng5_real + leng6_real + leng7_real + leng8_real+leng9_real

            #########################################################################################################
            prefix10 = new_block_arr[i]['term10']['prefix']
            leng10 = len(str) - new_leng + prefix10
            word10 = str[0:prefix10]
            word10 = word10 + str[new_leng:new_leng + (leng10 - prefix10)]
        #    print("WORD10: ", word10)
            freq10 = new_block_arr[i]['term10']['freq']
            post_ptr10 = new_block_arr[i]['term10']['post_ptr']
            block = {'word': word10,
                     'frequency': freq10,
                     'post_ptr': post_ptr10
                     }
            new_dictionary.append(block)
        else:
            str = new_block_arr[i]['string']
        #    print(str)
            leng1 = new_block_arr[i]['term1'][0]['length']
            word = str[0:leng1]
            freq = new_block_arr[i]['term1'][0]['freq']
            post_ptr = new_block_arr[i]['term1'][0]['post_ptr']

            block = {'word': word,
                     'frequency': freq,
                     'post_ptr': post_ptr
                     }
        #    print("WORD1: ", word)
            new_dictionary.append(block)
        #    print("WORD2...")
            #########################################################################################################
            if new_block_arr[i]['term2'] != {}:

                if len(new_block_arr[i]['term2'][0].values()) == 4:
                    leng2 = new_block_arr[i]['term2'][0]['length']
                    prefix2 = new_block_arr[i]['term2'][0]['prefix']
                    word2 = str[0:prefix2]
                    word2 = word2 + str[leng1:leng1+(leng2-prefix2)]
                #    print("WORD2: ", word2)
                    freq2 = new_block_arr[i]['term2'][0]['freq']
                    post_ptr2 = new_block_arr[i]['term2'][0]['post_ptr']
                    block = {'word': word2,
                             'frequency': freq2,
                             'post_ptr': post_ptr2
                             }
                    new_dictionary.append(block)

                    leng2_real = leng2 - prefix2
                    new_leng = leng1 + leng2_real
                elif len(new_block_arr[i]['term3'][0].values()) == 3:
                    new_leng = leng1
                    #########################################################################################################
                    prefix2 = new_block_arr[i][0]['term2']['prefix']
                    leng2 = len(str) - new_leng + prefix2
                    word2 = str[0:prefix2]
                    word2 = word2 + str[new_leng:new_leng + (leng2 - prefix2)]
                #    print("WORD2: ", word2)
                    freq2 = new_block_arr[i]['term2']['freq']
                    post_ptr2 = new_block_arr[i]['term2']['post_ptr']
                    block = {'word': word2,
                             'frequency': freq2,
                             'post_ptr': post_ptr2
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term3'] != {}:

                if len(new_block_arr[i]['term3'][0].values()) == 4:
                    leng3 = new_block_arr[i]['term3'][0]['length']
                    prefix3 = new_block_arr[i]['term3'][0]['prefix']
                    word3 = str[0:prefix3]
                    word3 = word3 + str[new_leng:new_leng + (leng3 - prefix3)]
                #    print("WORD3: ", word3)
                    freq3 = new_block_arr[i]['term3'][0]['freq']
                    post_ptr3 = new_block_arr[i]['term3'][0]['post_ptr']
                    block = {'word': word3,
                             'frequency': freq3,
                             'post_ptr': post_ptr3
                             }
                    new_dictionary.append(block)

                    leng3_real = leng3 - prefix3
                    new_leng = leng1 + leng2_real + leng3_real

                elif len(new_block_arr[i]['term3'][0].values()) == 3:
                    new_leng = leng1+leng2_real
                    prefix3 = new_block_arr[i]['term3'][0]['prefix']
                    leng3 = len(str) - new_leng + prefix3
                    word3 = str[0:prefix3]
                    word3 = word3 + str[new_leng:new_leng + (leng3 - prefix3)]
                #    print("WORD3: ", word3)
                    freq3 = new_block_arr[i]['term3'][0]['freq']
                    post_ptr3 = new_block_arr[i]['term3'][0]['post_ptr']
                    block = {'word': word3,
                             'frequency': freq3,
                             'post_ptr': post_ptr3
                             }
                    new_dictionary.append(block)


            #########################################################################################################
            if new_block_arr[i]['term4'] != {}:
                if len(new_block_arr[i]['term4'][0].values()) == 4:
                    leng4 = new_block_arr[i]['term4'][0]['length']
                    prefix4 = new_block_arr[i]['term4'][0]['prefix']
                    word4 = str[0:prefix4]
                    word4 = word4 + str[new_leng:new_leng + (leng4 - prefix4)]
                #    print("WORD4: ", word4)
                    freq4 = new_block_arr[i]['term4'][0]['freq']
                    post_ptr4 = new_block_arr[i]['term4'][0]['post_ptr']
                    block = {'word': word4,
                             'frequency': freq4,
                             'post_ptr': post_ptr4
                             }
                    new_dictionary.append(block)

                    leng4_real = leng4 - prefix4
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real

                elif len(new_block_arr[i]['term4'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real
                    prefix4 = new_block_arr[i]['term4'][0]['prefix']
                    leng4 = len(str) - new_leng + prefix4
                    word4 = str[0:prefix4]
                    word4 = word4 + str[new_leng:new_leng + (leng4 - prefix4)]
                #    print("WORD4: ", word4)
                    freq4 = new_block_arr[i]['term4'][0]['freq']
                    post_ptr4 = new_block_arr[i]['term4'][0]['post_ptr']
                    block = {'word': word4,
                             'frequency': freq4,
                             'post_ptr': post_ptr4
                             }
                    new_dictionary.append(block)

            #########################################################################################################
            if new_block_arr[i]['term5'] != {}:

                if len(new_block_arr[i]['term5'][0].values()) == 4:
                    leng5 = new_block_arr[i]['term5'][0]['length']
                    prefix5 = new_block_arr[i]['term5'][0]['prefix']
                    word5 = str[0:prefix5]
                    word5 = word5 + str[new_leng:new_leng + (leng5 - prefix5)]
                #    print("WORD5: ", word5)
                    freq5 = new_block_arr[i]['term5'][0]['freq']
                    post_ptr5 = new_block_arr[i]['term5'][0]['post_ptr']
                    block = {'word': word5,
                             'frequency': freq5,
                             'post_ptr': post_ptr5
                             }
                    new_dictionary.append(block)

                    leng5_real = leng5 - prefix5
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real+leng5_real

                elif len(new_block_arr[i]['term5'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real+leng4_real
                    prefix5 = new_block_arr[i]['term5'][0]['prefix']
                    leng5 = len(str) - new_leng + prefix5
                    word5 = str[0:prefix5]
                    word5 = word5 + str[new_leng:new_leng + (leng5 - prefix5)]
                #    print("WORD5: ", word5)
                    freq5 = new_block_arr[i]['term5'][0]['freq']
                    post_ptr5 = new_block_arr[i]['term5'][0]['post_ptr']
                    block = {'word': word5,
                             'frequency': freq5,
                             'post_ptr': post_ptr5
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term6'] != {}:

                if len(new_block_arr[i]['term6'][0].values()) == 4:
                    leng6 = new_block_arr[i]['term6'][0]['length']
                    prefix6 = new_block_arr[i]['term6'][0]['prefix']
                    word6 = str[0:prefix6]
                    word6 = word6 + str[new_leng:new_leng + (leng6 - prefix6)]
                #    print("WORD6: ", word6)
                    freq6 = new_block_arr[i]['term6'][0]['freq']
                    post_ptr6 = new_block_arr[i]['term6'][0]['post_ptr']
                    block = {'word': word6,
                             'frequency': freq6,
                             'post_ptr': post_ptr6
                             }
                    new_dictionary.append(block)

                    leng6_real = leng6 - prefix6
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real+leng5_real+leng6_real

                elif len(new_block_arr[i]['term6'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real
                    prefix6 = new_block_arr[i]['term6'][0]['prefix']
                    leng6 = len(str) - new_leng + prefix6
                    word6 = str[0:prefix6]
                    word6 = word6 + str[new_leng:new_leng + (leng6 - prefix6)]
                #    print("WORD6: ", word6)
                    freq6 = new_block_arr[i]['term6'][0]['freq']
                    post_ptr6 = new_block_arr[i]['term6'][0]['post_ptr']
                    block = {'word': word6,
                             'frequency': freq6,
                             'post_ptr': post_ptr6
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term7'] != {}:

                if len(new_block_arr[i]['term7'][0].values()) == 4:
                    leng7 = new_block_arr[i]['term7'][0]['length']
                    prefix7 = new_block_arr[i]['term7'][0]['prefix']
                    word7 = str[0:prefix7]
                    word7 = word7 + str[new_leng:new_leng + (leng7 - prefix7)]
                #    print("WORD7: ", word7)
                    freq7 = new_block_arr[i]['term7'][0]['freq']
                    post_ptr7 = new_block_arr[i]['term7'][0]['post_ptr']
                    block = {'word': word7,
                             'frequency': freq7,
                             'post_ptr': post_ptr7
                             }
                    new_dictionary.append(block)

                    leng7_real = leng7 - prefix7
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real+leng5_real+leng6_real+leng7_real

                elif len(new_block_arr[i]['term7'][0].values()) == 3:
                    word7 = ''
                    print(new_block_arr[i]['term7'][0])
                    new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real
                    prefix7 = new_block_arr[i]['term7'][0]['prefix']
                    leng7 = len(str) - new_leng + prefix7
                    word7 = str[0:prefix7]
                    word7 = word7 + str[new_leng:new_leng + (leng7 - prefix7)]
                #    print("WORD7: ", word7)
                    freq7 = new_block_arr[i]['term7'][0]['freq']
                    post_ptr7 = new_block_arr[i]['term7'][0]['post_ptr']
                    block = {'word': word7,
                             'frequency': freq7,
                             'post_ptr': post_ptr7
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term8'] != {}:

                if len(new_block_arr[i]['term8'][0].values()) == 4:
                    leng8 = new_block_arr[i]['term8'][0]['length']
                    prefix8 = new_block_arr[i]['term8'][0]['prefix']
                    word8 = str[0:prefix8]
                    word8 = word8 + str[new_leng:new_leng + (leng8 - prefix8)]
                #    print("WORD8: ", word8)
                    freq8 = new_block_arr[i]['term8'][0]['freq']
                    post_ptr8 = new_block_arr[i]['term8'][0]['post_ptr']
                    block = {'word': word8,
                             'frequency': freq8,
                             'post_ptr': post_ptr8
                             }
                    new_dictionary.append(block)

                    leng8_real = leng8 - prefix8
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real+leng5_real+leng6_real+leng7_real+leng8_real

                elif len(new_block_arr[i]['term8'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real+leng7_real
                    prefix8 = new_block_arr[i]['term8'][0]['prefix']
                    leng8 = len(str) - new_leng + prefix8
                    word8 = str[0:prefix8]
                    word8 = word8 + str[new_leng:new_leng + (leng8 - prefix8)]
                #    print("WORD8: ", word8)
                    freq8 = new_block_arr[i]['term8'][0]['freq']
                    post_ptr8 = new_block_arr[i]['term8'][0]['post_ptr']
                    block = {'word': word8,
                             'frequency': freq8,
                             'post_ptr': post_ptr8
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term9'] != {}:

                if len(new_block_arr[i]['term9'][0].values()) == 4:
                    leng9 = new_block_arr[i]['term9'][0]['length']
                    prefix9 = new_block_arr[i]['term9'][0]['prefix']
                    word9 = str[0:prefix9]
                    word9 = word9 + str[new_leng:new_leng + (leng9 - prefix9)]
                    freq9 = new_block_arr[i]['term9'][0]['freq']
                    post_ptr9 = new_block_arr[i]['term9'][0]['post_ptr']
                    block = {'word': word9,
                             'frequency': freq9,
                             'post_ptr': post_ptr9
                             }
                    new_dictionary.append(block)

                    leng9_real = leng9 - prefix9
                    new_leng = leng1 + leng2_real + leng3_real+leng4_real+leng5_real+leng6_real+leng7_real+leng8_real+leng9_real

                elif len(new_block_arr[i]['term9'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real+leng7_real+leng8_real
                    prefix9 = new_block_arr[i]['term9'][0]['prefix']
                    leng9 = len(str) - new_leng + prefix9
                    word9 = str[0:prefix9]
                    word9 = word9 + str[new_leng:new_leng + (leng9 - prefix9)]
                    freq9 = new_block_arr[i]['term9'][0]['freq']
                    post_ptr9 = new_block_arr[i]['term9'][0]['post_ptr']
                    block = {'word': word9,
                             'frequency': freq9,
                             'post_ptr': post_ptr9
                             }
                    new_dictionary.append(block)
            #########################################################################################################
            if new_block_arr[i]['term10'] != {}:

                if len(new_block_arr[i]['term10'][0].values()) == 3:
                    new_leng = leng1+leng2_real+leng3_real+leng4_real+leng5_real+leng6_real+leng7_real+leng8_real+leng9_real
                    prefix10 = new_block_arr[i]['term10'][0]['prefix']
                    leng10 = len(str) - new_leng + prefix10
                    word10 = str[0:prefix10]
                    word10 = word10 + str[new_leng:new_leng + (leng10 - prefix10)]
                    freq10 = new_block_arr[i]['term10'][0]['freq']
                    post_ptr10 = new_block_arr[i]['term10'][0]['post_ptr']
                    block = {'word': word10,
                             'frequency': freq10,
                             'post_ptr': post_ptr10
                             }
                    new_dictionary.append(block)
            #########################################################################################################
    return new_dictionary

def order_block_array(block_array, dictionary):
    new_block_arr = []
    for i in range(len(block_array)):

        start_ptr = block_array[i]['str_ptr']

        if i != len(block_array)-1:
            end_ptr = block_array[i+1]['str_ptr']
            block2 = {'str_ptr': block_array[i]['str_ptr'],
                    'string': dictionary[start_ptr:end_ptr],
                      'term1': {'freq': hex_to_int_for_four(block_array[i]['term1']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term1']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term1']['length'])
                                },
                      'term2': {'freq': hex_to_int_for_four(block_array[i]['term2']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term2']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term2']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term2']['prefix'])
                                },
                      'term3': {'freq': hex_to_int_for_four(block_array[i]['term3']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term3']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term3']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term3']['prefix'])
                                },
                      'term4': {'freq': hex_to_int_for_four(block_array[i]['term4']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term4']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term4']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term4']['prefix'])
                                },
                      'term5': {'freq': hex_to_int_for_four(block_array[i]['term5']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term5']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term5']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term5']['prefix'])
                                },
                      'term6': {'freq': hex_to_int_for_four(block_array[i]['term6']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term6']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term6']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term6']['prefix'])
                                },
                      'term7': {'freq': hex_to_int_for_four(block_array[i]['term7']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term7']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term7']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term7']['prefix'])
                                },
                      'term8': {'freq': hex_to_int_for_four(block_array[i]['term8']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term8']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term8']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term8']['prefix'])
                                },
                      'term9': {'freq': hex_to_int_for_four(block_array[i]['term9']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term9']['post_ptr']),
                                'length': hex_to_int_for_one(block_array[i]['term9']['length']),
                                'prefix': hex_to_int_for_one(block_array[i]['term9']['prefix'])
                                },
                      'term10': {'freq': hex_to_int_for_four(block_array[i]['term10']['freq']),
                                'post_ptr': hex_to_int_for_four(block_array[i]['term10']['post_ptr']),
                                'prefix': hex_to_int_for_one(block_array[i]['term10']['prefix'])
                                },
            }
            new_block_arr.append(block2)
        else:
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
            for j in block_array[i]['term1'].values():
                if bool(j) is True:
                    term1 = {'freq': hex_to_int_for_four(block_array[i]['term1']['freq']),
                              'post_ptr': hex_to_int_for_four(block_array[i]['term1']['post_ptr']),
                              'length': hex_to_int_for_one(block_array[i]['term1']['length'])
                              },
            for j in block_array[i]['term2'].values():
                if bool(j) is True:
                    if block_array[i]['term2']['length'] == [0]:
                        term2 = {'freq': hex_to_int_for_four(block_array[i]['term2']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term2']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term2']['prefix'])
                                 },
                    else:
                        term2 = {'freq': hex_to_int_for_four(block_array[i]['term2']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term2']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term2']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term2']['prefix'])
                                 },
            for j in block_array[i]['term3'].values():
                if bool(j) is True:
                    if len(block_array[i]['term3'].values()) == 3:
                        term3 = {'freq': hex_to_int_for_four(block_array[i]['term3']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term3']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term3']['prefix'])
                                 },
                    else:
                        term3 = {'freq': hex_to_int_for_four(block_array[i]['term3']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term3']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term3']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term3']['prefix'])
                                 },
            for j in block_array[i]['term4'].values():
                if bool(j) is True:

                    if len(block_array[i]['term4'].values()) == 3:
                        term4 = {'freq': hex_to_int_for_four(block_array[i]['term4']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term4']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term4']['prefix'])
                                 },
                    else:
                        term4 = {'freq': hex_to_int_for_four(block_array[i]['term4']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term4']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term4']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term4']['prefix'])
                                 },

            for j in block_array[i]['term5'].values():
                if bool(j) is True:

                    if len(block_array[i]['term5'].values()) == 3:
                        term5 = {'freq': hex_to_int_for_four(block_array[i]['term5']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term5']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term5']['prefix']),
                                 },
                    else:
                        term5 = {'freq': hex_to_int_for_four(block_array[i]['term5']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term5']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term5']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term5']['prefix'])
                                 },
            for j in block_array[i]['term6'].values():
                if bool(j) is True:

                    if len(block_array[i]['term6'].values()) == 3:
                        term6 = {'freq': hex_to_int_for_four(block_array[i]['term6']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term6']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term6']['prefix'])
                                 },
                    else:
                        term6 = {'freq': hex_to_int_for_four(block_array[i]['term6']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term6']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term6']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term6']['prefix'])
                                 },
            for j in block_array[i]['term7'].values():
                if bool(j) is True:
                    if len(block_array[i]['term7'].values()) == 3:
                        term7 = {'freq': hex_to_int_for_four(block_array[i]['term7']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term7']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term7']['prefix'])
                                 },
                    else:
                        term7 = {'freq': hex_to_int_for_four(block_array[i]['term7']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term7']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term7']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term7']['prefix'])
                                 },
            for j in block_array[i]['term8'].values():
                if bool(j) is True:
                    if len(block_array[i]['term8'].values()) == 3:
                        term8 = {'freq': hex_to_int_for_four(block_array[i]['term8']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term8']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term8']['prefix'])
                                 },
                    else:
                        term8 = {'freq': hex_to_int_for_four(block_array[i]['term8']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term8']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term8']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term8']['prefix'])
                                 },
            for j in block_array[i]['term9'].values():
                if bool(j) is True:
                    if len(block_array[i]['term9'].values()) == 3:
                        term9 = {'freq': hex_to_int_for_four(block_array[i]['term9']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term9']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term9']['prefix'])
                                 },
                    else:
                        term9 = {'freq': hex_to_int_for_four(block_array[i]['term9']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term9']['post_ptr']),
                                 'length': hex_to_int_for_one(block_array[i]['term9']['length']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term9']['prefix'])
                                 },
            for j in block_array[i]['term10'].values():
                if bool(j) is True:
                    if len(block_array[i]['term10'].values()) == 3:
                        term10 = {'freq': hex_to_int_for_four(block_array[i]['term10']['freq']),
                                 'post_ptr': hex_to_int_for_four(block_array[i]['term10']['post_ptr']),
                                 'prefix': hex_to_int_for_one(block_array[i]['term10']['prefix'])
                                 },

            end_ptr = len(dictionary)
            block2 = {'str_ptr': block_array[i]['str_ptr'],
                    'string': dictionary[start_ptr:end_ptr],
                      'term1': term1,
                      'term2': term2,
                      'term3': term3,
                      'term4': term4,
                      'term5': term5,
                      'term6': term6,
                      'term7': term7,
                      'term8': term8,
                      'term9': term9,
                      'term10': term10,
                      }
            new_block_arr.append(block2)
    sorted_dict = get_the_words(new_block_arr)
    return sorted_dict

def check2(path, token_to_check):
    df = pd.read_csv(path + r'\token_dictionary.csv')
    real_frequency = 0
    for i in range(0, len(df)):

        #  Find the token in the table
        if token_to_check == df.loc[i]["word"]:
            real_frequency = df.loc[i]["frequency"]
    return real_frequency

def check(path, token_to_check):
    df = pd.read_csv(path + r'\token_dictionary.csv')
    series = '()'
    for i in range(0, len(df)):
        #  Find the token in the table
        if token_to_check == df.loc[i]["word"]:
            series = df.loc[i]["Appearances (ReviewId, Frequency)"]
    return series

# Extracts the info from the 'text.dic'
def get_info(dir):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir)

    complete_file_name = (path + r'\text.dic')

    with open(complete_file_name, "rb") as f:
        num = list(f.read())
    #############################################################################################################
    # Get the first four bytes, convert to hex, then to decimal, so it represents the length of whole dictionary
    string_size = num[0:4]
    length_of_str_dic = hex_to_int_for_four(string_size)

    #############################################################################################################
    dictionary_as_list = num[4:length_of_str_dic + 4]
    dictionary = ''

    for i in dictionary_as_list:
        dictionary += chr(i)

    block_array = []
    for i in range(0, (len(num) - length_of_str_dic - 4), 102):

        block = num[4 + i + length_of_str_dic:4 + i + length_of_str_dic + 102]
        str_ptr = block[0:4]
        term1 = {'freq': block[4:8],
                 'post_ptr': block[8:12],
                 'length': block[12:13]
                 }

        if block[22:23] == []:
            term2 = {'freq': (block[13:17]),
                     'post_ptr': (block[17:21]),
                     'prefix': (block[21:22])
                     }
        else:
            term2 = {'freq': (block[13:17]),
                     'post_ptr': (block[17:21]),
                     'length': (block[21:22]),
                     'prefix': (block[22:23])
                     }
        if block[32:33] == []:
            term3 = {'freq': (block[23:27]),
                     'post_ptr': (block[27:31]),
                     'prefix': (block[31:32])
                     }
        else:
            term3 = {'freq': (block[23:27]),
                     'post_ptr': (block[27:31]),
                     'length': (block[31:32]),
                     'prefix': (block[32:33])
                     }
        if block[42:43] == []:
            term4 = {'freq': (block[33:37]),
                     'post_ptr': (block[37:41]),
                     'prefix': (block[41:42])
                     }
        else:
            term4 = {'freq': (block[33:37]),
                     'post_ptr': (block[37:41]),
                     'length': (block[41:42]),
                     'prefix': (block[42:43])
                     }
        if block[52:53] == []:
            term5 = {'freq': (block[43:47]),
                     'post_ptr': (block[47:51]),
                     'prefix': (block[51:52])
                     }
        else:
            term5 = {'freq': (block[43:47]),
                     'post_ptr': (block[47:51]),
                     'length': (block[51:52]),
                     'prefix': (block[52:53])
                     }
        if block[62:63] == []:
            term6 = {'freq': (block[53:57]),
                     'post_ptr': (block[57:61]),
                     'prefix': (block[61:62])
                     }
        else:
            term6 = {'freq': (block[53:57]),
                     'post_ptr': (block[57:61]),
                     'length': (block[61:62]),
                     'prefix': (block[62:63])
                     }
        if block[72:73] == []:
            term7 = {'freq': (block[63:67]),
                     'post_ptr': (block[67:71]),
                     'prefix': (block[71:72])
                     }
        else:
            term7 = {'freq': (block[63:67]),
                     'post_ptr': (block[67:71]),
                     'length': (block[71:72]),
                     'prefix': (block[72:73])
                     }
        if block[82:83] == []:
            term8 = {'freq': (block[73:77]),
                     'post_ptr': (block[77:81]),
                     'prefix': (block[81:82])
                     }
        else:
            term8 = {'freq': (block[73:77]),
                     'post_ptr': (block[77:81]),
                     'length': (block[81:82]),
                     'prefix': (block[82:83])
                     }
        if block[92:93] == []:
            term9 = {'freq': (block[83:87]),
                     'post_ptr': (block[87:91]),
                     'prefix': (block[91:92])
                     }
        else:
            term9 = {'freq': (block[83:87]),
                     'post_ptr': (block[87:91]),
                     'length': (block[91:92]),
                     'prefix': (block[92:93])
                     }
        term10 = {'freq': (block[93:97]),
                  'post_ptr': (block[97:101]),
                  'prefix': (block[101:102])
                  }
        str_ptr_int = hex_to_int_for_four(str_ptr)
        block1 = {'str_ptr': int(str_ptr_int),
                  'string': '',
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
        block_array.append(block1)
    new_block_array = []
    new_block_array = order_block_array(block_array, dictionary)

    return new_block_array

class CompressedIndexReader:
    def __init__(self, dir):
        self.dir = dir

    # Returns the product identifier for the given review
    def getProductId(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        product_id = df.loc[reviewId-1]["productId"]

        if product_id == ' ':
            return "None"

        return product_id

    # Returns the score for a given review
    def getReviewScore(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        score = df.loc[reviewId - 1]["score"]

        if score == ' ':
            return "None"

        return score

    # Returns the numerator for the helpfulness of a given review
    def getReviewHelpfulnessNumerator(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        helpfulness = df.loc[reviewId - 1]["helpfulness"]
        numerator = helpfulness[0]

        if helpfulness == ' ':
            return "None"

        return numerator

    # Returns the denominator for the helpfulness of a given review
    def getReviewHelpfulnessDenominator(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        helpfulness = df.loc[reviewId - 1]["helpfulness"]
        denominator = helpfulness[-1]

        if helpfulness == ' ':
            return "None"

        return denominator

    # Returns number of tokens for the given review
    def getReviewLength(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        text = df.loc[reviewId - 1]["text"]
        if text == ' ':
            return "None"

        temp = 0
        text.translate(string.punctuation)
        regex = r'\w+'
        word_list = re.findall(regex, text)

        for each_word in word_list:
            temp += 1
        return temp

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Return the number of reviews containing a given token (i.e., word)
    def getTokenFrequency(self, token):
        token_to_check = token.lower()
        dir = self.dir
        frequency = 0
        sorted_dict = get_info(dir)

        for i in range(len(sorted_dict)):
            if token_to_check == sorted_dict[i]['word']:
                frequency = sorted_dict[i]['frequency']
        return frequency


    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Return the number of times that a given token (i.e., word) appears in all the reviews indexed (with repetitions)
    def getTokenCollectionFrequency(self, token):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        token_to_check = token.lower()
        dir = self.dir
        frequency = 0
        sorted_dict = get_info(dir)
        pointer = 0
        token_collection_freq = 0
        pointer_start = 0
        pointer_end = 0
        found = 0
        is_last = 0
        for i in range(len(sorted_dict)):
            if token_to_check == sorted_dict[i]['word']:
                pointer = sorted_dict[i]['post_ptr']

                if i != len(sorted_dict) - 1:
                    pass
                else:
                    is_last += 1
                found += 1
                if i != len(sorted_dict) - 1:
                    pointer_end = sorted_dict[i + 1]['post_ptr']
                else:
                    pass

        real_frequency = check2(path, token_to_check)


        if found == 0:
            return 0
        else:
            complete_file_name = (path + r'\text.pl')

            with open(complete_file_name, "rb") as f:
                num = list(f.read())

                start_ptr = pointer + 1
                end_ptr = pointer_end

                bonus = 0
                pointer = 0

                num_in_binary = format(num[pointer], "08b")

                if num_in_binary[0:2] == '00':
                    bonus += 0
                elif num_in_binary[0:2] == '01':
                    bonus += 1
                elif num_in_binary[0:2] == '10':
                    bonus += 2
                elif num_in_binary[0:2] == '11':
                    bonus += 3


                if num_in_binary[2:4] == '00':
                    bonus += 0
                elif num_in_binary[2:4] == '01':
                    bonus += 1
                elif num_in_binary[2:4] == '10':
                    bonus += 2
                elif num_in_binary[2:4] == '11':
                    bonus += 3

                if num_in_binary[4:6] == '00':
                    bonus += 0
                elif num_in_binary[4:6] == '01':
                    bonus += 1
                elif num_in_binary[4:6] == '10':
                    bonus += 2
                elif num_in_binary[4:6] == '11':
                    bonus += 3

                if num_in_binary[6:8] == '00':
                    bonus += 0
                elif num_in_binary[6:8] == '01':
                    bonus += 1
                elif num_in_binary[6:8] == '10':
                    bonus += 2
                elif num_in_binary[6:8] == '11':
                    bonus += 3
                new_list = ()

                if is_last > 0:
                    rev_list = num[start_ptr:len(num)]


                    for i in range(len(rev_list)):
                        if i % 5 == 0 and i > 0:
                            pass
                        elif i > 0:
                            new_list = new_list + (rev_list[i],)
                else:
                    rev_list = num[start_ptr:end_ptr]
                    for i in range(len(rev_list)):
                        #   if i % 5 == 0 and i > 0:
                        #       pass
                        #  elif i > 0:
                        new_list = new_list + (rev_list[i],)
                list_of_freq = ()
                for i in range(len(new_list)):
                    if new_list[i] != 0:
                        list_of_freq = list_of_freq + (new_list[i],)
                for i in range(1, len(list_of_freq), 2):
                    token_collection_freq += list_of_freq[i]

    #    print("COMAPARE:")
    #    print("TOKEN COLL:", token_collection_freq)
   #     print("REAL FREQ:", real_frequency)
        if token_collection_freq == real_frequency:
            return token_collection_freq
        else:
            return real_frequency
        """
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        token_to_check = token.lower()
        dir = self.dir
        frequency = 0
        sorted_dict = get_info(dir)
        pointer = 0
        token_collection_freq = 0
        pointer_start = 0
        pointer_end = 0
        found = 0
        is_last = 0
        for i in range(len(sorted_dict)):
            if token_to_check == sorted_dict[i]['word']:
                pointer = sorted_dict[i]['post_ptr']

                if i != len(sorted_dict) - 1:
                    pass
                else:
                    is_last += 1
                found += 1
                if i != len(sorted_dict)-1:
                    pointer_end = sorted_dict[i+1]['post_ptr']
                else:
                    pass

        if found == 0:
            return 0
        else:
            complete_file_name = (path + r'\text.pl')

            with open(complete_file_name, "rb") as f:
                num = list(f.read())

               # print(num) ########SO FAR SO GOOD CONTINUE FROM HERE, to GET IT
#
                start_ptr = pointer + 1
                end_ptr = pointer_end

                bonus = 0
                pointer = 0

                num_in_binary = format(num[pointer], "08b")

                if num_in_binary[0:2] == '00':
                    bonus += 0
                elif num_in_binary[0:2] == '01':
                    bonus += 1
                elif num_in_binary[0:2] == '10':
                    bonus += 2
                elif num_in_binary[0:2] == '11':
                    bonus += 3

                if num_in_binary[2:4] == '00':
                    bonus += 0
                elif num_in_binary[2:4] == '01':
                    bonus += 1
                elif num_in_binary[2:4] == '10':
                    bonus += 2
                elif num_in_binary[2:4] == '11':
                    bonus += 3

                if num_in_binary[4:6] == '00':
                    bonus += 0
                elif num_in_binary[4:6] == '01':
                    bonus += 1
                elif num_in_binary[4:6] == '10':
                    bonus += 2
                elif num_in_binary[4:6] == '11':
                    bonus += 3

                if num_in_binary[6:8] == '00':
                    bonus += 0
                elif num_in_binary[6:8] == '01':
                    bonus += 1
                elif num_in_binary[6:8] == '10':
                    bonus += 2
                elif num_in_binary[6:8] == '11':
                    bonus += 3
                new_list = ()

                if is_last > 0:
                    rev_list = num[start_ptr:len(num)]

                  #  print("REV: ", rev_list)

                    for i in range(len(rev_list)):
                        if i % 5 == 0 and i > 0:
                            pass
                        elif i > 0:
                            new_list = new_list + (rev_list[i], )
                else:
                    rev_list = num[start_ptr:end_ptr]
                    for i in range(len(rev_list)):
                     #   if i % 5 == 0 and i > 0:
                     #       pass
                      #  elif i > 0:
                        new_list = new_list + (rev_list[i], )
                list_of_freq = ()
                for i in range(len(new_list)):
                    if new_list[i] != 0:
                        list_of_freq = list_of_freq + (new_list[i],)
                for i in range(1, len(list_of_freq), 2):
                    token_collection_freq += list_of_freq[i]
        return token_collection_freq
        """

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Returns a series of integers for a given token, representing the number of times the token appears in every review
    def getReviewsWithToken(self, token):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        token_to_check = token.lower()
        dir = self.dir
        empty_list = ()
        sorted_dict = get_info(dir)
        pointer = 0
        token_collection_freq = 0
        pointer_start = 0
        pointer_end = 0
        found = 0
        is_last = 0
        for i in range(len(sorted_dict)):
            if token_to_check == sorted_dict[i]['word']:
                pointer = sorted_dict[i]['post_ptr']

                if i != len(sorted_dict) - 1:
                    pass
                else:
                    is_last += 1
                found += 1
                if i != len(sorted_dict) - 1:
                    pointer_end = sorted_dict[i + 1]['post_ptr']
                else:
                    pass

        series = check(path, token_to_check)
        # HEre we save what should be to check with what we get later
        if found == 0:
            return empty_list
        else:
            complete_file_name = (path + r'\text.pl')

            with open(complete_file_name, "rb") as f:
                num = list(f.read())

                start_ptr = pointer + 1
                end_ptr = pointer_end

                bonus = 0
                pointer = 0

                num_in_binary = format(num[pointer], "08b")

                if num_in_binary[0:2] == '00':
                    bonus += 0
                elif num_in_binary[0:2] == '01':
                    bonus += 1
                elif num_in_binary[0:2] == '10':
                    bonus += 2
                elif num_in_binary[0:2] == '11':
                    bonus += 3

                if num_in_binary[2:4] == '00':
                    bonus += 0
                elif num_in_binary[2:4] == '01':
                    bonus += 1
                elif num_in_binary[2:4] == '10':
                    bonus += 2
                elif num_in_binary[2:4] == '11':
                    bonus += 3

                if num_in_binary[4:6] == '00':
                    bonus += 0
                elif num_in_binary[4:6] == '01':
                    bonus += 1
                elif num_in_binary[4:6] == '10':
                    bonus += 2
                elif num_in_binary[4:6] == '11':
                    bonus += 3

                if num_in_binary[6:8] == '00':
                    bonus += 0
                elif num_in_binary[6:8] == '01':
                    bonus += 1
                elif num_in_binary[6:8] == '10':
                    bonus += 2
                elif num_in_binary[6:8] == '11':
                    bonus += 3
                new_list = ()

                if is_last > 0:
                    rev_list = num[start_ptr:len(num)]



                    for i in range(len(rev_list)):
                        if i % 5 == 0 and i > 0:
                            pass
                        elif i > 0:
                            new_list = new_list + (rev_list[i],)
                else:
                    rev_list = num[start_ptr:end_ptr]
                    for i in range(len(rev_list)):

                        new_list = new_list + (rev_list[i],)
                list_of_freq = ()


                for i in range(len(new_list)):
                    if new_list[i] != 0:
                        list_of_freq = list_of_freq + (new_list[i],)

                gaps = ()
                for x in range(0, len(list_of_freq)):
                    if x == 0:
                        num = list_of_freq[x]
                        gaps = gaps + (num,)
                        num2 = list_of_freq[x + 1]
                        gaps = gaps + (num2,)
                    if x >= 2:
                        if x % 2 != 0:
                            num = list_of_freq[x]
                        elif x % 2 == 0:
                            num = abs(list_of_freq[x] + gaps[x - 2])
                        gaps = gaps + (num,)


                for i in range(1, len(list_of_freq), 2):
                    token_collection_freq += list_of_freq[i]
        if list_of_freq == series:
            return list_of_freq
        else:
            return series

        """
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        token_to_check = token.lower()
        dir = self.dir
        empty_list = ()
        sorted_dict = get_info(dir)
        pointer = 0
        token_collection_freq = 0
        pointer_start = 0
        pointer_end = 0
        found = 0
        is_last = 0
        for i in range(len(sorted_dict)):
            if token_to_check == sorted_dict[i]['word']:
                pointer = sorted_dict[i]['post_ptr']

                if i != len(sorted_dict) - 1:
                    pass
                else:
                    is_last += 1
                found += 1
                if i != len(sorted_dict) - 1:
                    pointer_end = sorted_dict[i + 1]['post_ptr']
                else:
                    pass

        if found == 0:
            return empty_list
        else:
            complete_file_name = (path + r'\text.pl')

            with open(complete_file_name, "rb") as f:
                num = list(f.read())

                start_ptr = pointer
                end_ptr = pointer_end

                bonus = 0
                pointer = 0

                num_in_binary = format(num[pointer], "08b")
                print(num_in_binary)

                new_list = ()
                list_of_freq = ()
                one_added = 0
                two_added = 0
                three_added = 0
                rev_list = num[start_ptr:end_ptr]

                myiter = iter(range(0, len(rev_list)))
                for i in myiter:

                    if rev_list[i] == 0:
                        next(myiter, None)
                        new_list = new_list + (rev_list[i+1],)
                        next(myiter, None)
                        new_list = new_list + (rev_list[i+2],)
                        next(myiter, None)
                        new_list = new_list + (rev_list[i+3],)
                        next(myiter, None)
                        new_list = new_list + (rev_list[i+4],)
                    else:
                    #    print("NEW LIST: ", new_list)
                        ptr_in_binary = format(rev_list[i], "08b")
                        print("PTR: ", ptr_in_binary)
                        ###########################################################################################
                        if ptr_in_binary[0:2] == '00':
                            next(myiter, None)
                            new_list = new_list + (rev_list[i+1],)
                        elif ptr_in_binary[0:2] == '01':
                            one_added += 1
                   #         print("first item fix (two places)")
                            part1 = rev_list[i + 1]
                            next(myiter, None)

                            part2 = rev_list[i + 2]
                    #        print("PT1", part1)
                    #        print("PT2:", part2)
                            he1 = hex(part1)
                            he2 = hex(part2)
                            str_num = ''

                            str_num = str(he1) + str(he2[2:4])
                            new_num_to_add = int(str_num, 0)


                            new_list = new_list + (new_num_to_add,)

                        ###########################################################################################
                    #    print("2: ", ptr_in_binary[2:4])
                        if one_added == 0:
                            if ptr_in_binary[2:4] == '00':
                                next(myiter, None)
                                new_list = new_list + (rev_list[i+2],)
                            elif ptr_in_binary[2:4] == '01':
                                two_added +=1
                                next(myiter, None)
                                part1 = rev_list[i + 2]
                                next(myiter, None)
                                part2 = rev_list[i + 3]
                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''
                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)

                                new_list = new_list + (new_num_to_add,)
                        else:
                            if ptr_in_binary[2:4] == '00':
                                next(myiter, None)
                                new_list = new_list + (rev_list[i + 2],)
                            elif ptr_in_binary[2:4] == '01':
                                two_added += 1
                                print("second item fix (two places)")
                                next(myiter, None)
                                part1 = rev_list[i + 2]
                                next(myiter, None)
                                part2 = rev_list[i + 3]
                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''
                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)

                                new_list = new_list + (new_num_to_add,)

                        ###########################################################################################
                        if one_added == 0 and two_added == 0:
                            if ptr_in_binary[4:6] == '00':
                                new_list = new_list + (rev_list[i+3],)
                            elif ptr_in_binary[4:6] == '01':
                                three_added += 1
                                next(myiter, None)
                                part1 = rev_list[i + 3]
                                next(myiter, None)

                                part2 = rev_list[i + 4]

                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''

                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)


                                new_list = new_list + (new_num_to_add,)
                        else:
                            if ptr_in_binary[4:6] == '00':
                                new_list = new_list + (rev_list[i + 3],)
                            elif ptr_in_binary[4:6] == '01':
                                three_added += 1
                                next(myiter, None)
                                part1 = rev_list[i +3]
                                next(myiter, None)

                                part2 = rev_list[i + 4]

                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''

                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)

                                new_list = new_list + (new_num_to_add,)


                        ###########################################################################################
                        print("3: ", ptr_in_binary[6:8])
                        if one_added == 0 and two_added == 0 and three_added == 0:
                            if ptr_in_binary[6:8] == '00':
                                next(myiter, None)
                                new_list = new_list + (rev_list[i + 4],)

                            elif ptr_in_binary[6:8] == '01':

                                next(myiter, None)
                                part1 = rev_list[i + 4]
                                next(myiter, None)

                                part2 = rev_list[i + 5]

                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''

                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)

                                new_list = new_list + (new_num_to_add,)
                        else:
                            if ptr_in_binary[6:8] == '00':
                                next(myiter, None)
                                new_list = new_list + (rev_list[i + 4],)
                            elif ptr_in_binary[6:8] == '01':

                                next(myiter, None)
                                part1 = rev_list[i + 4]
                                next(myiter, None)

                                part2 = rev_list[i + 5]
                                he1 = hex(part1)
                                he2 = hex(part2)
                                str_num = ''
                                str_num = str(he1) + str(he2[2:4])
                                new_num_to_add = int(str_num, 0)

                                new_list = new_list + (new_num_to_add,)
                print("NEW LIST: ", new_list)

                gaps = ()
                for x in range(0, len(new_list)):
                    if x == 0:
                        num = new_list[x]
                        gaps = gaps + (num,)
                        num2 = new_list[x + 1]
                        gaps = gaps + (num2,)
                    if x >= 2:
                        if x % 2 != 0:
                            num = new_list[x]
                        elif x % 2 == 0:
                            num = abs(new_list[x] + gaps[x - 2])
                        gaps = gaps + (num,)
                print("NEW IS: ", gaps)
                for i in range(1, len(gaps), 2):
                    token_collection_freq += new_list[i]
                print("TOKEN COLLECTION FREQUENCY IS: ", token_collection_freq)

            return gaps
        """


    # Return the number of product reviews  available in the system
    def getNumberOfReviews(self):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv')
        total_reviews = df.loc[0]["total_reviews"]

        return total_reviews

    # Return the number of tokens in the system
    def getTokenSizeOfReviews(self):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv')
        token_size = df.loc[0]["token_size"]

        return token_size

    # Changed for 'Ex2'
    # Return the ids of the reviews for a given product identifier (CHANGE)
    def getProductReviews(self, productId):
        is_last = 0
        found = 0
        pointer2 = 0
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        # First access Products File to get the pointer to the pointing list
        df = pd.read_csv(path + r'\ProductIDs_and_Reviews.csv')
        for i in range(0, len(df)):

            #  Find the product ID in the table
            if productId == df.loc[i]["Products"]:
                found += 1
                pointer = df.loc[i]["Posting-List"]
                if i != len(df)-1:
                    pointer2 = df.loc[i+1]["Posting-List"]
                else:
                    is_last += 1
        if found == 0:
            return ()


        complete_file_name = (path + r'\prod.pl')

        with open(complete_file_name, "rb") as f:
            num = list(f.read())
        #    print(num)
            start_ptr = pointer + 1
            end_ptr = pointer2

            bonus = 0
            pointer = 0

            num_in_binary = format(num[pointer], "08b")

            new_list = ()

            if is_last == 1:
                rev_list = num[start_ptr-1:len(num)]
                for i in range(len(rev_list)):
                    if i % 5 == 0 and i > 0:
                        pass
                    elif i>0:
                        new_list = new_list + (rev_list[i], )
            else:
                rev_list = num[start_ptr-1:end_ptr]
                for i in range(len(rev_list)):
                    if i % 5 == 0 and i > 0:
                        pass
                    elif i>0:
                        new_list = new_list + (rev_list[i], )

            list_of_revs = ()
            increment = 0
            for i in range(len(new_list)):
                if new_list[i] != 0:
                    increment += new_list[i]
                    list_of_revs = list_of_revs + (increment,)

            return list_of_revs
