import re


m=re.match('^f[a-z]*\.?o$','fooog.o')
if m is not None:
    print(m.group())


s=re.match('^((ht{2}ps?|HT{2}PS?):?(/{2})?)?w{3}\.[123]{3}\.\D{1,3}','https://www.123.com')
if s is not None:
    print(s.group())


s=re.match("\w*\.db$","af_123.db")
if s is not None:
    print(s.group())