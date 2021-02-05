
stopWords=["的", "了", "与", "和", "呢", "乃", "或", "着", "而", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def comnCharNum(str_a, str_b):
	times=0
	uniqChars=set()
	for c in str_a:
		if c in str_b and c not in stopWords:
			uniqChars.add(c)
	return len(uniqChars)

