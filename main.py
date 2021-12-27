from CompressedIndexWriter import CompressedIndexWriter
from CompressedIndexReader import CompressedIndexReader


# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    DIR = "prj_index"

    # create an instance of the index writer class

    idxW = CompressedIndexWriter('100.txt', DIR)

    idxR = CompressedIndexReader(DIR)

    REVIEW_ID = 18

    TOKEN = "Covid19"
    TOKEN2 = "products"
    TOKEN3 = "food"
    TOKEN_LAST_IN_10 = "yummy"

    PROD_TRIAL = "B0019CW0HE"  # last
    PROD_TRIAL2 = "B005DUM9UQ"
    PRODUCT_ID = "B000E7L2R4"
    PRODUCT_ID2 = "B001EO5QW8"
    PRODUCT_ID4 = "B006F2NYI2"
    PRODUCT_ID3 = "ZMNKSI093"
    TRIAL = "B000G6RPMY"

# use the index reader to query the system
    print("Product ID for the review")
    print(idxR.getProductId(REVIEW_ID))

    print("Review Score")
    print(idxR.getReviewScore(REVIEW_ID))

    print("Numerator:")
    print(idxR.getReviewHelpfulnessNumerator(REVIEW_ID))

    print("Denominator:")
    print(idxR.getReviewHelpfulnessDenominator(REVIEW_ID))

    print("Review Length:")
    print(idxR.getReviewLength(REVIEW_ID))

    ##### WORKS (ABOVE)









    ##### NEWWW: WORKS BELOW

    print("Token Frequency for COVID19:")
    print(idxR.getTokenFrequency(TOKEN))
    print("Token Frequency for 'products':")
    print(idxR.getTokenFrequency(TOKEN2))
    print("Token Frequency for 'food':")
    print(idxR.getTokenFrequency(TOKEN3))
    print("Token Frequency for 'and':")
    print(idxR.getTokenFrequency('and'))
    print("Token Frequency for LAST: 'yummy':")
    print(idxR.getTokenFrequency('yummy'))
    print("Token Frequency for: 'your':")
    print(idxR.getTokenFrequency('your'))


    # FIX
    print("TOKEN collection frequency for '0':")
    print(idxR.getTokenCollectionFrequency('0'))
    print("TOKEN collection frequency for 'a':")
    print(idxR.getTokenCollectionFrequency('a'))
    print("TOKEN collection frequency for food:")
    print(idxR.getTokenCollectionFrequency(TOKEN3))
    print("TOKEN collection frequency for not COVID19:")
    print(idxR.getTokenCollectionFrequency(TOKEN))
    print("Token collection Frequency for 'and':")
    print(idxR.getTokenCollectionFrequency('and'))
    print("Token collection Frequency for 'yummy':") ##
    print(idxR.getTokenCollectionFrequency(TOKEN_LAST_IN_10)) ##

    # FIX
    print("Series (work) - '0'")
    print(idxR.getReviewsWithToken('0'))

    print("Series (work) - products")
    print(idxR.getReviewsWithToken(TOKEN2))
    print("Series (work) - food")
    print(idxR.getReviewsWithToken(TOKEN3))
    print("Series (not work) - COVID19")
    print(idxR.getReviewsWithToken(TOKEN))
    print("Series  - yummy")
    print(idxR.getReviewsWithToken('yuMmY'))
    print("Series  - yunnab")
    print(idxR.getReviewsWithToken('yunnan'))
    # (3, 1, 5, 1, 15, 1, 74, 1, 155, 1, 156, 1, 281, 1, 318, 1, 379, 1, 451, 1, 482, 1, 540, 1, 608, 1, 620, 1, 896, 1, 953, 1, 996, 1)
    print("Series  - zucchini")
    print(idxR.getReviewsWithToken('zucchini'))
    # (902, 2, 30, 1, 10, 1, 2, 1)






    ############### WORKS (BELOW)

    print("NUM OF REVIEWS:")
    print(idxR.getNumberOfReviews())

    print("TOTAL TOKEN SIZE:")
    print(idxR.getTokenSizeOfReviews())

    print("REVIEWS for p ID (works")
    print("LAST: ", idxR.getProductReviews(PROD_TRIAL))

    print("THIS: (64, 1, 1, 1, 1, 0, 0, 0),        WE GOT: ", idxR.getProductReviews(PROD_TRIAL2))


    print("REVIEWS for p ID (works")
    print("(9, 0, 0, 0) -------------------", idxR.getProductReviews(PRODUCT_ID))
    print("(33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0): ", idxR.getProductReviews(PRODUCT_ID2))
    print("NOT IN 100: ", idxR.getProductReviews(PRODUCT_ID4))
    print("REVIEWS for p ID (not works")
    print(idxR.getProductReviews(PRODUCT_ID3))
    print("REVIEWS TRIAL")
    print(idxR.getProductReviews(TRIAL))

    idxW.removeIndex(DIR)









