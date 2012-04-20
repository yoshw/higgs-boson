def promptuser(room):
    
    while True:
        x = raw_input(prompt).lower()

        if x == "inv":
            inventory()
        elif x == "exit":
            print "\nGoodbye!\n"
            exit(0)
        elif x == "look":
            print "You can't just look, you have to look at something!\n"
        elif x == "talk":
            print "You can't just talk, you have to talk to someone!\n"
        elif x == "open" or x == "use" or x == "take":
            print "You can't just %s, you have to %s an object!\n" % (x, x)
        elif "look" in x:
            mode = 0
            action = x
            return mode, action
        elif "talk" in x:
            mode = 1
            action = x
            return mode, action
        elif "open" in x:
            mode = 2
            action = x
            return mode, action
        elif "use" in x:
            mode = 3
            action = x
            return mode, action
        elif "take" in x:
            mode = 4
            action = x
            return mode, action
        else:
            print "I'm sorry, I don't understand.\n"
