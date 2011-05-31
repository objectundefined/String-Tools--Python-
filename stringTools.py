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
