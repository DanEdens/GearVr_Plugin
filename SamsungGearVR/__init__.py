    # add variables with string that you want to be able to have translated
    # using the language editor in here
    # you want to add any variables that can be access from anywhere inside of
    # your plugin here
    # you will want to add any startup parameters and also run any startup code
    # here
    # this gets called when eg is being closed and you can run code when that
    # happens
    # this gets called as well when EG closes but it also gets called when a
    # plugin gets disabled. This is where you will do things like close any
    # open sockets
    # You will replace the code in this method if you want to make a plugin
    # configuration dialog.
    # The next 2 are pretty self explanatory
    # This gets called when a plugin gets deleted from the tree. so here if
    # you use eg.PersistantData to store any data. that data needs to be
    # deleted when the plugin gets removed. this is where that gets done.
