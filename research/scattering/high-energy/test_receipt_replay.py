import copy
import unittest
from receipt_replay import assert_receipt_matches


class ReceiptReplayTests(unittest.TestCase):
    def setUp(self):
        self.receipt={'status':'pass','hash':'abc','flag':False,'values':[1.25,{'residual':1e-12}],'nodes':33}

    def test_roundoff_accepted(self):
        changed=copy.deepcopy(self.receipt);changed['values'][0]+=1e-10
        assert_receipt_matches(self.receipt,changed)

    def test_changed_numeric_rejected(self):
        changed=copy.deepcopy(self.receipt);changed['values'][0]+=.01
        with self.assertRaises(AssertionError):assert_receipt_matches(self.receipt,changed)

    def test_nested_residual_rejected(self):
        changed=copy.deepcopy(self.receipt);changed['values'][1]['residual']=1e-5
        with self.assertRaises(AssertionError):assert_receipt_matches(self.receipt,changed)

    def test_disposition_hash_shape_and_nonfinite_rejected(self):
        for key,value in [('flag',True),('hash','xyz'),('nodes',34),('values',[1.25]),('values',[float('nan'),{'residual':1e-12}])]:
            changed=copy.deepcopy(self.receipt);changed[key]=value
            with self.subTest(key=key),self.assertRaises(AssertionError):assert_receipt_matches(self.receipt,changed)


if __name__=='__main__':unittest.main()
