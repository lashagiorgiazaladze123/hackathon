def opa(word,argument):
    res = []
    result = ""
    for i in word:
        if i != argument:
            res.append(i)
    for i in res:
        result+= i
    return result
print(opa("hello","l"))