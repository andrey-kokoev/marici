"""Exact weighted-blowup audit at D2 cap D3=(u,y)=(0,0)."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent))
from gysin_ordinary_crossing_blowup import (P,K,t,Z,O,ER,add,mul,scale,
    matrix_residue_e,matrix_finite_e,rank,indicial,residue_t,text_matrix,
    shear_connection)

def power(a,n):
    out=[O]
    for _ in range(n): out=mul(out,a)
    return out

def substitute_series(fit,us,vs):
    def conv(terms):
        out=[Z]
        for i,j,c in terms:
            out=add(out,scale(mul(power(us,i),power(vs,j)),K.convert(c)))
        return out
    return ER(conv(fit['numerator']),conv(fit['denominator']))

def pullback(fits,chart):
    if chart=='u_chart':
        # u=e, y=e^2 t, v=2+2y-u.
        us=[Z,O]; vs=[K.convert(2),-O,2*t]
        duz, dvz = ER([O]), ER([-O,4*t])
        dut, dvt = ER([Z]), ER([Z,Z,2*O])
    else:
        # u=e t, y=e^2, v=2+2e^2-et.  t is the stack-chart s.
        us=[Z,t]; vs=[K.convert(2),-t,K.convert(2)]
        duz,dvz=ER([t]),ER([-t,K.convert(4)])
        dut,dvt=ER([Z,O]),ER([Z,-O])
    au=[[substitute_series(fits[('u',i,j)],us,vs) for j in range(4)] for i in range(4)]
    av=[[substitute_series(fits[('v',i,j)],us,vs) for j in range(4)] for i in range(4)]
    ae=[[au[i][j]*duz+av[i][j]*dvz for j in range(4)] for i in range(4)]
    at=[[au[i][j]*dut+av[i][j]*dvt for j in range(4)] for i in range(4)]
    return ae,at

def valuation_matrix(a): return [[x.valuation() for x in row] for row in a]

def feasible_weights(vals,bound=8):
    # Require val(A_ij)+w_i-w_j >= -1; normalize min(w)=0.
    ans=[]
    import itertools
    for w in itertools.product(range(bound+1),repeat=4):
        if min(w): continue
        if all(vals[i][j]+w[i]-w[j]>=-1 for i in range(4) for j in range(4)):
            ans.append(w)
    return sorted(ans,key=lambda x:(sum(x),x))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('connection',type=Path);ap.add_argument('output',type=Path);a=ap.parse_args()
    d=json.loads(a.connection.read_text()); fits={(e['axis'],e['row'],e['col']):e['fit'] for e in d['entries']}
    out=[]
    for chart in ['u_chart','stack_chart']:
        ae,at=pullback(fits,chart); vals=valuation_matrix(ae); candidates=feasible_weights(vals)
        if not candidates: raise RuntimeError(f'no logarithmic shear in {chart}: {vals}')
        w=list(candidates[0]); be,bt=shear_connection(ae,at,w)
        re=matrix_residue_e(be); tang=matrix_finite_e(bt)
        # In U_u the strict transforms are t=+/-1.  In the stack chart they
        # are the mu_2-orbits s^2=+/-1 and are recorded through U_u instead
        # of choosing noncanonical geometric square roots.
        points=[('D2',1),('D3',P-1)] if chart=='u_chart' else []
        strict=[]
        for label,pt in points:
            rr=[]; orders=[]
            for row in tang:
                ro=[];oo=[]
                for x in row:
                    z,q=residue_t(x,pt);ro.append(z);oo.append(q)
                rr.append(ro);orders.append(oo)
            strict.append({'divisor':label,'point':pt,'minimum_order':min(map(min,orders)),
                'residue_rank':rank(rr),'residue':text_matrix(rr),
                'L1_kernel_dimension':4-rank(indicial(rr,1))})
        out.append({'chart':chart,'raw_exceptional_valuations':vals,'minimal_shear':w,
            'exceptional_residue':text_matrix(re),'exceptional_rank':rank(re),
            'exceptional_kernel_dimension':4-rank(re),
            'exceptional_L1_kernel_dimension':4-rank(indicial(re,1)),
            'positive_indicial_kernel_dimensions':{str(m):4-rank(indicial(re,m)) for m in range(1,11)},
            'strict_transforms':strict})
    a.output.write_text(json.dumps({'schema':'marici.gm.gysin_weighted_crossing.v1',
      'weights':{'u':1,'y':2},'charts':out},indent=2))

if __name__=='__main__': main()
