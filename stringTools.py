import string

def caesar(shift, inp):
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    shifted = []
    for x in inp:
        if x.strip() and x in letters_lower:
            shifted.append(letters_lower[(letters_lower.index(x) + shift) % 26])
        elif x.strip() and x in letters_upper:
            shifted.append(letters_upper[(letters_upper.index(x) + shift) % 26])
        else:
            shifted.append(x)
    return ''.join(shifted)

def fancyConcat(string='',length=None,word=False,elip=False):
  length = length or len(string)
  if elip:
      length = length - 3
  concat = len(string) > length
  newstr = string[:length]
  if word and concat:
      if concat and string[length] != ' ':
          lastspace = newstr.rfind(' ')
          newstr = string[:lastspace] if lastspace > -1 else string
  if elip and concat:
      newstr = newstr + '...'
  return newstr

def stripTags(string=''):
  import re
  p = re.compile(r'<.*?>')
  return p.sub('', string)

def convertToUnicode(str):
  if type(str) is unicode:
    return str
  try:
    return str.decode('ascii')
  except UnicodeDecodeError, err:
    pass
  try:
    return str.decode('utf8')
  except UnicodeDecodeError, err:
    pass
  try:
    return str.decode('latin1')
  except UnicodeDecodeError, err:
    pass  

def convertToUTF8(str):
  if type(str) is unicode:
    return str.encode('utf8')
  return convertToUnicode(str).encode('utf8')
