"""Do the five complementary threads define one global incidence duality? Prescribe endpoint reversal, propagate along threads, test all dihedral maps of the remaining decagon against the full flag set."""
from ramsey_unused_flag_threads import run as threads,m,mate,P,T,D,json

def run():
    r=threads();ring,=r['rings'];base={a:b for p in r['paths'] for a,b in zip(p,reversed(p))};flags={(P.index(d),j) for j,t in enumerate(T,15) for d in t};out=[]
    for sign in (-1,1):
        for k in range(10):
            f=base|{x:ring[(k+sign*i)%10] for i,x in enumerate(ring)};image=lambda s:{tuple(sorted((f[a],f[b]))) for a,b in s};
            if image(flags)!=flags:continue
            out.append(dict(ring_shift=k,ring_sign=sign,involution=all(f[f[x]]==x for x in f),preserves_rows=image(m)==m and image(mate)==mate,exchanges_rows=image(m)==mate and image(mate)==m,absolute_flags=sorted((a,b) for a,b in flags if f[a]==b),map=f))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_antipode_extension.json').write_text(json.dumps(out)+'\n')
