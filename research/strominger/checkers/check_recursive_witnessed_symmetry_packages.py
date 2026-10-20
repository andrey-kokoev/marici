"""Exact finite model of recursive source-derived symmetry packages.

C_n=P x Aut(P)^n, with transported source action on the WHOLE retained package.
This uses inherited symmetry lifts, not arbitrary permutations of flattened
higher records. Recursion depth has no temporal or spatial-dimension semantics.
"""
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def compose(f,g):return tuple(f[g[i]] for i in range(len(g)))
def inverse(f):return tuple(f.index(i) for i in range(len(f)))


def main():
    P=tuple(range(4));group=list(permutations(P));index={g:i for i,g in enumerate(group)}
    unit=index[P];inverses=[index[inverse(g)] for g in group]
    multiplication=[[index[compose(g,h)] for h in group] for g in group]
    conjugation=[[index[compose(compose(h,g),inverse(h))] for g in group] for h in group]
    def act(h,state):
        p,syms=state
        return (group[h][p],tuple(conjugation[h][a] for a in syms))
    def project(state):return state[0],state[1][:-1]
    def section(state):return state[0],state[1]+(unit,)
    # Elementary operation certificates determine all recursively lifted actions.
    for h,k,g in product(range(24),repeat=3):
        assert conjugation[multiplication[h][k]][g]==conjugation[h][conjugation[k][g]]
    levels=[]
    all_states=[]
    for n in range(3):
        states=[(p,syms) for p in P for syms in product(range(24),repeat=n)]
        all_states.append(states)
        assert len(states)==4*24**n
        for state in states:
            assert act(unit,state)==state
            for h in range(24):
                assert act(inverses[h],act(h,state))==state
                assert section(act(h,state))==act(h,section(state))
                if n:assert project(act(h,state))==act(h,project(state))
        representatives={min(act(h,state) for h in range(24)) for state in states}
        # Independent Burnside count, retaining point-fixing and conjugation.
        fixed=[]
        for h in range(24):
            points=sum(group[h][p]==p for p in P)
            centralizer=sum(conjugation[h][a]==a for a in range(24))
            fixed.append(points*centralizer**n)
        assert sum(fixed)%24==0
        assert sum(fixed)//24==len(representatives)
        assert len(representatives)==(4*24**n+12*4**n+8*3**n)//24
        if n:
            for parent in all_states[n-1]:
                fiber=[(parent[0],parent[1]+(a,)) for a in range(24)]
                assert len(set(fiber))==24 and all(project(x)==parent for x in fiber)
                assert project(section(parent))==parent
        levels.append({'depth':n,'retained_states':len(states),
                       'relabeling_orbit_count':len(representatives),
                       'representatives':[[p,list(syms)] for p,syms in sorted(representatives)]})
    # Explicit full group-law check on the whole first-level package, beyond
    # mere endpoint action. Uniform extension follows coordinatewise above.
    for state in all_states[1]:
        for h,k in product(range(24),repeat=2):
            assert act(h,act(k,state))==act(multiplication[h][k],state)
    # Once a witness is RETAINED, its last symmetry supplies a natural,
    # potentially nonidentity operation on the entire package. This is not
    # source-free selection of a first nonidentity symmetry.
    retained_actions=[]
    for n in (1,2):
        changed=0
        def forward(state):return act(state[1][-1],state)
        def backward(state):return act(inverses[state[1][-1]],state)
        for state in all_states[n]:
            out=forward(state)
            assert out[1][-1]==state[1][-1]
            assert backward(out)==state and forward(backward(state))==state
            changed+=out!=state
            for h in range(24):
                assert forward(act(h,state))==act(h,forward(state))
        assert changed>0
        retained_actions.append({'depth':n,'nonidentity_state_images':changed,
                                 'two_sided_recovery_and_equivariance':True})
    # Canonical relabeling-equivariant selection s:P->Aut(P): its value at 0
    # must centralize the stabilizer of 0. Only identity survives in S4.
    stabilizer=[h for h in range(24) if group[h][0]==0]
    possible=[a for a in range(24) if all(conjugation[h][a]==a for h in stabilizer)]
    assert possible==[unit]
    # A chosen transposition does supply a nonidentity witness, but its failure
    # to be invariant exposes the extra marking rather than hiding it.
    transposition=index[(1,0,2,3)]
    hostile=next(h for h in stabilizer if conjugation[h][transposition]!=transposition)
    assert group[hostile][0]==0
    # Forgetting symmetry while retaining p loses distinguishable full records.
    assert (0,(unit,))!=(0,(transposition,))
    assert project((0,(unit,)))==project((0,(transposition,)))
    # Flattening and taking every permutation of the 96 states would admit
    # maps that do not preserve even the original source projection.
    x=(0,(unit,));y=(1,(unit,));z=(0,(transposition,))
    def hostile_flat_swap(state):return y if state==x else x if state==y else state
    assert x[0]==z[0] and hostile_flat_swap(x)[0]!=hostile_flat_swap(z)[0]
    # Hence no base map can make this particular 96-state permutation commute
    # with projection. It is not an inherited structured symmetry.
    orbit_details=[]
    for p,syms in sorted({min(act(h,state) for h in range(24)) for state in all_states[1]}):
        state=(p,syms);orbit={act(h,state) for h in range(24)}
        stab=[h for h in range(24) if act(h,state)==state]
        assert len(orbit)*len(stab)==24
        g=group[syms[0]]
        cycle=[];cursor=p
        while cursor not in cycle:cycle.append(cursor);cursor=g[cursor]
        assert cursor==p
        unseen=set(P)-set(cycle);other=[]
        while unseen:
            start=min(unseen);c=[];cursor=start
            while cursor not in c:c.append(cursor);cursor=g[cursor]
            unseen-=set(c);other.append(len(c))
        orbit_details.append({'representative':[p,list(syms)],
            'marked_cycle_length':len(cycle),'other_cycle_lengths':sorted(other),
            'orbit_size':len(orbit),'stabilizer_size':len(stab)})
    assert len(orbit_details)==7
    sources=[BASE/'anchored-boundary-meta-coherence-v1.md',
             ROOT/'research/nima/whole-package-generators.md',
             ROOT/'research/nima/composable-witness-specialization.md',
             Path(__file__).resolve()]
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result={'status':'pass','source_size':4,'symmetry_group_size':24,
        'construction':'C_n=P x Aut(P)^n with diagonal transported source action',
        'levels':levels,'first_level_orbits':orbit_details,
        'operations_from_retained_witnesses':retained_actions,
        'projection_fiber_size':24,'source_equivariant_selector_options_at_mark_0':possible,
        'identity_index':unit,
        'nonidentity_selector_hostile':{'chosen_symmetry':transposition,'source_fixing_relabeling':hostile,
                                       'conjugated_symmetry':conjugation[hostile][transposition]},
        'flattened_automorphism_violates_source_projection':True,
        'source_hashes':hashes,
        'scope':'Exact finite set/group action model and written uniform coordinatewise laws. Not a universal WG law, maximal structured automorphism classification, physical state count, arbitrary higher filler or source-free selector.'}
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    (BASE/'results/recursive-witnessed-symmetry-packages.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','state_counts':[x['retained_states'] for x in levels],
                      'orbit_counts':[x['relabeling_orbit_count'] for x in levels],
                      'equivariant_selector_on_bare_source':'identity_only','projection_fiber_size':24,
                      'nonidentity_retained_action_counts':[x['nonidentity_state_images'] for x in retained_actions]}))


if __name__=='__main__':main()
