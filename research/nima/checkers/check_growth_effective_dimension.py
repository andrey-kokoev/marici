# /// script
# dependencies = ["numpy>=2,<3", "scipy>=1.14,<2"]
# ///
"""Scale-dependent volume and diffusion dimensions of paw promotions0..7.

Volume uses all-source BFS already checked in check_line_graph_geometry.py.
Diffusion uses a lazy unit-edge walk: Q=(I+D^-1/2 A D^-1/2)/2.
Full eigenvalues through396 vertices;64-probe trace estimation at4552 vertices.
No physical clock, continuum limit, or dimension is assumed from cycle labels.
"""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
import json
import math
import hashlib
import numpy as np
import scipy
from scipy.sparse import csr_matrix
from scipy.linalg import eigvalsh

HERE = Path(__file__).resolve().parent
geometry = json.loads((HERE.parent/'results/line-graph-geometry.json').read_text())
assert geometry['status']=='passed'
TIMES = (1,2,4,8,16,32,64,128)
PROBES = 64
SEED = 20260929


def transition(n,edges):
    degree = np.zeros(n)
    for a,b in edges: degree[a]+=1;degree[b]+=1
    row=list(range(n));col=list(range(n));weights=[0.5]*n
    for a,b in sorted(edges):
        weight=0.5/math.sqrt(degree[a]*degree[b])
        row.extend((a,b));col.extend((b,a));weights.extend((weight,weight))
    Q=csr_matrix((weights,(row,col)),shape=(n,n))
    stationary=np.sqrt(degree/degree.sum())
    assert np.max(np.abs(Q@stationary-stationary))<1e-12
    return Q,stationary


def trace_estimate(Q,u):
    n=Q.shape[0]
    rng=np.random.default_rng(SEED)
    z=(2*rng.integers(0,2,size=(n,PROBES))-1).astype(float)
    # Remove the known stationary eigenvector and add its exact1/N contribution.
    z-=u[:,None]*(u@z)[None,:]
    evolved=z.copy(); samples={}
    for t in range(1,max(TIMES)+1):
        evolved=Q@evolved
        if t in TIMES:
            samples[t]=np.sum(z*evolved,axis=0)/n+1/n
    return samples


def dimensions(returns,n):
    result=[]
    for t in TIMES[:-1]:
        a,b=returns[t],returns[2*t]
        ds=-2*math.log(b['mean']/a['mean'])/math.log(2)
        # Explicit screening conventions, not inferred continuum criteria.
        usable=(t>=4 and b['mean']>=5/n)
        result.append({'t':t,'to':2*t,'spectral_dimension':ds,
                       'away_from_one_step_and_stationary_floor':usable,
                       'stationary_fraction_at_end':(1/n)/b['mean']})
    return result


# Calibrate the estimator on a known3D periodic cubic lattice. The spectrum
# is analytic, so a large control needs no explicit262144-vertex adjacency.
cosines=np.cos(2*np.pi*np.arange(64)/64)
cubic_eigenvalues=(.5+(cosines[:,None,None]+cosines[None,:,None]+cosines[None,None,:])/6).ravel()
cubic_returns={t:{'mean':float(np.mean(cubic_eigenvalues**t)), 'standard_error':0.0} for t in TIMES}
cubic_ds=dimensions(cubic_returns,64**3)
assert abs(cubic_ds[-2]['spectral_dimension']-3)<.2
assert abs(cubic_ds[-1]['spectral_dimension']-3)<.1
print('3D cubic control:',[(d['t'],round(d['spectral_dimension'],4)) for d in cubic_ds[-2:]],flush=True)

