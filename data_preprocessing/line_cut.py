import nltk

def sentence_split(str_centence):
	list_ret = list()
	for s_str in str_centence.split('。'):
		if '?' in s_str:
			list_ret.extend(s_str.split('？'))
		elif '!' in s_str:
			list_ret.extend(s_str.split('！'))
		else:
			list_ret.append(s_str)
	return list_ret
