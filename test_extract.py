import unittest
from unittest.mock import patch, MagicMock
from utils.extract import fetch_product_data  # Pastikan path ini sesuai dengan struktur proyekmu

class TestProductScraping(unittest.TestCase):

    @patch('utils.extract.requests.get')
    def test_fetch_product_data_success(self, mock_get):
        # Mock HTML content sesuai struktur asli di fetch_product_data
        mock_html_content = '''
<html>
  <body>
    <div class="collection-card">
      <h3 class="product-title">Fashion T-Shirt</h3>
      <div class="price-container">$120.00</div>
      <p>Rating: 4.7</p>
      <p>Colors: 4 Colors</p>
      <p>Size: XL</p>
      <p>Gender: Unisex</p>
    </div>
  </body>
</html>
'''
        # Mock response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = mock_html_content
        mock_get.return_value = mock_response

        # Call the function to fetch product data
        extracted_data = fetch_product_data(1)

        # Debugging output (opsional)
        print(extracted_data)

        # Assert that the length of the extracted data is correct (1 product found)
        self.assertEqual(len(extracted_data), 1)
        self.assertEqual(extracted_data[0]['Title'], 'Fashion T-Shirt')
        self.assertEqual(extracted_data[0]['Price'], '$120.00')
        self.assertEqual(extracted_data[0]['Rating'], 'Rating: 4.7')
        self.assertEqual(extracted_data[0]['Colors'], 'Colors: 4 Colors')
        self.assertEqual(extracted_data[0]['Size'], 'Size: XL')
        self.assertEqual(extracted_data[0]['Gender'], 'Gender: Unisex')

    @patch('utils.extract.requests.get')
    def test_fetch_product_data_empty_page(self, mock_get):
        # Mock empty HTML response
        mock_empty_response = MagicMock()
        mock_empty_response.status_code = 200
        mock_empty_response.text = '<html><body>No items available!</body></html>'
        mock_get.return_value = mock_empty_response

        # Call the function to fetch product data
        result = fetch_product_data(1)

        # Assert that no data was extracted
        self.assertEqual(len(result), 0)

    @patch('utils.extract.requests.get')
    def test_fetch_product_data_network_error(self, mock_get):
        # Simulate a network error
        mock_get.side_effect = Exception("Connection error occurred")

        # Ensure the function raises an exception on network error
        with self.assertRaises(Exception):
            fetch_product_data(1)

if __name__ == '__main__':
    unittest.main()
