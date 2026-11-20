import json
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from unittest.mock import patch
import ramsey_relational_lift_net as net

class TestLiftNet(unittest.TestCase):
    def setUp(self):self.c=json.loads(net.CONTRACT.read_text())
    def test_ready(self):self.assertEqual(set(net.evaluate(self.c)['ready']),{'cells','pair-types','pentagon-8d-continuations','t184-port-readings','t184-opposite-face-star','tetrahedral-foam-37','blue-five-set-pair-coverage','olap-ramsey-index-coverage','vertipaq-ramsey-storage','ramsey-single-matrix-optimizer','redundant-links-by-joint-reconstruction','db-literature-ramsey-constructor','db-six-antipodal-roles','system-of-claims-and-implications','rooted-core-size-crossover'})
    def test_cycle(self):
        next(n for n in self.c['conjectures'] if n['id']=='clock')['requires']=['clock'];self.assertRaises(ValueError,net.evaluate,self.c)
    def test_missing(self):
        self.c['conjectures'][0]['requires']=['missing'];self.assertRaises(ValueError,net.evaluate,self.c)
    def test_premature_root(self):
        self.c['objective']['outcome']='++';self.assertRaises(ValueError,net.evaluate,self.c)
    def test_premature_child(self):
        self.c['conjectures'][-1]['outcome']='++';self.assertRaises(ValueError,net.evaluate,self.c)
    def test_wrong_control(self):
        next(n for n in self.c['conjectures'] if n['id']=='positions-only')['outcome']='++';self.assertRaises(ValueError,net.evaluate,self.c)
    def test_prior_source_drift(self):
        self.c['prior_sources']['moments'][1]='changed';self.assertRaises(ValueError,net.evaluate,self.c)
    def test_prior_binding(self):
        d={'branch':'weights'};self.assertRaises(ValueError,net.check_prior_response,self.c,d);p=net.priors(self.c,'cells','weights');self.assertIn('prior-local-pair',p);d['prior_response']={k:{'relation':'different_scope','reason':'fixture'} for k in p};net.check_prior_response(self.c,d)
    def test_blocked_priority(self):
        self.c['next']='weights';self.assertRaises(ValueError,net.evaluate,self.c)
    def test_stale_evidence(self):
        with TemporaryDirectory() as d,patch.object(net,'HISTORY',Path(d)/'attempts'):
            net.HISTORY.write_text(json.dumps(dict(id='1',node='clock',outcome='++',summary='test',evidence=self.c['validator'],sha256='changed')));self.assertRaises(ValueError,net.evaluate,self.c)
class TestRouteReview(unittest.TestCase):
    def setUp(self):
        tmp=TemporaryDirectory();self.addCleanup(tmp.cleanup);self.d=Path(tmp.name);self.rows=[];self.num=0;self.base=dict(route='example');self.grants=[];self.branch='sixth';self.alg=self.d/'fixture.py';self.alg.write_text("def lift(l,k):return {'occurrences':[str(i) for i in range(l*k+2)]}\ndef reduce_once(x):return {'cells':{i:[i] for i in x['occurrences']}}\ndef coordinates(q):return [3,7]\ndef witnesses(q):return list(q['cells'])[-2:],[]\n");self.e=self.d/'fixture.txt';self.e.write_text('Synthetic lifecycle fixture only.')
    def event(self,action,**kw):
        self.num+=1;p=self.d/f'{self.num}.json';p.write_text(json.dumps(dict(self.base,action=action,**kw)));h=net.digest(p);rows=self.rows+[{'file':p.name,'digest':h}];self.rs=net.replay(rows,lambda name:self.d/name,'contract',{'phase'},self.grants);self.rows=rows;return h
    def freeze(self,kind='family'):
        data={f:'fixture' for f in net.SPEC};data.update(domain='fixture domain',domain_kind=kind,correction_kind='additional',dimension='4',geometry='span');self.spec=self.event('freeze',branch=self.branch,contract='contract',implementation_sha256=net.digest(self.alg),**dict(data,lift_algorithm=self.alg.name))
    def submit(self,stage):
        fields={f:'fixture argument' for f in net.STAGES[stage]};p=self.e
        if stage=='prediction':
            from ramsey_lift_execution import execute
            p=self.d/'synthetic_run.json';p.write_text(json.dumps(execute(self.alg,3,7)));fields['predicted_order']='23'
        return self.event('submit',spec=self.spec,stage=stage,author='author',evidence=p.name,evidence_sha256=net.digest(p),**fields)
    def review(self,stage,h,verdict='accept',reviewer='reviewer'):
        return self.event('review',spec=self.spec,stage=stage,submission=h,reviewer=reviewer,reason='fixture review',verdict=verdict)
    def finish(self,kind):
        self.freeze(kind)
        for stage in net.STAGES:h=self.review(stage,self.submit(stage))
        return h
    def close(self,h):return self.event('root_review',spec=self.spec,scope='fixture domain',closure_review=h,reviewer='operator',scope_acceptance='fixture only',reason='fixture')
    def test_family_closure(self):
        h=self.finish('family');self.assertRaises(ValueError,self.close,h);self.grants.append(dict(spec=self.spec,domain='fixture domain',closure_review=h));self.close(h);self.assertEqual(self.rs['example']['state'],'root_closed_for_declared_domain')
    def test_novel_route_progress(self):
        self.freeze();self.review('lift',self.submit('lift'));v=net.dashboard(self.rs)['example'];self.assertEqual(v['next'],'reduction');self.assertIn('sixth',v['nodes'])
    def test_cell_identity(self):
        from ramsey_lift_execution import execute,inspect_run
        t=execute(self.alg,3,7);t['extra']=['absent','also absent'];self.assertRaises(ValueError,inspect_run,t)
    def test_distinct_witnesses(self):
        from ramsey_lift_execution import execute,inspect_run
        t=execute(self.alg,3,7);t['extra']=['1','1'];self.assertRaises(ValueError,inspect_run,t)
    def test_pilot_stays_scoped(self):h=self.finish('pilot');self.assertRaises(ValueError,self.close,h)
    def test_prediction_precedes_comparison(self):self.freeze();self.assertRaises(ValueError,self.submit,'threshold')
    def test_review_and_revision(self):
        self.freeze();h=self.submit('lift');self.assertRaises(ValueError,self.review,'lift',h,'accept','author');self.review('lift',h,'revise');self.review('lift',self.submit('lift'),'refute');self.assertEqual(self.rs['example']['state'],'refuted')
    def test_route_mixing(self):self.freeze();h=self.submit('lift');self.spec='other route';self.assertRaises(ValueError,self.review,'lift',h)
    def test_evidence_drift(self):self.freeze();h=self.submit('lift');self.e.write_text('altered');self.assertRaises(ValueError,self.review,'lift',h)

if __name__=='__main__':unittest.main()