edges={(0,1),(0,2),(1,2),(0,3)}
results=[]
for cycle in range(8):
    g=geometry['cycles'][cycle]
    n=g['vertices']
    assert g['edges']==len(edges)
    Q,u=transition(n,edges)
    returns={}
    samples=None
    if n<=396:
        eigenvalues=eigvalsh(Q.toarray(),check_finite=True)
        assert eigenvalues[0]>=-1e-10 and eigenvalues[-1]<=1+1e-10
        eigenvalues=np.clip(eigenvalues,0,1)
        assert abs(eigenvalues[-1]-1)<1e-10
        for t in TIMES:
            returns[t]={'mean':float(np.mean(eigenvalues**t)),'standard_error':0.0}
        method='full numerical spectrum'
        if n==396:
            samples=trace_estimate(Q,u)
            for t,vals in samples.items():
                se=float(np.std(vals,ddof=1)/math.sqrt(PROBES))
                assert abs(float(vals.mean())-returns[t]['mean']) <= 5*se+1e-12
    else:
        samples=trace_estimate(Q,u)
        for t,vals in samples.items():
            returns[t]={'mean':float(vals.mean()),
                        'standard_error':float(np.std(vals,ddof=1)/math.sqrt(PROBES))}
        method='64-probe Hutchinson estimate with exact stationary mode'
    if samples is None or n<=396:
        assert abs(returns[1]['mean']-.5)<1e-12
    assert all(returns[t]['mean']>=1/n-1e-12 for t in TIMES)
    assert all(returns[2*t]['mean']<=returns[t]['mean']+1e-12 for t in TIMES[:-1])
    ds=dimensions(returns,n)
    if n>396:
        # Paired bootstrap preserves correlations between the two walk times.
        rng=np.random.default_rng(SEED+1)
        selections=rng.integers(0,PROBES,size=(1000,PROBES))
        for d in ds:
            t=d['t']
            draws=-2*np.log(samples[2*t][selections].mean(axis=1)/samples[t][selections].mean(axis=1))/np.log(2)
            d['bootstrap_95_percent_interval']=np.quantile(draws,[.025,.975]).tolist()
    balls={int(r):Fraction(v) for r,v in g['mean_ball_volumes'].items()}
    volume=[]
    for r in sorted(balls):
        if r and 2*r in balls:
            dimension=math.log(float(balls[2*r]/balls[r]))/math.log(2)
            volume.append({'r':r,'to':2*r,'volume_dimension':dimension,
                           'end_ball_fraction':float(balls[2*r]/n),
                           'below_quarter_graph':balls[2*r]<=Fraction(n,4),
                           'includes_microscopic_radius':r==1})
    results.append({'cycle':cycle,'records':n,'method':method,
                    'return_probabilities':returns,'spectral_dimensions':ds,'volume_dimensions':volume})
    print('cycle',cycle,'N',n,'volume d(1,2)',round(volume[0]['volume_dimension'],4),
          'spectral d(4,8)',round(ds[2]['spectral_dimension'],4),
          'screened windows',[(d['t'],round(d['spectral_dimension'],3)) for d in ds if d['away_from_one_step_and_stationary_floor']],flush=True)
    if cycle<7:
        incident=defaultdict(list)
        for i,(a,b) in enumerate(sorted(edges)):
            incident[a].append(i);incident[b].append(i)
        edges={tuple(sorted(pair)) for ids in incident.values() for pair in combinations(ids,2)}

report={'status':'passed','numpy':np.__version__,'scipy':scipy.__version__,
        'metric':'unit-edge hop distance','walk':'lazy simple random walk, uniform starting-vertex trace average',
        'spectral_formula':'-2 log[P(2t)/P(t)] / log2',
        'volume_formula':'log[B(2r)/B(r)] / log2',
        'seed':SEED,'probes':PROBES,'cycles':results,
        'cubic_3D_control':cubic_ds,
        'volume_source':'results/line-graph-geometry.json',
        'volume_source_sha256':hashlib.sha256((HERE.parent/'results/line-graph-geometry.json').read_bytes()).hexdigest(),
        'scope':'Finite graph diagnostics; no asserted continuum/Planck dimension or physical time. Screening thresholds are stated conventions.'}
(HERE.parent/'results/growth-effective-dimension.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
