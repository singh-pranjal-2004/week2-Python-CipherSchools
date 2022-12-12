def divide(a,b):
    try :
        return a/b
    except ZeroDivisionError as err:
        # print("You Cannot Divide a number by Zero")
        print(err)
    except TypeError as err:
        print("Numbers must be int or floats")
    except :
        print("Unexpected error")

divide(10, '2')