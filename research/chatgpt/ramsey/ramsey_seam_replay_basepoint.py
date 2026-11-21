"""Replay the actual finite seed execution adapter. Test the EXTRA bridge B-column=common basepoint; control by recutting the SAME directed cycles, without reversing any arrow."""
from pathlib import Path
import sys,json
D=Path(__file__).resolve().parent;sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import execute,validate,paths

def measure(p,q):
    base=p[0][0];assert p[-1][1]==base==q[0][0]==q[-1][1];result=[]
    for path,letter in ((p,'AB'),(q,'BA')):
        start,end,_,_=next(ev for ev in path if ev[3]==letter);assert base in (start,end);role='source' if start==base else 'target';pole='111' if role=='source' else '000';result.append(dict(base_role=role,pole=pole,probe_red=pole=='000'))
    return dict(base=base,words=[[e[3] for e in x] for x in (p,q)],readings=result)

r=measure(*paths[:2]);p,q=[validate(execute(w)) for w in [('BC','CA','AB'),('BA','AD','DB')]];c=measure(p,q);assert all(set(x)==set(y) for x,y in zip(r['words'],c['words']));assert r['base']=='A' and c['base']=='B';assert all(x['probe_red']!=y['probe_red'] for x,y in zip(r['readings'],c['readings']));out={'binding_hypothesis':'stationary B-column denotes common start/end of the two closed executions','adapter_supplied_cut':r,'recut_control':c};print(json.dumps(out));(D/'ramsey_seam_replay_basepoint.json').write_text(json.dumps(out)+'\n')
