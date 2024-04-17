import subprocess
import unittest
import re
import random
import time
 
def is_rigth_equestion(expression, user_choice):
    numbers = re.findall(r'\d+', expression)
    nums=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if numbers[0] not in nums or numbers[1] not in nums:
        raise ValueError('Something is wrong with the example\n There is an extra number!')
    else:
        return int(numbers[0])+int(numbers[1])==user_choice
    
def is_rigth_question(question, user_choice):
    dic_questions = {'Which element is used as fuel in a nuclear power stations?':'C',
                     'Which country uses the most nuclear power?':'A',
                     "Which country opened the first nuclear power plant in 1954 known as \'Atom Mirny\'?":'B'}
    
    if question not in dic_questions.keys():
        print(question)
        raise ValueError("Somethin wrong with question\nUser queston not found!")
    else:
        return dic_questions[question] == user_choice


class RandomError(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

class AccessError(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

class TestProgram(unittest.TestCase):
    def test_1(self):
        i = 0
        k = 0
        n = 0
        Okey = 0
        num_yes=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        qu_yes=['A', 'B', 'C']

        while True:
            
            Test = False
            num_rand = random.randint(0,18)
            let_rand = random.choice(qu_yes)
            process = subprocess.Popen(['python', 'atom.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(input=f'{num_rand}\n{let_rand}\n6502\n')
                
            out =  stdout.split('\n')

            #Checking examples and questions
            if out[0][0] in num_yes:
                num_yes.remove(out[0][0])
            elif out[0][2] in num_yes:
                num_yes.remove((out[0][2]))
            if len(num_yes)==0:
                n=1
            if is_rigth_equestion(out[0],num_rand) and is_rigth_question(out[1],let_rand):
                Test=True 

            #We guessed the correct values
            if Test and (let_rand in qu_yes) and  Okey==0: 
                    qu_yes.remove(let_rand)
                    k+=1

                    if out[-2] != 'Access granted':
                        raise AccessError('Access is denied when entering correct data')
            if k>=3:
                qu_yes.append('C')
                Okey=1

            #Stop condition    
            if Okey==1 and n==1:
                break
            if i>400:
                raise RandomError('The program has been running for too long')

            print(f'Test 1.{i} passed')
            i+=1

        print('All tests 1 passed')

    def test_2(self):
        process = subprocess.Popen(['python', 'atom.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=f'9\nC\n6501\n')
        
        out=stdout.split('\n')

        if out[-2] == 'Access denied':
            print('Test 2.0 passed')

if __name__ == '__main__':  
    unittest.main()