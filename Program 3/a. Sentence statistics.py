# 3a) find no of words, digits, uppercases, lowercases
sentence=input("Enter the sentence:")
wordlist=sentence.split(" ")
print("The sentence has ",len(wordlist),"words")

digcnt=upcnt=locnt=0
for ch in sentence:
    if ch.isdigit():
        digcnt+=1
    elif ch.isupper():
        upcnt+=1
    elif ch.islower():
        locnt+=1
print("\n This sentence has",digcnt,"digits\n",upcnt,"Upper case letters\n",locnt,"Lower case letters\n")                