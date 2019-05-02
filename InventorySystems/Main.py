while True:
    import Inv as i
    cmd = input("Command:")
    cmd = cmd.lower()
    if cmd == "show":
        i.show()
    elif cmd == "fill":
        i.fill()
    elif cmd == "drop":
        item = input("Item to drop?")
        i.drop(item)
    elif cmd == "empty":
        i.empty()
    elif cmd == "test":
        print("BETA: May be buggy!")
        i.test()

