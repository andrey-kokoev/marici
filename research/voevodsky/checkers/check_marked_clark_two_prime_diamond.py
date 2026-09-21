"""Two-prime marked Clark recorder: exact ranks, seam transport, Green mate.

Analytical inputs are the existing injective shell-tail feature map and unitary
cut reassembly. This checker audits their finite incidence and pairing algebra.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]


def main():
    # Minimal common refinement: [2,4], [4,6], [6,12] in exponential labels.
    A=sp.Matrix([1,0,0]); B=sp.Matrix([0,1,0]); D=sp.Matrix([0,0,1])
    windows=((A,B+D),(A+B,D))
    masks=list(product((0,1),repeat=2))
    keys=[()]+[(i,) for i in range(3)]+list(product(range(3),repeat=2))
    idx={word:i for i,word in enumerate(keys)}
    columns=[]
    for route in windows:
        for mask in masks:
            terms={():sp.Integer(1)}
            for marked,v in zip(mask,route):
                if marked:
                    terms={word+(i,):coefficient*v[i] for word,coefficient in terms.items() for i in range(3) if v[i]}
            columns.append(sp.Matrix([terms.get(word,0) for word in keys]))
    M=sp.Matrix.hstack(*columns)
    k0=sp.Matrix([1,0,0,0,-1,0,0,0])
    k1=sp.Matrix([0,1,1,0,0,-1,-1,0])
    assert M.rank()==6 and M*k0==sp.zeros(13,1) and M*k1==sp.zeros(13,1)
    assert sp.Matrix.hstack(k0,k1).rank()==2
    lift=sp.zeros(8,2)
    for route in range(2):
        for m in range(4):lift[4*route+m,route]=1
    unmarked=M*lift
    assert unmarked.rank()==2
    difference=unmarked[:,0]-unmarked[:,1]
    assert difference[idx[(0,1)]]==1 and difference[idx[(1,2)]]==-1
    assert sum(v!=0 for v in difference)==2

    # Retaining the typed middle cut keeps the two arrow records separately.
    one_event=[()]+[(i,) for i in range(3)]
    cut_keys=[(middle,left,right) for middle in (4,6) for left in one_event for right in one_event]
    cut_index={key:i for i,key in enumerate(cut_keys)}
    cut=sp.zeros(32,8)
    for route,window_pair in enumerate(windows):
        middle=(4,6)[route]
        for m,mask in enumerate(masks):
            pieces=[]
            for marked,v in zip(mask,window_pair):
                pieces.append({(i,):v[i] for i in range(3) if v[i]} if marked else {():1})
            for left,x in pieces[0].items():
                for right,y in pieces[1].items():
                    cut[cut_index[(middle,left,right)],4*route+m]=x*y
    rejoin=sp.zeros(13,32)
    for j,(middle,left,right) in enumerate(cut_keys):
        rejoin[idx[left+right],j]=1
    assert cut.rank()==8 and rejoin*cut==M
    assert cut*k0!=sp.zeros(32,1) and cut*k1!=sp.zeros(32,1)

    # Cut fibers list the remaining tail first, then the stored past.
    def reassembly(cut):
        order=list(range(cut,3))+list(range(cut))
        R=sp.zeros(3)
        for j,i in enumerate(order):R[i,j]=1
        return R
    transport=lambda a,b:reassembly(b).T*reassembly(a)
    assert transport(1,3)*transport(0,1)==transport(2,3)*transport(0,2)==transport(0,3)
    for a,b in ((0,1),(1,3),(0,2),(2,3)):
        T=transport(a,b)
        assert T.T*T==sp.eye(3)

    # Four-port Clark signed form on tensor histories of degree <=2.
    C=sp.Matrix([[0,0,-1,1],[0,0,-1,1],[-1,-1,0,0],[1,1,0,0]])/2
    tau=sp.Rational(1,2)
    words=[()]+[(i,) for i in range(4)]+list(product(range(4),repeat=2))
    wi={word:i for i,word in enumerate(words)}
    J=sp.diag(sp.ones(1),tau**2*C,tau**4*sp.kronecker_product(C,C))
    # An independent complex feature tests conjugation as well as signs.
    feature=sp.Matrix([1+sp.I,2-sp.I,-1+2*sp.I,3])
    creation=sp.zeros(21);mate=sp.zeros(21)
    Cfeature=C*feature
    for word in words:
        if len(word)<2:
            for j in range(4):
                creation[wi[word+(j,)],wi[word]]=feature[j]
                mate[wi[word],wi[word+(j,)]]=tau**2*sp.conjugate(Cfeature[j])
    assert creation.conjugate().T*J==J*mate
    assert creation*mate!=sp.eye(21)
    # The underlying Hilbert adjoint has feature, not C*feature, contraction.
    hilbert=sp.diag(sp.ones(1),tau**2*sp.eye(4),tau**4*sp.eye(16))
    hilbert_adjoint=hilbert.inv()*creation.conjugate().T*hilbert
    assert hilbert_adjoint!=mate

    result={
        'schema':'marici.voevodsky.marked-clark-two-prime-diamond.v1',
        'passed':True,
        'source_routes':[[2,4,12],[2,6,12]],
        'minimal_shell_endpoints':[2,4,6,12],
        'marked_path_order':[[route,list(mask)] for route in range(2) for mask in masks],
        'marked_observation_rank':6,
        'marked_kernel_basis':[[int(x) for x in k0],[int(x) for x in k1]],
        'unmarked_lift_rank':2,
        'route_difference':'e_A tensor e_B - e_B tensor e_C',
        'seam_transport_composes_exactly':True,
        'recording_green_mate':'tau^2 times right annihilation with C times the emitted feature',
        'green_mate_is_inverse':False,
        'terminal_marked_faithfulness':False,
        'typed_middle_cut_rank':8,
        'rejoining_typed_cut_equals_terminal_recorder':True,
        'typed_middle_cut_faithful_on_all_eight_marked_paths':True,
        'scope':'Fixed prepared forcing and added linear event recorder. No physical memory implementation or full stable-cut faithfulness is asserted.',
    }
    out=ROOT/'research/voevodsky/results/marked-clark-two-prime-diamond.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
