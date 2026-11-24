# Match-case statement (switch): An alternative to using many 'elif' statements
#                                                          Execute some code if a value matches a 'case'
#                                                          Benefits: cleaner and syntax is more readable

def is_weekend(day):
    if day in ("Saturday", "Sunday"):
        return True
    elif day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
        return False
    else:
        return False

print(is_weekend("Monday"))