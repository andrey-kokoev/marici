"""Measure successor support before completion, not just finished tours. Separate native ledger output from three proposed Hall admission filters."""
import sys
from ramsey_exit_port_types import run as exits,D,json
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_natural_tower_return import PACKETS
from retained_path_successor import RetainedSuccessorLedger

def run():
    g=RetainedSuccessorLedger(PACKETS);st=g.root;words=set()
    for _ in range(3):
        st=g.successor(st);words.update(tuple(e[2] for e in p) for p in st.paths)
    out=[]
    for t in exits():
        active=set(sum([t['blocks'][j] for j in t['typed_order']],[]));rows=[]
        for row in t['rows']:
            first,finish=row['arc'];mid=first[1];opp,=set('AB')-{mid};across=mid+opp;probes=[(first,finish),(first,across),(first,across,across[::-1]),(first,across,across[::-1],finish)]
            def accept(w,h):
                if w not in words:return False
                if h=='selected':return set(w)<=active
                if h=='edge_once':return len(set(map(frozenset,w)))==len(w)
                return len(set(w))==len(w)
            result={h:[accept(w,h) for w in probes] for h in ['selected','edge_once','native_arrow_once']};assert result==dict(selected=[True,False,False,False],edge_once=[True,True,False,False],native_arrow_once=[True]*4);assert all(w in words for w in probes);rows.append(dict(probes=probes,observed_native=[w in words for w in probes],conditional=result))
        out.append(dict(binding=t['binding'],rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_exit_three_successor_probes.json').write_text(json.dumps(out)+'\n')
