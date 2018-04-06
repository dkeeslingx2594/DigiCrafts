name = raw_input("What is your name? ")
print "Hello, " + name + "!"

name = raw_input("WHAT IS YOUR NAME? ")
new_string = "HELLO, "+ name + "!"
print new_string.upper()
print "YOUR NAME HAS " + str(len(name)) + " LETTERS IN IT!"

name= raw_input("Give me a name. ")
job= raw_input("Give me a job. ")
job2= raw_input("Give me another job. ")
print "%s is a %s trying to become an %s" % (name, job, job2)
