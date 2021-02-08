from subprocess import PIPE, Popen
import unittest

class tests(unittest.TestCase):
    
    def test_2(self):
        server = Popen("./server", stdout=PIPE)
        client = Popen("./client", stdout=PIPE)
        realServerOutput = server.stdout.read()
        expectedServerOutput = b'Client : Hello from client\nHello message sent.\n'

        self.assertEqual(expectedServerOutput, realServerOutput)

    def test_3(self):
        print("hello world")

    def test_4(self):
        exit(0)
    
    def test_5(self):
        exit(1)
    

unittest.main()
