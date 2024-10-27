"""Unittests for decoder.py"""

import unittest
from unittest import mock
from io import StringIO
from decoder import main


class TestDecoder(unittest.TestCase):
    """Unittest class"""

    @mock.patch("sys.argv", ["decoder.py", "../out/test.pkl", "../out/test.json"])
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_valid_input(
        self,
        mock_stdout,
    ):
        """Tests correct model IO"""
        main()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Conversion complete: ../out/test.pkl -> ../out/test.json\n",
        )

    @mock.patch("sys.argv", ["decoder.py"])
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_little_argvs(self, mock_stdout):
        """Tests case with insufficient number of arguments"""
        main()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Usage: python convert_pickle_to_json.py <input_pickle_file> <output_json_file>\n",
        )

    @mock.patch("sys.argv", ["decoder.py", "../out/test.pikl", "../out/test.json"])
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input(self, mock_stdout):
        """Tests invalid input path processing"""
        main()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Error: The input file must have a .pkl extension.\n",
        )

    @mock.patch(
        "sys.argv",
        ["decoder.py", "../out/test.pkl", "../out/test.jason"],
    )
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_invalid_output_file(self, mock_stdout):
        """Tests invalid output processing"""
        main()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Error: The output file must have a .json extension.\n",
        )


if __name__ == "__main__":
    unittest.main()
