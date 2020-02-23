"""
•	Copy a short paragraph from any online resource into a string
•	Split the string into words and create a list of words
•	Write the code to count the number of unique words in your paragraph
"""

paragraph=("Copy a short paragraph from any online resource into a string Split the string into words and create a list of words Write the code to count the number of unique words in your paragraph")


s_para= paragraph.split()
print(s_para)
myset = set(s_para)
print("the unique words in that paragraph are: ")
print(myset)
