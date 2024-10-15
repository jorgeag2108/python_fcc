def arithmetic_arranger(problems, show_answers=False):

    first_numbers=[]
    second_numbers=[]
    operators=[]
    results=[]

    first_line=[]
    second_line=[]
    lines=[]
    last_line=[]
    

    first_num_lengths=[]
    second_num_lengths=[]
    results_lengths=[]
            
    all_good=True # if this gets to the end unchanged then everything is fine
    theres_a_letter=0
    result=0
    
    if len(problems)>5:
        string_to_return='Error: Too many problems.'
        all_good=False 
        

    for problem in problems: #find position of spaces
        count=0
        spaces_index=[]
        operator=0 #this will be useful to determine if there's more than one operator
        
        for char in problem:
            if char.isalpha():
                string_to_return='Error: Numbers must only contain digits.'
                all_good=False
                theres_a_letter=1
        
            elif char==' ':
                spaces_index.append(count)
            elif not char.isalnum():
                if operator != 0:
                    raise ValueError('There is more than one operator!')
                operator=char 

            count+=1
        
        # knowing where the spaces are we can find all the numbers 
        first_number=problem[0:spaces_index[0]:1]
        second_number=problem[spaces_index[-1]+1::1]

        # we need to find the result of the operation and check if it's + or -
        
        if theres_a_letter==0:
            int_first_number=int(first_number)
            int_second_number=int(second_number)
        else:
            int_first_number=0
            int_second_number=0 #this way the code keeps working even if theres an invalid string

        if operator != '+':
            if operator != '-':
                string_to_return="Error: Operator must be '+' or '-'."
                all_good=False 
            else:
                result=int_first_number-int_second_number
        else:
            result=int_first_number+int_second_number
        result=str(result) #we need to transform the result to a string
        
        
        

        first_numbers.append(first_number)
        second_numbers.append(second_number)
        operators.append(operator)
        results.append(result)



        
        
        

    # find lengths of numbers, that'll be useful continuing forward
    for number in first_numbers: 
        first_num_lengths.append(len(number))
    for number in second_numbers: 
        second_num_lengths.append(len(number))
    for number in results:
        results_lengths.append(len(number))
    
    for i in range(len(first_num_lengths)):
        number_length=max(first_num_lengths[i], second_num_lengths[i])
        if number_length>4:
            string_to_return='Error: Numbers cannot be more than four digits.'
            all_good=False 

        line_length=number_length+2 

        length_dif_upper=abs(number_length-first_num_lengths[i])
        length_dif_lower=abs(number_length-second_num_lengths[i])
        length_dif_result=abs(line_length-results_lengths[i])
        
        second_line.append(operators[i]+' ')
        if number_length>first_num_lengths[i]:
            first_line.append(abs(length_dif_upper)*' ')
        else:
            second_line.append(abs(length_dif_lower)*' ')
        
        first_line.append('  '+first_numbers[i]+'    ')
        second_line.append(second_numbers[i]+'    ')
        line=('-'*(line_length)+'    ')
        lines.append(line)
        last_line.append(' '*length_dif_result+results[i]+'    ')
        

        upper_line=''.join(first_line)
        upper_line=upper_line[:-4]
        lower_line=''.join(second_line)
        lower_line=lower_line[:-4]
        bottom_line=''.join(last_line)
        bottom_line=bottom_line[:-4]

        division=''.join(lines)
        division=division[:-4]


    if all_good==True:
        if show_answers==True:
            string_to_return=upper_line+'\n'+lower_line+'\n'+division+'\n'+bottom_line
        else: 
            string_to_return=upper_line+'\n'+lower_line+'\n'+division

    
    

    return string_to_return


print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
