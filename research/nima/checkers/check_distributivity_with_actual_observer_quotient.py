"""Typed distributivity through the actual seven-reading -> vacuum-pair quotient.

Exact finite-domain matrix identities plus explicit AST normalization routes.
No general rewrite-confluence or arbitrary-source reconstruction claim.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


ast=load('ast_rules',ROOT/'checkers/check_typed_ast_distributivity.py');p=ast.p;a=p.a
mat=load('matrix_tools',ROOT/'checkers/check_residual_tower_of_towers.py')
reader=load('reading_contract',ROOT.parent/'voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py')
mm,inv,eye=mat.mm,mat.inv,mat.eye

def transpose(A):return list(map(list,zip(*A)))
def rank(A):return len(a.rref(A,len(A[0]))[1]) if A else 0
def add(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def subtract(A,B):return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]
def mv(A,x):return a.apply(A,x)
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rules(x):
    yield from ast.local_rules(x)
    if x[0]=='H':yield 'expand_H_definition',p.plus(p.leaf('Q',x[1]),p.scale(-1,p.leaf('P',x[1])))


def successors(x):
    for address,node in ast.nodes(x):
        for rule,replacement in rules(node):
            nxt=ast.replace(x,address,replacement)
            if nxt!=x:yield rule,address,nxt


def source_vector(x):
    source=ast.value(x);keys=[next(iter(a.paths(v,0,3))) for v in a.basis(8)]
    assert set(source)<=set(keys)
    return [source.get(key,Q(0)) for key in keys]


def main():
    counts={'reading_basis_checks':0,'ast_steps':0,'ast_reading_row_checks':0,
            'canonical_roundtrips':0,'fiber_comparisons':0,'depth_squares':0,'depth_transition_squares':0,'wire_roundtrips':0}
    shapes=[tuple(('e',u,v,0) for u,v in seams) for seams in reader.SEAMS]
    def actual_readings(source):return [Q(a.f['vacuum_rows'](0,63,source,len(shape)).get(shape,0)) for shape in shapes]
    reading_matrix=transpose([actual_readings(a.paths(v,0,3)) for v in a.basis(8)])
    counts['reading_basis_checks']=56
    # Path coordinates u_b=a_b, b=1..7; a_0=-sum u_b. Interaction coordinates m_1..m_7.
    D=[[-Q(1)]*7]+eye(7)
    Z=[[Q(b&t==t) for b in range(1,8)] for t in range(1,8)];X=inv(Z)
    assert mm(Z,X)==mm(X,Z)==eye(7)
    decoder=[[Q(c) for c in row] for row in reader.INVERSE]
    E=mm(reading_matrix,D);Em=mm(E,X)
    assert mm(reading_matrix,decoder)==eye(7) and mm(decoder,E)==D
    P=eye(7)[:2];W=mm(P,E);Wm=mm(W,X)
    S=[[Q(c) for c in row] for row in ((1,0),(0,1),(0,0),(1,1),(0,0),(-1,-1),(0,0))]
    N=[[Q(i==j+2) for j in range(5)] for i in range(7)]
    R=[[Q(c) for c in row] for row in ((0,0,1,0,0,0,0),(-1,-1,0,1,0,0,0),
                                    (0,0,0,0,1,0,0),(1,1,0,0,0,1,0),(0,0,0,0,0,0,1))]
    assert mm(P,S)==eye(2) and mm(R,N)==eye(5)
    assert mm(P,N)==[[0]*5 for _ in range(2)] and mm(R,S)==[[0]*2 for _ in range(5)]
    assert add(mm(S,P),mm(N,R))==eye(7)
    # Reconstruction squares and residual values agree on the ENTIRE domain.
    assert mm(E,X)==Em and mm(W,X)==Wm and mm(mm(R,E),X)==mm(R,Em)
    K=mm(inv(E),N);Km=mm(Z,K)
    assert rank(transpose(K))==5 and mm(W,K)==mm(Wm,Km)==[[0]*5 for _ in range(2)]
    kernel_flags=[]
    for order in (1,2,3):
        low=[eye(7)[t-1] for t in range(1,8) if t.bit_count()<order]
        fiber=a.solve(Wm+low,[0]*(2+len(low)),7)
        kernel_flags.append(len(fiber[1]))
    assert kernel_flags==[5,2,0]
    # These five actual sources explain the kernel and its inherited filtration.
    adapted=[]
    for t in (1,2,4,5,6):
        m=[Q(0)]*7;m[t-1]=1;m[2]-=(-1)**t.bit_count()
        u=mv(X,m);source=a.paths(mv(D,u),0,3)
        assert mv(W,u)==[0,0]
        for depth in range(t.bit_count()):assert not a.f['vacuum_rows'](0,63,source,depth)
        assert a.f['vacuum_rows'](0,63,source,t.bit_count())
        adapted.append(u)
    assert rank(adapted)==5
    # Intersect coarse rows with the available jets; do not reuse the pair at every depth.
    coarse_dims=[];coarse_rows={};jet_rows={};coarse_from_jet={}
    for depth in range(4):
        J=[t for t in range(1,8) if t.bit_count()<=depth]
        jet_rows[depth]=[Z[t-1] for t in J]
        coarse_dims.append(rank(W)+rank(jet_rows[depth])-rank(W+jet_rows[depth]))
        coarse_rows[depth]=W if depth==3 else [[x+y for x,y in zip(*W)]] if depth==2 else []
        coarse_from_jet[depth]=Wm if depth==3 else [[Q((-1)**t.bit_count()) for t in J]] if depth==2 else []
        assert mm(coarse_from_jet[depth],jet_rows[depth])==coarse_rows[depth]
        # Both presentation routes reach the same physical coarse rows.
        assert mm(coarse_rows[depth],X)==mm(coarse_from_jet[depth],mm(jet_rows[depth],X))
        counts['depth_squares']+=1
    assert coarse_dims==[0,0,1,2]
    assert mm([[Q(1),Q(1)]],W)==coarse_rows[2]
    for high in range(4):
        high_labels=[t for t in range(1,8) if t.bit_count()<=high]
        for low in range(high+1):
            low_labels=[t for t in range(1,8) if t.bit_count()<=low]
            jet_transition=[[Q(t==u) for u in high_labels] for t in low_labels]
            coarse_transition=(eye(coarse_dims[high]) if low==high else [[Q(1),Q(1)]] if (high,low)==(3,2) else [])
            assert mm(coarse_from_jet[low],jet_transition)==mm(coarse_transition,coarse_from_jet[high])
            assert mm(jet_transition,jet_rows[high])==jet_rows[low]
            counts['depth_transition_squares']+=1
    fiber_point_matrix=mm(inv(E),S)
    assert mm(W,fiber_point_matrix)==eye(2)
    for c in ([Q(0),Q(0)],[Q(1),Q(0)],[Q(1),Q(-1)],[Q(2,3),Q(-5,7)]):
        path_fiber=a.solve(W,c,7);mode_fiber=a.solve(Wm,c,7)
        via_modes=a.image(X,mode_fiber)
        via_residual=(mv(inv(E),mv(S,c)),transpose(K))
        assert a.canonical(path_fiber,7)==a.canonical(via_modes,7)==a.canonical(via_residual,7)
        assert len(path_fiber[1])==5
        counts['fiber_comparisons']+=1
    section_id='pair12-and-top-filtered-linear-section-v1'
    residual_ids=['r'+str(i) for i in range(5)]
    def pack(y):
        return json.loads(json.dumps({'schema':'presentation-bridge-residual-v1','model_sha256':reader.MODEL_SHA256,
            'section':section_id,'visible':dict(zip(reader.IDS[:2],map(str,mv(P,y)))),
            'residual':dict(zip(residual_ids,map(str,mv(R,y))))}))
    def unpack(envelope):
        if set(envelope)!={'schema','model_sha256','section','visible','residual'}:raise ValueError('fields')
        if envelope['schema']!='presentation-bridge-residual-v1' or envelope['model_sha256']!=reader.MODEL_SHA256 or envelope['section']!=section_id:raise ValueError('contract')
        if set(envelope['visible'])!=set(reader.IDS[:2]) or set(envelope['residual'])!=set(residual_ids):raise ValueError('missing coordinates')
        c=[reader.rational(envelope['visible'][key]) for key in reader.IDS[:2]]
        r=[reader.rational(envelope['residual'][key]) for key in residual_ids]
        y=[x+z for x,z in zip(mv(S,c),mv(N,r))]
        payload={'schema':'seven-dimensional-ideal-readings-v1','model_sha256':reader.MODEL_SHA256,
                 'readings':dict(zip(reader.IDS,map(str,y)))}
        decoded=reader.reconstruct(payload)
        return list(map(Q,decoded['path_coefficients']))
    saved_trace=None
    def normalize(root,inside_first,keep_trace=False):
        nonlocal saved_trace
        current=root;trace=[]
        for _ in range(2000):
            options=list(successors(current))
            if not options:
                if keep_trace:saved_trace={'root':root,'steps':trace,'terminal':current}
                return current
            rule,address,nxt=sorted(options,key=lambda item:((-len(item[1]) if inside_first else len(item[1])),item[0],item[1]))[0]
            assert nxt in [ast.replace(current,address,repl) for name,repl in rules(ast.at(current,address)) if name==rule]
            assert p.span(nxt)==p.span(current)==(0,3)
            assert ast.value(current)==ast.value(nxt) and ast.interactions(current)==ast.interactions(nxt)
            before=actual_readings(ast.value(current));after=actual_readings(ast.value(nxt))
            assert before==after
            assert mv(P,before)==mv(P,after) and mv(R,before)==mv(R,after)
            counts['ast_steps']+=1;counts['ast_reading_row_checks']+=7
            if keep_trace:trace.append({'rule':rule,'address':address,'before_sha256':digest(current),'after_sha256':digest(nxt)})
            current=nxt
        raise RuntimeError('normalization bound exceeded')
    samples=a.basis(7)+adapted+[[Q(0)]*7,[Q(i) for i in range(1,8)],mv(X,[Q(int(i==6)) for i in range(7)])]
    for index,u in enumerate(samples):
        coefficients=mv(D,u);m=mv(Z,u)
        factor=p.expression([Q(0)]+m,3,0,'H')
        path=p.expression(coefficients,3,0,'Q')
        roots=[normalize(factor,False,index==len(samples)-2),normalize(factor,True),normalize(path,False)]
        assert len({ast.formal_normal_form(root) for root in roots})==1
        assert all(source_vector(root)==coefficients for root in roots)
        # Reverse via coordinates, not via archived before/after trees.
        recovered_m=a.moments(source_vector(roots[0]))
        assert recovered_m==[Q(0)]+m and p.expression(recovered_m,3,0,'H')==factor
        y=actual_readings(p.expand(factor))
        assert y==mv(E,u)==mv(Em,m)
        wire=pack(y);assert unpack(wire)==coefficients
        counts['canonical_roundtrips']+=1;counts['wire_roundtrips']+=1
    # Replay the selected AST witness using only rules and addresses from its initial tree.
    received=json.loads(json.dumps(saved_trace));cursor=ast.freeze(received['root'])
    for step in received['steps']:
        assert digest(cursor)==step['before_sha256']
        address=tuple(step['address'])
        replacements=[r for name,r in rules(ast.at(cursor,address)) if name==step['rule']]
        assert len(replacements)==1
        cursor=ast.replace(cursor,address,replacements[0]);assert digest(cursor)==step['after_sha256']
    assert cursor==ast.freeze(received['terminal'])
    # Conditional reachable history: append P-Q twice, independently checked in the source.
    H=[Q(1),Q(-1)];T10=a.action(H,1);T21=a.action(H,2)[1:];T20=mm(T21,T10)
    assert mm(W,T20)==eye(2)
    for c in a.basis(2):
        expected=a.f['multiply'](a.f['multiply'](a.paths(c,0,1),a.paths(H,1,1)),a.paths(H,2,1))
        assert a.paths(mv(D,mv(T20,c)),0,3)==expected
    assert rank(transpose(K)+transpose(T20))==7
    history_section=mm(E,T20);history_residual=mm(R,history_section)
    assert history_residual==[[0,0],[-1,-1],[0,0],[1,1],[0,0]]
    assert subtract(history_section,S)==mm(N,history_residual)
    history_digest=digest({'reading_model':reader.MODEL_SHA256,'T20':mat.wire_matrix(T20),
                           'meaning':'externally admitted history appending P-Q in the second and third blocks'})
    def reverse_on_history(c,admitted_history=None):
        if admitted_history!=history_digest:raise ValueError('history assumption not admitted')
        return mv(D,mv(T20,c))
    for c in ([Q(1),Q(0)],[Q(0),Q(1)],[Q(2,3),Q(-5,7)]):
        reached=reverse_on_history(c,history_digest)
        assert mv(reading_matrix,reached)==mv(history_section,c)
        assert unpack(pack(mv(history_section,c)))==reached
    # Ambient ambiguity remains real, even where the constrained history has none.
    hidden=transpose(K)[0]
    assert mv(W,hidden)==[0,0] and any(hidden)
    assert mv(R,mv(E,hidden))!=[0]*5
    pair=[Q(1),Q(0)];history_source=reverse_on_history(pair,history_digest)
    ambient_alternative=[x+y for x,y in zip(history_source,mv(D,hidden))]
    assert mv(P,mv(reading_matrix,ambient_alternative))==pair and ambient_alternative!=history_source
    assert mv(decoder,mv(S,pair))!=history_source # Zero residual under THIS section is wrong.
    rejected=[]
    bad=pack(mv(E,hidden));del bad['residual']['r0']
    try:unpack(bad)
    except ValueError:rejected.append('missing_residual')
    else:raise AssertionError('missing residual accepted')
    bad=pack(mv(E,hidden));bad['section']='untracked-history-section'
    try:unpack(bad)
    except ValueError:rejected.append('untracked_section')
    else:raise AssertionError('untracked section accepted')
    try:reverse_on_history(pair)
    except ValueError:rejected.append('unadmitted_history_inverse')
    else:raise AssertionError('history inferred from pair alone')
    top=[Q(int(t==7)) for t in range(1,8)]
    assert mv(mm(jet_rows[2],X),top)==[0]*6 and mv(Wm,top)==[-1,1]
    for row in Wm:assert a.solve(transpose(mm(jet_rows[2],X)),row,6) is None
    report={'schema':'distributivity-with-actual-observer-quotient-v1','passed':True,'checks':counts,
        'reading_model_sha256':reader.MODEL_SHA256,'coarse_dimensions_by_jet_depth':coarse_dims,
        'kernel_inherited_dimensions':kernel_flags,'kernel_in_path_coordinates':mat.wire_matrix(K),
        'kernel_in_interaction_coordinates':mat.wire_matrix(Km),
        'all_fibers':{'path_point_matrix':mat.wire_matrix(fiber_point_matrix),
                      'formula':'For any vacuum pair c, the entire path-coordinate fiber is point_matrix*c + K*r, r in Q^5; regrouping sends it to Z*point_matrix*c + Z*K*r.'},
        'reading_anchor_path':mat.wire_matrix(E),'reading_anchor_interaction':mat.wire_matrix(Em),
        'residual_extraction':mat.wire_matrix(R),'section':section_id,'section_matrix':mat.wire_matrix(S),
        'source_bridge':{'regroup':mat.wire_matrix(Z),'expand':mat.wire_matrix(X)},
        'history':{'admission_digest':history_digest,'source_map':mat.wire_matrix(T20),
                   'forced_residual':mat.wire_matrix(history_residual),'kernel_intersection_dimension':0,
                   'admission':'external source-support and dynamics assumption, not inferred from readings or a digest'},
        'ast_rewrite_witness':saved_trace,'negative_controls_rejected':rejected,
        'additional_obstructions':{'individual_vacuum_rows_do_not_descend_to_order_two':True,
             'ambient_pair_has_distinct_sources':True,'zero_residual_section_is_not_the_history_source':True},
        'meaning':'Canonical expansion/regrouping intertwines the actual readings, noninvertible quotient, residual reconstruction, affine fibers and depth-compatible coarse tower. History-relative inversion is explicitly conditional.',
        'scope':'Matrix identities cover the declared seven-dimensional rational ideal slice. AST routes are tested on its basis, kernel generators and additional fixtures, not a general confluence proof. No physical acquisition, arbitrary source support or global bimodule splitting is certified.'}
    out=ROOT/'results/distributivity-with-actual-observer-quotient.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('passed','checks','coarse_dimensions_by_jet_depth','kernel_inherited_dimensions','negative_controls_rejected','additional_obstructions','scope')},indent=2))


if __name__=='__main__':main()
