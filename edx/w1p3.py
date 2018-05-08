#s = 'azcbobobegghakl'
#s = 'akfowraabv'
#s = 'ouifwvewpfeclpedmfiazp'
s = 'ocsuohrwrwdtxjkekrki'
counter = 0
prev_counter = 0
prev_ord = 0
str_len = len(s)
cindex = 0

for i, c in enumerate(s):
    if ord(c) >= prev_ord:
        counter += 1
        prev_ord = ord(c)
    else:
        if counter > prev_counter:
            prev_counter = counter
            cindex = i
        counter = 1
        prev_ord = ord(c)

    if i == str_len-1:
        if counter > prev_counter:
            prev_counter = counter
            cindex = i+1

print("Longest substring in alphabetical order is:", s[cindex-prev_counter:cindex])
