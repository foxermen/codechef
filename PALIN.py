def inc_char(ch):
    return chr(ord(ch) + 1)


def inc_half(half):
    cur = True
    ls = [x for x in half[::-1]]
    for i in range(len(half)):
        if cur and ls[i] == '9':
            ls[i] = '0'
        else:
            ls[i] = inc_char(ls[i])
            cur = False
            break
    if cur:
        ls.append('1')
    return ''.join(ls[::-1])

cnt = int(input().strip())
for _ in range(cnt):
    string = input().strip()
    n = len(string)
    if n == 1:
        if string != '9':
            print(inc_char(string))
        else:
            print(11)
        continue
    start_half_len = n // 2
    mid = string[n // 2] if n % 2 == 1 else ''
    half = string[:start_half_len]
    if half + mid + half[::-1] > string:
         print(half + mid + half[::-1])
    else:
        if mid != '' and mid != '9':
            print(half + inc_char(mid) + half[::-1])
        else:
            half = inc_half(half)
            if len(half) > start_half_len:
                if mid != '':
                     print(half + half[::-1])
                else:
                     print(half[:-1] + half[::-1])
            else:
               if mid != '':
                   print(half + '0' + half[::-1])
               else:
                   print(half + half[::-1])


