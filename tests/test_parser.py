import unittest
from parser import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()
    
    
    def test_parse_content_success(self):
        html_content = '''
        <html>
            <body>
                <table>
                    <tbody>
                        <tr><td>1. (141)</td><td>Pibox</td><td>667</td></tr>
                        <tr><td>2. (29)</td><td>Makea Games</td><td>239</td></tr>
                    </tbody>
                </table>
            </body>
        </html>
        '''
        
        result = self.parser.parse_content(html_content)
        
        expected_result = {
            'Pibox': ['1. (141)', '667'],
            'Makea Games': ['2. (29)', '239']
        }
        
        self.assertEqual(result, expected_result)


    def test_parse_content_no_table(self):
        html_content = '<html><body>No table here!</body></html>'
        
        result = self.parser.parse_content(html_content)
        
        self.assertEqual(result, {})