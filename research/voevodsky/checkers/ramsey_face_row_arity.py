"""Minimum number of marked second-side rows required for the residual 52-edge failure. Record counts and inclusion-minimal clique certificates."""
from ramsey_face_pair_obstruction import CAT,D,decode,ind,bits
from itertools import combinations,islice
import json,gzip

def audit():
    src=json.loads((D.parent/'ramsey_face_pair_obstruction.json').read_text());r,=[r for r in src['failures'] if not r['blocked']];idx=src['record']
    with gzip.open(CAT.parent/'r37_21.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    I=ind(a);mark=sum(1<<v for v in r['mark']);dom=[[s|m for s in I if s.bit_count()==3 and not s&mark and s|m in A] for A in [set(I)] for m in r['req']];qs=[q for q in I if 4<=q.bit_count()<=6];full=(1<<len(qs))-1;sizes={k:sum(1<<j for j,q in enumerate(qs) if q.bit_count()==k) for k in (4,5,6)};miss={s:sum(1<<j for j,q in enumerate(qs) if not q&s) for d in dom for s in d};out=[]
    def search(group,mask,first=False):
        n=0;w=None
        def dfs(j,rows,once,twice,thrice):
            nonlocal n,w
            if j==len(group):n+=1;w=rows;return first
            for s in dom[group[j]]:
                m=miss[s]&mask
                if m&((once&sizes[6])|(twice&sizes[5])|(thrice&sizes[4])):continue
                if dfs(j+1,rows+[s],once|m,twice|(once&m),thrice|(twice&m)):return True
        dfs(0,[],0,0,0);return n,w
    for k in (2,3,4):
        for g in combinations(range(4),k):
            n,w=search(g,full);row=dict(group=g,count=n,witness=w)
            if not n and not any(set(t['group'])<set(g) and not t['count'] for t in out):
                # Grow a blocking certificate by counterexamples, then remove redundant cliques.
                mask=0
                while True:
                    _,w=search(g,mask,True)
                    if w is None:break
                    bad=[j for j,q in enumerate(qs) if q.bit_count()+sum(not q&s for s in w)>=8];assert bad
                    mask|=1<<bad[0]
                for j in bits(mask):
                    if search(g,mask^(1<<j),True)[1] is None:mask^=1<<j
                row['certificate']=[bits(qs[j]) for j in bits(mask)]
            out.append(row)
    pair_ok=lambda s,t:not (miss[s]&miss[t]&sizes[6]);left=[{s for s in dom[0] if pair_ok(s,t)} for t in dom[1]];right=[{s for s in dom[0] if pair_ok(s,t)} for t in dom[3]];pairs=[(i,j) for i,s in enumerate(dom[1]) for j,t in enumerate(dom[3]) if pair_ok(s,t)];bridge=dict(legal_5_9_pairs=len(pairs),triples_passing_all_pair_tests=sum(len(left[i]&right[j]) for i,j in pairs),row0_compatible_with_some_5=len(set.union(*left)),row0_compatible_with_some_9=len(set.union(*right)),row0_compatible_with_both_separately=len(set.union(*left)&set.union(*right)))
    res=dict(pair_test=bridge,record=idx,mark=r['mark'],required=list(map(bits,r['req'])),domains=list(map(len,dom)),pocket_row_ids=bits(r['t']),tests=out);print(res);(D.parent/'ramsey_face_row_arity.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
