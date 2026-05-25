def check_if_array_is_a_palindrome(numbers):

    begining = 0;
    end = len(numbers) - 1;

    while begining < end:

        if numbers[begining] != numbers[end]: 
            return False;

    begining+=1;
    end-=1;


    return True;



