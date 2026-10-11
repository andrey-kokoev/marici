"""One symmetric reservoir completes the retained incidence response.

Exact fixed-source comparisons; both energy sign conventions are exposed.
Reservoir edge strength is scanned, not selected by a mass target.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[1]
STAGES = ('raw', 'local', 'aligned')


def solve(a, b):
    m = [[F(v) for v in row]+[F(rhs)] for row,rhs in zip(a,b)]
    n = len(b)
    for k in range(n):
        pivot = next(i for i in range(k,n) if m[i][k])
        m[k],m[pivot] = m[pivot],m[k]
        c=m[k][k]
        m[k]=[v/c for v in m[k]]
        for i in range(n):
            if i != k:
                c=m[i][k]
                m[i]=[v-c*w for v,w in zip(m[i],m[k])]
    return [row[-1] for row in m]


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def main():
    source = ROOT/'results/twelve-triangle-1836-arrows.json'
    content = source.read_bytes()
    pairs = [(tuple(a['source']),tuple(a['target'])) for a in json.loads(content)]
    nodes = sorted({v for edge in pairs for v in edge})
    assert len(pairs)==1836 and len(nodes)==108
    assert all(sum(v[0]==s for v in nodes)==36 for s in STAGES)
    index = {s:i for i,s in enumerate(STAGES)}
    # Compute the aggregate stiffness from the actual source graph.
    lap = [[F(0) for _ in STAGES] for _ in STAGES]
    for a,b in pairs:
        i,j=index[a[0]],index[b[0]]
        lap[i][i]+=1; lap[j][j]+=1
        lap[i][j]-=1; lap[j][i]-=1
    assert lap == [[1404,-108,-1296],[-108,540,-432],[-1296,-432,1728]]
    jp=[F(1),F(0),F(0)]
    je=[F(0),F(0),F(-1)]
    pair=[a+b for a,b in zip(jp,je)]
    rows=[]
    for k in (F(1,4),F(1),F(4)):
        matrix=[[lap[i][j]+(36*k if i==j else 0) for j in range(3)] for i in range(3)]
        def response(j):
            x=solve(matrix,j)
            # Verify the unreduced 108 port equations, not just aggregation.
            potential={v:x[index[v[0]]] for v in nodes}
            flux={v:k*potential[v] for v in nodes}
            for a,b in pairs:
                d=potential[a]-potential[b]
                flux[a]+=d; flux[b]-=d
            assert all(flux[v]==j[index[v[0]]]/36 for v in nodes)
            reservoir_flux=-sum(k*potential[v] for v in nodes)
            assert reservoir_flux==-sum(j)
            assert sum(x)==sum(j)/(36*k)
            energy=sum((potential[a]-potential[b])**2 for a,b in pairs)/2
            energy+=sum(k*potential[v]**2 for v in nodes)/2
            assert energy==dot(j,x)/2
            return x,energy
        xp,ep=response(jp)
        xe,ee=response(je)
        xpair,epair=response(pair)
        assert xpair==[a+b for a,b in zip(xp,xe)]
        field_cross=epair-ep-ee
        assert field_cross==dot(jp,xe)==dot(je,xp)<0
        # Minimizing field energy minus source work changes the sign.
        relaxed_cross=(-epair)-(-ep)-(-ee)
        assert relaxed_cross==-field_cross>0
        xsame,esame=response([F(1),F(0),F(1)])
        assert esame-ep-ee==-field_cross>0
        assert -esame+ep+ee==field_cross<0
        rows.append(dict(reservoir_edge_strength=str(k),
                         proton_response=list(map(str,xp)),electron_response=list(map(str,xe)),
                         pair_response=list(map(str,xpair)),
                         isolated_proton_field_energy=str(ep),isolated_witness_field_energy=str(ee),
                         pair_field_energy=str(epair),
                         opposite_sign_field_cross=str(field_cross),field_cross_decimal=float(field_cross),
                         opposite_sign_relaxation_cross=str(relaxed_cross),
                         reservoir_sources={'proton':-1,'witness':1,'pair':0}))
    assert len({r['opposite_sign_field_cross'] for r in rows})==3
    # The neutral pair's constant-mode source vanishes; isolated sources have
    # energy 1/(216*k) in that mode. Check exact neutral k->0 gauge-fixed limit.
    x0=[F(5,6912),F(1,6912),F(0)]
    mean=sum(x0)/3
    centered=[v-mean for v in x0]
    assert [dot(row,centered) for row in lap]==pair and sum(centered)==0
    assert dot(pair,centered)/2==F(5,13824)
    result=dict(schema='marici.nima.wg-reservoir-completion.v1',status='pass',
                source_sha256=hashlib.sha256(content).hexdigest(),
                graph={'original_ports':108,'original_arrows':1836,'reservoir_nodes':1,'added_links':108},
                assumption='equal reservoir links and uniform layer sources; no WG derivation of their weights',
                rows=rows,neutral_zero_coupling_field_energy='5/13824',
                isolated_constant_mode_field_energy='1/(216*k)',
                mechanism='Opposite signed sources lower stored-field energy but raise minimized scalar-relaxation energy relative to isolated sources. These are distinct readouts, not interchangeable signs.',
                controls=['all 109 flux equations', 'common reservoir for every source configuration',
                          'superposition', 'field-energy/source-work identity', 'same-sign reversal',
                          'reservoir-strength dependence', 'neutral zero-mode limit'],
                residual='Reservoir completion makes comparison possible, but neither coupling scale nor physical energy readout is selected by current WG. No mass target was used.')
    out=ROOT/'results/wg-reservoir-completion.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
