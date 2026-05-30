#Total number of words
#Longest word
#Shortest word
#How many words start with a vowel (a, e, i, o, u)
def info_word(sentence):
    
    words=sentence.split()

    biggest_word=words[0]
    shortest_word=words[0]
    starts_vowel=0
    total=0
    for word in words:
        word=word.strip()
        if len(word)>=1:
            total+=1
        if len(word)>len(biggest_word):
            biggest_word=word
        if len(shortest_word)>len(word):
            shortest_word=word
        if word[0].lower() in                                                         ("a","e","i","o","u"):
            starts_vowel+=1
    
    print(f"""Biggest word:{biggest_word}
    shortest word:{shortest_word}
    starts vowel:{starts_vowel} 
    total words:{total }""" )







info_word ("I am a fairy")




















