"""Search for a fractional budget gap using legal-support challenges, and certify tight upper bounds on the entire domain when a small column pool suffices."""
from ramsey312_shadow_exact_weights import *
import random,math

def main():
 src,label=sys.argv[1:3];el=list(sets(F,11));out=[]
 for line in open(src):
    d,*s=map(int,line.split());k=d.bit_count();rng=random.Random(d);ss=rng.sample(s,min(180,len(s)));cols=set();rec=dict(d=d,n=len(s))
    for it in range(24):
        val,y,c=solve(d,ss,el,k);cols.update((g,b,t) for g,b,t,a in c)
        if val>k:rec.update(lower_bound=str(val),dual=y);break
        miss=[x for x in s if sum(a for g,b,t,a in c if x&b and not x&t)<1-1e-7];rng.shuffle(miss);ss+=miss[:48]
        if it%4==3 or not miss:
            cs=restricted(d,s,sorted(cols));print(d,it,len(cols),'tight',bool(cs),flush=True)
            if cs:
                den=math.lcm(*(a.denominator for g,b,t,a in cs));rows=[(g,b,t,int(a*den)) for g,b,t,a in cs];assert all(sum(w for g,b,t,w in rows if x&b and not x&t)>=den for x in s);rec.update(den=den,rows=rows);break
    out.append(rec);(D/f'ramsey312_fractional_pressure_{label}.json').write_text(json.dumps(out))
if __name__=='__main__':main()
