import unittest,copy,json
from sqlite_affinity_witness import run
DEMO={'values': ['3', '003', '3.0e+5']}
class DomainTests(unittest.TestCase):
 def test_unary_plus_removes_affinity(self):
  x=run(DEMO);self.assertTrue(x['TEXT'][0]['column_equals_three']);self.assertFalse(x['TEXT'][0]['expression_equals_three'])
 def test_numeric_storage_changes(self):
  x=run(DEMO);self.assertEqual(x['NUMERIC'][1]['value'],3);self.assertEqual(x['NUMERIC'][2]['value'],300000);self.assertEqual(x['TEXT'][2]['value'],'3.0e+5')
 def test_parameterized_values(self):
  x=run({'values':["');drop table TEXT;--"]});self.assertEqual(len(x['TEXT']),1)
