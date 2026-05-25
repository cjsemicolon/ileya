
def collect_even_elements(numbers):

    even_elements = [];

    even_index = 0;

    for element in numbers:

        if element % 2 == 0:

            even_elements.append(element);
            even_index+=1;

    return even_elements;



def collect_odd_elements(numbers):

    odd_elements = [];

    odd_index = 0;

    for element in numbers:

        if element % 2 != 0:

            odd_elements.append(element)
            odd_index+=1;    

    return odd_elements;



def split_array(numbers):

    even_elements =   collect_even_elements(numbers); 

    odd_elements =   collect_odd_elements(numbers);    

    split_array = [even_elements, odd_elements];
    
    return split_array;




