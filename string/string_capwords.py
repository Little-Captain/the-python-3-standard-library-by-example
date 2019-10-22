import string

s = 'The quick brown fox jumped over the lazy dog.'

print(s)
print(string.capwords(s))
# string.capwords
# (sep or ' ').join(x.capitalize() for x in s.split(sep))