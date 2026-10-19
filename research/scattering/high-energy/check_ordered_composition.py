"""Exact H2: independently built Boolean-cube graph versus ordered operator products."""
import argparse
import json
from itertools import permutations
from pathlib import Path
import sympy as s
from high_energy_scattering_net import ROOT, HOME, digest
from check_local_switches import audit as local_audit, ARCHIVE

RESULT=HOME/'results/ordered-switch-composition.v1.json'


def audit():
    gates={};local=local_audit(gates)
    simp=lambda m:s.Matrix(m).applyfunc(lambda x:s.simplify(s.expand(x)))
    def eq(a,b):assert simp(a-b)==s.zeros(*a.shape)
    def witness(a,b):
        d=simp(a-b)
        for i in range(d.rows):
            for j in range(d.cols):
                if d[i,j]!=0:return {'row':i,'column':j,'exact_difference':str(d[i,j])}
        raise AssertionError('expected a nonzero operator defect')
    records=[]
    for sign,faces in gates.items():
        assert len(faces)==3
        Q=[s.SparseMatrix(q) for _,q in faces]
        # Graph construction uses only one-bit adjacency, never path permutations.
        V=s.MutableSparseMatrix(160,160,{})
        for target in range(8):
            for origin in range(8):
                diff=target^origin
                if diff not in (1,2,4):continue
                gate=Q[diff.bit_length()-1]
                for (i,j),value in gate.todok().items():V[20*target+i,20*origin+j]=value
        eq(V.H,V)
        # Matrix multiplication on the whole graph, restricted only at input/output.
        graph=simp((V[140:160,:]*V)*V[:,0:20])
        # Independently enumerate ordered products on the original C20 carrier.
        terms=[simp(Q[c]*Q[b]*Q[a]) for a,b,c in permutations(range(3))]
        summed=simp(sum(terms,s.zeros(20)));eq(graph,summed)
        small=2 if sign==1 else 3
        common=[2*small,2*small+1,2*(small+5),2*(small+5)+1]
        B=summed.extract(common,common)
        eq(B*B,s.Rational(4,9)*s.eye(4));assert s.trace(B)==0
        extended=s.zeros(20)
        for i,row in enumerate(common):
            for j,col in enumerate(common):extended[row,col]=B[i,j]
        eq(summed,extended)
        noncommuting=[{'pair':[a,b],'witness':witness(Q[a]*Q[b],Q[b]*Q[a])} for a,b in ((0,1),(0,2),(1,2))]
        controls={'six_copies_of_one_order':witness(summed,6*terms[0]),
                  'one_order_deleted':witness(summed,summed-terms[0]),
                  'selected_order_reversed':witness(terms[0],terms[-1])}
        records.append({'endpoint':sign,'face_bit_order':[name for name,_ in faces],'graph_dimension':160,
                        'input_output_dimension':20,'orders':6,'common_coordinates':common,
                        'common_block':[[str(x) for x in row] for row in B.tolist()],
                        'common_block_square':'(4/9)I4','common_block_trace':'0','complement_dimension':16,
                        'complement_operator':'zero','graph_minus_ordered_sum':'zero',
                        'noncommuting_pairs':noncommuting,'hostile_defects':controls})
        print('exact graph/path comparison at endpoint',sign,flush=True)
    sources=[Path(__file__),HOME/'check_local_switches.py',ARCHIVE,HOME/'pentachoron_open_product_flux_note.md']
    return {'schema':'marici.scattering.ordered-switch-composition.v1','status':'pass','sympy_version':s.__version__,
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},
            'local_identities_replayed':local['status']=='pass','endpoint_count':len(records),'records':records,
            'scope':'Third-order off-diagonal adjacency operator only; native evolution, contact coefficients, higher-order revisits and observed probabilities are not equated to this operator. No measurement of coherent path order.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale H2 receipt'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: H2 exact full-carrier graph/path equality, both endpoints; distinct orders remain distinct.')


if __name__=='__main__':main()
