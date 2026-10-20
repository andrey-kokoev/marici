"""Finite groupoid/control model for anchored boundary re-presentations.

Not a proof of univalence, arbitrary higher fillers, or generation of a source
from nothing. The common source and its two coordinate fields are supplied.
"""
from itertools import permutations, product, combinations
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def compose(f,g):return tuple(f[g[i]] for i in range(len(g)))
def inv(f):return tuple(f.index(i) for i in range(len(f)))


def main():
    P=tuple(range(4));identity=P
    anchors=list(permutations(P))
    presentations=[(label,e) for label in range(3) for e in anchors]
    def comparison(a,b):return compose(b[1],inv(a[1]))
    assert len(presentations)==72
    comparisons={}
    for i,a in enumerate(presentations):
        for j,b in enumerate(presentations):
            h=comparison(a,b)
            assert compose(h,a[1])==b[1]
            assert compose(comparison(b,a),h)==identity
            # Exhaust all maps admitted as equivalences: anchor compatibility
            # leaves exactly one, not merely one selected convenient map.
            possible=[candidate for candidate in anchors if compose(candidate,a[1])==b[1]]
            assert possible==[h]
            comparisons[i,j]=h
    triangles=0
    for i,j,k in product(range(72),repeat=3):
        assert compose(comparisons[j,k],comparisons[i,j])==comparisons[i,k]
        triangles+=1
    # Total element groupoid: arrows preserve normalized underlying content.
    components={p:[] for p in P}
    for i,(_,e) in enumerate(presentations):
        for x in P:
            components[inv(e)[x]].append([i,x])
    assert [len(components[p]) for p in P]==[72]*4
    for p,component in components.items():
        for (i,x),(j,y) in product(component,repeat=2):
            assert comparisons[i,j][x]==y
    for p,q in combinations(P,2):
        for (i,x),(j,y) in product(components[p],components[q]):
            assert comparisons[i,j][x]!=y
    # Same displayed state after forgetting the anchor, different source values.
    swap=(1,0,2,3)
    assert inv(identity)[0]==0 and inv(swap)[0]==1
    # Unanchored copy groupoid has all 24 self-bijections, not only identity.
    assert len(anchors)==24 and swap!=identity
    assert compose(swap,swap)==identity
    # A concrete field-cut lattice on the supplied source P={0,1}^2.
    cuts=[(),(0,),(1,),(0,1)]
    bits={p:(p//2,p%2) for p in P}
    def shadow(cut,p):return tuple(bits[p][i] for i in cut)
    def graph(cut,p):return (p,shadow(cut,p))
    def recover_graph(row):return row[0]
    def chart_map(cut,row):return graph(cut,recover_graph(row))
    lattice=[]
    for a,b in product(cuts,repeat=2):
        meet=tuple(sorted(set(a)&set(b)));join=tuple(sorted(set(a)|set(b)))
        assert meet in cuts and join in cuts
        lattice.append({'left':a,'right':b,'meet':meet,'join':join})
        for p in P:
            assert chart_map(a,chart_map(b,graph(a,p)))==graph(a,p)
    for a,b,c,p in product(cuts,cuts,cuts,P):
        assert chart_map(c,chart_map(b,graph(a,p)))==chart_map(c,graph(a,p))
    fibers=[]
    for cut in cuts:
        images=sorted({shadow(cut,p) for p in P})
        sizes=[sum(shadow(cut,p)==x for p in P) for x in images]
        assert set(sizes)=={2**(2-len(cut))}
        fibers.append({'cut':cut,'shadow_count':len(images),'fiber_sizes':sizes,
                       'complete_graph_count':len({graph(cut,p) for p in P})})
    # Independent input/output chart changes preserve a NONINVERTIBLE process.
    # Do not mistake equivalent function presentations for reversible operations.
    process=(0,1,0,1)
    assert len(set(process))==2
    for e,f in product(anchors,repeat=2):
        presented=compose(f,compose(process,inv(e)))
        assert compose(inv(f),compose(presented,e))==process
        assert len(set(presented))==2
    # Retaining a source record really changes that operation's output package.
    recorded=tuple((process[p],p) for p in P)
    assert len(set(recorded))==4
    assert tuple(row[1] for row in recorded)==P
    # Mere reverse syntax cannot invert the erased two-valued output.
    assert process[0]==process[2] and 0!=2
    # Higher packaging can retain an entire interface, not only its endpoint.
    sample=(presentations[0],presentations[-1],comparisons[0,71],comparisons[71,0])
    wrapped={'boundary':'complete_interface','payload':sample}
    assert wrapped['payload']==sample
    # The wrapper is retention, not a claim to synthesize arbitrary witnesses.
    sources=[ROOT/'research/voevodsky/a-common-graph-presentation-generates-all-opposite-edges-at-fixed-realization-dimension.md',
             ROOT/'research/voevodsky/closure-four-presentations-hott-proof.md',
             ROOT/'research/voevodsky/observer-relative-computation/anchored-dependent-records.md',
             ROOT/'research/nima/typed-generator-coherence.md',
             Path(__file__).resolve()]
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result={'status':'pass','source_states':4,'anchored_presentations':72,
        'unique_anchor_preserving_comparisons':72**2,'triangle_identities':triangles,
        'anchored_presentation_groupoid_components':1,
        'anchored_presentation_automorphisms_per_object':1,
        'total_presented_content_components':4,
        'presentations_per_content_component':72,
        'unanchored_automorphisms_per_copy':24,
        'anchor_forgetting_hostile':{'same_displayed_value':0,'normalized_values':[0,1]},
        'cut_lattice':lattice,'boundary_fibers':fibers,
        'independent_input_output_presentations_tested':24**2,
        'noninvertible_process_rank':2,'record_retaining_output_cardinality':4,
        'source_hashes':hashes,
        'scope':'Finite groupoid and set-fiber test with a supplied source and field-cut lattice. General higher coherence requires the written common-anchor argument and adopted path/univalence framework; no arbitrary WG filler or source-creation theorem.'}
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    (BASE/'results/anchored-boundary-presentation-synthesis.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','anchored_presentations','triangle_identities','total_presented_content_components','unanchored_automorphisms_per_copy']}))


if __name__=='__main__':main()
