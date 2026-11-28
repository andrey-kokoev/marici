"""Predeclared 88-edge holdout: deterministic random sample of 1374 (previous test layer size), budget 608. Count all legal unordered support pairs, allowing identical supports. No maximal-row approximation."""
import gzip,json,tempfile,subprocess,random
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from concurrent.futures import ThreadPoolExecutor
from ramsey_contact_overlap_transfer import profile,decode,find,CAT,D


def pairs(a,e):
    edge=sum(1<<v for v in e);I=[0]
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v]);
    Q=[q for q in I if q.bit_count()==7];broken=[q for q in Q if q&edge==edge];live=[q for q in Q if q&edge!=edge];S=[s for s in I if s&edge!=edge];full=(1<<len(S))-1
    # For each first row, the bitset of seconds must miss some broken Q and hit all live Q missed by the first.
    by=[int.from_bytes(bytes(sum(1<<j for j,s in enumerate(S[t:t+8]) if s>>i&1) for t in range(0,len(S),8)),'little') for i in range(27)]
    def hit(q):
        h=0
        while q:
            b=q&-q;q-=b;h|=by[b.bit_length()-1]
        return h
    dead=[(q,full^hit(q)) for q in broken];keep=sorted(((q,hit(q)) for q in live),key=lambda p:p[1].bit_count());ordered=diag=0
    for i,s in enumerate(S):
        opts=0
        for q,m in dead:
            if not q&s:opts|=m
        if not opts:continue
        for q,h in keep:
            if not q&s:
                opts&=h
                if not opts:break
        ordered+=opts.bit_count();diag+=(opts>>i)&1
    assert (ordered-diag)%2==0;return (ordered+diag)//2

def audit():
    refs=json.loads((D.parent/'ramsey_contact_overlap_transfer.json').read_text())['training_profiles'];w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);G={i:l.strip().decode() for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if sum(l.strip()[1:].translate(w))==88};ids=sorted(random.Random(4355).sample(sorted(G),1374));budget=608
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'pack.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_intact27_seven_pack.rs')),'-o',str(exe)],check=True)
        def truth(rows):
            p=subprocess.run([str(exe)],input='\n'.join(f'{j} {s}' for j,(_,s) in enumerate(rows)),text=True,capture_output=True,check=True);assert int(p.stderr)==len(rows);return {rows[k][0] for k in map(int,p.stdout.split()) if find(decode(rows[k][1]))['example']}
        baseline=truth([(i,G[i]) for i in ids]);scores={}
        for i in ids:
            if i in baseline:continue
            a=decode(G[i]);
            for u,v in combinations(range(27),2):
                if a[u]&((1<<v)|a[v]):continue
                h=profile(a,(u,v));scores[i,u,v]=min(sum(abs(x-y) for x,y in zip(h,r)) for r in refs)
        cut=sorted(scores.values())[budget-1];fixed={k for k,v in scores.items() if v<cut};tied={k for k,v in scores.items() if v==cut};slots=budget-len(fixed);print('cut',cut,'fixed',len(fixed),'ties',len(tied),'slots',slots,flush=True)
        ranked=sorted(tied,key=lambda k:(-pairs(decode(G[k[0]]),k[1:]),k));taken=set(ranked[:slots]);rows=[]
        for k in sorted(fixed|tied):
            i,u,v=k;s=G[i];t=v*(v-1)//2+u;j=1+t//6;rows.append((k,s[:j]+chr(63+((ord(s[j])-63)^(1<<(5-t%6))))+s[j+1:]))
        wins=truth(rows);f=len(fixed&wins);h=len(tied&wins);actual=len(taken&wins);expected=Fraction(slots*h,len(tied));out=dict(layer=88,sample_seed=4355,sample=len(ids),eligible=len(ids)-len(baseline),safe_links=len(scores),budget=budget,cut=cut,fixed=len(fixed),fixed_hits=f,tied=len(tied),tie_slots=slots,tied_hits=h,pair_hits_in_tie=actual,total_hits=f+actual,random_expected_total=str(f+expected),pass_test=actual>expected,all_hits_at_or_below_cutoff=sorted(wins),selected_tie=ranked[:slots]);print({k:v for k,v in out.items() if k not in ('selected_tie','all_hits_at_or_below_cutoff')});(D.parent/'ramsey_new_pairs_holdout.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
