"""Negative controls for integrity versus scientific outcome separation."""
import copy,json,tempfile,unittest
from pathlib import Path
from check_retained_reaggregation_net import ROOT,CONTRACT,validate,NetError

class ReaggregationNetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.contract=json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    def reject(self,mutate):
        c=copy.deepcopy(self.contract);mutate(c)
        with self.assertRaises(NetError):validate(ROOT,c)
    def test_live_bootstrap(self):
        r=validate(ROOT,self.contract)
        self.assertTrue(r['validation_passed']);self.assertIsNone(r['scientific_outcome'])
        self.assertEqual(r['ready_actions'],['prove/freeze-common-interface'])
        self.assertFalse(r['physical_admission'])
    def test_no_automatic_target_proof(self):
        self.reject(lambda c:c['conjectures'][6].update(outcome='++'))
    def test_no_automatic_refutation(self):
        self.reject(lambda c:c['conjectures'][1].update(outcome='-+'))
    def test_attempt_not_component_promotion(self):
        self.reject(lambda c:c['conjectures'][0]['attempts'].append({'intent':'prove','outcome':'++'}))
    def test_unknown_dependency(self):
        self.reject(lambda c:c['conjectures'][1]['depends_on'].append('unknown'))
    def test_cycle(self):
        self.reject(lambda c:c['conjectures'][0]['depends_on'].append('conditional-reaggregation-comparison'))
    def test_duplicate_node(self):
        self.reject(lambda c:c['conjectures'].append(copy.deepcopy(c['conjectures'][0])))
    def test_orphan_obligation(self):
        self.reject(lambda c:c['conjectures'][6]['depends_on'].remove('same-input-discriminator'))
    def test_wrong_semantics(self):
        self.reject(lambda c:c.update(outcome_semantics='static-polarity-arrows'))
    def test_no_unvalidated_import(self):
        self.reject(lambda c:c['imports'].append({'id':'copied-nima-proof','outcome':'++'}))
    def test_no_invented_probability(self):
        self.reject(lambda c:c['planner'].update(priors={'target':0.9}))
    def test_unknown_issue(self):
        self.reject(lambda c:c['conjectures'][0]['issue_ids'].append('U12'))
    def test_vacuum_control_preserved(self):
        self.reject(lambda c:c['frozen_comparison'].update(rival_control='I-Pi'))
    def test_comparison_no_silent_refit(self):
        self.reject(lambda c:c['frozen_comparison']['candidate_parameters'].update(vertex_g='372/373'))
    def test_unsafe_path(self):
        self.reject(lambda c:c['evidence_bindings'][0].update(path='../outside.md'))
    def test_stale_digest(self):
        self.reject(lambda c:c['evidence_bindings'][0].update(sha256='0'*64))
    def test_changed_evidence_fails_closed_without_repin(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for b in self.contract['evidence_bindings']:
                p=root/b['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/b['path']).read_bytes())
            policy_rel='research/voevodsky/contracts/retained-reaggregation-context-policy.v1.json'
            policy=root/policy_rel;policy.parent.mkdir(parents=True,exist_ok=True)
            policy.write_bytes((ROOT/policy_rel).read_bytes())
            self.assertTrue(validate(root,self.contract)['validation_passed'])
            p=root/self.contract['evidence_bindings'][0]['path'];p.write_bytes(p.read_bytes()+b'\nchanged\n')
            with self.assertRaises(NetError):validate(root,self.contract)

    def test_context_exception_cannot_change_historical_pin(self):
        self.reject(lambda c:c['evidence_bindings'][-1].update(sha256='0'*64))
    def test_context_exception_cannot_promote_role(self):
        self.reject(lambda c:c['evidence_bindings'][-1].update(role='theorem evidence'))
    def test_context_exception_is_reported_not_proof(self):
        r=validate(ROOT,self.contract)
        p='research/nima/completion-refinement-conjecture-net.md'
        self.assertNotIn(p,r['evidence_hashes'])
        self.assertEqual(r['unpinned_context_observations'][p]['status'],'context_only_not_proof_evidence')

if __name__=='__main__':unittest.main()
