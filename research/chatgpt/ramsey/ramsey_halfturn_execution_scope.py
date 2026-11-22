"""Compare a two-event execution advancing one vertex to its half-turn image with relabeling an entire six-event receipt by that same permutation."""
import sys
from ramsey_handoff_distance_audit import run as tours,D,json
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from retained_path_successor import RetainedSuccessorLedger
from check_natural_tower_return import PACKETS

def run():
    g=dict(zip('ABCD','BADC'));ledger=RetainedSuccessorLedger(PACKETS);child=ledger.successor(ledger.root);words=[tuple(e[2] for e in p) for p in child.paths];opposite=[(e,f) for e,f in words if f[-1]==g[e[0]]];assert len(words)==10 and len(opposite)==4 and {e[0] for e,_ in opposite}==set(g)
    ts=tours();records=[]
    for t in ts:
        w=t['word'];pairs=list(zip(w,w[1:]+w[:1]));present=[p for p in pairs if p in opposite];moved=[''.join(g[v] for v in e) for e in w];rot=lambda x:[x[i:]+x[:i] for i in range(len(x))];other,=[u for u in ts if moved in rot(u['word'])];assert other['seam']==g[t['seam']] and moved not in rot(w) and len(present)==3;records.append(dict(seam=t['seam'],realized_two_steps=present,missing=list(set(opposite)-set(present)),relabeled_seam=other['seam']))
    return dict(native_words=len(words),half_turn_words=opposite,tours=records)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_halfturn_execution_scope.json').write_text(json.dumps(out)+'\n')
