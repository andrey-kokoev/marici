"""WG-I5: independently reuse actual composition and actual compiler."""
import contextlib
import io
import json
import runpy
import sys
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima'))
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from nnmhv_coherence_paths import compile_nnmhv_histories, supports_component_23, terminal_r_state
from check_wg_interval_operation_bridge import source_move, validate


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_path(n,p):
    require(bool(p), 'empty path object')
    m=n-5
    require(all(isinstance(e,tuple) and len(e)==2 and 1<=e[0]<=m and e[1]==e[0]+1 for e in p), 'not forward line edges')
    require(all(a[1]==b[0] for a,b in zip(p,p[1:])), 'disconnected word')


def line_path(i,j):
    return tuple((k,k+1) for k in range(i,j+1))


def main():
    log=io.StringIO()
    with contextlib.redirect_stdout(log):
        native=runpy.run_path(str(ROOT/'research/nima/checkers/check_indexed_path_synthesis.py'))
    compose=native['compose']
    counts=dict(objects=0,extensions=0,endpoint_squares=0,executions=0,binary_splits=0,triple_splits=0)
    hostiles=[]
    for n in range(6,16):
        m=n-5
        selected=[h for h in compile_nnmhv_histories(n) if supports_component_23(h)]
        lookup={(h.inner_pair[1]-4,h.outer_pair[1]-4):h for h in selected}
        require(len(lookup)==len(selected)==m*(m+1)//2,'source enumeration')
        def decode(p):
            validate_path(n,p)
            return lookup[(p[0][0],p[-1][0])]
        def encode(h):
            validate(h)
            require(h.n==n,'source cutoff mismatch')
            return line_path(h.inner_pair[1]-4,h.outer_pair[1]-4)
        def tags(p):
            return tuple(t for t,ok in (('L',p[0][0]>1),('R',p[-1][0]<m)) if ok)
        def step(p,tag):
            validate_path(n,p)
            require(tag in tags(p),'unavailable edge action')
            if tag=='L':
                i=p[0][0]
                out=compose({((i-1,i),)},{p})
            else:
                j=p[-1][0]
                out=compose({p},{((j+1,j+2),)})
            require(len(out)==1,'non-singleton native composition')
            result=next(iter(out))
            validate_path(n,result)
            return result
        def words(p):
            yield ()
            for t in tags(p):
                for tail in words(step(p,t)):
                    yield (t,)+tail
        def execute(p,w):
            history=[p]
            for t in w:
                history.append(step(history[-1],t))
            return tuple(history)
        for h in selected:
            p=encode(h)
            require(decode(p)==h and encode(decode(p))==p,'full object inverses')
            counts['objects']+=1
            for tag in tags(p):
                q=step(p,tag)
                expected=source_move(h,tag)
                require(decode(q)==expected,'full operation square')
                require(terminal_r_state(decode(q))==terminal_r_state(expected),'spinor payload')
                counts['extensions']+=1
            if len(tags(p))==2:
                lr,rl=execute(p,('L','R')),execute(p,('R','L'))
                require(lr[-1]==rl[-1] and lr!=rl,'execution-order erasure')
                require(decode(lr[-1])==decode(rl[-1]),'full endpoint square')
                counts['endpoint_squares']+=1
            if n<=10:
                for w in words(p):
                    execution=execute(p,w)
                    records=[h]
                    for tag in w:
                        records.append(source_move(records[-1],tag))
                    require(tuple(decode(x) for x in execution)==tuple(records),'execution square')
                    require(tuple(encode(x) for x in records)==execution,'execution recovery')
                    counts['executions']+=1
                    for cut in range(len(w)+1):
                        a=execute(p,w[:cut]);b=execute(a[-1],w[cut:])
                        require(a[:-1]+b==execution,'binary execution composition')
                        counts['binary_splits']+=1
                        for cut2 in range(cut,len(w)+1):
                            mid=execute(a[-1],w[cut:cut2]);end=execute(mid[-1],w[cut2:])
                            require((a[:-1]+mid)[:-1]+end == a[:-1]+(mid[:-1]+end) == execution,'execution associator')
                            counts['triple_splits']+=1
        for name,action in [
            ('empty-object',lambda:decode(())),
            ('non-line-edge',lambda:decode(((1,3),))),
            ('reversed-edge',lambda:decode(((2,1),))),
            ('disconnected-word',lambda:decode(((1,2),(3,4)))),
            ('left-boundary',lambda:step(line_path(1,1),'L')),
            ('right-boundary',lambda:step(line_path(m,m),'R'))]:
            try: action()
            except ValueError: pass
            else: raise AssertionError('hostile accepted: '+name)
            if n==6: hostiles.append(name)
        if n==9:
            p=line_path(2,2); h=decode(p)
            for name,bad in [('stale-upper',replace(decode(step(p,'L')),boundary_updates=h.boundary_updates)),
                             ('stale-prefix',replace(decode(step(p,'R')),inner_prefix=h.inner_prefix))]:
                try: validate(bad)
                except ValueError: hostiles.append(name)
                else: raise AssertionError('stale payload accepted')
            require(compose({p},{p})==set(),'self-composition confused with extension')
            # Original reindexing fixture on its own admitted four-state carrier.
            original=native['paths1']
            recovered=native['recover'](native['fibers'](original,native['source']),native['source'])
            require(recovered==original and all(len(x)==1 for x in recovered),'reindexing changed paths')
            require(len(step(p,'R'))==2,'extension did not add edge')
            hostiles+=['self-composition-is-not-extension','reindexing-is-not-extension','LR-RL-history-erasure']
    paths=['research/nima/wg-path-composition-interval-contract.md',
           'research/nima/wg-path-composition-interval-proof.md',
           'research/nima/checkers/check_wg_path_composition_interval.py',
           'research/nima/checkers/check_indexed_path_synthesis.py',
           'research/nima/checkers/check_wg_interval_operation_bridge.py',
           'research/nima/nnmhv_coherence_paths.py']
    result={'schema':'marici.nima.wg-path-composition-interval.v1','passed':True,
        'scope':'WG-I5 selected line-path composition specialization; written all-n proof, exact finite regression, no autonomous scheduling or physical source selection.',
        'counts':counts,'hostiles':hostiles,'original_fixture_stdout':log.getvalue(),
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/nima/results/wg-path-composition-interval.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
