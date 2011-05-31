FancyConcat Use:
	
	str = 'My Name Is Earl'
	FancyConcat(string=str,length=9,word=True,elip=True)
	// returns 'My Name...'	
	// returns only full words and a maximum of 9 characters (including the elipses)

StripTags Use:

	str = stripTags('<span>hi</span>')
	// returns 'hi'

ConvertToUnicode:

	converts any string or buffer data into a unicode object.

ConvertToUTF8:
	
	converts any string or buffer data into unicode, then utf8 
