"""Predict reopenable slots solely by all currently violated fives. Independently solve each fixed triple by exact residual tight-row intersection, without restricting fourth supports to the original screen. Track minimum total replacements against all valid maximal assignments."""
from ramsey_capacity_transfer_78 import check,decode,D,json,inds,bits,verify,grow
from collections import Counter

def audit(H,idx):
    bad=[];good=[];check(H,lambda s,t:(good if t=='valid' else bad).append(s));I=inds(H);rows=[s for s in I if 4<=s.bit_count()<=6];out=[]
    for S in bad:
        W=[s for s in rows if s.bit_count()+sum(not(t&s) for t in S)>=8];assert W and all(s.bit_count()==5 for s in W);slots=[]
        for j,m in enumerate(S):
            pred=all(not t&m for t in W);q=S[:j]+S[j+1:];slacks=[7-t.bit_count()-sum(not a&t for a in q) for t in rows];tight=[t for t,z in zip(rows,slacks) if z==0];sol=[] if min(slacks)<0 else [s for s in I if all(s&t for t in tight)];
            if sol:verify(grow(H,q+[sol[0]]),8)
            assert pred or not sol;slots.append(dict(pred=pred,solutions=len(sol),example=sol[0] if sol else None))
        common=lambda g:sum((Counter(g)&Counter(S)).values());best=max(good,key=common);out.append(dict(record=idx,supports=S,violated=W,slots=slots,min_replacements=4-common(best),closest=best))
    return out
if __name__=='__main__':
    src=json.loads((D/'ramsey_capacity_transfer_78.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[r for i,s in enumerate(src['catalogue']) if s['counts'].get('miss5') for r in audit(decode(lines[i]),i+1)];print(len(out),Counter((s['pred'],bool(s['solutions'])) for r in out for s in r['slots']),Counter(r['min_replacements'] for r in out));print(out[0]);(D/'ramsey_missed_row_reopen_78.json').write_text(json.dumps(out)+'\n')
