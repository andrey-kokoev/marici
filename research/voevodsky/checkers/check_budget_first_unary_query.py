"""Budget-first principal-port phases settle simultaneous NIL locally."""
from pathlib import Path
import json

def wire(a,b):return frozenset((a,b))
def linear(ws):
    ports=[p for w in ws for p in w]
    assert all(len(w)==2 for w in ws) and len(ports)==len(set(ports))

def interior():
    # Q_B.p--KUNIT.p and Q_B.a--COUNT.p; KUNIT.a--BTAIL.p.
    # Q_C.p--COUNT.p, Q_C.a--BTAIL.p. Symmetric count phase.
    old={wire('Q.p','UNIT.p'),wire('Q.a','OTHER.p'),wire('UNIT.a','TAIL.p')}
    new={wire('Qnext.p','OTHER.p'),wire('Qnext.a','TAIL.p')}
    linear(old);linear(new)
    return {p for w in old for p in w if p in ('OTHER.p','TAIL.p')}=={p for w in new for p in w if p in ('OTHER.p','TAIL.p')}

def terminal():
    old={wire('Q.p','NIL.p'),wire('Q.a','OTHER.p'),wire('Q.r','OUT.p')}
    new={wire('BOOL.p','OUT.p'),wire('ERASE.p','OTHER.p')}
    linear(old);linear(new)
    return True

assert interior() and terminal()
def run(count,k):
    c,b=count,k;phase='budget';steps=0
    while True:
        if phase=='budget':
            if b==0:return True,steps,c,b
            b-=1;phase='count'
        else:
            if c==0:return False,steps,c,b
            c-=1;phase='budget'
        steps+=1

cases=0
for count in range(65):
    for k in range(65):
        answer,steps,c,b=run(count,k)
        assert answer==(count>=k)
        assert steps==2*min(count,k)+(1 if count<k else 0)
        assert c>=0 and b>=0
        cases+=1
report={'passed':True,'cases':cases,'phase_order':'Q_B checks budget NIL first (true); KUNIT -> Q_C; Q_C checks count NIL (false); UNIT -> Q_B','zero_cases':'0>=0 true, 0>=positive false, positive>=0 true','port_templates':'both interior and terminal replacements linear, external endpoints once','limits':'Abstract phase evaluator plus local boundary templates; full instantiated port graph and eraser cleanup not yet run.'}
out=Path(__file__).resolve().parents[1]/'results/budget-first-unary-query.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
