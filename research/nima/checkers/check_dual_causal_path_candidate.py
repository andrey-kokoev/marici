"""Independent exact regression of the frozen reversible-envelope candidate."""
import contextlib
import io
import json
import runpy
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima'))
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23


def require(ok,msg):
    if not ok: raise ValueError(msg)


def main():
    with contextlib.redirect_stdout(io.StringIO()):
        original=runpy.run_path(str(ROOT/'research/nima/checkers/check_indexed_path_synthesis.py'))
    compose=original['compose']
    counts=dict(objects=0,inverses=0,future_edges=0,shared_R=0,squares=0,cone_controls=0)
    for m in range(1,11):
        n=m+5
        records={(h.inner_pair[1]-4,h.outer_pair[1]-4):h for h in compile_nnmhv_histories(n) if supports_component_23(h)}
        def word(i,j): return tuple((k,k+1) for k in range(i,j+1))
        def pair(p): return p[0][0],p[-1][0]
        def decode(p): return records[pair(p)]
        def visible(p): return p[0][0]<p[-1][0]
        def chart(p):
            require(visible(p),'diagonal metric boundary')
            return pair(p)
        def tags(p):
            i,j=pair(p)
            return tuple(t for t,ok in (('L',i>1),('R',j<m),('l',i<j),('r',i<j)) if ok)
        def step(p,t):
            require(t in tags(p),'operation outside source domain')
            i,j=pair(p)
            if t=='L': out=next(iter(compose({((i-1,i),)},{p})))
            elif t=='R': out=next(iter(compose({p},{((j+1,j+2),)})))
            elif t=='l': out=p[1:]
            else: out=p[:-1]
            require(bool(out) and out==word(*pair(out)),'invalid output path')
            return out
        def execution(p,w):
            history=[p]
            for t in w: history.append(step(history[-1],t))
            return tuple(history)
        inverse={'L':'l','l':'L','R':'r','r':'R'}
        for i,j in records:
            p=word(i,j)
            counts['objects']+=1
            for t in tags(p):
                q=step(p,t)
                back=step(q,inverse[t])
                require(back==p and decode(back)==decode(p),'inverse lost full state')
                # Boundary replacement is restored on returning to a diagonal.
                require(bool(decode(q).boundary_updates)==(pair(q)[0]==pair(q)[1]),'boundary replacement mismatch')
                counts['inverses']+=1
                if not (visible(p) and visible(q)): continue
                u,v=chart(p); U,V=chart(q); a,b=U-u,V-v
                for branch,C,future in (('plus',F(4),('L','R')),('minus',F(-4),('l','R'))):
                    if t not in future: continue
                    norm=C*a*b/F((v-u)**2)
                    dt=(V-U)-(v-u) if branch=='plus' else (U+V)-(u+v)
                    require(norm==0 and dt==1,'future null ray')
                    if branch=='plus': require(a<=0 and b>=0,'plus order')
                    else: require(a>=0 and b>=0,'minus order')
                    counts['future_edges']+=1
                if t=='R':
                    require(a==0 and b==1,'shared action differs')
                    counts['shared_R']+=1
            if not visible(p): continue
            for w,z in ((('L','R'),('R','L')),(('l','R'),('R','l'))):
                try: a,b=execution(p,w),execution(p,z)
                except ValueError: continue
                if not all(visible(q) for q in a+b): continue
                require(a[-1]==b[-1] and a!=b,'square/history distinction')
                require(decode(a[-1])==decode(b[-1]),'square full record')
                counts['squares']+=1
            for a,b in ((-1,1),(-2,3),(1,1),(2,3)):
                gp=F(4*a*b,(j-i)**2);gm=-gp
                require((gp<0)==(a<0) and (gm<0)==(a>0),'opposite interiors')
                counts['cone_controls']+=1
        try: chart(word(1,1))
        except ValueError: pass
        else: raise AssertionError('diagonal promoted to metric point')
    # Fresh explicit controls in m=10 environment.
    p=word(3,6)
    l=step(p,'l')
    require(pair(l)==(4,6),'inverse source action')
    require(pair(l)[0]>pair(p)[0],'inverse not genuinely new')
    # Every forward-only L/R word has nonincreasing first endpoint: l cannot arise there.
    u,v=pair(p);U,V=pair(step(p,'L'))
    require((U+V)-(u+v)<0,'L incorrectly called minus-future')
    loop=execution(p,('L','l'))
    require(loop[0]==loop[-1] and len(loop)==3,'inverse history erased')
    paths=['research/nima/dual-causal-path-candidate.md',
           'research/nima/checkers/check_dual_causal_path_candidate.py',
           'research/nima/checkers/check_indexed_path_synthesis.py',
           'research/nima/nnmhv_coherence_paths.py']
    result={'schema':'marici.nima.dual-causal-path-candidate.v1','passed':True,
        'disposition':'conditional_mathematical_candidate_constructed; physical_WG_I3_open',
        'counts':counts,'hostiles':['diagonal-is-not-metric-domain','same-containment-cone-fails-minus',
            'L-is-minus-past','inverse-action-not-in-forward-only-source','inverse-execution-not-empty'],
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/nima/results/dual-causal-path-candidate.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
