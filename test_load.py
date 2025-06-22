import unittest
import pandas as pd
from unittest.mock import patch
from utils.load import save_to_csv

class SaveDataTests(unittest.TestCase):

    def test_successful_csv_save(self):
        data = {
            'Product Name': ['T-shirt Cool', 'Casual Shirt'],
            'Price': [1500000.0, 2500000.0],
            'Rating': [4.8, 4.2],
            'Colors': [5, 3],
            'Size': ['M', 'L'],
            'Gender': ['Unisex', 'Male'],
            'Timestamp': ['2025-05-16 23:10:28', '2025-05-16 23:10:28']
        }
        df = pd.DataFrame(data)

        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            save_to_csv(df, "test_output.csv")  
            mock_to_csv.assert_called_once_with("test_output.csv", index=False)

    @patch('pandas.DataFrame.to_csv')
    def test_save_empty_csv(self, mock_to_csv):
        empty_df = pd.DataFrame(columns=['Product Name', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'Timestamp'])
        
        save_to_csv(empty_df, "empty_output.csv")
        mock_to_csv.assert_called_once_with("empty_output.csv", index=False)

if __name__ == '__main__':
    unittest.main()