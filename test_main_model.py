"""Unittests for model.py"""
import unittest
from unittest import mock
from io import StringIO
from model import main



class TestMainModel(unittest.TestCase):
    """Unittest class"""
    @mock.patch(
        "sys.argv", ["model.py", "./images", "./out/re.fuck", "./ft_resnet_10e.pt"]
    )
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_valid_input(
        self,
        mock_stdout,
    ):
        """Tests correct model IO"""
        main()
        self.assertEqual(mock_stdout.getvalue(), "")

    @mock.patch(
        "sys.argv", ["model.py", "./t/resh", "./out/re.fuck", "./ft_resnet_10e.pt"]
    )
    def test_invalid_input_file(self):
        """Tests invalid input processing"""
        with self.assertRaises(AssertionError):
            main()

    @mock.patch(
        "sys.argv", ["model.py", "./images", "./out/re.fuck", "./ft_resnet_10e.pttx"]
    )
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_invalid_weights_file(self, mock_stdout):
        """Tests invalid weights path processing"""
        main()
        self.assertEqual(mock_stdout.getvalue(), "Incorrect weights path\n")

    @mock.patch(
        "sys.argv",
        ["model.py", "./images", "./o/u/t/r/e/./f/u/c/k", "./ft_resnet_10e.pt"],
    )
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_invalid_output_file(self, mock_stdout):
        """Tests invalid output processing"""
        main()
        self.assertEqual(mock_stdout.getvalue(), "Incorrect output path\n")


if __name__ == "__main__":
    unittest.main()
