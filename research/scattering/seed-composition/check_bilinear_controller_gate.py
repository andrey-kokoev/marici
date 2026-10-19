"""Source bilinear controller gate: two products are necessary; coarse loss persists.

Exact finite claims only. Two retained products do not authorize a physical
coherent sum, and a context-to-control preparation is still supplied.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, apply, eye, encode
from check_controller_preparation_audit import audit as controller_audit
from check_retained_word_transport import RetainedSuccessorLedger

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/bilinear-controller-gate.v1.json'


def audit():
    previous=controller_audit()
    source=json.loads((BASE/'three-vertex-candidate.v1.json').read_text(encoding='utf-8'))
    packets=[(owner+':'+a+b,a,b) for owner,cycle in source['primitive_cycles'].items() for a,b in zip(cycle,cycle[1:])]
    edges=[(a,b) for _,a,b in packets]
    ledger=RetainedSuccessorLedger(packets)
    paths=tuple(((a,b,label),) for label,a,b in packets)
    ids={label:i for i,(label,_,_) in enumerate(packets)}
    N=[[F(b==c) for _,b in edges] for c,_ in edges]
    assert rank(N)==7

    def compose(x,y):
        left=ledger.retain_path_payload(paths,tuple(map(F,x)))
        right=ledger.retain_path_payload(paths,tuple(map(F,y)))
        product=ledger.compose_payloads(left,right)
        assert ledger.deconstruct_payload(product)[0]==(left,right)
        return product

    def summary(product):
        out=[F(0)]*10
        for word,value in zip(product.paths,product.values):out[ids[word[-1][2]]]+=value
        return out

    # Fresh 100 basis-pair checks certify the bilinear identity on all rational
    # inputs; its coefficients also define the same identity after scalar extension.
    I=eye(10)
    for x in I:
        for y in I:
            product=compose(x,y)
            assert len(product.paths)==16
            assert summary(product)==[a*b for a,b in zip(y,apply(N,x))]

    # The smallest actual source minor occurs at B. Both composites are in the
    # supplied dictionary: AB then BC (AC), CB then BA (CA).
    first=compose(I[0],I[1])
    second=compose(I[8],I[9])
    assert first.paths==second.paths
    summed=[a+b for a,b in zip(first.values,second.values)]
    expected=[F(tuple(ids[e[2]] for e in word) in [(0,1),(8,9)]) for word in first.paths]
    assert summed==expected
    block=[[F(1),F(0)],[F(0),F(1)]]
    assert rank(block)==2
    # A single B(x,y) would require x_AB*y_BC=x_CB*y_BA=1 and
    # x_AB*y_BA=x_CB*y_BC=0, contradicting its zero 2x2 determinant.
    assert block[0][0]*block[1][1]-block[0][1]*block[1][0]==1

    # Extend the same source-cut theorem to all 18 supplied contexts. Different
    # vertices are separate composability blocks, NOT a global dense outer product.
    contexts=previous['controller']['contexts']
    vertices=sorted({a for a,_ in edges})
    profiles=[[F(0)]*10 for _ in range(2)]
    branch_of={}
    blocks={}
    for vertex in vertices:
        outgoing=[i for i,(a,_) in enumerate(edges) if a==vertex]
        for color,edge in enumerate(outgoing):
            profiles[color][edge]=1;branch_of[edge]=color
        rows=[c for c in contexts if c['vertex']==vertex]
        matrix=[[F(c['expected_primitive']==edge) for edge in outgoing] for c in rows]
        blocks[vertex]={'states':[c['state'] for c in rows],'outgoing':outgoing,'rank':rank(matrix)}
    assert {v:b['rank'] for v,b in blocks.items()}=={'A':2,'B':2,'C':2,'D':1,'Dp':1,'E':1,'Ep':1}
    controls=[[F(branch_of[c['expected_primitive']]==color) for c in contexts] for color in range(2)]
    for c in contexts:
        for edge in c['available_primitives']:
            reconstructed=sum(controls[color][c['state']]*profiles[color][edge] for color in range(2))
            assert reconstructed==F(edge==c['expected_primitive'])
    # Generic nonzero context amplitudes do not change the two-product bound.
    amplitudes=[F(i+1) for i in range(18)]
    for c in contexts:
        for edge in c['available_primitives']:
            assert sum(amplitudes[c['state']]*controls[k][c['state']]*profiles[k][edge] for k in range(2))==amplitudes[c['state']]*F(edge==c['expected_primitive'])

    # Final-occurrence aggregation remains blind to a needed source direction.
    w=[F(i==0)-F(i==8) for i in range(10)]  # AB-CB: both enter B
    assert apply(N,w)==[0]*10
    Prep=previous['preparation']['counting_metric_projector']
    prepared=apply(Prep,w)
    assert any(prepared) and prepared==[F(1,2),0,-F(1,2),0,0,F(1,2),0,0,-F(1,2),0]
    raw=compose(w,[F(1)]*10)
    assert any(raw.values) and summary(raw)==[0]*10
    for right in I:
        assert summary(compose(w,right))==[0]*10
    # Left/context conditioning can expose the lost direction, but it is an
    # additional operation and demonstrates why a right operand alone is not enough.
    conditioned=compose([w[i] if i==0 else F(0) for i in range(10)],I[1])
    assert summary(conditioned)==I[1]

    dependencies=list(previous['source_sha256'])+[
        'research/scattering/seed-composition/check_bilinear_controller_gate.py',
        'research/nima/bilinear-branch-preparation-synthesis.md',
        'research/nima/retained-interaction-end-to-end-audit.md',
        'research/nima/retained-proton-operation.md',
        'research/voevodsky/shape-interaction-finite-operator-audit.md']
    return {
        'schema':'marici.scattering.bilinear-controller-gate.v1',
        'status':'single_product_controller_obstructed_two_product_retained_recipe_and_coarse_loss_certified',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'source_bilinear_identity':{'formula':'aggregate B(x,y) = diag(y) N x','basis_pairs_checked':100,
                                    'primitive_word_count':16,'N_rank':7,'N':N},
        'controller':{'smallest_minor':{'vertex':'B','rows':['AB','CB'],'columns':['BC','BA'],
                                       'desired_matrix':block,'determinant':1},
                      'context_blocks':blocks,'minimum_products_for_full_nonzero_context_table':2,
                      'right_profiles':profiles,'left_context_controls':controls,
                      'actual_source_products_constructed_for_B_minor':2,
                      'sum_readout_checked_not_registered_as_source_preparation':True,
                      'contexts_or_control_amplitudes_derived':False},
        'coarse_obstruction':{'input_witness':w,'primitive_summary':apply(N,w),
                              'required_prepared_witness':prepared,
                              'retained_word_values':list(raw.values),
                              'all_right_inputs_remain_blind':True,
                              'scope':'same left input, bilinear endpoint composition, final-occurrence aggregation; not a no-go for retained or context-conditioned operations'},
        'source_search':[
            {'path':'research/nima/bilinear-branch-preparation-synthesis.md','disposition':'supplies rank-one cut law and exact branch detail; input coefficients remain supplied'},
            {'path':'research/nima/retained-interaction-end-to-end-audit.md','disposition':'conditional kick/drift action and bookkeeping; source control and native clock attachment remain open'},
            {'path':'research/nima/retained-proton-operation.md','disposition':'bound proton execution only; electron exchange and contact adapter explicitly unbound'},
            {'path':'research/voevodsky/shape-interaction-finite-operator-audit.md','disposition':'finite toy isometries/propagators; native phase and retained-intermediate adapter remain open'}],
        'boundary':{'physical_control_interaction_identified':False,'coherent_two_branch_preparation_derived':False,
                    'independent_photons_constructed':False,'physical_annihilation_derived':False,
                    'ratio_372_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Derive two context-conditioned retained product channels, including their selection/relative phase and preparation residual; do not aggregate away the AB-CB witness before control.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:
            raise SystemExit('FAIL: missing or stale bilinear-controller receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: 100 source basis-pair identities; one-product controller fails rank-2 minor; two retained products suffice algebraically.')
    print('PASS: AB-CB is invisible after every right-weighted final summary but needed by preparation.')
    print('Boundary: two-channel control and coherent preparation remain supplied, not a physical interaction theorem.')


if __name__=='__main__':main()
