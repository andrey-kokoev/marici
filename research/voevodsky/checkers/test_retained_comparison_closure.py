"""Temporary-repository admission tests; synthetic reuse is never live evidence."""
import copy,unittest
import test_reaggregation_harness as fixtures
from reaggregation_harness import ROOT,LEDGER,read,digest,mutate,write_atomic,analyze
from check_retained_reaggregation_net import NetError
from check_retained_comparison_closure import CLASSIFY,DISCRIMINATE,TARGET,required,validate_receipt,exact_sector_checks,GATE
from sector_theorem import ID,ASSUMPTIONS,CONCLUSIONS,SOURCE_K

class ClosureTests(unittest.TestCase):
    def setUp(self):
        self.base=fixtures.HarnessTests('runTest');self.base.setUp();self.addCleanup(self.base.doCleanups)
        self.root=self.base.root
        path,start=self.base.accounting_fixture();mutate(self.root,'finish',receipt=path,outcome='++')
        ledger=read(ROOT,LEDGER);start=next(e for e in ledger['events'] if e['type']=='start' and e['action']=='prove/'+CLASSIFY)
        p='research/voevodsky/results/reaggregation-attempts/'+start['nonce']+'.closure.json'
        self.template=read(ROOT,p)
        for name in self.template['source_hashes']:
            dst=self.root/name;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((ROOT/name).read_bytes())
    def receipt(self,claim):
        mutate(self.root,'start',action='prove/'+claim)
        receipt=copy.deepcopy(self.template);receipt['node_id']=claim;receipt['attempt_nonce']=self.base.state()['active']
        receipt['checks']={k:True for k in required(claim)};receipt['required_checks']=sorted(required(claim))
        if claim==DISCRIMINATE:
            bundle={'schema':'marici.voevodsky.sector-theorem-proof.v1','theorem_id':ID,'status':'admitted','fresh_execution':True,'physical_admission':False,'kernel_verified_analytic_theorem':False,
                'reviewer':'synthetic test fixture only','proof_kind':'validator fixture, not live scientific evidence','assumptions':{k:True for k in ASSUMPTIONS},'conclusions':{n:{k:True for k in group} for n,group in CONCLUSIONS.items()},
                'verifier':{'path':GATE,'sha256':digest(self.root,GATE)},'fresh_checks':receipt['detail_checks'],'source_hashes':dict(receipt['source_hashes'])}
            p='test-bundle.json';write_atomic(self.root/p,bundle)
            receipt['source_hashes'][p]=digest(self.root,p);receipt['sector_theorem_evidence']={'path':p,'sha256':digest(self.root,p)}
        p='test-'+claim+'.json';write_atomic(self.root/p,receipt)
        return p,receipt
    def test_typed_operator_identities(self):
        self.assertTrue(all(exact_sector_checks().values()))
    def test_incomplete_or_upgraded_typed_receipts_rejected(self):
        path,original=self.receipt(CLASSIFY)
        for change in ('phase','annihilation','detail','pin','nonce','photon'):
            r=copy.deepcopy(original)
            if change=='phase':r['phase_contract']['conjugate_right_weight']=1
            elif change=='annihilation':r['sector_classification']['carrier_change']=True
            elif change=='detail':r['detail_checks'].pop('record_commutator_nonzero')
            elif change=='pin':r['source_hashes'].pop(SOURCE_K)
            elif change=='nonce':r['attempt_nonce']='wrong'
            else:r['physical_admission']=True
            write_atomic(self.root/path,r)
            with self.subTest(change=change),self.assertRaises(NetError):mutate(self.root,'finish',receipt=path,outcome='++')
    def test_certified_bounds_and_energy_must_match(self):
        path,r=self.receipt(CLASSIFY)
        for field,value in (('occupation_bounds',{'primary_lower':'0','primary_upper':'1','rival':'0'}),('energy_accounting',{'measurement_energy_increase':'0'})):
            changed=copy.deepcopy(r);changed[field]=value
            with self.subTest(field=field),self.assertRaises(NetError):validate_receipt(self.root,changed,CLASSIFY)
    def test_ordered_closure_preserves_budget_and_physical_gate(self):
        with self.assertRaises(NetError):mutate(self.root,'start',action='prove/'+DISCRIMINATE)
        path,r=self.receipt(CLASSIFY);result=mutate(self.root,'finish',receipt=path,outcome='++')
        self.assertIsNone(result['sector_theorem']['outcome']);self.assertIsNone(result['target_outcome'])
        path,r=self.receipt(DISCRIMINATE);result=mutate(self.root,'finish',receipt=path,outcome='++')
        self.assertEqual(result['sector_theorem']['outcome'],'++');self.assertIsNone(result['target_outcome'])
        path,r=self.receipt(TARGET);result=mutate(self.root,'finish',receipt=path,outcome='++')
        self.assertEqual(result['target_outcome'],'++');self.assertFalse(result['physical_admission'])
        self.assertEqual(result['physical_gate']['status'],'awaiting_physical_evidence')
        self.assertEqual(len(result['physical_gate']['missing_evidence_classes']),5)
        self.assertIsNone(result['recommended_action'])
        spent=sum(e['cost'] for e in read(self.root,LEDGER)['events'] if e['type']=='start')
        self.assertEqual(result['remaining_effort'],18-spent)
    def test_bundle_missing_assumption_blocks_discriminator(self):
        p,r=self.receipt(CLASSIFY);mutate(self.root,'finish',receipt=p,outcome='++')
        p,r=self.receipt(DISCRIMINATE);b=read(self.root,'test-bundle.json');b['assumptions'].pop('K_commutes_with_c_and_Pi')
        write_atomic(self.root/'test-bundle.json',b)
        r['source_hashes']['test-bundle.json']=digest(self.root,'test-bundle.json');r['sector_theorem_evidence']['sha256']=digest(self.root,'test-bundle.json');write_atomic(self.root/p,r)
        with self.assertRaises(NetError):mutate(self.root,'finish',receipt=p,outcome='++')
    def test_stale_closure_dependency_blocks_replay(self):
        p,r=self.receipt(CLASSIFY);mutate(self.root,'finish',receipt=p,outcome='++')
        (self.root/GATE).write_text('# changed proof gate')
        with self.assertRaises(NetError):self.base.state()

if __name__=='__main__':unittest.main()
