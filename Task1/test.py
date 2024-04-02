import unittest
import subprocess

class TestProgram(unittest.TestCase):
    def test_1(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='9681\n')
        print(stdout)
        self.assertIn('CORRECT PIN', stdout)
        print("Test 1 passed")

    def test_2(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='4321\n9681\n')
        outs = stdout.split('\n')
        self.assertIn('INCORRECT PIN', outs[0])
        self.assertIn('CORRECT PIN', outs[1])
        print("Test 2 passed")

    def test_3(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='43212\n43\n4321\n9681\n')
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        self.assertIn('INVALID PIN FORMAT', outs[1])
        assert 'INCORRECT PIN' == outs[2]
        self.assertIn('CORRECT PIN', outs[3])        
        print("Test 3 passed")

    def test_4(self):
        inputs = '00000\n78923\n12\n1234\n1234\n9681\n'
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=inputs)
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        self.assertIn('INVALID PIN FORMAT', outs[1])
        self.assertIn('INVALID PIN FORMAT', outs[2])
        assert 'INCORRECT PIN' == outs[3]
        assert 'INCORRECT PIN' == outs[4]
        assert 'CORRECT PIN' == outs[5]
        print("Test 4 passed")

    def test_5(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='43211\n43\n12341\n1234\n5332\n7543\n')
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        self.assertIn('INVALID PIN FORMAT', outs[1])
        self.assertIn('INVALID PIN FORMAT', outs[2])
        assert 'INCORRECT PIN' == outs[3]
        assert 'INCORRECT PIN' == outs[4]
        assert 'INCORRECT PIN' == outs[5]
        self.assertIn('BANK CARD HELD', outs[6])
        print("Test 5 passed")

    def test_6(self):
        process = subprocess.Popen(['python', 'atm.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input='43211\n4783\n12341\n1234\n53329\n7543\n')
        outs = stdout.split('\n')
        self.assertIn('INVALID PIN FORMAT', outs[0])
        assert 'INCORRECT PIN' == outs[1]
        self.assertIn('INVALID PIN FORMAT', outs[2])
        assert 'INCORRECT PIN' == outs[3]
        self.assertIn('INVALID PIN FORMAT', outs[4])
        assert 'INCORRECT PIN' == outs[5]
        self.assertIn('BANK CARD HELD', outs[6])
        print("Test 6 passed")


if __name__ == '__main__':
    unittest.main()
