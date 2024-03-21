# jsut implement byte-pair encoding and test it


text = "low low low lowest lowest wider new new"
text = text+" "
words = text.split(" ")
corpus = {}
for word in words:
    if word != "":
        corpus[word+" "] = text.count(word+" ")
print(corpus)


def byte_pair_encoding(corpus, k):
    chars = list(set("".join(list(corpus.keys()))))
    print(chars)
    for _ in range(k):
        pairs = []
        for char in chars:
            for char2 in chars:
                pairs.append(char+char2)
        max_pair_freq = 0
        max_pair = ""
        for pair in pairs:
            freq = 0
            for key in corpus:
                freq+=corpus[key]*key.count(pair)
            if freq>max_pair_freq and not pair in chars:
                max_pair_freq=freq
                max_pair = pair
        if max_pair != "":
            chars.append(max_pair)
    return chars

print(byte_pair_encoding(corpus, 50))
