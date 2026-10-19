"""Uniform NCT compiler; exact bounded checks of the frozen finite claim."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json, random
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/finite-reversible-witnessed-realization.v1.json'
NOTE='research/conjecture_net/FINITE-REVERSIBLE-WITNESSED-REALIZATION.md'
OUT='research/voevodsky/results/finite-reversible-witnessed-realization-v1.json'

def require(ok,msg):
    if not ok:raise ValueError(msg)
def run(word,state):
    for gate in word:
        *controls,target=gate
        if all(state&(1<<c) for c in controls):state^=1<<target
    return state
def mcx(controls,target,work):
    d=len(controls)
    if d<=2:return [tuple(controls)+(target,)]
    require(len(work)>=d-2,'clean work bound')
    compute=[(controls[0],controls[1],work[0])]
    for i in range(1,d-2):compute.append((work[i-1],controls[i+1],work[i]))
    return compute+[(work[d-3],controls[-1],target)]+list(reversed(compute))
def adjacent(k,a,b):
    changed=a^b;require(changed and changed&(changed-1)==0,'adjacent edge')
    target=changed.bit_length()-1;controls=[i for i in range(k) if i!=target]
    neg=[(i,) for i in controls if not(a&(1<<i))]
    return neg+mcx(controls,target,list(range(k,k+max(k-3,0))))+list(reversed(neg))
def transposition(k,a,b):
    if a==b:return []
    path=[a]
    for bit in range(k):
        if (a^b)&(1<<bit):path.append(path[-1]^(1<<bit))
    edges=list(zip(path,path[1:]));word=[]
    for edge in edges+list(reversed(edges[:-1])):word+=adjacent(k,*edge)
    return word
def compile_perm(k,f):
    require(tuple(sorted(f))==tuple(range(1<<k)),'bijection specification')
    current=list(range(1<<k));word=[]
    for x in range(1<<k):
        u,v=current[x],f[x]
        if u==v:continue
        word+=transposition(k,u,v)
        current=[v if y==u else u if y==v else y for y in current]
    require(tuple(current)==tuple(f),'transposition decomposition')
    return word
def inverse_table(f):
    g=[0]*len(f)
    for x,y in enumerate(f):g[y]=x
    return tuple(g)
def graph_words(k,word):
    def move(g,offset):return tuple(i+offset if i<k else 2*k+i-k for i in g)
    ac=[(i,k+i) for i in range(k)]+[move(g,k) for g in word]
    bc=[(k+i,i) for i in range(k)]+[move(g,0) for g in reversed(word)]
    return ac,bc

def main():
    rng=random.Random(314159);cases=[];input_checks=0;max_gates={};graphs=0
    for k in range(1,6):
        size=1<<k
        if k<=2:targets=list(permutations(range(size)))
        else:
            targets=[tuple(range(size)),tuple(reversed(range(size))),tuple((x+1)%size for x in range(size))]
            for _ in range(12):
                f=list(range(size));rng.shuffle(f);targets.append(tuple(f))
        for f in targets:
            word=compile_perm(k,f);inv=list(reversed(word));g=inverse_table(f);ac,bc=graph_words(k,word)
            # Gate signature is the whole frozen primitive set, not an oracle.
            require(all(1<=len(gate)<=3 and len(set(gate))==len(gate) and
                        all(0<=i<k+max(k-3,0) for i in gate) for gate in word),'source gate typing')
            bound=(size-1)*(2*k-1)*(2*(k-1)+(1 if k<=3 else 2*k-5))
            require(len(word)<=bound,'uniform gate budget')
            continuation=tuple((y+1)%size for y in range(size));hword=compile_perm(k,continuation)
            composed=tuple(continuation[f[x]] for x in range(size));composite_word=compile_perm(k,composed)
            for x in range(size):
                y=run(word,x);require(y==f[x],'full-input forward and clean workspace')
                require(run(inv,y)==x and run(word,run(inv,x))==x,'both inverse laws')
                require(run(inv,x)==g[x],'inverse specification')
                graph=run(ac,x);require(graph==x+(f[x]<<k),'graph ac and clean work')
                require(run(bc,f[x]<<k)==graph,'common rooted graph')
                require(run(list(reversed(ac)),graph)==x,'graph ca recovery')
                require(run(list(reversed(bc)),graph)==f[x]<<k,'graph cb recovery')
                require(run(inv,run(list(reversed(bc)),graph)>>k)==x,'A triangle return')
                graph_b=run(bc,x<<k)
                require(run(word,run(list(reversed(ac)),graph_b))==x,'B triangle return')
                require(run(word+hword,x)==run(composite_word,x)==composed[x],'composition square')
                # Equality of successor states implies preservation of EVERY predicate.
                require(run(hword,y)==continuation[f[x]],'continuation transport')
                input_checks+=1;graphs+=1
            cases.append(dict(k=k,target=list(f),gates=len(word)))
            max_gates[k]=max(max_gates.get(k,0),len(word))
    # Extensional erasure hostile: same full action, different words and marks of history.
    empty=[];two_not=[(0,),(0,)]
    require(empty!=two_not and all(run(empty,x)==run(two_not,x) for x in (0,1)),'history-erasure counterexample')
    # Deliberate incomplete clean-work sequence, three positive controls.
    dirty=mcx([0,1,2],3,[4])[:-1]
    require(run(dirty,7)&(1<<4),'unclean-work mutation detected')
    mutant=compile_perm(2,(3,1,2,0));require(mutant,'nonempty mutation case')
    require(any(run(mutant[:-1],x)!=(3,1,2,0)[x] for x in range(4)),'gate-deletion mutation detected')
    paths=[DEF,NOTE,Path(__file__).relative_to(ROOT).as_posix()]
    result=dict(schema='marici.finite-reversible-witnessed-realization-validation.v1',passed=True,
                bounded_cases=len(cases),full_input_checks=input_checks,graph_checks=graphs,
                exhaustive_permutations_at_k=[1,2],sampled_k=[3,4,5],max_gate_count_by_k=max_gates,
                uniform_proof='written Gray transposition and clean-work chain argument in guide',
                higher_scope='Set-level extensional equality; no nontrivial homotopy witness universality claimed',
                output_only_history_decoder_refuted=True,mutation_controls_passed=True,
                all_k_kernel_proof=False,shared_outcome_admission=False,physical_execution=False,
                source_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},cases=cases)
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','cases')},indent=2))
if __name__=='__main__':main()
