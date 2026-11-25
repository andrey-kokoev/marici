"""Conditional LP: when the red newcomer graph has alpha<=3, any shared-red-neighbor family has capacity <=3 and all eight newcomers have at least two red neighbors among themselves, hence support size<=9."""
from ramsey312_capacity_oracle import *
from ramsey312_degree_lp import pool_lp

def main():
 f,label=sys.argv[1:3];k,*s=map(int,open(f).read().split());ss=[x for x in s if x.bit_count()<=9];z=[l.split() for l in (D/'ramsey312_release26_two_targets.txt').open()][k];h=F^int(z[2]);g=adj.copy()
 for e in z[5:]:i,j=map(int,e.split(':'));g[i]^=1<<j;g[j]^=1<<i
 cs=[(1<<i,0,min(3,11-(g[i]&h).bit_count())) for i in bits(h) if (g[i]&h).bit_count()<11];res=pool_lp(ss,cs,k,threshold=8)
 if not res:
    root=D/f'ramsey312_oracle_tree27_{label}.jsonl'
    if root.exists() and root.stat().st_size:cs=list({(b,t,min(3,c) if b else c) for b,t,c in json.loads(root.read_text())['pool'] if b or t});res=pool_lp(ss,cs,k,threshold=8)
 if not res:
    el=list(sets(F,11));T={e&h for e in el};T=sorted(t for t in T if 5<=t.bit_count()<=10 and all(not t&g[i] for i in bits(t)));res=search(ss,h,g,T,k,140,alpha=3)
 print(k,len(ss),'success',bool(res.get('cert')),res.get('lp'),flush=True);(D/f'ramsey312_alpha3_27_{label}.json').write_text(json.dumps(dict(k=k,case=z,**res)))
if __name__=='__main__':main()
