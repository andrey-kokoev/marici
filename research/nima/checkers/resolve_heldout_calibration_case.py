"""Preserve exact Arb endpoints when exchanging the held-out problem."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import copy
import json
from flint import arb

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


def main():
    s=load('solver',ROOT/'certificates/diagonal_task_solver.py')
    v=load('verifier',ROOT/'certificates/verify_diagonal_task.py')
    t=load('calibration',HERE/'certify_noisy_attachment_task.py')
    catalogue=json.loads((ROOT/'results/certificate-acquisition-planner.json').read_text())
    records=catalogue['records']
    parents={r['parent'] for r in records if r['parent'] is not None}
    unresolved=[r for r in records if r['id'] not in parents and r['certificate']['status']=='UNRESOLVED']
    assert len(unresolved)==1
    old=unresolved[0]['problem'];assert s.solve(old)['status']=='UNRESOLVED'
    t.c.CELLS=32768;t.c.scaled_residual.cache_clear()
    E=t.c.scaled_residual(2)*t.c.scaled_residual(12)*(-arb.pi()*148).exp()/5
    lo,hi=t.endpoints(E)
    previous_lo,previous_hi=map(F,old['rows'][0]['calibration'])
    assert previous_lo<lo<=hi<previous_hi
    p=copy.deepcopy(old);p['rows'][0]['calibration']=[str(lo),str(hi)]
    for key in old:
        if key!='rows':assert p[key]==old[key]
    for i in range(len(p['rows'])):
        assert p['rows'][i]['data']==old['rows'][i]['data']
        assert p['rows'][i]['weight']==old['rows'][i]['weight']
    cert=s.solve(p);assert v.verify(p,cert)
    assert cert['status']=='AMBIGUOUS'
    sums={key:str(sum(F(a)*F(x) for a,x in zip(p['target']['coefficients'],cert[key])))
          for key in ('false_witness','true_witness')}
    assert F(sums['false_witness'])<0<F(sums['true_witness'])
    # A persistent incompleteness fixture: exact datum, uncertain calibration.
    thin=[]
    for k in range(1,21):
        delta=F(1,2**k)
        problem={'model':s.MODEL,'rows':[{'data':['1','1'],
                 'calibration':[str(2-delta),str(2+delta)],'weight':'1'}],
                 'budget':'1','target':{'coefficients':['1'],'threshold':'0'}}
        answer=s.solve_fixed(problem);assert answer['status']=='UNRESOLVED' and v.verify(problem,answer)
        improved=s.solve(problem);assert improved['status']=='TARGET_TRUE' and v.verify(problem,improved)
        # For every allowed E the actual source x=1/E is feasible and positive.
        assert 0<1/(2+delta)<=1/(2-delta)<1
        thin.append({'problem':problem,'certificate':answer})
    exact=copy.deepcopy(thin[-1]['problem']);exact['rows'][0]['calibration']=['2','2']
    exact_cert=s.solve(exact);assert exact_cert['status']=='TARGET_TRUE' and v.verify(exact,exact_cert)
    result={'passed':True,'original_record_id':unresolved[0]['id'],
        'resolution':'AMBIGUOUS: exact endpoints recover information lost by conservative printed-ball exchange',
        'same_calibration_work':'32768 cells, 192 bits, same scaled cutoff and physical formula',
        'old_calibration':old['rows'][0]['calibration'],'exact_endpoint_calibration':[str(lo),str(hi)],
        'problem':p,'certificate':cert,'target_values':sums,
        'target_value_displays':{k:t.decimal_bounds(t.A(F(x))) for k,x in sums.items()},
        'persistent_thin_data_tests_version_1_only':thin,'exact_calibration_control':{'problem':exact,'certificate':exact_cert},
        'scope':'The remaining held-out case has opposite-sign robust source witnesses. The thin-data fixture proves no unconditional termination claim for interval calibration is valid for this fixed-witness certificate schema.'}
    (ROOT/'results/resolved-heldout-calibration-case.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'resolved_status':cert['status'],
        'target_values':result['target_value_displays'],'thin_data_unresolved_tests':len(thin),
        'exact_calibration_control':exact_cert['status']},indent=2))


if __name__=='__main__':main()
