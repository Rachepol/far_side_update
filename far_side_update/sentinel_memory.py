# try writing to a file
def memory_recall(url_inp):
    mem_f = open("last_update.txt", "r")

    f_test = mem_f.read()
    url_data = url_inp

    if len(url_data) == 0:
        print("No value")
    elif f_test == url_data:
        print("Same value")
        return False
    else:
        print("Mismatch")
        mem_f = open("last_update.txt", "w+")
        mem_f.write(url_data)
        return True

    mem_update = open("last_update.txt", "r")
    new_val = mem_update.read()
    print(new_val)
#mem_f.close()

#if len(f_test) == 0:
    #print("No text", len(inp))
#    mem_f.write("Hey! Is anybody home?")
#else:
    #print("text", len(inp))
#    pass
#result = mem_f.read()
