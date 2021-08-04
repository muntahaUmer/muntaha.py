def hamming_distance(myusername, mytwitter_handle):
 distance = 0
 L = len(myusername)
 for i in range(L):
 if myusername[i] != mytwitter_handle[i]:
 distance += 1
return distance
def personal_details():
 name, email,slackusername,biostack,twitter_handle, = "muntaha","muntaha.bsbi589@iiu.pk","@muntaha","drug developement anf genomics","@muntaha111"
 example_dist = hamming_distance("@muntaha", "@muntaha111")
 print("name: {}\nemail: {}\nslack_username: {}\nbiostack: {}\ntwitter_handle:{}\nhamming_distance:{}".format(name, email, slackusername,biostack,twitter_handle,example_dist))
personal_details()
