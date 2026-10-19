import copy
import unittest
import check_hodge_refutation_direction as s


class DirectionTests(unittest.TestCase):
    def setUp(self):self.c=s.load(s.CONTRACT);self.p=s.load(s.POLICY)
    def check(self):return s.validate_direction(self.c,self.p)

    def test_complete_refutation_only_inventory(self):
        r=self.check();self.assertEqual(r['dismissed_construction_count'],52)
        self.assertEqual(r['active_refutation_count'],4)
        self.assertFalse(r['administrative_change_is_mathematical_evidence'])

    def test_confirmation_permission_rejected(self):
        self.p['confirmation_research_allowed']=True
        with self.assertRaisesRegex(ValueError,'confirmation research'):self.check()

    def test_dismissed_search_not_in_frontier(self):
        self.c['frontier']['entry_nodes'].append('algebraic-witness-search')
        with self.assertRaisesRegex(ValueError,'frontier'):self.check()

    def test_recommending_prime_screen_rejected(self):
        self.c['frontier']['recommended_start']='scalar-37-full-screen'
        with self.assertRaisesRegex(ValueError,'frontier'):self.check()

    def test_cannot_hide_unclassified_new_conjecture(self):
        n=copy.deepcopy(self.c['conjectures'][-1]);n['id']='unclassified-confirmation-task';self.c['conjectures'].append(n)
        with self.assertRaisesRegex(ValueError,'node coverage'):self.check()

    def test_omitted_dismissal_rejected(self):
        self.p['dismissed_construction_nodes'].pop()
        with self.assertRaisesRegex(ValueError,'dismissal inventory'):self.check()

    def test_reactivated_dismissed_node_rejected(self):
        next(n for n in self.c['conjectures'] if n['id']=='scalar-37-full-screen')['active_research']=True
        with self.assertRaisesRegex(ValueError,'reactivated'):self.check()

    def test_dismissal_cannot_falsify_historical_theorem(self):
        next(n for n in self.c['conjectures'] if n['id']=='scalar-37-full-screen')['verdict']='rejected'
        with self.assertRaisesRegex(ValueError,'not mathematical rejection'):self.check()

    def test_positive_algebraic_controls_cannot_be_removed(self):
        self.p['positive_controls_required']=False
        with self.assertRaisesRegex(ValueError,'falsifiers removed'):self.check()

    def test_no_claim_of_hodge_refutation_from_registration(self):
        n=next(n for n in self.c['conjectures'] if n['id']==s.NEW[0]);n['status']='resolved';n['verdict']='constructed'
        with self.assertRaisesRegex(ValueError,'changed or promoted'):self.check()

    def test_cannot_retarget_fixed_alpha(self):
        self.c['scope']['candidate_p']=4
        with self.assertRaisesRegex(ValueError,'fixed target substituted'):self.check()

    def test_cannot_substitute_operator_conjecture(self):
        self.c['research_hypothesis']['statement']='The fixed alpha is algebraic.'
        with self.assertRaisesRegex(ValueError,'operator conjecture'):self.check()

    def test_universal_cycle_gap_cannot_be_replaced_by_library_gap(self):
        self.p['first_unresolved_proof_obligation']='algebraic-witness-search'
        with self.assertRaisesRegex(ValueError,'gap displaced'):self.check()

    def test_divisor_only_claim_cannot_replace_all_cycles(self):
        next(n for n in self.c['conjectures'] if n['id']=='all-algebraic-cycles-annihilation')['statement']='Prove vanishing on tested divisor products.'
        with self.assertRaisesRegex(ValueError,'universal refutation gate weakened'):self.check()

    def test_both_new_hypotheses_have_real_falsifiers(self):
        for identifier in s.NEW:
            n=next(n for n in self.c['conjectures'] if n['id']==identifier)
            self.assertEqual(n['status'],'open');self.assertEqual(n['evidence'],[])
            self.assertTrue(n['falsifier']);self.assertEqual(n['aim'],'refute_rational_Hodge')

    def test_inventory_does_not_claim_all_possible_conjectures(self):
        self.assertFalse(self.check()['inventory_exhausts_possible_conjectures'])


if __name__=='__main__':unittest.main()
