"""H3 exact retained encoder audit; see RETAINED-ENCODER-PROOF.md for both-pose proof."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile
import sympy as s
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_exit_gate_bundle.zip'
PROOF=HOME/'RETAINED-ENCODER-PROOF.md'
RESULT=HOME/'results/retained-encoder.v1.json'


def audit():
    historical_validate()
    with ZipFile(ARCHIVE) as z:
        raw=z.read('pentachoron_exit_gate_results.json')
        matrices=json.loads(raw)['exact_matrices']
    mats={k:s.Matrix(v) for k,v in matrices.items()}
    simp=lambda m:s.Matrix(m).applyfunc(lambda x:s.simplify(s.expand(x)))
    def eq(a,b):assert simp(a-b)==s.zeros(*a.shape)
    T=mats['T'];assert T.shape==(20,20)
    rebuilt=s.zeros(20);links={}
    for base in (0,5):
        for c in range(5):
            i,j=base+c,base+(c+1)%5
            V=T[2*j:2*j+2,2*i:2*i+2]
            eq(V.H*V,s.eye(2));rebuilt[2*j:2*j+2,2*i:2*i+2]=V;links[i,j]=V
    eq(T,rebuilt)
    records=[]
    for small in (2,3):
        rows=[];pairs=[]
        for (i,j),V in links.items():
            if (i in (small,small+5))!=(j in (small,small+5)):
                d=s.zeros(2,20);d[:,2*i:2*i+2]=-V;d[:,2*j:2*j+2]=s.eye(2)
                rows.append(d);pairs.append((i,j))
        assert pairs==[(small-1,small),(small,small+1),(small+4,small+5),(small+5,small+6)]
        D=s.Matrix.vstack(*rows);M=simp(D*D.H)
        eq((M-s.eye(8))*(M-3*s.eye(8)),s.zeros(8))
        P1=simp((3*s.eye(8)-M)/2);P3=simp((M-s.eye(8))/2)
        assert s.trace(P1)==s.trace(P3)==4
        R=simp(P1+P3/s.sqrt(3));eq(R*M*R,s.eye(8))
        W=simp(R*D);N=simp(s.eye(20)-W.H*W)
        eq(W*W.H,s.eye(8));eq(W*N,s.zeros(8,20));eq(N*N,N)
        eq(W.H*M*W,D.H*D)
        U=s.BlockMatrix([[N,W.H],[W,s.zeros(8)]]).as_explicit()
        eq(U.H,U);eq(U*U,s.eye(28))
        if small==2:
            for name,value in [('D',D),('M',M),('W',W),('N',N),('U',U)]:eq(value,mats[name])
        records.append({'small_cell':small,'crossing_links':pairs,'memory_spectrum':{'1':4,'3':4},'encoder_dimension':28,'exact_identities':'pass','frame':'archived positive endpoint frame; negative-pose transport covered by universal unitary-link proof'})
        print('exact encoder, small cell',small,flush=True)
    # Exact scalar polynomial reduction verifies the functional-calculus formulas.
    x=s.Symbol('x');minimal=(x-1)*(x-3);p1=(3-x)/2;p3=(x-1)/2;r=p1+p3/s.sqrt(3)
    for polynomial in (p1*p1-p1,p3*p3-p3,p1*p3,r*x*r-1):
        assert s.simplify(s.rem(s.expand(polynomial),minimal,x))==0
    # Independent outgoing Hamiltonian still fails similarity, not just this encoder.
    traces={k:str(s.trace(mats[k])) for k in ('HL','HR')}
    assert traces=={'HL':'136','HR':'120'}
    eq(mats['HL'].H,mats['HL']);eq(mats['HR'].H,mats['HR'])
    sources=[ARCHIVE,PROOF,Path(__file__),HOME/'pentachoron_open_product_flux_note.md']
    return {'schema':'marici.scattering.retained-encoder.v1','status':'pass','sympy_version':s.__version__,
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},
            'unitary_cycle_links_checked':len(links),'records':records,
            'continuation':'Universal norm-convergent matrix exponential argument for H_post=U H_pre U*, as proved in RETAINED-ENCODER-PROOF.md; no finite-time sampling.',
            'both_endpoint_coverage':'Arbitrary unitary-link path theorem plus source unitary frame transport; negative endpoint geometry not numerically or symbolically replayed by this checker.',
            'independent_native_traces':traces,'H_post_equals_H_F':False,'physical_explanation_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale H3 receipt'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: H3 retained encoder and explicitly transported continuation; native H_F identification remains refuted.')


if __name__=='__main__':main()
