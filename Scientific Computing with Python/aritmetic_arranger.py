import re

def arithmetic_arranger(problems, answer=False):
  if amount_validation(problems) is not None:
    return amount_validation(problems)
  else:
    #running through problems and concatenating all of them into a single variable problem
    problem = ''
    for i in range(len(problems)):
      problem = problem + ' ' + problems[i]
    
    digit_validation(problem)
    #finding the numbers of all the ecuations
    numbers = re.findall('[0-9]+', problem)
    # taking the first term numbers from all the ecuations into a list
    term1 = [numbers[i] for i in range(len(numbers)) if i%2 == 0]
    # taking the second term numbers from all the ecuations into a list
    term2 = [numbers[i] for i in range(len(numbers)) if i%2 != 0]
    # finding the sings for all the ecuations and saving it in a list
    sing = re.findall('[+-]+', problem)
    if sing_validation(sing, problems) is not None:
      return sing_validation(sing, problems)
    else:
      # finding the max lenght for all the ecuations and saving it in a list
      length = []
      for i in range(len(problems)):
        if len(term1[i]) <= len(term2[i]):
          length.append(len(term2[i]))
        else:
          length.append(len(term1[i]))
      # creating the string for each line of the final return
      t1 = ''
      t2 = ''
      slashes = ''
      for i in range(len(problems)):
        t1 = t1 + f'{term1[i]:>{length[i]+2}}' + '   '
        t2 = t2 + f'{sing[i]} {term2[i]:>{length[i]}}' + '   '
        slashes = slashes + ('-' * (length[i]+2)) + '   '
      
      
      if answer == True:
        resuls = ''
        # runing through all the ecuations 
        for i in range(len(problems)):
          # cheking if it is an adittion of a substraction
          if sing[i] == '+':
            resul = int(term1[i]) + int(term2[i])
          else:
            resul = int(term1[i]) - int(term2[i])
          #creating the string line for the results
          resuls = resuls + f'{resul:>{length[i]+2}}' + '   '
        
        return (f'{t1}\n{t2}\n{slashes}\n{resuls}')
      else:
        return (f'{t1}\n{t2}\n{slashes}')
    
def amount_validation(problems):
  if len(problems) > 5:
    return ('Error: Too many problems.')

def sing_validation(sings, problems):
  if len(sings) != len(problems):
    return ('Error: Operator must be "+" or "-".')

def digit_validation(problem):
  numbers = re.findall('[^0-9+-]', problem)
  if numbers != []:
    return('Error: Numbers must only contain digits.')
  
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))