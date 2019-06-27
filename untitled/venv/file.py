f = open('data.txt', 'w')
string = """
Но я люблю её, за что не знаю сам,
её степей холодное молчанье,
её лесов безбрежных колыханье,
разливы рек её, подобные морям.
"""
f.write(string)
f.close()

f = open('data.txt', 'r')
text = f.read()
f.close()
for word in text.split():
    print(word)