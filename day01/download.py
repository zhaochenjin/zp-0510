from urllib.request import urlopen

with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4') as f:
    counter = 1
    for line in f.readlines():
        line = line.decode('utf-8')
        if 'img class=""' in line:
            url = line.strip()[len('<img class="" src="'):len(line.strip()) - 1]
            with urlopen(url) as f1:
                with open('images/' + str(counter) + '.jpg', 'wb') as f2:
                    f2.write(f1.read())
                    counter = counter + 1
