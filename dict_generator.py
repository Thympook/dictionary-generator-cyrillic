import string


splitted_list = []
output = []
buff = ''

print('In process...')

try:
    with open('input.txt', encoding='UTF-8') as file:
        text = file.readlines()

    for line in text:
        splitted_list.extend(line.split())

    text.clear()

    for word in splitted_list:
        for char in word:
            if char in string.ascii_letters or char in string.digits or char in string.punctuation:
                continue
            else:
                buff += char
        if len(buff) < 3:
            buff = ''
            continue
        else:
            output.append(buff.lower())
            buff = ''

    splitted_list.clear()
    output = list(set(output))
    output.sort()

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(output))

except Exception as exc:
    print(exc)
    print('Something went wrong :C')
else:
    print('Success!')
