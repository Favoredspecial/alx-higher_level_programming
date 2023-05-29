#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sfd = a / b
    except ZeroDivisionError:
        sfd = None
    finally:
        print("Inside result: {}".format(sfd))
    return sfd
