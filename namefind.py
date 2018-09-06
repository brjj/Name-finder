import itertools

def findStars(name):
    for i, l in enumerate(name):
        if l == "*":
            yield i;


def findNames(name, content):
    alphabet = "abcedfghijklmnopqrstuvwxyzåäö";
    stars = list(findStars(name))
    replacements = itertools.product(alphabet, repeat=len(stars))
    for replacement in replacements:
        replacement_with_index = tuple(zip(stars, replacement))
        wordAsList = list(name)
        for i, l in replacement_with_index:
            wordAsList[i] = l
        candidate = "".join(wordAsList)
        if candidate in content:
            yield candidate
        



with open("names.txt") as f:
    content = f.readlines();
for i in range(0, len(content)):
    content[i] = content[i].strip().lower();
while True:
    name = input("Name: ").lower().split();
    for l in name:
        for foundName in findNames(l, content):
            print(foundName);
