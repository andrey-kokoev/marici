"""Regression checks for the explicitly non-admitting progress artifact."""
import json,unittest
from fractions import Fraction
from hashlib import sha256
from check_sector_theorem_progress import ROOT,BASE,occupation_bounds

class SectorProgressTests(unittest.TestCase):
    def test_readout_bounds_are_exact_and_separated(self):
        lo,hi=occupation_bounds()
        self.assertGreater(lo,Fraction(21,100));self.assertLess(hi,Fraction(22,100))
        self.assertLess(hi-lo,Fraction(1,10**18))
        self.assertLess(lo,hi)
    def test_progress_does_not_claim_admission(self):
        result=json.loads((ROOT/(BASE+'results/sector_theorem_progress.v1.json')).read_text())
        self.assertEqual(result['status'],'partial_conditional_progress')
        self.assertIsNone(result['scientific_outcome']);self.assertFalse(result['physical_admission'])
        self.assertTrue(result['blockers']);self.assertTrue(all(result['checks'].values()))
        self.assertEqual(len(result['cases']),8)
        self.assertEqual({c['source_choice'] for c in result['cases']},{'mismatch_only','optional_cycle_defect'})
    def test_selected_source_k_is_checked_without_admission(self):
        result=json.loads((ROOT/(BASE+'results/selected_source_k.v1.json')).read_text())
        self.assertEqual(result['status'],'pass');self.assertIsNone(result['scientific_outcome'])
        self.assertFalse(result['physical_admission']);self.assertEqual(result['vacuum_energy'],'0')
        self.assertEqual(result['selection'],'optional_cycle_defect')
        self.assertEqual(len(result['selected_cases']),4)
        self.assertTrue(all(v is True for v in result['checks'].values()))
        self.assertTrue(result['remaining_obligations'])
    def test_selected_source_k_pins_are_current(self):
        result=json.loads((ROOT/(BASE+'results/selected_source_k.v1.json')).read_text())
        for path,digest in result['source_hashes'].items():
            with self.subTest(path=path):self.assertEqual(sha256((ROOT/path).read_bytes()).hexdigest(),digest)
    def test_progress_dependencies_are_current(self):
        result=json.loads((ROOT/(BASE+'results/sector_theorem_progress.v1.json')).read_text())
        for path,digest in result['source_hashes'].items():
            with self.subTest(path=path):self.assertEqual(sha256((ROOT/path).read_bytes()).hexdigest(),digest)

if __name__=='__main__':unittest.main()
