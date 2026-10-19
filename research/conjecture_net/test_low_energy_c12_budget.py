"""The remaining C12 review is not an implicitly renewed two-unit attempt."""
import copy
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('c12_budget_adapter',ROOT/'research/conjecture_net/plan_low_energy.py')
adapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(adapter)
# Pin the effort-unit-1 snapshot, even after the live planner advances.
adapter.CONTRACT='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v5.json'
adapter.PATHS={'low-energy':adapter.CONTRACT}
adapter.ESTIMATES='research/conjecture_net/contracts/low-energy-test-planning.v3.json'
adapter.CARDS='research/conjecture_net/contracts/low-energy-action-cards.v3.json'
KEY='low-energy:pentachoron-bright-threshold-regularity'


class C12BudgetTests(unittest.TestCase):
    def setUp(self):
        self.model=adapter.planning.load(adapter.ESTIMATES)
        self.cards=adapter.planning.load(adapter.CARDS)
        self.source=adapter.planning.load(adapter.CONTRACT)

    def test_one_remaining_review_is_recommended(self):
        report=adapter.run(self.model,self.cards,self.source)
        self.assertEqual(report['recommendation'],KEY)
        self.assertEqual(report['frontier'][0]['assistant_effort_units'],1)

    def test_cannot_silently_restore_two_card_units(self):
        bad=copy.deepcopy(self.cards)
        next(c for c in bad['cards'] if c['id']==KEY)['protocol_accounting']['remaining_effort_units']=2
        with self.assertRaises(AssertionError):adapter.run(self.model,bad,self.source)

    def test_forecast_cost_must_match_remaining_budget(self):
        bad=copy.deepcopy(self.model)
        next(r for r in bad['conjectures'] if r['id']==KEY)['test_cost']['assistant_effort_units']=2
        with self.assertRaisesRegex(AssertionError,'remaining C12 effort'):
            adapter.run(bad,self.cards,self.source)


if __name__=='__main__':unittest.main()
