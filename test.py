str_1 = "Hi, my name is Kadamb Kaluskar . I live in India."

str_2 = "Hi, my name is {{first_name}} {{last_name}} . I live in {{country_name}}."



arr_1 = str_1.split(" ")
arr_2 = str_2.split(" ")



for i in range(0,len(arr_1)) : 
	if arr_1[i] != arr_2[i] :
		x = arr_2[i].strip('{{')
		x = x.strip('}}')
		print x+" : " + arr_1[i]
