def reverse1(word1):
    import random
    s1=word1
    s2=""
    len1=len(s1)
    for i in range(0,len1,1):
        s2=s2+s1[len1-i-1:len1-i]
    print(s2)
reverse1("Next visit, I am going to teach him Python coding to build some simple games and puzzles")
