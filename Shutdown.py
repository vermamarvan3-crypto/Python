def shutdown():
    condition1 = input("Is Your Work Saved?: ")
    if condition1 == "Yes" or condition1 == "yes":
        condition2 = input("Are All Your Apps Closed?: ")
        if condition2 == "Yes" or condition2 == "yes":
            confirm = input("Are You Sure You Want To Shut Down This Computer?: ")
            if confirm == "Yes" or confirm == "yes":
                print("Shutting Down...")
            else:
                print("Shutdown cancelled.")
        else:
            print("Check Everything And Try Again.")
    else:
        print("Check Everything And Try Again.")

shutdown()
