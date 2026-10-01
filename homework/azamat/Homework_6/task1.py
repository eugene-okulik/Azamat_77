text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

t = text.split()
for t in t:
        if t[-1] == ',' or t[-1] == '.':
                print(t[:-1] + "‘ing’" + t[-1], end=' ')
        else:
                print(t + "‘ing’", end=' ')
