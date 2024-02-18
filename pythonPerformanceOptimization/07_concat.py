import time
start_time = time.time()

# test 1
from nltk.corpus import words # pip install nltk
word_list = words.words()
mystr = ""
for s in word_list:
    mystr += s
    mystr += ","
print(mystr)

# test 2
from nltk.corpus import words # pip install nltk
word_list = words.words()
mystr = ",".join(word_list)
print(mystr)

end_time = time.time()
print(end_time - start_time)