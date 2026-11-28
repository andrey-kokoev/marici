"""Replicate the 88-edge test on the disjoint remainder. Nearest-integer matched fraction of eligible safe links."""
from ramsey_new_pairs_holdout import *
from math import comb

def audit():
    prev=json.loads((D.parent/'ramsey_new_pairs_holdout.json').read_text());refs=json.loads((D.parent/'ramsey_contact_overlap_transfer.json').read_text())['training_profiles'];w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);G={i:l.strip().decode() for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if sum(l.strip()[1:].translate(w))==88};ids=set(G)-set(random.Random(prev['sample_seed']).sample(sorted(G),prev['sample']));assert len(ids)==10541
    with tempfile.TemporaryDirectory() as td:
        def compile(name):
            exe=Path(td)/(name+'.exe');subprocess.run(['rustc','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True);return str(exe)
        pack=compile('ramsey_intact27_seven_pack');pair=compile('ramsey_pair_score')
        def truth(rows):
            p=subprocess.run([pack],input='\n'.join(f'{j} {s}' for j,(_,s) in enumerate(rows)),text=True,capture_output=True,check=True);assert int(p.stderr)==len(rows);return {rows[k][0] for k in map(int,p.stdout.split()) if find(decode(rows[k][1]))['example']}
        baseline=truth([(i,G[i]) for i in sorted(ids)]);scores={}
        for i in sorted(ids-baseline):
            a=decode(G[i]);
            for u,v in combinations(range(27),2):
                if a[u]&((1<<v)|a[v]):continue
                h=profile(a,(u,v));scores[i,u,v]=min(sum(abs(x-y) for x,y in zip(h,r)) for r in refs)
        budget=round(Fraction(len(scores)*prev['budget'],prev['safe_links']));cut=sorted(scores.values())[budget-1];fixed={k for k,v in scores.items() if v<cut};tied=sorted(k for k,v in scores.items() if v==cut);slots=budget-len(fixed);print('budget',budget,'ties',len(tied),'slots',slots,flush=True)
        def count(keys):
            p=subprocess.run([pair],input='\n'.join(f'{G[i]} {u} {v}' for i,u,v in keys),text=True,capture_output=True,check=True);vals=list(map(int,p.stdout.split()));assert len(keys)==len(vals);return dict(zip(keys,vals))
        with ThreadPoolExecutor(8) as pool:ps={k:v for chunk in pool.map(count,[tied[j:j+24] for j in range(0,len(tied),24)]) for k,v in chunk.items()}
        for k in (tied[0],max(ps,key=ps.get)):assert ps[k]==pairs(decode(G[k[0]]),k[1:])
        ranked=sorted(tied,key=lambda k:(-ps[k],k));taken=set(ranked[:slots]);rows=[]
        for k in sorted(fixed|set(tied)):
            i,u,v=k;s=G[i];t=v*(v-1)//2+u;j=1+t//6;rows.append((k,s[:j]+chr(63+((ord(s[j])-63)^(1<<(5-t%6))))+s[j+1:]))
        wins=truth(rows);f=len(wins&fixed);h=len(wins)-f;actual=len(taken&wins);N=len(tied);expected=Fraction(slots*h,N);prob=sum(Fraction(comb(slots,j)*comb(N-slots,h-j),comb(N,h)) for j in range(actual,h+1) if j<=slots and h-j<=N-slots);out=dict(layer=88,remainder=len(ids),eligible=len(ids-baseline),safe=len(scores),budget=budget,cutoff=cut,fixed=len(fixed),fixed_hits=f,tied=N,slots=slots,tie_hits=h,pair_hits=actual,total_hits=f+actual,expected_random_total=str(f+expected),random_tail=float(prob),pass_test=actual>expected,cut_pair_score=ps[ranked[slots-1]],hits_at_or_below_cutoff=[(k,ps.get(k),k in fixed|taken) for k in sorted(wins)]);print(out);(D.parent/'ramsey_new_pairs_remainder.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
