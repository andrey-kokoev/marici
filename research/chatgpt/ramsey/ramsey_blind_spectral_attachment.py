"""Blind deletion benchmark. uv run --offline --with numpy --with networkx python ramsey_blind_spectral_attachment.py. Freeze: normalized Laplacian lowest two positive modes including entire boundary eigenspace (tol 1e-9); smaller squared interpoint distance first. Compare lower mean residual degree, larger mean codegree, iid bivariate normal coordinates and uniform ranking. Score within historical degree ONLY. Expected first legal rank under uniform tie breaking; scores rounded to 9 decimals. One representative per verified rooted isomorphism class per parent. No solver data in scoring."""
import csv,gzip,json,math,sys
from pathlib import Path
from itertools import combinations
import networkx as nx
import numpy as np
D=Path(__file__).resolve().parent

def independent(A):
    n=len(A);adj=[sum(1<<int(v) for v in np.flatnonzero(row)) for row in A];I=[0]
    for v,h in enumerate(adj):I.extend([s|(1<<v) for s in I if not s&h])
    return I

def embed(A):
    q=A.sum(1)**-.5;ev,X=np.linalg.eigh(np.eye(len(A))-q[:,None]*A*q);pos=ev[ev>1e-9];return X[:,(ev>1e-9)&(ev<=pos[1]+1e-9)]

def ranks(scores,legal):
    s=np.round(scores,9);v=s[legal].min();eq=s==v;return float((s<v).sum()+(eq.sum()+1)/(1+(eq&legal).sum()))

def orbit_reps(G):
    # Stable equitable refinement separates vertices; verify orbits within each unresolved cell.
    col=[0]*len(G)
    while True:
        sig=[(col[v],tuple(sorted(col[w] for w in G[v]))) for v in G];mp={s:i for i,s in enumerate(sorted(set(sig)))};nxt=[mp[s] for s in sig];
        if nxt==col:break
        col=nxt
    reps=[]
    for v in G:
        for r in reps:
            w=r[0];
            if col[v]!=col[w]:continue
            P=G.copy();Q=G.copy();nx.set_node_attributes(P,{i:(i==v,col[i]) for i in G},'key');nx.set_node_attributes(Q,{i:(i==w,col[i]) for i in G},'key');
            if nx.is_isomorphic(P,Q,node_match=lambda a,b:a['key']==b['key']):r.append(v);break
        else:reps.append([v])
    return reps

def figure(A,X,s):
    xy=X[:,:2];xy=25+230*(xy-xy.min(0))/np.maximum(np.ptp(xy,axis=0),1e-10);svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 310"><rect width="580" height="310" fill="white"/>'];
    for p,label in enumerate(['Blind core','Same coordinates: legal support']):
        pts=xy+np.array([p*290,0]);svg.append(f'<text x="{12+p*290}" y="293">{label}</text>');
        for i,j in combinations(range(len(A)),2):
            if A[i,j]:svg.append('<line x1="%f" y1="%f" x2="%f" y2="%f" stroke="#bbc2cc"/>'%(*pts[i],*pts[j]))
        for i,(x,y) in enumerate(pts):svg.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{("#bf4100" if p and s>>i&1 else "#234467")}"/>')
    (D/'ramsey_blind_spectral_example.svg').write_text(''.join(svg)+'</svg>')

def trial(A,d,a,seed,draw=False):
    I=independent(A);T=[s for s in I if s.bit_count()==a];P=[s for s in I if s.bit_count()==d];legal=np.array([all(s&t for t in T) for s in P]);assert legal.any();V=np.array([[i for i in range(len(A)) if s>>i&1] for s in P]);X=embed(A);B=A@A;Y=np.random.default_rng(seed).normal(size=(len(A),2));idx,jdx=np.triu_indices(d,1);u=V[:,idx];v=V[:,jdx];dist=lambda x:np.square(x[:,None,:]-x[None,:,:]).sum(2);M=dist(X)
    if draw:
        rev=np.arange(len(A))[::-1];assert np.allclose(M,dist(embed(A[rev][:,rev]))[rev][:,rev],atol=1e-9);figure(A,X,P[int(np.flatnonzero(legal)[0])])
    return dict(candidates=len(P),legal=int(legal.sum()),dimensions=X.shape[1],spectral=ranks(M[u,v].mean(1),legal),common=ranks(-B[u,v].mean(1),legal),degree=ranks(A.sum(1)[V].mean(1),legal),random_xy=ranks(dist(Y)[u,v].mean(1),legal),uniform=(len(P)+1)/(legal.sum()+1))

def run():
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();rows=[]
    for i,l in enumerate(lines,1):
        G=nx.from_graph6_bytes(l);A=nx.to_numpy_array(G);
        for orbit in orbit_reps(G):
            v=orbit[0];keep=np.arange(len(A))!=v;rows.append(dict(record=i,root=v,multiplicity=len(orbit),size=G.degree(v),**trial(A[keep][:,keep],G.degree(v),6,i*100+v,not rows)))
    with (D/'ramsey_blind_spectral_orbits.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    keys=['spectral','common','degree','random_xy','uniform'];cores=[dict(record=i,orbits=len(rs),**{k:np.mean([r[k] for r in rs]) for k in keys}) for i in range(1,len(lines)+1) if (rs:=[r for r in rows if r['record']==i])];
    with (D/'ramsey_blind_spectral_cores.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=cores[0]);w.writeheader();w.writerows(cores)
    print(len(rows),{k:np.mean([r[k] for r in cores]) for k in keys},sum(r['spectral']<r['common'] for r in cores),sum(r['spectral']<r['uniform'] for r in cores))
if __name__=='__main__':run()
