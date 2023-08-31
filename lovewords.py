lovewords={"british":["love","honey","darling"],
           "turkish":["balım","canım","aşkım","bir tanem"],
           "tagalog":["mahal","sinta"],
           }
print("love words dictionary of keanne and ilayda")
for dd in lovewords:
    print(dd)
    for aa in lovewords[dd]:
        print("\t",aa,)


lang=input("in which language would you like to be spoiled today?")
if lang in lovewords:
    print("available words:",lovewords[lang])
    word=input("which one you'd like to hear this morning?")
    if word in lovewords[lang]:
        print("I will be spoiling you with all my affection today,", word)

