import re
def arithmetic_arranger(problems, answer=False):
#running through problems
  for i in range(len(problems)):
      problem = problems[i]
      #finding the numbers of the ecuation
      numbers = re.findall('[0-9]+', problem)
      #finding the largest number
      length = 0
      for number in numbers:
          if length < len(number):
            length = len(number)
      #changing the str variable to a int variable
      # for i in range(len(numbers)):
      #       numbers[i] = int(numbers[i])
      #finding the sing of the problem
      sing = re.findall('[+-]+', problem)
      # alining the numbers 
      ecuation=f'''{numbers[0]:>{length+2}}
{sing[0]} {numbers[1]:>{length}}\n'''
      # adding the slashes to the ecuation
      slashes = '-' * (length+2)
      ecuation = ecuation + slashes
      print (ecuation)

      
      
  
  #return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])