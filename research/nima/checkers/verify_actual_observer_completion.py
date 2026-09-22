"""Recheck the full finite constraint presentation against the source recorder.

Uses no generic numerical calibration. Verifies null-basis completeness,
all ideal-product generators, evaluation entries and the top-rank certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,combinations
from collections import defaultdict,Counter
import importlib.util,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('source',ROOT.parent/'voevodsky/certificates/verify_filtered_obstruction.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
import sympy as S


def clean(v):return {k:c for k,c in v.items() if c}
def axpy(v,w,c):
    for k,x in w.items():v[k]=v.get(k,Q(0))+c*x
    for k in list(v):
        if not v[k]:del v[k]
def readcol(col,parse=Q):
    result={i:parse(c) for i,c in col};assert len(result)==len(col)
    return result

def windows_polynomial(poly):
    out=Counter()
    for ((a,b),(c,d)),v in poly.items():
        for x,sg in ((b,1),(a,-1)):
            for y,tg in ((d,1),(c,-1)):
                if x and y:out[tuple(sorted((x,y)))]+=v*sg*tg
    return clean(out)


def main():
    path=ROOT/'results/actual-observer-full-finite-presentation.json.gz'
    with gzip.open(path,'rt',encoding='utf-8') as stream:data=json.load(stream)
    for name,sha in data['inputs'].items():assert hashlib.sha256((ROOT/'results'/name).read_bytes()).hexdigest()==sha
    base=json.loads((ROOT/'results/actual-private-core-with-original-cubic.json').read_text())
    union=json.loads((ROOT/'results/actual-retained-cubic-observer-union.json').read_text())
    assert data['source_generator_count']==51550 and data['ambient_rows']==3591
    corners={};sources=[];source_corners=[];free={};grades=[]
    for raw in data['source_corners']:
        a,b=raw['corner'];assert 0<=a<=b<64 and a&b==a and (a^b).bit_count()>=2
        events=[i for i in range(6) if (a^b)&(1<<i)]
        expected=[]
        for w in permutations(events):
            for degree in range(min(2,len(w))+1):
                for kept in combinations(range(len(w)),degree):expected.append((w,tuple(int(i in kept) for i in range(len(w)))))
        paths=[(tuple(w),tuple(m)) for w,m in raw['paths']];assert paths==expected
        rank=s.rank([s.record(a,*p) for p in paths]);assert rank==raw['recorder_rank']
        cols=[readcol(col) for col in raw['ideal_basis_columns']]
        assert len(cols)==len(paths)-rank and len(set(raw['free_path_indices']))==len(cols)
        assert raw['generator_offset']==len(sources)
        for pivot,col in zip(raw['free_path_indices'],cols):
            assert col[pivot]==1 and set(col)&set(raw['free_path_indices'])=={pivot}
            source={paths[i]:v for i,v in col.items()}
            assert not s.rho_column(a,source)
            degree=sum(paths[pivot][1]);assert all(sum(m)==degree for w,m in source)
            gid=len(sources);free[a,b,paths[pivot]]=gid
            sources.append(source);source_corners.append((a,b));grades.append(degree)
        corners[a,b]=(raw['generator_offset'],len(cols))
    assert len(corners)==473 and len(sources)==data['source_generator_count']
    print('verified complete source null bases',flush=True)
    def coordinates(a,b,source):return {free[a,b,p]:v for p,v in source.items() if (a,b,p) in free and v}
    assert len(set(data['coefficient_atoms']))==len(data['coefficient_atoms'])
    exprs=[{data['coefficient_atoms'][i]:Q(v) for i,v in expr} for expr in data['expressions']]
    assert all(len(poly)==len(raw) for poly,raw in zip(exprs,data['expressions']))
    # Independently reconstruct coefficient functionals from the owning row files.
    bycorner=defaultdict(lambda:defaultdict(list));row_count=0
    mapping={'1':{'1':Q(1)},'-rho':{'rho':Q(-1)},'-sigma':{'sigma':Q(-1)},'rho*sigma':{'rho*sigma':Q(1)}}
    def insert(corner,terms):
        nonlocal row_count
        for p,coefficient in terms.items():bycorner[corner][p].append((row_count,coefficient))
        row_count+=1
    for row in base['rows']:
        insert(tuple(row['corner_masks']),{(tuple(t['word']),tuple(t['marks'])):mapping[t['coefficient']] for t in row['terms']})
    for frame in union['frames']:
        for row in frame['rows']:
            terms={}
            for t in row['terms']:
                value={};w=tuple(map(tuple,t['windows']))
                for j,c in enumerate(t['component_coefficients']):
                    if not c:continue
                    if frame['family']=='two_private' or (frame['family']=='matched_memory' and j==0):
                        assert len(frame['denominators'][j])==1
                        normalizer=frame['denominators'][j][0]
                        assert tuple(map(tuple,normalizer['windows']))==w and normalizer['coefficient']==1
                        axpy(value,{'1':Q(1),'rho':Q(-1),'sigma':Q(-1),'rho*sigma':Q(1)} if j==0 else {'rho':Q(-1)},Q(c))
                    else:
                        atom=frame['family']+':'+str(j)+':'+','.join(str(x) for edge in w for x in edge)
                        axpy(value,{atom:Q(1)},Q(c))
                terms[tuple(t['word']),tuple(t['marks'])]=value
            insert(tuple(row['corner_masks']),terms)
    assert row_count==3591
    for gid,(source,corner) in enumerate(zip(sources,source_corners)):
        result=defaultdict(dict)
        for p,v in source.items():
            for row,poly in bycorner[corner].get(p,()):axpy(result[row],poly,v)
        expected={row:poly for row,poly in result.items() if poly}
        actual={row:exprs[expr] for row,expr in data['G0_evaluation_columns'][gid]}
        assert len(actual)==len(data['G0_evaluation_columns'][gid]) and actual==expected
    print('verified all calibrated evaluation columns',flush=True)
    J1=[readcol(col) for col in data['J1_I_squared_columns']]
    actual_products=set()
    assert len(data['J1_source_product_witnesses'])==len(J1)
    for col,witness in zip(J1,data['J1_source_product_witnesses']):
        left,right,den=witness;factor=Q(den)
        a,c=source_corners[left];cc,b=source_corners[right];assert c==cc and factor
        product_source=s.multiply(sources[left],sources[right])
        coords=coordinates(a,b,product_source)
        assert {gid:v/factor for gid,v in coords.items()}==col
        actual_products.add(tuple(sorted(col.items())))
    assert len(actual_products)==len(J1)==24550
    count=0
    for a,b in corners:
        if (a^b).bit_count()<4:continue
        for c in range(64):
            if (a,c) not in corners or (c,b) not in corners:continue
            lo,ln=corners[a,c];ro,rn=corners[c,b]
            for i in range(lo,lo+ln):
                for j in range(ro,ro+rn):
                    if grades[i]+grades[j]>2:continue
                    coords=coordinates(a,b,s.multiply(sources[i],sources[j]));count+=1
                    if coords:
                        factor=coords[min(coords)]
                        assert tuple(sorted((gid,v/factor) for gid,v in coords.items())) in actual_products
    assert count==25940
    print('verified complete I-squared generation',flush=True)
    J2=[readcol(col) for col in data['J2_I_cubed_columns']]
    assert len(J2)==len(data['J2_source_product_witnesses'])==630
    J21=[readcol(col) for col in data['J21_F2_to_F1_columns']]
    assert len(J21)==len(J2)
    for target,col in zip(J2,J21):
        result={}
        for index,c in col.items():axpy(result,J1[index],c)
        assert result==target
    full_monos={}
    for i,row in enumerate(base['rows']):
        if row['corner_masks']==[0,63] and len(row['terms'])==1:
            term=row['terms'][0];assert term['coefficient']=='1'
            full_monos[tuple(term['word']),tuple(term['marks'])]=i
    assert len(full_monos)==270
    p0=((0,1,2,3,4,5),(1,0,1,0,0,0));px=((0,2,1,3,4,5),(1,0,1,0,0,0))
    rho,sigma=S.symbols('rho sigma');S0=(1-rho)*(1-sigma);Sx=-rho
    original=base['rows'][base['seed_indices']['original_cubic']]['terms']
    pivots=set();top_checks=0;cube_products=set()
    for col,witness in zip(J2,data['J2_source_product_witnesses']):
        pairs=witness['pairs'];kinds=witness['kinds']
        assert len(pairs)==len(kinds)==3 and all(len(pair)==2 and pair==sorted(pair) for pair in pairs)
        assert sorted(e for pair in pairs for e in pair)==list(range(6))
        assert all(kind in (0,1) for kind in kinds) and sum(kinds)<=2
        key=(tuple(map(tuple,pairs)),tuple(kinds));assert key not in cube_products;cube_products.add(key)
        source={((),()):Q(1)}
        for pair,kind in zip(witness['pairs'],witness['kinds']):source=s.multiply(source,s.relation(pair,kind))
        assert coordinates(0,63,source)==col
        top0,topx=source.get(p0,0),source.get(px,0)
        value=sum(S.sympify(t['coefficient'])*source.get((tuple(t['word']),tuple(t['marks'])),0) for t in original)
        assert S.cancel(value-S0*top0-Sx*topx)==0
        if sum(witness['kinds'])==2:
            nz=[i for p,i in full_monos.items() if source.get(p,0)]
            assert len(nz)==1 and nz[0] not in pivots;pivots.add(nz[0])
        else:assert not any(source.get(p,0) for p in full_monos)
        for frame in union['frames']:
            raw=[Counter(),Counter()]
            for term in frame['rows'][frame['seed_row']]['terms']:
                c=source.get((tuple(term['word']),tuple(term['marks'])),0)
                for j,v in enumerate(term['component_coefficients']):raw[j][tuple(map(tuple,term['windows']))]+=c*v
            for j,target in enumerate((top0,topx)):
                expected={tuple(map(tuple,t['windows'])):Q(t['coefficient'])*target for t in frame['denominators'][j]}
                assert windows_polynomial(raw[j])==windows_polynomial(expected)
                top_checks+=1
    assert len(pivots)==270 and len(cube_products)==630
    H=[readcol(col,S.sympify) for col in data['old_projection_columns']]
    def heval(col):
        out=[S.Integer(0)]*9
        for gid,c in col.items():
            for i,v in H[gid].items():out[i]+=S.sympify(c)*v
        return [S.cancel(v) for v in out]
    for gid,col in enumerate(data['G0_evaluation_columns']):
        ambient={row:exprs[expr] for row,expr in col};expected={}
        for i,row,factor in base['projection_to_O2']:
            if row in ambient:
                v=S.cancel(S.sympify(factor)*sum(S.Rational(c.numerator,c.denominator)*S.sympify(atom) for atom,c in ambient[row].items()))
                if v!=0:expected[i]=v
        assert H[gid]==expected
    for j,col in enumerate(data['old_source_lift_columns']):assert heval(readcol(col,S.sympify))==[S.Integer(i==j) for i in range(9)]
    pivot=data['kernel_F1_old_row'];L1=readcol(data['kernel_F1_lift'],S.sympify)
    assert heval(L1)==[S.Integer(i==pivot) for i in range(9)]
    v2=s.multiply(s.relation((0,1),1),s.relation((2,3),0));v2c=coordinates(0,15,v2)
    factor=heval(v2c)[pivot]
    assert all(S.cancel(L1.get(gid,0)-S.sympify(v)/factor)==0 for gid,v in v2c.items()) and set(L1)==set(v2c)
    for col,value in zip(J1,data['kernel_F1_old_values']):
        assert heval(col)==[S.sympify(value) if i==pivot else S.Integer(0) for i in range(9)]
    assert all(heval(col)==[0]*9 for col in J2)
    # The unfiltered right inverse must NOT be used for the inherited K1 flag.
    unit_rows=[]
    for row in base['rows']:
        if row['corner_masks']==[0,15] and len(row['terms'])==1:
            term=row['terms'][0]
            if term['coefficient']=='1' and sum(term['marks'])==1:
                unit_rows.append((tuple(term['word']),tuple(term['marks'])))
    corner_products=[col for col in J1 if col and source_corners[next(iter(col))]==(0,15) and grades[next(iter(col))]==1]
    source_rank=s.rank(corner_products)
    observed=[]
    for col in corner_products:
        raw={}
        for gid,c in col.items():axpy(raw,sources[gid],c)
        observed.append({i:raw.get(path,0) for i,path in enumerate(unit_rows) if raw.get(path,0)})
    assert source_rank==s.rank(observed)==12
    old_lift=readcol(data['old_source_lift_columns'][pivot],S.sympify)
    raw_lift={}
    for gid,c in old_lift.items():axpy(raw_lift,sources[gid],c)
    assert all(raw_lift.get(path,0)==0 for path in unit_rows)
    assert heval(old_lift)[pivot]==1
    # Injectivity on the degree-one I^2 corner forces any hypothetical filtered
    # lift with these zero unit values to be zero there, contradicting H=1.
    report={'passed':True,'presentation_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'complete_source_corner_bases':len(corners),'evaluated_source_generators':len(sources),
        'I_squared_products_exhausted':count,'I_squared_generators':len(J1),'I_cubed_generators':len(J2),
        'fixed_calibration_top_component_identities':top_checks,'F2_dimension':270,
        'filtration_inclusion_identity':'J1*J21=J2 verified on all 630 columns',
        'kernel_projector_identities':'H*L0=Id9; H*L1=e_p; H*J1=e_p*h1; H*J2=0',
        'unfiltered_lift_negative_control':{'I_squared_degree_one_corner_rank':12,
            'private_unit_observation_rank':12,'old_lift_private_values':'zero','old_lift_O2_value':'one',
            'conclusion':'The chosen L0 lift is not in F1; use the separately certified L1 for the inherited kernel filtration.'},
        'result':'Full exact finite linear-constraint presentation and inherited kernel filtration verified without generic numerical rank assumptions.',
        'rank_scope':'Nonminimal presentation. No total numerical rank for G0 or G0*J1 is asserted.'}
    (ROOT/'results/actual-observer-presentation-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
