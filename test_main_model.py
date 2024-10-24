import unittest
from model import main
from unittest import mock
from io import StringIO


class TestMainModel(unittest.TestCase):    
    
    @mock.patch('sys.argv', ['model.py', './tresh', './out/re.fuck', './ft_resnet_10e.pt'])
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout, ):
        main()
        self.assertEqual(mock_stdout.getvalue(), '')
        
        
    @mock.patch('sys.argv', ['model.py', './t/resh', './out/re.fuck', './ft_resnet_10e.pt'])
    def test_invalid_input_file(self):
        with self.assertRaises(AssertionError):
            main()
            
            
    @mock.patch('sys.argv', ['model.py', './tresh', './out/re.fuck', './ft_resnet_10e.pttx'])
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_invalid_weights_file(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), "Incorrect weights path\n")
        
        
    @mock.patch('sys.argv', ['model.py', './tresh', './o/u/t/r/e/./f/u/c/k', './ft_resnet_10e.pt'])
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_invalid_output_file(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue(), "Incorrect output path\n")

        
if __name__ == "__main__":
    unittest.main()
