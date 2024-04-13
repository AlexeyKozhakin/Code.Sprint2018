import subprocess
import unittest
import subprocess
import re
import random

def is_rigth_equestion(expression, user_choice):
    numbers = re.findall(r'\d+', expression)
    return int(numbers[0])+int(numbers[1])==user_choice
    
def is_rigth_question(question, user_choice):
    dic_questions = {'Which element is used as fuel in a nuclear power stations?':'C',
                     'Which country uses the most nuclear power?':'A',
                     'Which country opened the first nuclear power plant in 1954 known as \'Atom Mirny\'?':'B'}
    if question not in dic_questions:
        print(question)
        raise ValueError("Somethin wrong with question\nUser queston not found!")
    else:
        return dic_questions[question] == user_choice
    
class TestProgram(unittest.TestCase):
    def test_1(self):
         i = 0
         while True:
             i+=1
             num_rand=random.randint(0,18)
             let_rand=random.choice(['A','B','C'])
             process = subprocess.Popen(['python', 'atom.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
             stdout, stderr = process.communicate(input=f'{num_rand}\n{let_rand}\n6502\n')
             for out in stdout.split('\n'):
                print(out)
                
             out =  stdout.split('\n')
             
             print(out[0])
             print(out[1])
             print(is_rigth_eq(out[0]))
             if out[-2] == "Access granted":
                print(i)
                break
        # process = subprocess.Popen(['python', 'atom.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # stdout, stderr = process.communicate(input='9681\n\8918\n')
        # print(stdout)                

if __name__ == '__main__':
    unittest.main()