import re
def arithmetic_arranger(problems, answer=False):
  
  for i in range(len(problems)):
        problem = problems[i]
        numbers = re.findall('[0-9]+', problem)
        length = 0
        for number in numbers:
          if length < len(number):
            length = len(number)
        
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        sing = re.findall('[+-]+', problem)
        
        print(numbers, sing, length)
      
      
  
  #return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])