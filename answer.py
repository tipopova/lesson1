def get_answer(q):
	answer = {"Hello" : "And you", "how are you?": "Nice", "Bye" : "See you"}
 	if q in answer:return(answer[q])
 c = input ("Story")
 g = get_answer(c)
 print (g)
