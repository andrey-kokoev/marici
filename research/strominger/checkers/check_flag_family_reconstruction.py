"""Exact integer/rational source-family test. No numerical eigensolver needed."""
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product,combinations
from math import comb
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
FIXTURE=ROOT/'research/strominger/inputs/flag-family-reconstruction-v1.json'
PACKET=ROOT/'research/strominger/dual-tetrahedral-branching-iteration-02.md'
MODEL=ROOT/'research/strominger/scc-models/flag-family-reconstruction-v1.json'
COMPILER=ROOT/'research/aspect/scc/categorical_compiler.py'
OUT=ROOT/'research/strominger/results/flag-family-reconstruction'


def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def gram(a):return mm(list(map(list,zip(*a))),a)
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def pprod(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def ppow(a,k):
    out=[1]
    for _ in range(k):out=pprod(out,a)
    return out

def charpoly(a):
    n=len(a);power=eye(n);traces=[];descending=[1]
    for k in range(1,n+1):
        power=mm(a,power);traces.append(sum(power[i][i] for i in range(n)))
        numerator=-sum(descending[k-i]*traces[i-1] for i in range(1,k+1))
        assert numerator%k==0;descending.append(numerator//k)
    return descending[::-1]

def apply_h(a,adj,degree):
    return [[degree*a[i][j]-sum(a[u][j] for u in adj[i]) for j in range(len(a[0]))] for i in range(len(a))]

def encoded_matrix(a,denominator=1):return [[str(Q(x,denominator)) for x in row] for row in a]
def token(a):return sha256(json.dumps(a,sort_keys=True).encode()).hexdigest()
def diagram(name,left,right):
    return {'id':name,'objects':[{'id':'same_based_fiber'}],
      'arrows':[{'id':side,'source':'same_based_fiber','target':'same_based_fiber','evaluated_map':a,'map_token':token(a)} for side,a in [('left',left),('right',right)]],
      'cells':[{'id':name,'routes':[['left'],['right']],'threshold':'exact_zero'}],'obstructions':[],'claims':[],
      'scope':'Evaluated rational source maps; failed coarse composition is not fundamental H incoherence.'}


def run(report):
    f=json.loads(FIXTURE.read_text(encoding='utf-8'));checks=report['checks']
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    previous=json.loads((ROOT/f['iteration1_result']).read_text(encoding='utf-8'))
    source=json.loads((ROOT/f['source_geometry']).read_text(encoding='utf-8'))
    original=json.loads((ROOT/f['iteration1_source']).read_text(encoding='utf-8'))
    check('fresh_prior_science_passed_and_pins_current',all(r['status']=='pass' and all(r['checks'].values()) and all(sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in r['source_sha256'].items()) for r in [previous,source]))
    spec=importlib.util.spec_from_file_location('family_scc_compiler',COMPILER);compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
    cases=[]
    for d in f['dimensions']:
        tag=f'd{d}';signs=list(product((-1,1),repeat=d));q=len(signs);m=q//2;degree=2*(d-1)
        facet_index={s:i for i,s in enumerate(signs)}
        flags=[{'facet':a,'marked_axis':i,'vertex':2*i+int(s[i]>0)} for a,s in enumerate(signs) for i in range(d)]
        N=len(flags);adj=[set() for _ in flags]
        for k,flag in enumerate(flags):
            a,i=flag['facet'],flag['marked_axis'];sigma=signs[a]
            for j in range(d):
                if j==i:continue
                adj[k].add(a*d+j)
                changed=list(sigma);changed[j]*=-1;adj[k].add(facet_index[tuple(changed)]*d+i)
        check(tag+'_original_flag_count_and_reciprocal_moves',N==d*2**d and all(len(row)==degree and all(i in adj[j] for j in row) for i,row in enumerate(adj)))
        reached={0};queue=[0]
        for i in queue:
            for j in adj[i]:
                if j not in reached:reached.add(j);queue.append(j)
        check(tag+'_connected',len(reached)==N)
        B=[[int(j==flag['vertex']) for j in range(2*d)] for flag in flags]
        Hv=[[degree if i==j else (-1 if i//2!=j//2 else 0) for j in range(2*d)] for i in range(2*d)]
        HB=apply_h(B,adj,degree);HHB=apply_h(HB,adj,degree)
        def left_vertex(a):
            out=[[0]*len(a[0]) for _ in range(2*d)]
            for i,flag in enumerate(flags):
                for j,x in enumerate(a[i]):out[flag['vertex']][j]+=x
            return out
        check(tag+'_lift_Gram_and_exact_first_compression',gram(B)==[[m*x for x in row] for row in eye(2*d)] and [[2*x for x in row] for row in left_vertex(HB)]==[[m*x for x in row] for row in Hv])
        L=[[2*HB[i][j]-Hv[flag['vertex']][j] for j in range(2*d)] for i,flag in enumerate(flags)]
        T=[[int(j==(i^1)) for j in range(2*d)] for i in range(2*d)]
        odd2=[[int(i==j)-T[i][j] for j in range(2*d)] for i in range(2*d)]
        GL=gram(L);expected=[[2*m*(d-1)*x for x in row] for row in odd2]
        check(tag+'_normalized_leakage_Gram_is_dminus1_Podd',GL==expected and mm(odd2,odd2)==[[2*x for x in row] for row in odd2])
        V2=mm(Hv,Hv);raw2=left_vertex(HHB)
        composition_num=[[4*raw2[i][j]-m*V2[i][j] for j in range(2*d)] for i in range(2*d)]
        check(tag+'_second_compression_defect_has_certified_rank_d',composition_num==GL and sum(odd2[i][i] for i in range(2*d))==2*d)
        selected=[2*i+1 for i in range(d)]
        memory=[[row[j] for j in selected] for row in L]
        check(tag+'_explicit_local_memory_formula',all(memory[k][j]==(0 if flag['marked_axis']==j else -signs[flag['facet']][j]) for k,flag in enumerate(flags) for j in range(d)))
        W=[b+v for b,v in zip(B,memory)];gdiag=[m]*(2*d)+[2*m*(d-1)]*d
        check(tag+'_positive_Gram_proves_3d_independent_modes',gram(W)==[[gdiag[i] if i==j else 0 for j in range(3*d)] for i in range(3*d)])
        S=[[int(v==2*i+1)-int(v==2*i) for v in range(2*d)] for i in range(d)]
        A2=[[0]*(3*d) for _ in range(3*d)]
        for i in range(2*d):
            for j in range(2*d):A2[i][j]=Hv[i][j]
            for j in range(d):A2[i][2*d+j]=2*(d-1)*S[j][i]
        for i in range(d):
            for j in range(2*d):A2[2*d+i][j]=S[i][j]
            A2[2*d+i][2*d+i]=6
        HW=apply_h(W,adj,degree)
        check(tag+'_whole_source_intertwiner_2HW_equals_WA2',[[2*x for x in row] for row in HW]==mm(W,A2))
        check(tag+'_induced_operator_is_metric_self_adjoint',all(gdiag[i]*A2[i][j]==gdiag[j]*A2[j][i] for i in range(3*d) for j in range(3*d)))
        check(tag+'_minimality_no_fitted_projection',mm(memory,S)==L)
        expected_closed=pprod(pprod([0,1],ppow([-2*d,1],d-1)),ppow([8*(d-1),-2*(d+2),1],d))
        check(tag+'_closed_characteristic_polynomial',charpoly(A2)==expected_closed)
        witness=[row[0] for row in memory];read_now=[sum(witness[i] for i,flag in enumerate(flags) if flag['vertex']==v) for v in range(2*d)]
        Hw=apply_h([[x] for x in witness],adj,degree);read_next=[Q(x[0],m) for x in left_vertex(Hw)]
        check(tag+'_discarded_source_distinction_detectable_after_H',not any(read_now) and read_next==[Q((d-1)*S[0][v]) for v in range(2*d)])
        vector=[(i*i)%17-8 for i in range(N)];coarse=[Q(sum(vector[i] for i,flag in enumerate(flags) if flag['vertex']==v),m) for v in range(2*d)]
        residual=[Q(x)-coarse[flag['vertex']] for x,flag in zip(vector,flags)]
        check(tag+'_complete_packet_reconstructs_and_retains_residual',all(coarse[flag['vertex']]+residual[i]==vector[i] for i,flag in enumerate(flags)) and all(sum(residual[i] for i,flag in enumerate(flags) if flag['vertex']==v)==0 for v in range(2*d)))
        chars=[[(-1 if sum(1 for j in range(d) if mask>>j&1 and sigma[j]<0)%2 else 1) for mask in range(q)] for sigma in signs]
        sums=[sum(row[t] for row in chars) for t in range(q)]
        check(tag+'_full_Walsh_basis_is_invertible_not_a_quotient',sums==[q]+[0]*(q-1) and all(row[t]*row[1<<j]==row[t^(1<<j)] for row in chars for t in range(q) for j in range(d)))
        factors=[];all_actions=True
        for mask in range(q):
            weight=mask.bit_count()
            block=[[(d+2*weight-2*((mask>>i)&1) if i==j else 0)-1 for j in range(d)] for i in range(d)]
            for j in range(d):
                vec=[chars[flag['facet']][mask] if flag['marked_axis']==j else 0 for flag in flags]
                observed=[degree*vec[i]-sum(vec[k] for k in adj[i]) for i in range(N)]
                all_actions=all_actions and all(observed[i]==chars[flag['facet']][mask]*block[flag['marked_axis']][j] for i,flag in enumerate(flags))
            if mask==(1<<weight)-1:
                if weight==0:polynomial=pprod([0,1],ppow([-d,1],d-1))
                elif weight==d:polynomial=pprod([-(2*d-2),1],ppow([-(3*d-2),1],d-1))
                else:polynomial=pprod(pprod(ppow([-(d+2*weight-2),1],weight-1),ppow([-(d+2*weight),1],d-weight-1)),[2*weight*(d+2*weight-3),-(d+4*weight-2),1])
                check(tag+f'_actual_weight{weight}_block_polynomial',charpoly(block)==polynomial)
                factors.append({'weight':weight,'number_of_blocks':comb(d,weight),'block':block,'characteristic_coefficients_ascending':polynomial})
        check(tag+'_all_full_source_Walsh_actions_exact',all_actions and sum(c['number_of_blocks']*d for c in factors)==N)
        bad=diagram(tag+'_coarse_composition',encoded_matrix(raw2,m),encoded_matrix(V2,4))
        good=diagram(tag+'_nonzero_residual_identity',encoded_matrix(composition_num,4*m),encoded_matrix(odd2,2//1))
        # The expected residual is (d-1)/2 times (I-antipode).
        good['arrows'][1]['evaluated_map']=encoded_matrix([[(d-1)*x for x in row] for row in odd2],2)
        good['arrows'][1]['map_token']=token(good['arrows'][1]['evaluated_map'])
        cbad=compiler.compile_diagram(bad);cgood=compiler.compile_diagram(good)
        check(tag+'_SCC_fails_only_unsupported_coarse_equality',not cbad['passed'] and cgood['passed'])
        case={'d':d,'facet_signs':signs,'flags':flags,'edges':[(i,j) for i,row in enumerate(adj) for j in sorted(row) if i<j],
          'raw_flags':N,'degree':degree,'vertex_source_dimension':2*d,'memory_dimension':d,'minimal_closure_dimension':3*d,'other_full_flag_modes':N-3*d,
          'B':B,'twice_leakage_L':L,'closure_inclusion_W':W,'closure_Gram_diagonal':gdiag,'twice_closed_operator':A2,'twice_closed_characteristic_coefficients':expected_closed,
          'vertex_operator_Hv':Hv,'second_compression_numerator_4m':composition_num,'composition_defect_rank':d,
          'witness':{'source_flag_vector':witness,'reader_now_numerator':read_now,'reader_after_H':[str(x) for x in read_next]},
          'full_packet_example':{'source':vector,'vertex_means':[str(x) for x in coarse],'flag_residual':[str(x) for x in residual]},
          'full_Walsh_block_factors':factors,'full_transform_formula':'F[(sigma,i),(T,j)]=delta(i,j)*product(sigma[a] for a in T); F^T F=2^d I',
          'compiled_cells':{'coarse':cbad,'nonzero_residual_identity':cgood}}
        cases.append(case)
        OUT.mkdir(parents=True,exist_ok=True)
        for suffix,diagram_data in [('coarse',bad),('residual',good)]:
            (OUT/(tag+'-'+suffix+'-diagram.json')).write_text(json.dumps(diagram_data,indent=2)+'\n',encoding='utf-8')
        if d==4:
            old_vertices=source['regular_candidates']['16-cell']['geometry']['vertices'];axis_sign={}
            for v,coords in enumerate(old_vertices):
                axis,a,b=next((i,a,b) for i,(a,b) in enumerate(coords) if (a,b)!=(0,0));assert b==0;axis_sign[v]=(axis,a//4)
            index={(sigma,i):a*d+i for a,sigma in enumerate(signs) for i in range(d)};mapping=[]
            for oldflag in original['flags']:
                sigma=[0]*d
                for v in oldflag['tetrahedron_vertices']:
                    axis,sign=axis_sign[v];sigma[axis]=sign
                mapping.append(index[tuple(sigma),axis_sign[oldflag['vertex']][0]])
            check('d4_actual_original_source_bijection_and_all_edges',len(set(mapping))==64 and {tuple(sorted((mapping[i],mapping[j]))) for i,j in original['edges']}=={(i,j) for i,row in enumerate(adj) for j in row if i<j})
            check('d4_canonical_lift_transports_with_original_vertex_labels',all(B[mapping[i]][2*axis_sign[v][0]+int(axis_sign[v][1]>0)]==int(v==oldflag['vertex']) for i,oldflag in enumerate(original['flags']) for v in range(8)))
            denom=2*m*(d-1)
            new_projector=[[2*(d-1)*sum(B[a][k]*B[b][k] for k in range(2*d))+sum(memory[a][k]*memory[b][k] for k in range(d)) for b in range(N)] for a in range(N)]
            old_unseen=previous['minimal_closure']['other_modes_projector']
            transported=[[Q(int(i==j))-Q(old_unseen[i][j]) for j in range(64)] for i in range(64)]
            left=[[str(Q(new_projector[mapping[i]][mapping[j]],denom)) for j in range(64)] for i in range(64)]
            right=[[str(x) for x in row] for row in transported]
            check('d4_entire_original_closure_projector_transported_not_just_rank',left==right)
            d4diagram=diagram('d4_original_closure_covariance',left,right)
            check('d4_SCC_source_closure_covariance',compiler.compile_diagram(d4diagram)['passed'])
            (OUT/'d4-source-covariance-diagram.json').write_text(json.dumps(d4diagram,indent=2)+'\n',encoding='utf-8')
            case['iteration1_source_flag_bijection']=mapping
    report.update({'classification':'raw_exponential_flags_but_minimal_vertex_task_closure_3d','iteration':2,'cases':cases,
      'summary':[{'d':c['d'],'raw_flags':c['raw_flags'],'vertex_modes':c['vertex_source_dimension'],'memory_modes':c['memory_dimension'],'minimal_closure':c['minimal_closure_dimension'],'other_full_modes':c['other_full_flag_modes'],'coarse_defect_rank':c['composition_defect_rank']} for c in cases],
      'general_source_identity':'For every d>=2, Lplus[(sigma,i),j]=0 if i=j else -sigma[j]. Its exact sign sums give Gram diag(m I_2d,2m(d-1) I_d), and source moves give 2HW=W A2. This proves the3d task law, rather than extrapolating from tested d2..6.',
      'scope':'Task-relative mathematical reconstruction. All original d2^d modes remain available; d is not principal shell number, and no physical spin, P/N/E attachment or occupation is derived.',
      'enabled_successor':'Determine minimum faithful tetrahedral face-reader covers on the fixed d4 twelve-mode task using source restriction ranks, not additive per-face capacity by assumption.'})


def main():
    f=json.loads(FIXTURE.read_text(encoding='utf-8'))
    paths=[HERE,FIXTURE,PACKET,MODEL,ROOT/f['initial_net_revision'],ROOT/f['iteration1_result'],ROOT/f['iteration1_source'],ROOT/f['source_geometry'],COMPILER]
    report={'schema':'marici.strominger.flag-family-reconstruction.verification.v1','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':{},'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:run(report);report['status']='pass'
    except Exception as error:report.update(status='fail',error=repr(error));raise
    finally:
        OUT.mkdir(parents=True,exist_ok=True)
        (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'status':report['status'],'classification':report.get('classification','execution_failure'),'checks':len(report['checks']),'summary':report.get('summary'),'receipt':(OUT/'verification.json').relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
