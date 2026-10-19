"""Exact sparse multihomogeneous face identities and cycle bookkeeping."""
from collections import Counter
from pathlib import Path
import json

N=6
ONE={(0,)*N:1}


def var(i):
    e=[0]*N;e[i]=1
    return {tuple(e):1}


def add(*polys):
    out=Counter()
    for p in polys:
        for e,c in p.items():out[e]+=c
    return {e:c for e,c in out.items() if c}


def scale(p,c):return {e:c*v for e,v in p.items() if c*v}


def mul(*polys):
    out=ONE
    for p in polys:
        acc=Counter()
        for e,c in out.items():
            for f,d in p.items():acc[tuple(x+y for x,y in zip(e,f))]+=c*d
        out={e:c for e,c in acc.items() if c}
    return out


def sub(p,values):
    out=Counter()
    for e,c in p.items():
        ex=list(e)
        for i,value in values.items():
            c*=value**ex[i];ex[i]=0
        out[tuple(ex)]+=c
    return {e:c for e,c in out.items() if c}


def chain(*terms):
    out=Counter()
    for name,c in terms:out[name]+=c
    return {name:c for name,c in out.items() if c}


def main():
    s,t,u,v,a,b=[var(i) for i in range(N)]
    F=add(mul(t,t,u,add(a,scale(b,-1))),mul(s,v,add(mul(b,add(s,t)),scale(mul(a,t),-1))))
    assert all((e[0]+e[1],e[2]+e[3],e[4]+e[5])==(2,1,1) for e in F)
    face_specs=[({2:0,3:1},mul(s,add(mul(b,add(s,t)),scale(mul(a,t),-1)))),
                ({3:0,2:1},mul(t,t,add(a,scale(b,-1)))),
                ({4:0,5:1},add(scale(mul(t,t,u),-1),mul(s,add(s,t),v))),
                ({5:0,4:1},mul(t,add(mul(t,u),scale(mul(s,v),-1))))]
    for values,expected in face_specs:assert sub(F,values)==expected
    corners=[({2:0,3:1,4:0,5:1},mul(s,add(s,t))),
             ({2:0,3:1,5:0,4:1},scale(mul(s,t),-1)),
             ({3:0,2:1,4:0,5:1},scale(mul(t,t),-1)),
             ({3:0,2:1,5:0,4:1},mul(t,t))]
    for values,expected in corners:
        assert sub(F,values)==expected and expected
    raw=chain(('Gg',1),('Gfg',-1),('Gf',1),('V0',1),('Vinf',-2),('Vinf',1))
    normalized={k:v for k,v in raw.items() if not k.startswith('V')}
    assert raw=={'Gg':1,'Gfg':-1,'Gf':1,'V0':1,'Vinf':-1}
    assert normalized=={'Gg':1,'Gfg':-1,'Gf':1} and raw!=normalized
    # Missing one infinity multiplicity is invisible only AFTER the degeneracy quotient.
    bad=chain(*raw.items(),('Vinf',1))
    assert bad!=raw and {k:v for k,v in bad.items() if not k.startswith('V')}==normalized
    divisors={'Gf':{'0':1,'inf':-1},'Gg':{'-1':1,'inf':-1},
              'Gfg':{'0':1,'-1':1,'inf':-2},'V0':{},'Vinf':{}}
    d2=chain(*[(point,c*m) for name,c in raw.items() for point,m in divisors[name].items()])
    assert d2=={}
    wrong=chain(('Gg',1),('Gfg',1),('Gf',-1))
    assert chain(*[(point,c*m) for name,c in wrong.items() for point,m in divisors[name].items()])!={}
    r={'passed':True,'classification':'global_nonconstant_filler_with_explicit_degenerate_vertical_correction',
       'face_identities':4,'corner_identities':4,'raw_vertical_correction':{'V0':1,'Vinf':-1},
       'raw_and_normalized_distinguished':True,'multiplicity_sign_and_omission_controls':True,
       'Hodge_proved':False,'Hodge_refuted':False,
       'residuals':['No general moving lemma, degree-three associator or sixfold obstruction computed.']}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-global-multiplicativity-faces-v1.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))


if __name__=='__main__':main()
