"""Finite constraint presentation of the actual assembled observer and its flag.

Eliminates the ABSTRACT source ideal: rational bases for ker(rho), explicit
product columns for I^2 and I^3, and the full calibrated evaluation matrix.
Relation spaces are given by explicit linear equations, not generic ranks.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,combinations,product
from collections import defaultdict
import importlib.util,json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('old',ROOT/'checkers/export_actual_old_observer.py')
o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o);s=o.s;S=o.S


def axpy(target,source,c):
    for k,v in source.items():
        w=target.get(k,Q(0))+c*v
        if w:target[k]=w
        elif k in target:del target[k]


def source_basis(a,b):
    events=[i for i in range(6) if (a^b)&(1<<i)];paths=[];basis={};kernels=[];free=[]
    for w in permutations(events):
        for q in range(min(2,len(w))+1):
            for kept in combinations(range(len(w)),q):
                m=tuple(int(i in kept) for i in range(len(w)));index=len(paths);paths.append((w,m))
                v=s.record(a,w,m);lift={index:Q(1)}
                while v:
                    pivot=min(v)
                    if pivot not in basis:
                        factor=v[pivot];basis[pivot]=({k:c/factor for k,c in v.items()},{k:c/factor for k,c in lift.items()});break
                    vec,rep=basis[pivot];factor=v[pivot]
                    axpy(v,vec,-factor);axpy(lift,rep,-factor)
                if not v:
                    assert lift[index]==1
                    kernels.append(lift);free.append(index)
    # Verify the complete rational null basis against the recorder.
    for column in kernels:
        assert not s.rho_column(a,{paths[i]:c for i,c in column.items()})
    assert len(kernels)+len(basis)==len(paths)
    assert all(set(col)&set(free)=={p} for p,col in zip(free,kernels))
    assert all(all(sum(paths[i][1])==sum(paths[p][1]) for i in col) for p,col in zip(free,kernels))
    return {'paths':paths,'lookup':{p:i for i,p in enumerate(paths)},'basis':kernels,'free':free,
            'rho_rank':len(basis),'grade':[sum(paths[p][1]) for p in free]}


def main():
    basepath=ROOT/'results/actual-private-core-with-original-cubic.json'
    unionpath=ROOT/'results/actual-retained-cubic-observer-union.json'
    oldpath=ROOT/'results/actual-old-observer-symbolic.json'
    base=json.loads(basepath.read_text());union=json.loads(unionpath.read_text());old=json.loads(oldpath.read_text())
    assert union['base']['sha256']==hashlib.sha256(basepath.read_bytes()).hexdigest()
    atoms=['1','rho','sigma','rho*sigma'];atom_index={x:i for i,x in enumerate(atoms)}
    expressions=[()];expression_index={():0}
    def intern(poly):
        key=tuple(sorted((i,c) for i,c in poly.items() if c))
        if key not in expression_index:expression_index[key]=len(expressions);expressions.append(key)
        return expression_index[key]
    def atom(name):
        if name not in atom_index:atom_index[name]=len(atoms);atoms.append(name)
        return atom_index[name]
    def oldcoef(value):
        return {'1':{0:Q(1)},'-rho':{1:Q(-1)},'-sigma':{2:Q(-1)},'rho*sigma':{3:Q(1)}}[value]
    rows=[]
    for row in base['rows']:
        rows.append((tuple(row['corner_masks']),{(tuple(t['word']),tuple(t['marks'])):intern(oldcoef(t['coefficient'])) for t in row['terms']}))
    offsets={}
    for frame in union['frames']:
        offsets[frame['family']]=len(rows)
        for row in frame['rows']:
            terms={}
            for t in row['terms']:
                poly={};windows=tuple(map(tuple,t['windows']))
                for j,c in enumerate(t['component_coefficients']):
                    if not c:continue
                    if frame['family']=='two_private' or (frame['family']=='matched_memory' and j==0):
                        assert len(frame['denominators'][j])==1
                        den=frame['denominators'][j][0]
                        assert tuple(map(tuple,den['windows']))==windows and den['coefficient']==1
                        axpy(poly,{0:Q(1),1:Q(-1),2:Q(-1),3:Q(1)} if j==0 else {1:Q(-1)},Q(c))
                    else:
                        name=frame['family']+':'+str(j)+':'+','.join(str(v) for edge in windows for v in edge)
                        axpy(poly,{atom(name):Q(c)},Q(1))
                terms[tuple(t['word']),tuple(t['marks'])]=intern(poly)
            rows.append((tuple(row['corner_masks']),terms))
    bycorner=defaultdict(lambda:defaultdict(list))
    for row,(corner,terms) in enumerate(rows):
        for path,expr in terms.items():bycorner[corner][path].append((row,expr))
    corners={};generators=[];evaluation=[];global_free={};corner_audits=[]
    for a in range(64):
        for b in range(64):
            if a&b!=a or (a^b).bit_count()<2:continue
            c=source_basis(a,b);c['offset']=len(generators);corners[a,b]=c
            for i,column in enumerate(c['basis']):
                gid=len(generators);generators.append(((a,b),column))
                global_free[a,b,c['free'][i]]=gid
                result=defaultdict(dict)
                for path_index,coef in column.items():
                    for row,expr in bycorner[a,b].get(c['paths'][path_index],()):axpy(result[row],dict(expressions[expr]),coef)
                evaluation.append({row:intern(poly) for row,poly in result.items() if poly})
            corner_audits.append({'corner':[a,b],'paths':len(c['paths']),'recorder_rank':c['rho_rank'],'ideal_basis':len(c['basis'])})
    print('source basis complete:',len(generators),'generators',flush=True)
    def source_coordinates(a,b,col):
        c=corners[a,b];out={}
        for path,coef in col.items():
            index=c['lookup'][path]
            if (a,b,index) in global_free and coef:out[global_free[a,b,index]]=coef
        rebuilt={}
        for gid,coef in out.items():
            for p,v in generators[gid][1].items():
                key=c['paths'][p];axpy(rebuilt,{key:v},coef)
        assert rebuilt=={p:v for p,v in col.items() if v}
        return out
    def product_column(a,c,b,left,right):
        lc,rc=corners[a,c],corners[c,b]
        col=s.multiply({lc['paths'][i]:v for i,v in left.items()},{rc['paths'][i]:v for i,v in right.items()})
        return source_coordinates(a,b,col)
    F1=[];F1_witnesses=[];seen=set();product_count=0
    for (a,b),c in corners.items():
        if (a^b).bit_count()<4:continue
        for middle in range(64):
            if (a,middle) not in corners or (middle,b) not in corners:continue
            left,right=corners[a,middle],corners[middle,b]
            for i,l in enumerate(left['basis']):
                for j,r in enumerate(right['basis']):
                    if left['grade'][i]+right['grade'][j]>2:continue
                    col=product_column(a,middle,b,l,r);product_count+=1
                    if not col:continue
                    factor=col[min(col)];key=tuple(sorted((k,v/factor) for k,v in col.items()))
                    if key not in seen:
                        seen.add(key);F1.append(dict(key))
                        F1_witnesses.append([left['offset']+i,right['offset']+j,str(factor)])
    print('I^2 products complete:',product_count,'products;',len(F1),'columns',flush=True)
    F2=[];F2_witnesses=[];J21=[]
    F1_index={tuple(sorted(col.items())):i for i,col in enumerate(F1)}
    def pairings(items):
        if not items:yield ();return
        for pair in combinations(items,2):
            for tail in pairings(tuple(i for i in items if i not in pair)):yield (pair,)+tail
    for pairs in pairings(tuple(range(6))):
        for kinds in product((0,1),repeat=3):
            if sum(kinds)>2:continue
            source={((),()):Q(1)}
            for pair,kind in zip(pairs,kinds):source=s.multiply(source,s.relation(pair,kind))
            final=source_coordinates(0,63,source)
            F2.append(final);F2_witnesses.append({'pairs':pairs,'kinds':kinds})
            middle=sum(1<<e for e in pairs[0])
            left=source_coordinates(0,middle,s.relation(pairs[0],kinds[0]))
            right=source_coordinates(middle,63,s.multiply(s.relation(pairs[1],kinds[1]),s.relation(pairs[2],kinds[2])))
            inclusion={}
            for lg,lv in left.items():
                for rg,rv in right.items():
                    col=product_column(0,middle,63,generators[lg][1],generators[rg][1])
                    if not col:continue
                    factor=col[min(col)];key=tuple(sorted((gid,v/factor) for gid,v in col.items()))
                    axpy(inclusion,{F1_index[key]:lv*rv*factor},Q(1))
            reconstructed={}
            for index,coefficient in inclusion.items():axpy(reconstructed,F1[index],coefficient)
            assert reconstructed==final
            J21.append(inclusion)
    assert len(F2)==630
    # Export the actual old projection on the finite source generators.
    def symbolic(expr):
        assert all(i<4 for i,c in expressions[expr])
        return sum(S.Rational(c.numerator,c.denominator)*S.sympify(atoms[i]) for i,c in expressions[expr])
    H=[]
    for col in evaluation:
        value={}
        for i,row,factor in base['projection_to_O2']:
            if row in col:
                v=S.cancel(S.sympify(factor)*symbolic(col[row]))
                if v!=0:value[i]=v
        H.append(value)
    def old_eval(coords):
        result=[S.Integer(0)]*9
        for gid,c in coords.items():
            for i,v in H[gid].items():result[i]+=S.sympify(c)*v
        return [S.cancel(v) for v in result]
    lifts=[]
    for j,rep in enumerate(old['source_representatives']):
        source={(tuple(t['word']),tuple(t['marks'])):S.sympify(t['coefficient']) for t in rep['terms']}
        c=corners[tuple(rep['corner_masks'])]
        coords={global_free[*rep['corner_masks'],c['lookup'][path]]:v for path,v in source.items()
                if (*rep['corner_masks'],c['lookup'][path]) in global_free}
        reconstructed={}
        for gid,coefficient in coords.items():
            for path_index,value in generators[gid][1].items():
                path=c['paths'][path_index]
                reconstructed[path]=reconstructed.get(path,S.Integer(0))+coefficient*value
        assert all(S.cancel(reconstructed.get(path,0)-source.get(path,0))==0 for path in set(reconstructed)|set(source))
        assert old_eval(coords)==[S.Integer(i==j) for i in range(9)]
        lifts.append(coords)
    v2=s.multiply(s.relation((0,1),1),s.relation((2,3),0))
    v2c=source_coordinates(0,15,v2);oldv2=old_eval(v2c)
    pivot=next(i for i,v in enumerate(oldv2) if v!=0)
    assert sum(v!=0 for v in oldv2)==1
    first=v2c[min(v2c)]
    assert tuple(sorted((gid,v/first) for gid,v in v2c.items())) in seen
    F1lift={gid:S.cancel(S.sympify(v)/oldv2[pivot]) for gid,v in v2c.items()}
    assert old_eval(F1lift)==[S.Integer(i==pivot) for i in range(9)]
    F1_old=[]
    for col in F1:
        v=old_eval(col);assert all(x==0 for i,x in enumerate(v) if i!=pivot)
        F1_old.append(v[pivot])
    assert all(old_eval(col)==[0]*9 for col in F2)
    # Sparse column encodings use global source-generator indices.
    def rational_column(col):return [[i,str(c)] for i,c in sorted(col.items())]
    payload={'schema':'actual-observer-full-finite-constraint-presentation-v1',
        'inputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (basepath,unionpath,oldpath)},
        'coefficient_field':'The fixed actual analytical scalar field specified in the union artifact; no generic independent-window specialization.',
        'coefficient_atoms':atoms,
        'atom_semantics':'Base atoms 1,rho,sigma,rho*sigma. family:j:a,b,c,d means S[j]*W(a,b)*W(c,d)/family.denominator[j], with the owning fixed R or N test. All owning analytic/additivity relations remain in force.',
        'expressions':[[[i,str(c)] for i,c in expression] for expression in expressions],
        'source_corners':[{'corner':[a,b],'paths':[[w,m] for w,m in c['paths']],
                           'generator_offset':c['offset'],'free_path_indices':c['free'],
                           'ideal_basis_columns':[rational_column(col) for col in c['basis']],
                           'recorder_rank':c['rho_rank']} for (a,b),c in corners.items()],
        'ambient_rows':len(rows),'source_generator_count':len(generators),
        'G0_evaluation_columns':[[[row,expr] for row,expr in sorted(col.items())] for col in evaluation],
        'J1_I_squared_columns':[rational_column(col) for col in F1],
        'J1_source_product_witnesses':F1_witnesses,
        'J2_I_cubed_columns':[rational_column(col) for col in F2],
        'J2_source_product_witnesses':F2_witnesses,
        'J21_F2_to_F1_columns':[rational_column(col) for col in J21],
        'observer_relations':'For source-coordinate vectors z,zprime, [z]=[zprime] iff EVERY exported row of G0*(z-zprime) is zero at the actual fixed calibration. This is a finite linear constraint presentation, not a free ambient coordinate module.',
        'filtration':{'F0':'K^source_generator_count / ker(G0), over the fixed actual analytical coefficient field',
                      'F1':'classes of columns J1, relations G0*J1*c=0',
                      'F2':'classes of columns J2, relations G0*J2*c=0',
                      'F3':'0','inclusion_maps':'J1:F1->F0 and J21:F2->F1; J1*J21=J2 is checked exactly',
                      'certified_F2_dimension':270,
                      'higher_degree_source':'All source components with >=3 retained marks evaluate to zero and remain zero under source actions; omitted from the source-coordinate domain only for that reason.'},
        'old_projection_columns':[rational_column(col) for col in H],
        'old_source_lift_columns':[rational_column(col) for col in lifts],
        'kernel_generators':{'K0':'B0=identity-L0*H, with L0 the nine exported old_source_lift_columns; K0=im(G0*B0), relations G0*B0*c=0',
            'K1':'B1=J1-L1*h1, where L1 and h1 are exported below; K1=im(G0*B1), relations G0*B1*c=0',
            'K2':'B2=J2; K2=im(G0*J2), dimension 270','K3':'0',
            'inclusion_maps':'B1 maps K1 generators into K0 source-coordinate generators; J21 maps K2 generators into K1. B0*B1=B1 and B1*J21=J2 follow from the checked H identities.',
            'warning':'These are INHERITED filtration levels of ker(O3->O2), not ideal powers of that kernel.'},
        'kernel_F1_lift':rational_column(F1lift),'kernel_F1_old_row':pivot,
        'kernel_F1_old_values':[str(v) for v in F1_old],
        'prime_actions':'Use the pinned assembled ambient actions: base block plus each contextual frame block. They induce actions on the presented quotient because G0 intertwines source precomposition; no arbitrary complement or splitting is chosen.',
        'frame_row_offsets':offsets,
        'audit':{'all_source_corners':len(corners),'source_paths':sum(len(c['paths']) for c in corners.values()),
                 'source_ideal_generators':len(generators),'I_squared_products_checked':product_count,
                 'I_squared_generating_columns':len(F1),'I_cubed_generating_columns':len(F2),
                 'old_right_inverse_verified':True,'filtered_kernel_projectors_verified':True},
        'presentation_kind':'Full explicit finite constraint presentation, NOT a minimized basis. Total numerical ranks of G0 and G0*J1 are not claimed; no unproved analytic rank specialization is used.'}
    out=ROOT/'results/actual-observer-full-finite-presentation.json.gz'
    out.write_bytes(gzip.compress(json.dumps(payload,separators=(',',':')).encode('utf-8'),mtime=0))
    print(json.dumps({'passed':True,'artifact':str(out),'ambient_rows':len(rows),'coefficient_expressions':len(expressions),**payload['audit']},indent=2))


if __name__=='__main__':main()
