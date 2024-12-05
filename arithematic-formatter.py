def arithmetic_arranger(problems, show_answers=False):
    answers=[]
    first=[]
    second=[]
    third=[]
    answer=0
    if len(problems)>5:
        return 'Error: Too many problems.'
    for problem in problems:
        if '*' in problem or '/' in problem:
            return "Error: Operator must be '+' or '-'."
        if '+' in problem:
            numbers=problem.split('+')
            numbers[0]=numbers[0].strip(' ')
            numbers[1]=numbers[1].strip(' ')
            if not numbers[0].isdigit() or not numbers[1].isdigit():
                return 'Error: Numbers must only contain digits.'
            l1=len(numbers[0])
            l2=len(numbers[1])
            if l1>4 or l2>4:
                return 'Error: Numbers cannot be more than four digits.'
            answer=int(numbers[0])+int(numbers[1])
            m=max(l1,l2)
            n1=m-l1
            n2=m-l2
            numbers[0]=' '*(n1+2)+numbers[0]
            numbers[1]='+'+' '*(n2+1)+numbers[1]
            first.append(numbers[0])
            second.append(numbers[1])
            third.append('-'*len(numbers[1]))
            answers.append(' '*(len(numbers[1])-len(str(answer)))+str(answer))
        else:
            numbers=problem.split('-')
            numbers[0]=numbers[0].strip(' ')
            numbers[1]=numbers[1].strip(' ')
            if not numbers[0].isdigit() or not numbers[1].isdigit():
                return 'Error: Numbers must only contain digits.'
            l1=len(numbers[0])
            l2=len(numbers[1])
            if l1>4 or l2>4:
                return 'Error: Numbers cannot be more than four digits.'
            answer=int(numbers[0])-int(numbers[1])
            m=max(l1,l2)
            n1=m-l1
            n2=m-l2
            numbers[0]=' '*(n1+2)+numbers[0]
            numbers[1]='-'+' '*(n2+1)+numbers[1]
            first.append(numbers[0])
            second.append(numbers[1])
            third.append('-'*len(numbers[1]))
            answers.append(' '*(len(numbers[1])-len(str(answer)))+str(answer))
    if show_answers == True:
        return '    '.join(first)+'\n'+'    '.join(second)+'\n'+'    '.join(third)+'\n'+'    '.join(answers)
    return '    '.join(first)+'\n'+'    '.join(second)+'\n'+'    '.join(third)

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
