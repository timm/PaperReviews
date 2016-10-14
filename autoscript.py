import datetime

with open('template.txt', 'r') as f:
    content = f.readlines()

title = [l for l in content if l.startswith('Title:')][0][6:-1].strip(' ')
conf = [l for l in content if l.startswith('Conf')][0][5:-1].strip(' ')
author = [l for l in content if l.startswith('Author')][0][7:-1].strip(' ')
keyword = [l for l in content if l.startswith('Keywords')][0][9:-1].strip(' ')

print("Title: %s" % title)
print("Conference/Journal: %s"%conf)
print("Author: %s" % author)

# determine whether this paper existed
# TODO

notefilename = 'notes/'+title.replace(' ','_')+'.md'

with open('README.md', 'a') as f:
    f.write('|%s|[%s](%s)|%s|%s|\n' % (
        datetime.date.today().strftime('%b %m, %Y'),
        title,
        notefilename,
        conf,
        keyword))

with open(notefilename, 'w') as f:
    f.write('|Title|%s|\n'%title)
    f.write('|---------|---|\n')
    f.write('|Conference/Journal|%s|\n'%conf)
    f.write('|Author|%s|\n'%title)
    f.write('|Key words|%s|\n'%keyword)

    for i,v in enumerate(content):
        if v.startswith('~~~'): break

    incodemode = False
    while i < len(content)-1:
        i += 1
        l = content[i]
        
        if l.startswith('```') and not incodemode:
            incodemode = True
            f.write(l)
            continue
        
        if incodemode:
            f.write(l)
            if l.startswith('```'):
                incodemode = False
            continue
        
        if '-fig' in l:
            figname = l[5:-1]
            f.write('![](/figures/%s)  \n'%figname)
            continue
         
        f.write(l.replace('\n','  \n'))

