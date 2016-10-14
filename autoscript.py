with open('t.md', 'r') as f:
    content = f.readlines()

title = [l for l in content if l.startswith('Title:')][0][6:-1].strip(' ')
conf = [l for l in content if l.startswith('Conf')][0][5:-1].strip(' ')
author = [l for l in content if l.startswith('Author')][0][7:-1].strip(' ')

print(title)
print(conf)
print(author)
