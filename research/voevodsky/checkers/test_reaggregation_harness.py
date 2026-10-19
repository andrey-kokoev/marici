"""Executable lifecycle, Bayesian conditioning, admission and export controls.
All mutation tests use temporary repositories, never the live ledger.
"""
from pathlib import Path
from hashlib import sha256
import copy,json,tempfile,unittest
from check_retained_reaggregation_net import ROOT,CONTRACT,NetError,validate
from reaggregation_harness import MODEL,ROUTES,INVARIANTS,PHYSICAL,REFINEMENTS,SECTOR_THEOREM,SECTOR_MODULE,SOURCE_K,LEDGER,ENGINE,GATE,NATIVE_GATE,NATIVE,MEDIATOR,read,model_data,mutate,analyze,append_event,replay,new_ledger,write_atomic,digest,diagnose_routes,diagnose_physical_gate
sys_path=ROOT/'research/conjecture_net'

class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory();self.addCleanup(self.directory.cleanup);self.root=Path(self.directory.name)
        self.contract=read(ROOT,CONTRACT)
        paths=[b['path'] for b in self.contract['evidence_bindings']]+[CONTRACT,MODEL,ROUTES,INVARIANTS,PHYSICAL,REFINEMENTS,SECTOR_THEOREM,SECTOR_MODULE,SOURCE_K,ENGINE,GATE,NATIVE_GATE,NATIVE,MEDIATOR,'research/voevodsky/checkers/reaggregation_harness.py']
        for p in paths:
            q=self.root/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes((ROOT/p).read_bytes())
    def start(self):return mutate(self.root,'start',action='prove/freeze-common-interface')
    def state(self):
        c=read(self.root,CONTRACT);m,a,_,_=model_data(self.root,c);return replay(self.root,c,m,a,read(self.root,LEDGER))
    def test_planner_is_not_readiness_only(self):
        r=analyze(self.root,self.contract)
        self.assertEqual(r['recommended_action'],'prove/freeze-common-interface');self.assertGreater(r['central']['success_probability'],0)
        self.assertEqual(r['sensitivity']['scenario_count'],27);self.assertFalse(r['empirically_calibrated'])
    def test_coherence_invariants_are_scoped_and_not_promoted(self):
        r=analyze(self.root,self.contract);report=r['coherence_invariants']
        self.assertEqual(report['status'],'static_contract_consistency_pass_scientific_satisfaction_unresolved')
        self.assertTrue(all(not item['scientifically_satisfied'] for item in report['items']))
        self.assertEqual(len(report['items']),5)
    def test_invariant_carrier_conflict_blocks_planning(self):
        p=self.root/CONTRACT;c=json.loads(p.read_text());c['frozen_comparison']['carrier']='different carrier per rule';write_atomic(p,c)
        # A changed frozen contract also invalidates the ledger pin; either gate must fail closed.
        with self.assertRaises(NetError):analyze(self.root,c)
    def test_each_node_has_all_four_explicit_ports_and_actions(self):
        routing=read(self.root,ROUTES);c=self.contract;m,actions,_,_=model_data(self.root,c)
        self.assertEqual(set(routing['routes']),set(m['estimates']))
        for claim,ports in routing['routes'].items():
            self.assertEqual(set(ports),{'++','+-','-+','--'})
            self.assertIn('prove/'+claim,{a['id'] for a in actions})
            self.assertIn('reject/'+claim,{a['id'] for a in actions})
        self.assertNotIn('physical-admission-and-selection',routing['routes'])
    def test_physical_gate_requires_conditional_success_and_five_evidence_classes(self):
        d=diagnose_physical_gate(self.root,self.contract,{'freeze-common-interface':'++'})
        self.assertEqual(d['status'],'blocked_until_conditional_target_plusplus')
        self.assertEqual(len(d['missing_evidence_classes']),5)
        self.assertFalse(d['physical_admission'] or d['automatic_promotion'])
        target=self.contract['objective']['target']
        d=diagnose_physical_gate(self.root,self.contract,{target:'++'})
        self.assertEqual(d['status'],'awaiting_physical_evidence')
    def test_physical_gate_rejects_stale_evidence(self):
        p=self.root/PHYSICAL;g=json.loads(p.read_text());g['evidence_packages']=[{'class_id':'identified-native-system','path':CONTRACT,'sha256':'stale'}];write_atomic(p,g)
        with self.assertRaises(NetError):diagnose_physical_gate(self.root,self.contract,{})
    def test_component_refutation_blocks_only_primary_route(self):
        outcomes={'native-signed-record-rule':'-+'}
        diagnosis=diagnose_routes(self.root,self.contract,outcomes)
        self.assertEqual(diagnosis['primary_route_status'],'blocked_by_refuted_component')
        self.assertEqual(diagnosis['target_outcome'],None)
        self.assertEqual(diagnosis['target_direct_blockers'],[])
        self.assertEqual(diagnosis['alternative_status'],'none_registered_route_design_review_needed')
        self.assertEqual(diagnosis['reviewed_alternatives'],[])
    def test_target_refutation_is_distinct_from_component_blockage(self):
        diagnosis=diagnose_routes(self.root,self.contract,{'conditional-reaggregation-comparison':'-+'})
        self.assertEqual(diagnosis['primary_route_status'],'refuted')
        self.assertEqual(diagnosis['target_outcome'],'-+')
    def test_priority_weights_are_diagnostic_and_truth_neutral(self):
        r=analyze(self.root,self.contract);p=r['priority_diagnostic']
        self.assertTrue(p['central_policy_unchanged'] and p['weights_are_truth_neutral'])
        self.assertEqual(len(p['scenarios']),5)
        self.assertEqual(r['recommended_action'],r['central']['first_action'])
        self.assertTrue(r['planning_only'] and not r['scientific_outcomes_changed'])
        self.assertTrue(all(s['ranking'] for s in p['scenarios']))
    def test_shared_obligations_are_single_owned_evidence(self):
        report=analyze(self.root,self.contract)['shared_obligations']
        self.assertEqual(report['status'],'canonical_single_evidence_identity')
        for obligation in report['items']:
            self.assertTrue(obligation['one_evidence_identity'])
            self.assertTrue(obligation['consumers'])
    def test_coherent_worlds_keep_alternative_route(self):
        m,a,w,_=model_data(self.root,self.contract);t=m['target'];base=m['joint_model']['base_claim_probabilities']
        self.assertAlmostEqual(sum(x['probability'] for x in w),1)
        self.assertEqual(len(w),128)
        self.assertTrue(any(x['truth'][t] and not all(x['truth'][c] for c in base) for x in w))
    def test_reviewed_hard_constraint_conditions_worlds(self):
        p=self.root/MODEL;m=json.loads(p.read_text());claims=list(m['joint_model']['base_claim_probabilities'])[:2]
        m['joint_model']['hard_constraints']=[{'kind':'mutually_exclusive','claims':claims,'review_status':'admitted','evidence_path':CONTRACT,'evidence_sha256':digest(self.root,CONTRACT)}]
        write_atomic(p,m);_,_,worlds,report=model_data(self.root,self.contract)
        self.assertEqual(report['hard_constraint_count'],1);self.assertEqual(len(worlds),96)
        self.assertAlmostEqual(sum(w['probability'] for w in worlds),1)
    def test_unpinned_constraint_rejected(self):
        p=self.root/MODEL;m=json.loads(p.read_text());claims=list(m['joint_model']['base_claim_probabilities'])[:2]
        m['joint_model']['hard_constraints']=[{'kind':'mutually_exclusive','claims':claims,'review_status':'admitted','evidence_path':CONTRACT,'evidence_sha256':'bad'}]
        write_atomic(p,m)
        with self.assertRaises(NetError):model_data(self.root,self.contract)
    def test_start_charges_once_and_continues(self):
        r=self.start();self.assertEqual(r['spent_effort'],1);self.assertEqual(r['remaining_effort'],17)
        self.assertEqual(r['recommended_action'],'continue/prove/freeze-common-interface')
    def test_no_concurrent_attempt(self):
        self.start()
        with self.assertRaises(NetError):self.start()
    def test_pause_resume_no_budget_reset(self):
        self.start();r=mutate(self.root,'pause');self.assertEqual(r['continuation_action'],'resume/prove/freeze-common-interface')
        r=mutate(self.root,'resume');self.assertEqual(r['spent_effort'],1)
    def test_paused_cannot_start_other(self):
        self.start();mutate(self.root,'pause')
        with self.assertRaises(NetError):mutate(self.root,'start',action='reject/typed-operation-classification')
    def test_missing_prerequisite(self):
        with self.assertRaises(NetError):mutate(self.root,'start',action='prove/native-signed-record-rule')
    def test_budget_cannot_reset(self):
        mutate(self.root,'init')
        with self.assertRaises(NetError):mutate(self.root,'init')
    def test_failed_proof_updates_belief_not_truth(self):
        before=analyze(self.root,self.contract)['posterior_claim_probabilities']['freeze-common-interface']
        self.start();r=mutate(self.root,'fail',reason='bounded calculation unfinished')
        self.assertEqual(r['locally_refuted_claims'],[]);self.assertIsNone(r['target_outcome']);self.assertEqual(r['spent_effort'],1)
        self.assertLess(r['posterior_claim_probabilities']['freeze-common-interface'],before)
    def test_failed_action_cannot_replay(self):
        self.start();mutate(self.root,'fail')
        with self.assertRaises(NetError):self.start()
    def test_failed_rejection_is_not_proof(self):
        mutate(self.root,'start',action='reject/typed-operation-classification');r=mutate(self.root,'fail')
        self.assertEqual(r['locally_proved_claims'],[]);self.assertEqual(r['locally_refuted_claims'],[])
    def test_reviewed_attempt_records_actual_effort_but_does_not_autocalibrate(self):
        mutate(self.root,'start',action='prove/freeze-common-interface');r=mutate(self.root,'fail',reason='bounded attempt stopped')
        nonce=r['attempts'][0]['nonce']
        r=mutate(self.root,'review',action=nonce,actual_focus_effort_eu=0.75,blocker_category='incomplete-bound',review_result='inconclusive',reviewer='independent reviewer')
        self.assertEqual(r['calibration']['reviewed_sample_count'],1)
        self.assertFalse(r['calibration']['empirically_calibrated'])
        self.assertFalse(r['calibration']['model_estimates_changed'])
        self.assertFalse(r['calibration']['eligible_for_cost_model_review'])
        self.assertIn('independent truth labels',r['calibration']['likelihood_calibration_status'])
        self.assertEqual(r['remaining_effort'],17)
    def test_review_requires_actual_cost_and_reviewer(self):
        mutate(self.root,'start',action='prove/freeze-common-interface');r=mutate(self.root,'fail')
        nonce=r['attempts'][0]['nonce']
        with self.assertRaises(NetError):mutate(self.root,'review',action=nonce,actual_focus_effort_eu=0,blocker_category='unknown',review_result='confirmed',reviewer='reviewer')
    def test_checkpoint_and_staleness(self):
        self.start();p='checkpoint.json';(self.root/p).write_text('{}');mutate(self.root,'checkpoint',path=p)
        (self.root/p).write_text('{"changed":true}')
        with self.assertRaises(NetError):analyze(self.root,self.contract)
    def test_chain_tampering(self):
        self.start();p=self.root/LEDGER;l=json.loads(p.read_text());l['events'][0]['cost']=0;write_atomic(p,l)
        with self.assertRaises(NetError):analyze(self.root,self.contract)
    def test_model_change_requires_review(self):
        self.start();p=self.root/MODEL;m=json.loads(p.read_text());m['budget_effort_units']=100;write_atomic(p,m)
        with self.assertRaises(NetError):analyze(self.root,self.contract)
    def test_routing_contract_staleness_blocks_planning(self):
        p=self.root/ROUTES;r=json.loads(p.read_text());r['routes'].pop(next(iter(r['routes'])));write_atomic(p,r)
        with self.assertRaises(NetError):analyze(self.root,self.contract)
    def test_engine_change_requires_review(self):
        self.start();p=self.root/ENGINE;p.write_bytes(p.read_bytes()+b'\n#changed')
        with self.assertRaises(NetError):analyze(self.root,self.contract)
    def test_fake_pass_not_admitted(self):
        self.start();s=self.state();a=s['attempts'][s['active']];p='fake.json'
        write_atomic(self.root/p,{'node_id':a['claim'],'intent':'prove','outcome':'++','attempt_nonce':a['nonce'],'status':'pass','verification_passed':True})
        with self.assertRaises(NetError):mutate(self.root,'finish',receipt=p,outcome='++')
        self.assertEqual(self.state()['outcomes'],{})
    def test_no_intent_outcome_mix(self):
        self.start();p='failure.json';a=self.state()['attempts'][self.state()['active']]
        write_atomic(self.root/p,{'node_id':a['claim'],'intent':'prove','outcome':'--','attempt_nonce':a['nonce'],'status':'incomplete','scientific_outcome':None,'reason':'failed'})
        with self.assertRaises(NetError):mutate(self.root,'finish',receipt=p,outcome='--')
    def test_completed_live_receipt_replays_with_exact_dependencies(self):
        l=read(ROOT,LEDGER);l['events']=l['events'][:4];write_atomic(self.root/LEDGER,l)
        for e in l['events']:
            if e['type']=='finish':
                r=read(ROOT,e['receipt']);files=[e['receipt']]+list(r.get('source_hashes',{}))
                for name in files:
                    p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/name).read_bytes())
        state=self.state();self.assertEqual(state['outcomes']['freeze-common-interface'],'++')
        self.assertEqual(state['outcomes']['native-signed-record-rule'],'++')
        r=analyze(self.root,self.contract);self.assertEqual(r['recommended_action'],'prove/rival-defect-record-rule');self.assertEqual(r['remaining_effort'],15)
        self.assertIsNone(r['target_outcome']);self.assertFalse(r['physical_admission'])
        self.assertEqual(r['physical_gate']['status'],'blocked_until_conditional_target_plusplus')
    def test_primary_refinements_derive_from_exact_receipt(self):
        r=analyze(ROOT,read(ROOT,CONTRACT),False)
        outcomes={n['id']:n['outcome'] for n in r['refinement_nodes']}
        self.assertEqual(outcomes['primary-control-transport'],'++')
        self.assertEqual(outcomes['primary-complete-generator'],'++')
        self.assertEqual(r['combined_obligation_count'],13)
    def rival_fixture(self):
        ledger=read(ROOT,LEDGER)
        start=next(e for e in ledger['events'] if e['type']=='start' and e['action']=='prove/rival-defect-record-rule')
        ledger['events']=ledger['events'][:start['index']+1]
        path='research/voevodsky/results/reaggregation-attempts/'+start['nonce']+'.rival-defect-record.json'
        files={path}
        for event in ledger['events']:
            if event['type']=='finish':files.add(event['receipt'])
        for receipt_path in list(files):files.update(read(ROOT,receipt_path)['source_hashes'])
        for name in files:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/name).read_bytes())
        write_atomic(self.root/LEDGER,ledger)
        return path,start
    def test_rival_receipt_and_refinements_preserve_active_history(self):
        path,start=self.rival_fixture();before=read(self.root,LEDGER)
        result=mutate(self.root,'finish',receipt=path,outcome='++')
        after=read(self.root,LEDGER)
        self.assertEqual(after['events'][:-1],before['events'])
        self.assertEqual(after['events'][-1]['nonce'],start['nonce'])
        self.assertEqual(result['spent_effort'],5);self.assertEqual(result['remaining_effort'],13)
        self.assertEqual(result['recommended_action'],'prove/common-resource-accounting')
        self.assertTrue(all(n['outcome']=='++' for n in result['refinement_nodes']))
        self.assertFalse(result['physical_admission'])
    def test_rival_receipt_rejects_incomplete_or_stale_evidence(self):
        path,start=self.rival_fixture();original=read(self.root,path)
        for change in ('detail','check','pin','nonce','parameter','generator'):
            receipt=copy.deepcopy(original)
            if change=='detail':receipt['detail_checks'].pop('rival_control_zero_on_vacuum_1_0')
            elif change=='check':receipt['checks']['same_empty_reference']=1
            elif change=='pin':receipt['source_hashes'].pop(NATIVE)
            elif change=='nonce':receipt['attempt_nonce']='not-the-active-attempt'
            elif change=='parameter':receipt['candidate_parameters']['vertex_g']='2'
            else:receipt['control']='unrestricted I-Pi'
            write_atomic(self.root/path,receipt)
            with self.subTest(change=change),self.assertRaises(NetError):mutate(self.root,'finish',receipt=path,outcome='++')
        self.assertEqual(self.state()['active'],start['nonce'])
    def test_rival_vacuum_extension_and_generator_blocks(self):
        from check_rival_defect_record_rule import vacuum_extend,generator_blocks,A,Q,eye
        zero=((A(0),),);one=eye(1);g=A(Q(1,2))
        self.assertEqual(vacuum_extend(one),((A(1),A(0)),(A(0),A(0))))
        self.assertEqual(generator_blocks(zero,g),(((g,),),zero,((1+g,),)))
        self.assertEqual(generator_blocks(one,g),(((g,),),((-g,),),((1+g,),)))
    def sector_fixture(self):
        from sector_theorem import ID,ASSUMPTIONS,CONCLUSIONS
        path,start=self.rival_fixture();mutate(self.root,'finish',receipt=path,outcome='++')
        mutate(self.root,'start',action='prove/common-resource-accounting')
        nonce=self.state()['active'];verifier='test-sector-verifier.py'
        (self.root/verifier).write_text('# synthetic test evidence only\n')
        bundle={'schema':'marici.voevodsky.sector-theorem-proof.v1','theorem_id':ID,'status':'admitted','fresh_execution':True,'physical_admission':False,'kernel_verified_analytic_theorem':False,'reviewer':'test fixture','proof_kind':'synthetic validator fixture, not scientific evidence',
            'assumptions':{k:True for k in ASSUMPTIONS},'conclusions':{n:{k:True for k in checks} for n,checks in CONCLUSIONS.items()},
            'verifier':{'path':verifier,'sha256':digest(self.root,verifier)},'source_hashes':{p:digest(self.root,p) for p in (verifier,CONTRACT,SECTOR_THEOREM,SECTOR_MODULE,SOURCE_K)}}
        bp='test-sector-bundle.json';write_atomic(self.root/bp,bundle)
        checks=bundle['conclusions']['common-resource-accounting']
        receipt={'schema':'marici.voevodsky.scoped-review-receipt.v1','status':'admitted','fresh_execution':True,'physical_admission':False,'node_id':'common-resource-accounting','intent':'prove','outcome':'++','attempt_nonce':nonce,'reviewer':'test fixture','proof_kind':bundle['proof_kind'],'verifier':bundle['verifier'],
            'required_checks':sorted(checks),'checks':checks,'source_hashes':{p:digest(self.root,p) for p in (verifier,CONTRACT,SECTOR_THEOREM,SOURCE_K,bp)},'sector_theorem_evidence':{'path':bp,'sha256':digest(self.root,bp)}}
        rp='test-sector-receipt.json';write_atomic(self.root/rp,receipt)
        return bp,rp,bundle,receipt
    def test_sector_route_ready_without_duplicate_action_or_promotion(self):
        path,start=self.rival_fixture();mutate(self.root,'finish',receipt=path,outcome='++')
        r=analyze(self.root,self.contract,False)
        self.assertEqual(r['sector_theorem']['status'],'ready_for_proof')
        self.assertIsNone(r['sector_theorem']['outcome'])
        self.assertEqual(r['canonical_action_count'],14)
        spent=sum(e['cost'] for e in read(self.root,LEDGER)['events'] if e['type']=='start')
        self.assertEqual(r['spent_effort'],spent);self.assertEqual(r['remaining_effort'],18-spent)
        self.assertTrue(all(v is None for v in r['sector_theorem']['conclusion_outcomes'].values()))
    def test_sector_bundle_admits_only_the_active_conclusion(self):
        bp,rp,bundle,receipt=self.sector_fixture()
        result=mutate(self.root,'finish',receipt=rp,outcome='++')
        self.assertEqual(result['sector_theorem']['outcome'],'++')
        self.assertEqual(result['sector_theorem']['conclusion_outcomes']['common-resource-accounting'],'++')
        self.assertIsNone(result['sector_theorem']['conclusion_outcomes']['same-input-discriminator'])
        self.assertIsNone(result['sector_theorem']['conclusion_outcomes']['typed-operation-classification'])
        self.assertIsNone(result['target_outcome']);self.assertFalse(result['physical_admission'])
    def test_sector_bundle_rejects_missing_assumptions_or_conclusions(self):
        bp,rp,original,receipt=self.sector_fixture()
        for change in ('commutation','readout','pin','physical','kernel','scope'):
            bundle=copy.deepcopy(original)
            if change=='commutation':bundle['assumptions']['K_commutes_with_c_and_Pi']=False
            elif change=='readout':bundle['conclusions']['same-input-discriminator'].pop('frozen_time_readout_difference')
            elif change=='pin':bundle['source_hashes'].pop(SECTOR_MODULE)
            elif change=='physical':bundle['physical_admission']=True
            elif change=='kernel':bundle['kernel_verified_analytic_theorem']=True
            else:bundle['theorem_id']='unrelated-theorem'
            write_atomic(self.root/bp,bundle)
            r=copy.deepcopy(receipt);r['source_hashes'][bp]=digest(self.root,bp);r['sector_theorem_evidence']['sha256']=digest(self.root,bp);write_atomic(self.root/rp,r)
            with self.subTest(change=change),self.assertRaises(NetError):mutate(self.root,'finish',receipt=rp,outcome='++')
    def test_sector_evidence_reuse_keeps_independent_scoped_admission(self):
        bp,rp,bundle,receipt=self.sector_fixture();mutate(self.root,'finish',receipt=rp,outcome='++')
        with self.assertRaises(NetError):mutate(self.root,'start',action='prove/same-input-discriminator')
        for claim in ('typed-operation-classification','same-input-discriminator'):
            mutate(self.root,'start',action='prove/'+claim)
            r=copy.deepcopy(receipt);r['node_id']=claim;r['attempt_nonce']=self.state()['active']
            r['checks']=bundle['conclusions'][claim];r['required_checks']=sorted(r['checks'])
            target_path='test-'+claim+'.json';write_atomic(self.root/target_path,r)
            result=mutate(self.root,'finish',receipt=target_path,outcome='++')
        self.assertEqual(len(result['sector_theorem']['evidence']),1)
        self.assertTrue(all(v=='++' for v in result['sector_theorem']['conclusion_outcomes'].values()))
        self.assertIsNone(result['target_outcome']);self.assertFalse(result['physical_admission'])
        self.assertEqual(result['recommended_action'],'prove/conditional-reaggregation-comparison')
    def test_source_k_selection_rejects_changed_inputs(self):
        from sector_theorem import validate_source_k
        original=read(self.root,SOURCE_K)
        for key,value in (('vacuum_energy','1'),('selection','mismatch_only'),('additional_orbital_terms',['new term']),('matter_dimension',100),('scale','pi/4')):
            changed=copy.deepcopy(original);changed[key]=value;write_atomic(self.root/SOURCE_K,changed)
            with self.subTest(key=key),self.assertRaises(NetError):validate_source_k(self.root)
        write_atomic(self.root/SOURCE_K,original)
        self.assertEqual(validate_source_k(self.root)['selection'],'optional_cycle_defect')
    def test_source_k_migration_preserves_active_history(self):
        ledger=read(ROOT,LEDGER);migration=next(m for m in ledger['migration_history'] if m['version']=='selected-cycle-defect-source-k-v1')
        events=ledger['events'][:migration['preserved_event_count']]
        self.assertEqual(sha256(json.dumps(events,sort_keys=True).encode()).hexdigest(),migration['preserved_events_sha256'])
        self.assertEqual(ledger['source_k_sha256'],digest(ROOT,SOURCE_K))
        self.assertEqual(events[6]['nonce'],migration['active_nonce'])
        self.assertEqual(sum(e['cost'] for e in events if e['type']=='start'),7)
    def test_sector_receipt_must_pin_selected_source_k(self):
        bp,rp,bundle,receipt=self.sector_fixture()
        receipt['source_hashes'].pop(SOURCE_K);write_atomic(self.root/rp,receipt)
        with self.assertRaises(NetError):mutate(self.root,'finish',receipt=rp,outcome='++')
    def test_sector_bundle_staleness_blocks_replay(self):
        bp,rp,bundle,receipt=self.sector_fixture();mutate(self.root,'finish',receipt=rp,outcome='++')
        (self.root/bp).write_text('{}')
        with self.assertRaises(NetError):self.state()
    def test_sector_migration_preserves_live_history(self):
        ledger=read(ROOT,LEDGER);migration=next(m for m in ledger['migration_history'] if m['version']=='shared-sector-theorem-v1')
        self.assertEqual(sha256(json.dumps(ledger['events'][:6],sort_keys=True).encode()).hexdigest(),migration['preserved_events_sha256'])
        self.assertEqual(ledger['sector_theorem_sha256'],digest(ROOT,SECTOR_THEOREM))
        spec=read(self.root,SECTOR_THEOREM);spec['required_assumptions'].remove('K_commutes_with_c_and_Pi');write_atomic(self.root/SECTOR_THEOREM,spec)
        with self.assertRaises(NetError):model_data(self.root,self.contract)
    def accounting_fixture(self):
        ledger=read(ROOT,LEDGER)
        start=next(e for e in ledger['events'] if e['type']=='start' and e['action']=='prove/common-resource-accounting')
        ledger['events']=[e for e in ledger['events'] if e['index']<next((f['index'] for f in ledger['events'] if f['type']=='finish' and f['nonce']==start['nonce']),len(ledger['events']))]
        path='research/voevodsky/results/reaggregation-attempts/'+start['nonce']+'.common-resource.json'
        files={path}
        for e in ledger['events']:
            if e['type']=='finish':files.add(e['receipt'])
        for p in list(files):files.update(read(ROOT,p)['source_hashes'])
        files.update(e['path'] for e in ledger['events'] if e['type']=='checkpoint')
        for name in files:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/name).read_bytes())
        write_atomic(self.root/LEDGER,ledger)
        return path,start
    def test_accounting_admission_preserves_history_and_scope(self):
        path,start=self.accounting_fixture();before=read(self.root,LEDGER)
        result=mutate(self.root,'finish',receipt=path,outcome='++')
        after=read(self.root,LEDGER)
        self.assertEqual(after['events'][:-1],before['events'])
        self.assertEqual(after['events'][-1]['nonce'],start['nonce'])
        self.assertEqual(result['spent_effort'],7);self.assertEqual(result['remaining_effort'],11)
        self.assertIn('common-resource-accounting',result['locally_proved_claims'])
        self.assertIsNone(result['sector_theorem']['outcome']);self.assertIsNone(result['target_outcome'])
        self.assertNotIn('same-input-discriminator',result['locally_proved_claims'])
        self.assertFalse(result['physical_admission'])
    def test_accounting_rejects_missing_readout_or_wrong_energy(self):
        path,start=self.accounting_fixture();original=read(self.root,path)
        for change in ('readout','energy','pin','truthy','scope'):
            receipt=copy.deepcopy(original)
            if change=='readout':receipt['detail_checks'].pop('measurement_energy_change_operator')
            elif change=='energy':receipt['energy_accounting']['primary_after_nonselective_readout']='epsilon'
            elif change=='pin':receipt['source_hashes'].pop(SOURCE_K)
            elif change=='truthy':receipt['checks']['common_empty_reference_derived']=1
            else:receipt['physical_admission']=True
            write_atomic(self.root/path,receipt)
            with self.subTest(change=change),self.assertRaises(NetError):mutate(self.root,'finish',receipt=path,outcome='++')
        self.assertEqual(self.state()['active'],start['nonce'])
    def test_readout_exact_coefficient_identities(self):
        from check_common_resource_accounting import readout_checks,READOUT_CHECKS
        result=readout_checks();self.assertEqual(set(result),set(READOUT_CHECKS));self.assertTrue(all(result.values()))
    def test_native_signed_record_receipt_is_theorem_scoped(self):
        ledger=read(ROOT,LEDGER);finish=next(e for e in ledger['events'] if e['type']=='finish' and e['outcome']=='++' and read(ROOT,e['receipt'])['node_id']=='native-signed-record-rule')
        receipt=read(ROOT,finish['receipt'])
        self.assertEqual(receipt['schema'],'marici.voevodsky.native-signed-record-receipt.v1')
        self.assertEqual(receipt['native_pair_dimension'],100);self.assertEqual(receipt['retained_complement_dimension'],99)
        self.assertTrue(all(receipt['checks'].values()));self.assertFalse(receipt['physical_admission'])
        for path,h in receipt['source_hashes'].items():self.assertEqual(digest(ROOT,path),h)
    def test_shared_export_import_and_revocation(self):
        from outcome_reference import resolve
        head=next(p for p in (ROOT/'research/voevodsky/exports/reaggregation').glob('*/head.json') if json.loads(p.read_text())['status']=='active')
        pointer_path=str(head.with_name('pointer.json').relative_to(ROOT)).replace('\\','/')
        pointer=read(ROOT,pointer_path);export=read(ROOT,pointer['export']['path'])
        files=set(export['artifact_sha256'])|{pointer_path,pointer['head'],pointer['export']['path']}
        for name in files:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/name).read_bytes())
        resolved=resolve(self.root,pointer);self.assertEqual(resolved['outcome'],'++')
        c=copy.deepcopy(self.contract);c['imports']=[{'id':'prior-interface-reference','outcome_pointer':pointer_path,'role':'scoped reference, not physical admission'}]
        self.assertEqual(validate(self.root,c)['imports']['prior-interface-reference']['outcome'],'++')
        h=read(self.root,pointer['head']);h['status']='revoked';write_atomic(self.root/pointer['head'],h)
        with self.assertRaises(NetError):validate(self.root,c)
    def test_export_scope_upgrade_rejected(self):
        from outcome_reference import resolve,OutcomeReferenceError
        head=next(p for p in (ROOT/'research/voevodsky/exports/reaggregation').glob('*/head.json') if json.loads(p.read_text())['status']=='active')
        pointer=read(ROOT,str(head.with_name('pointer.json').relative_to(ROOT)).replace('\\','/'))
        pointer['accepted_verification']['kernel_verified_analytic_theorem']=True
        with self.assertRaises(OutcomeReferenceError):resolve(ROOT,pointer)
    def test_ledger_overdraft_even_if_rehashed(self):
        m,a,w,_=model_data(self.root,self.contract);l=new_ledger(self.root,m)
        append_event(l,{'type':'start','action':'prove/freeze-common-interface','cost':999,'nonce':'n'})
        with self.assertRaises(NetError):replay(self.root,self.contract,m,a,l)

if __name__=='__main__':unittest.main()
