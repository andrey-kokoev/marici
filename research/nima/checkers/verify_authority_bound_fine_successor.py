"""Fine-state and answer arithmetic; no session or vault imports.

History authority is an external precondition, never inferred by this checker.
"""
from fractions import Fraction as Q
import json,hashlib
from pathlib import Path
from verify_scalar_envelope_band import domain,envelopes
if not __debug__:raise RuntimeError('Assertions required')
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def verify_state(before,event,authorized_history,operation,after):
    assert before['family']=='owning-m4-moment-curve-two-history-v1' and authorized_history in ('A','B')
    assert set(operation)=={'kind','h_upper','point'} and operation['kind']=='fine-upper-point-admission'
    polygon=domain(before['request']['n']);lo,up=envelopes(before['request']['n']);rows=[]
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        nx,ny=b[1]-a[1],a[0]-b[0];rows.append(((nx,ny,Q(0)),nx*a[0]+ny*a[1]))
    rows.extend([((Q(0),Q(0),Q(-1)),Q(0)),((Q(0),Q(0),Q(1)),Q(1))])
    for a,b,c in lo if authorized_history=='A' else up:
        rows.append(((a,b,Q(-1)),-c) if authorized_history=='A' else ((-a,-b,Q(1)),c))
    rows.extend(((Q(r['normal'][0]),Q(r['normal'][1]),Q(0)),Q(r['upper'])) for r in before['frames'])
    rows.append(((Q(0),Q(0),Q(1)),Q(operation['h_upper'])))
    expected={'family':before['family'],'n':before['request']['n'],'history':authorized_history,
      'retirement_event':event,'parent_digest':digest(before),'operation':operation,
      'rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows],
      'capabilities':{'exact_point_admission':True,'exact_lift':True,'approximate_lift':False,'archive':False}}
    assert after==expected

def verify_answer(state,point,answer):
    assert answer['state']==state and answer['point']==point and type(answer['admits']) is bool
    p,q=map(Q,point);rows=[(tuple(map(Q,r['normal'])),Q(r['upper'])) for r in state['rows']]
    if 'violated_public_row' in answer:
        i=answer['violated_public_row'];assert type(i) is int and 0<=i<len(rows)
        (a,b,c),bound=rows[i];assert c==0 and a*p+b*q>bound and answer['admits'] is False
        assert 'source_lift' not in answer;return
    assert all(a*p+b*q<=bound for (a,b,c),bound in rows if c==0)
    lo=max((bound-a*p-b*q)/c for (a,b,c),bound in rows if c<0)
    hi=min((bound-a*p-b*q)/c for (a,b,c),bound in rows if c>0)
    assert answer['interval']==list(map(str,(lo,hi))) and answer['admits']==(lo<=hi)
    for i,bound,sign in zip(answer['bound_rows'],(lo,hi),(-1,1)):
        assert type(i) is int and 0<=i<len(rows)
        (a,b,c),h=rows[i];assert c*sign>0 and (h-a*p-b*q)/c==bound
    assert len(answer['bound_rows'])==2
    if lo>hi:assert 'source_lift' not in answer;return
    t=list(map(Q,answer['source_lift']));assert len(t)==4 and all(0<=v<=100+2*i for i,v in enumerate(t))
    d=Q(1,128**4);slopes=[Q(1,128**i) for i in range(4)];h=(t[0]-50)/d
    assert t[1]==51 and sum(t)==206+d*p
    assert sum(v*r for v,r in zip(t,slopes))==sum(v*r for v,r in zip((50,51,52,53),slopes))+d*q
    assert all(a*p+b*q+c*h<=bound for (a,b,c),bound in rows)

def main():
    out=Path(__file__).resolve().parents[1]/'results';report=json.loads((out/'authority-bound-fine-successor.json').read_text())
    for p,h in report['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    assert len(report['successors'])==2;count=0
    operation={'kind':'fine-upper-point-admission','h_upper':'1/2','point':['1','1']}
    for history,record in zip(('A','B'),report['successors']):
        assert record['owner_history']==history
        before=record['before'];assert before['request']=={'n':18,'eta':'1/100'} and before['frames']==[]
        assert before['epsilon']==str(Q(16513,128**4*100))
        after=record['committed']['state'];verify_state(before,record['event'],history,operation,after)
        assert record['candidate']=={'before_digest':digest(before),'retirement_event':record['event'],'after':after}
        assert len(record['answers'])==3
        for point,answer in zip((['1','1'],['1/18','1/324'],['0','0']),record['answers']):
            verify_answer(after,point,answer);count+=1
        assert record['answers'][0]['admits']==(history=='B') and record['answers'][1]['admits'] and not record['answers'][2]['admits']
        assert record['committed']['bytes']['section']==record['committed']['bytes']['replacement_section']==0
    result={'passed':True,'fine_successors':2,'exact_answers_verified':count,
      'scope':'Independent arithmetic replay conditional on fixture-authorized A/B identities; vault authority and atomicity are tested in-process, not inferred from this JSON.'}
    (out/'authority-bound-fine-successor-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
