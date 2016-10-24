import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')


mail.login('xyz@gmail.com', 'xyzxyzxyz')

print mail.list()
mail.select("INBOX")

status, response = mail.status('INBOX', '(UNSEEN)')



unread_msg_nums = response[0].split()

# Print the count of all unread messages
print len(unread_msg_nums)

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
print ids

id_list = ids.split()


for i in range(0,len(id_list)) :
	x = id_list[i]
	result, data = mail.fetch(x, "(RFC822)")
	raw_email = data[0][1]
	print raw_email
	print "<<<<<<<<<<<<<<*****************>>>>>>>>>>>>>>>>>>>>"
	email_message = email.message_from_string(raw_email)

	print email_message
	print "<<<<<<<<<<<<<<----------------->>>>>>>>>>>>>>>>>>>>"
