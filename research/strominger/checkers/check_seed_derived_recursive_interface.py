"""Source-derived comparison versus forced recursive content generation.

Imports the existing six-arrow registry, not a completed graph. Tests a declared
uncoloured directed-incidence signature; ordered triangle roles are a hostile.
No native WG admission or execution-identity issuance is inferred.
"""
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from check_natural_tower_return import PACKETS


def compose(h,g):return tuple(h[g[i]] for i in range(len(g)))
def inverse(h):return tuple(h.index(i) for i in range(len(h)))
def move_edges(h,edges):return frozenset((h[s],h[t]) for s,t in edges)
def automorphisms(edges):
    return tuple(h for h in permutations(range(4)) if move_edges(h,edges)==edges)
def unique_nonidentity(edges):
    choices=[h for h in automorphisms(edges) if h!=tuple(range(4))]
    assert len(choices)==1
    return choices[0]


def main():
    names='ABCD';identity=tuple(range(4))
    registry={label:(names.index(s),names.index(t)) for label,s,t in PACKETS}
    edges=frozenset(registry.values())
    assert len(registry)==len(edges)==6
    assert set(registry)=={'AB','BC','CA','BA','AD','DB'}
    group=automorphisms(edges);sigma=unique_nonidentity(edges)
    assert group==(identity,(1,0,3,2)) and sigma==(1,0,3,2)
    assert compose(sigma,sigma)==identity
    transports=tuple(permutations(range(4)))
    # Check naturality over every labelled copy, not only seed automorphisms.
    for h in transports:
        target=move_edges(h,edges)
        assert unique_nonidentity(target)==compose(compose(h,sigma),inverse(h))
        for k in transports:
            assert move_edges(k,target)==move_edges(compose(k,h),edges)
            assert unique_nonidentity(move_edges(k,target))==compose(compose(k,unique_nonidentity(target)),inverse(k))
    # Explicit complete word comparison preserving endpoints, seams, all labels,
    # and positions. This maps descriptions; it issues no runtime occurrences.
    label_by_edge={edge:label for label,edge in registry.items()}
    label_swap={label:label_by_edge[(sigma[s],sigma[t])] for label,(s,t) in registry.items()}
    def move_word(word):return tuple(label_swap[label] for label in word)
    def valid(word):return all(registry[a][1]==registry[b][0] for a,b in zip(word,word[1:]))
    paths=[(label,) for label in registry]
    path_counts=[]
    for length in range(1,7):
        assert all(len(path)==length and valid(path) for path in paths)
        for path in paths:
            moved=move_word(path)
            assert valid(moved) and move_word(moved)==path
            assert registry[moved[0]][0]==sigma[registry[path[0]][0]]
            assert registry[moved[-1]][1]==sigma[registry[path[-1]][1]]
            for cut in range(1,length):
                assert move_word(path)==move_word(path[:cut])+move_word(path[cut:])
        path_counts.append(len(paths))
        paths=[path+(label,) for path in paths for label in registry
               if registry[path[-1]][1]==registry[label][0]]
    # Two equally natural retention policies. Group coordinate 0=id, 1=sigma.
    # Their compatibility/recovery laws do not choose between their fiber sizes.
    levels=[]
    for n in range(4):
        forced=[(p,(1,)*n) for p in range(4)]
        full=[(p,a) for p in range(4) for a in product(range(2),repeat=n)]
        def action(h,state):
            p,syms=state
            # C2 conjugation is trivial. Identity/nonidentity roles are natural
            # across relabelled copies by the preceding 24-copy checks.
            return h[p],syms
        parent_forced={(p,(1,)*(n-1)) for p in range(4)} if n else set()
        parent_full={(p,a) for p in range(4) for a in product(range(2),repeat=n-1)} if n else set()
        for carrier in (forced,full):
            for z in carrier:
                assert action(sigma,action(sigma,z))==z
                for h in group:
                    assert action(h,action(sigma,z))==action(sigma,action(h,z))
                    assert (action(h,z)[0],action(h,z)[1]+(1,))==action(h,(z[0],z[1]+(1,)))
                if n:assert (z[0],z[1][:-1]) in (parent_forced if carrier is forced else parent_full)
        forced_orbits={min(action(h,z) for h in group) for z in forced}
        full_orbits={min(action(h,z) for h in group) for z in full}
        assert len(forced)==4 and len(forced_orbits)==2
        assert len(full)==4*2**n and len(full_orbits)==2*2**n
        # Distinct full witness sequences can have identical composite action.
        # Evaluating a sequence is an explicitly lossy boundary observation.
        composite_fibers={}
        for p,syms in full:
            composite_fibers.setdefault((p,sum(syms)%2),[]).append((p,syms))
        if n:
            assert len(composite_fibers)==8
            assert {len(fiber) for fiber in composite_fibers.values()}=={2**(n-1)}
        levels.append({'depth':n,'composite_observation_count':len(composite_fibers),
                       'composite_observation_fiber_sizes':sorted({len(fiber) for fiber in composite_fibers.values()}),
                       'forced_retained_states':len(forced),
                       'forced_source_orbits':len(forced_orbits),'full_retained_states':len(full),
                       'full_source_orbits':len(full_orbits)})
    # Automorphism is not a primitive transition: C->D and D->C are absent.
    missing=[names[p]+names[sigma[p]] for p in range(4) if (p,sigma[p]) not in edges]
    assert missing==['CD','DC']
    # Return on vertices is not equality of retained path records: AB BA
    # returns A but remains a two-occurrence word, not an empty identity word.
    return_word=('AB','BA')
    assert valid(return_word) and registry['AB'][0]==registry['BA'][1]
    assert len(return_word)==2 and return_word!=()
    # Signature hostile: distinguishing the two triangle roles removes sigma
    # from FIXED-source automorphisms, though transported comparisons still exist.
    triangle_roles=[frozenset(registry[label] for label in tri)
                    for tri in [('AB','BC','CA'),('AD','DB','BA')]]
    role_preserving=[h for h in group if all(move_edges(h,role)==role for role in triangle_roles)]
    assert role_preserving==[identity]
    assert move_edges(sigma,triangle_roles[0])==triangle_roles[1]
    # A unique symmetry does not select a tour: on the existing two cyclic
    # full-support tours it acts freely.
    def normalize(word):
        k=word.index('AB');return word[k:]+word[:k]
    tours=[('AB',)+rest for rest in permutations(tuple(label for label in registry if label!='AB'))
           if valid(('AB',)+rest) and registry[rest[-1]][1]==registry['AB'][0]]
    assert len(tours)==2
    assert all(normalize(move_word(t))!=t for t in tours)
    assert {normalize(move_word(t)) for t in tours}==set(tours)
    # Recover the existing unique reversible endpoint routing, without confusing
    # its conditional cycle-cover objective with a source-preserving symmetry.
    routings=[r for r in permutations(range(4)) if all((p,r[p]) in edges for p in range(4))]
    assert len(routings)==1
    routing=routings[0]
    assert compose(routing,routing)==sigma and routing not in group
    assert inverse(routing) not in routings
    sources=[Path(__file__).resolve(),ROOT/'research/nima/checkers/check_natural_tower_return.py',
             ROOT/'research/nima/checkers/check_seed_typed_execution.py',
             ROOT/'research/nima/seed-spectral-port-symmetry-comparison.md',
             ROOT/'research/nima/seed-section-comparison-boundary-audit.md']
    result={'status':'pass','signature':'uncoloured directed incidence, no fixed triangle-role order',
            'source_packets':PACKETS,'automorphisms':group,'unique_nonidentity':sigma,
            'relabellings_checked':24,'relabelling_composition_pairs_checked':576,
            'edge_label_transport':label_swap,'typed_path_counts_lengths_1_to_6':path_counts,
            'recursive_policies':levels,'forced_projection_fiber_size':1,'full_projection_fiber_size':2,
            'missing_primitive_sigma_transitions':missing,'fixed_triangle_role_automorphism_count':len(role_preserving),
            'cyclic_full_support_tours':tours,'invariant_single_tour_count':0,
            'unique_bijective_endpoint_routing':routing,'routing_square_is_sigma':True,
            'routing_is_source_automorphism':False,
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            'verdict':'Unique natural comparison recovered. Coherent recursion has at least two source-natural retention policies with inequivalent fibers. Full native WG admission and a constructor-selection principle remain unproved.'}
    out=ROOT/'research/strominger/results/seed-derived-recursive-interface.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','unique_nonidentity','typed_path_counts_lengths_1_to_6',
          'forced_projection_fiber_size','full_projection_fiber_size','missing_primitive_sigma_transitions','invariant_single_tour_count')}))


if __name__=='__main__':main()
