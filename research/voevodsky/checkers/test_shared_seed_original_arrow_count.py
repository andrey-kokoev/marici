"""Independent endpoint-support controls using the unchanged source convention."""
import copy,json,unittest
from fractions import Fraction as F
from hashlib import sha256
from check_shared_seed_original_arrow_count import certify,OWNER,ROOT,OUT

class OriginalCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.records=json.loads((OWNER/'results/pair-dense-7128-arrows.json').read_text())
    def test_complete_support_and_closed_cover(self):
        result=certify(self.records)
        self.assertEqual(result['primitive_arrow_count'],7128)
        self.assertEqual(result['body_partition'],{'body_A':1836,'body_B':1836,'between_bodies':3456})
        self.assertEqual(result['positive_three_step_cycles'],5184)
        self.assertEqual(result['minimum_single_arrow_trace_loss'],'1/129600')
    def test_primitive_deletion_rejected(self):
        with self.assertRaises(AssertionError):certify(self.records[1:])
    def test_duplicate_endpoints_rejected(self):
        with self.assertRaises(AssertionError):certify(self.records+[self.records[0]])
    def test_wrong_stage_rejected(self):
        r=copy.deepcopy(self.records);r[0]['target'][0]='aligned'
        with self.assertRaises(AssertionError):certify(r)
    def test_zero_is_not_counted_as_an_arrow(self):
        r=copy.deepcopy(self.records);r[0]['real']='0';r[0]['imag_sqrt3']='0'
        with self.assertRaises(AssertionError):certify(r)
    def test_coefficients_not_just_counts_verified(self):
        r=copy.deepcopy(self.records);r[0]['real']=str(2*F(r[0]['real']));r[0]['imag_sqrt3']=str(2*F(r[0]['imag_sqrt3']))
        with self.assertRaises(AssertionError):certify(r)
    def test_receipt_provenance_and_convention(self):
        result=json.loads(OUT.read_text());self.assertTrue(result['verification_passed'])
        self.assertFalse(result['counting_convention_changed']);self.assertFalse(result['compiler_instruction_count_included'])
        self.assertFalse(result['original_files_rewritten'])
        for p,h in result['source_hashes'].items():
            with self.subTest(path=p):self.assertEqual(sha256((ROOT/p).read_bytes()).hexdigest(),h)

if __name__=='__main__':unittest.main()
