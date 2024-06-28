def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = True
    if email[0].isalpha() == False:
        result = False
    elif len(email) <= 5 and len(email) >= 30:
        result = False
    elif '@' not in email:
        result = False
    elif '.' not in email[email.index('@'):]:
        result = False
        
    
    print (result)
        
        

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
