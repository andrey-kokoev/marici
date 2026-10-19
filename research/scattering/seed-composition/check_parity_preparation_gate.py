"""Positive forward preparation versus signed retained detail: scoped parity gate."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, mm, eye, rank, apply, transpose, encode
from check_retained_word_transport import RetainedSuccessorLedger
from check_controller_preparation_audit import audit as preparation_audit
from check_full_boundary_split import audit as full_audit
from check_graded_boundary_transport import add, scale

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/parity-preparation-gate.v1.json'


def minus(a,b):return add(a,scale(b,-1))
def nonnegative(a):return all(v>=0 for row in a for v in row)
def reflection_matrix(paths,edge_map):
    moved=[tuple(edge_map[e] for e in path) for path in paths]
    permutation=[paths.index(path) for path in moved]
    return [[F(i==permutation[j]) for j in range(len(paths))] for i in range(len(paths))]


def audit():
    full=full_audit();prep=preparation_audit();prior=incidence_audit()
    primitives=prior['primitive_order']
    packets=[(p['owner']+':'+''.join(p['edge']),*p['edge']) for p in primitives]
    ledger=RetainedSuccessorLedger(packets)
    edges=[(s,t,label) for label,s,t in packets]
    permutation=prep['symmetry']['primitive_permutations'][1]
    edge_map={e:edges[permutation[i]] for i,e in enumerate(edges)}
    stages=[];parent=ledger.root
    for depth in range(1,4):
        child=ledger.successor(parent)
        Jp=reflection_matrix(parent.paths,edge_map);Jc=reflection_matrix(child.paths,edge_map)
        L=[list(r) for r in child.step_lift];D=[list(r) for r in child.step_decoder]
        assert nonnegative(L) and nonnegative(D) and nonnegative(child.summary)
        assert mm(Jc,L)==mm(L,Jp) and mm(D,Jc)==mm(Jp,D)
        I=eye(len(child.paths));detail=minus(I,mm(L,D))
        even=scale(add(I,Jc),F(1,2));odd=scale(minus(I,Jc),F(1,2))
        assert mm(detail,detail)==detail and mm(detail,Jc)==mm(Jc,detail)
        assert any(v<0 for row in detail for v in row)
        er=rank(mm(detail,even));orr=rank(mm(detail,odd))
        assert er>0 and orr>0  # Detail is not an odd-parity selector.
        assert rank(mm(odd,L))>0  # Inherited odd inputs are killed by detail.
        assert mm(detail,mm(odd,L))==[[F(0)]*len(parent.paths) for _ in child.paths]
        # Exercise actual source API on every nonnegative coordinate input.
        witness=None
        for j in range(len(child.paths)):
            x=[F(i==j) for i in range(len(child.paths))]
            means,residual=ledger.split_payload(child,x)
            assert list(means)==apply(D,x) and list(residual)==apply(detail,x)
            assert [a+b for a,b in zip(apply(L,means),residual)]==x
            if any(v<0 for v in residual):witness={'slot':j,'means':means,'detail':residual}
        assert witness is not None
        stages.append({'word_length':child.word_length,'parent_slots':len(parent.paths),
                       'child_slots':len(child.paths),'detail_rank':rank(detail),
                       'even_detail_rank':er,'odd_detail_rank':orr,'signed_detail_witness':witness})
        parent=child

    # Source bilinear composition preserves the positive cone. Complete basis
    # products test every structurally allowed primitive-pair coefficient slot.
    root=ledger.root;first=ledger.successor(root)
    products=0
    for i in range(10):
        for j in range(10):
            x=[F(k==i) for k in range(10)];y=[F(k==j) for k in range(10)]
            values=ledger.compose_primitive_payloads(first,x,y)
            assert all(v>=0 for v in values)
            products+=1

    # Boundary parity alone is an orthogonal, reversible observer, even though
    # its further spectral restriction is generally oblique.
    perm=full['correlation_selector']['occurrence_permutation'];I=eye(12)
    J=[[F(i==perm[j]) for j in range(12)] for i in range(12)]
    even=scale(add(I,J),F(1,2));odd=scale(minus(I,J),F(1,2))
    assert mm(transpose(even),even)==even and mm(transpose(odd),odd)==odd
    assert add(mm(transpose(even),even),mm(transpose(odd),odd))==I
    x=I[0];ox=apply(odd,x);ex=apply(even,x)
    assert ox[0]==F(1,2) and ox[perm[0]]==-F(1,2)
    assert [a+b for a,b in zip(ox,ex)]==x
    # The API accepts signed data, but explicitly registers it as supplied.
    primitive_odd=apply(scale(minus(eye(10),reflection_matrix(root.paths,edge_map)),F(1,2)),eye(10)[0])
    payload=ledger.retain_payload(root,primitive_odd)
    assert payload.operation=='supplied' and any(v<0 for v in payload.values)

    dependencies=list(full['source_sha256'])+['research/scattering/seed-composition/check_parity_preparation_gate.py',
        'research/nima/checkers/retained_path_successor.py']
    return {
        'schema':'marici.scattering.parity-preparation-gate.v1',
        'status':'positive_forward_class_cannot_prepare_nonzero_odd_state_signed_detail_is_not_parity_preparation',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'positive_class':{'inputs':'nonnegative coefficient payloads only',
                          'operations':['successor copy','nonnegative incidence sums','fiber means','reindexing',
                                        'nonnegative supplied masks','bilinear retained concatenation'],
                          'invariant':'all outputs have nonnegative coefficients',
                          'odd_cone_intersection':'{0}: Jv=-v with J a permutation and v>=0 implies v=0',
                          'nonzero_odd_preparation_possible':False,
                          'scope':'no claim for signed inputs, signed controls, detail subtraction or all source operations'},
        'actual_source_checks':{'primitive_basis_products_tested':products,'retained_successor_stages':stages,
                                'detail_uses_subtraction':True,'detail_is_odd_selector':False,
                                'reflection_intertwines_successor_and_decoder':True,
                                'signed_odd_input_registration':payload.operation},
        'boundary_parity_observer':{'even_rank':rank(even),'odd_rank':rank(odd),
                                    'split_is_coordinate_counting_isometry':True,
                                    'reconstruction':'sum even and odd records',
                                    'basis_input':x,'odd_record':ox,'even_record':ex,
                                    'existing_source_stage_fibers_are_reflection_orbits':False},
        'boundary':{'all_signed_source_operations_excluded':False,'physical_probabilities_identified':False,
                    'coherent_parity_preparation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Construct a retained symmetry-orbit mean/detail adapter and test equivariance with source path concatenation; expose its required cross-word subtraction and distinguish an observer from an implemented preparation.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale parity-preparation receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: nonnegative forward transport cannot produce a nonzero odd-reflection payload.')
    print('PASS: actual signed mean/detail readouts retain both parities and do not implement odd preparation.')
    print('Boundary: signed supplied coefficients remain allowed; observer subtraction is not physical preparation.')


if __name__=='__main__':main()
