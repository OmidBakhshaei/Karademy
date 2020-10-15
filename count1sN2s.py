def count1sN2s():

    number = int(input("Please enter a number: "))

    numOf1s = 0
    numOf2s = 0
    ones = []
    twos = []
    
    for num in range (1,number+1) :
        realnum = num
        Sum = 0
        while Sum > 9 or Sum == 0 :
            Sum = sum([int(i) for i in str(num)])
            num = Sum
            if Sum == 1 :
                ones.append(realnum)
                numOf1s += 1
            elif Sum == 2 :
                twos.append(realnum)
                numOf2s += 1

    print (f'\nThere are "{numOf1s}" 1s and "{numOf2s}" 2s in the provided range.')

    if numOf1s>numOf2s :
        print (f'So there are more 1s than 2s.\n')
    elif numOf1s<numOf2s :
        print (f'So there are more 2s than 1s.\n')
    else :
        print (f'So there is an even number of 1s and 2s.\n')

    yes_or_no = input(f'If you want to see the numbers that lead to 1s and 2s between 0 and {number} please enter "Yes": ')
    if yes_or_no.lower() in ["yes", "y", ""] :
        print (f"\nThe numbers which lead to a 1 are: {ones} \n\nThe numbers which lead to a 2 are: {twos}")

count1sN2s()
