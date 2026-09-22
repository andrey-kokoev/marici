"""History-indexed naturality, anchored to the actual seven-reading decoder.

Synthetic exact histories of admitted forgotten-packet source actions.
No claim of physical acquisition or full marked-source/history coverage.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[1]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


t=load('towers',ROOT/'checkers/check_residual_tower_of_towers.py');a=t.a
reader=load('seven_readings',ROOT.parent/'voevodsky/certificates/reconstruct_seven_dimensional_ideal_slice.py')
mm,inv,eye,sub=t.mm,t.inv,t.eye,t.sub

def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def labels(m):return [j for j in range(1,8) if j.bit_count()<=m]
def projection(m,q):return [[Q(x==y) for y in labels(m)] for x in labels(q)]
def transpose(M):return list(map(list,zip(*M)))


def main():
    counts={'ordered_reading_coefficients':0,'history_squares':0,'observer_squares':0,
            'mixed_depth_history_squares':0,'observer_triangles':0,'higher_history_routes':0,
            'evidence_pullback_routes':0,'affine_history_fiber_comparisons':0}
    # Recover the reading matrix from the independent ordered-cut recorder.
    R=[]
    for seams in reader.SEAMS:
        row=[];key=tuple(('e',x,y,0) for x,y in seams)
        for source in a.basis(8):
            row.append(Q(a.f['vacuum_rows'](0,63,a.paths(source,0,3),len(seams)).get(key,0)))
            counts['ordered_reading_coefficients']+=1
        R.append(row)
    decoder=[[Q(x) for x in row] for row in reader.INVERSE]
    assert mm(R,decoder)==eye(7)
    # Final source coordinates u_b=a_b (b=1..7), with a_0=-sum u_b.
    D=[[-Q(1)]*7]+eye(7)
    assert mm(decoder,mm(R,D))==D
    H=[Q(1),Q(-1)]
    T10=a.action(H,1);append_last=a.action(H,2)
    T21=append_last[1:];assert mm(D,T21)==append_last
    dims={0:2,1:4,2:7}
    transitions={(h,h):eye(dims[h]) for h in dims}
    transitions[0,1]=T10;transitions[1,2]=T21;transitions[0,2]=mm(T21,T10)
    # The history arrows are actual marked-source products, not arbitrary matrices.
    for x in a.basis(2):
        assert a.paths(a.apply(T10,x),0,2)==a.f['multiply'](a.paths(x,0,1),a.paths(H,1,1))
    for x in a.basis(4):
        assert a.paths(a.apply(append_last,x),0,3)==a.f['multiply'](a.paths(x,0,2),a.paths(H,2,1))
    reading_anchors={2:mm(R,D),1:mm(R,append_last),0:mm(mm(R,append_last),T10)}
    Z=[[Q(b&j==j) for b in range(8)] for j in range(8)]
    frames=t.frames(3);E={};F={};B={}
    for m in (1,2,3):
        J=labels(m);As=[sub(A,J,J) for A in frames]
        E[m]=[mm(A,mm(sub(Z,J,range(8)),decoder)) for A in As]
        F[m]={(i,j):mm(As[j],inv(As[i])) for i,j in product(range(4),repeat=2)}
        for h in dims:
            for i in range(4):B[h,m,i]=mm(E[m][i],reading_anchors[h])
        for i,j,k in product(range(4),repeat=3):
            assert mm(F[m][j,k],F[m][i,j])==F[m][i,k]
            counts['observer_triangles']+=1
    history_jet_ranks=[[len(a.rref(B[h,m,0],dims[h])[1]) for m in (1,2,3)] for h in dims]
    assert history_jet_ranks==[[0,1,2],[1,3,4],[3,6,7]]
    # Each appended ideal relation consumes one cut: the final order-m jet
    # sees only order m-(2-h) in the earlier packet (negative means zero).
    for h in (0,1):
        n=h+1;past_mask=(1<<n)-1;future_mask=7^past_mask;sign=(-1)**(2-h)
        for m in (1,2,3):
            expected_rows=[[Q(sign*int((b&(j&past_mask))==(j&past_mask))) if j&future_mask==future_mask else Q(0)
                            for b in range(1<<n)] for j in labels(m)]
            assert B[h,m,0]==expected_rows
    for (h,k),T in transitions.items():
        for m in (1,2,3):
            for i in range(4):
                assert mm(B[k,m,i],T)==B[h,m,i]
                counts['history_squares']+=1
            for i,j in product(range(4),repeat=2):
                assert mm(F[m][i,j],B[h,m,i])==B[h,m,j]
                counts['observer_squares']+=1
                for q in range(1,m+1):
                    direct=mm(mm(projection(m,q),F[m][i,j]),mm(B[k,m,i],T))
                    assert direct==mm(F[q][i,j],B[h,q,i])==B[h,q,j]
                    counts['mixed_depth_history_squares']+=1
            for i,j,l,p in product(range(4),repeat=4):
                route=mm(F[m][l,p],mm(F[m][j,l],F[m][i,j]))
                assert mm(route,mm(B[k,m,i],T))==B[h,m,p]
                counts['higher_history_routes']+=1
    # Full history variables (x0,x1,u2), not disconnected marginal state sets.
    offsets={0:0,1:2,2:6};width=13
    equations=[];values=[]
    for h,k in ((0,1),(1,2)):
        for row_index,row in enumerate(transitions[h,k]):
            constraint=[Q(0)]*width;constraint[offsets[k]+row_index]=1
            for j,value in enumerate(row):constraint[offsets[h]+j]-=value
            equations.append(constraint);values.append(Q(0))
    historical=[Q(1),Q(1)]+[Q(0)]*11
    histories=a.solve(equations+[historical],values+[Q(1)],width)
    assert histories is not None and len(histories[1])==1
    physical_row=eye(7)[0] # vacuum_PPP in the owning seven-reading contract
    direct_past=a.pull([physical_row],reading_anchors[0])[0]
    assert direct_past==[1,0]
    covectors={i:a.pull([physical_row],inv(E[3][i]))[0] for i in range(4)}
    def embedded(row,h):return [Q(0)]*offsets[h]+row+[Q(0)]*(width-offsets[h]-len(row))
    direct_future=embedded(a.pull([physical_row],reading_anchors[2])[0],2)
    expected=a.restrict(histories,[direct_future],[Q(1)])
    assert expected is not None and expected[1]==[] and expected[0][:2]==[1,0]
    for h in dims:
        for i,j,k in product(range(4),repeat=3):
            # Pull the same physical evidence through two observer comparisons.
            pulled=a.pull([covectors[k]],mm(F[3][j,k],F[3][i,j]))[0]
            assert pulled==covectors[i]
            past_row=a.pull([pulled],B[h,3,i])[0]
            assert past_row==a.pull([physical_row],reading_anchors[h])[0]
            counts['evidence_pullback_routes']+=1
            refined=a.restrict(histories,[embedded(past_row,h)],[Q(1)])
            assert a.canonical(refined,width)==a.canonical(expected,width)
            counts['affine_history_fiber_comparisons']+=1
    # Nonempty refinement must not be implemented by overwriting earlier evidence.
    model={'seven_reading_model_sha256':reader.MODEL_SHA256,
           'stages':[{'stage':0,'domain':'two first-block forgotten paths','corner':[2,12]},
                     {'stage':1,'domain':'four two-block forgotten paths','corner':[2,420]},
                     {'stage':2,'domain':'seven-dimensional declared forgotten ideal slice','corner':[2,60060]}],
           'actions':['append (P-Q) in the second block','append (P-Q) in the third block'],
           'coordinate_conventions':{'0':'P,Q path coefficients','1':'P/Q path masks 0..3',
                                     '2':'path coefficients a1..a7, with a0=-sum(a1..a7)'},
           'transition_matrices':{'0_to_1':t.wire_matrix(T10),'1_to_2':t.wire_matrix(T21)},
           'history_constraints':'x1=T10*x0; u2=T21*x1; correlations are retained',
           'source_support':'assumed, not inferred from readings',
           'uncertainty':'exact rational synthetic fixture, no physical acquisition claim'}
    model_sha=digest(model)
    old_record={'id':'initial_terminal','stage':0,'row_label':'sum_first_block_path_coefficients',
                'value':'1','normalization':'unit vacuum','uncertainty':'exact synthetic',
                'history_model_sha256':model_sha}
    frozen=json.dumps(old_record,sort_keys=True)
    ledger={'schema':'source-history-evidence-v1','history_model_sha256':model_sha,'records':[old_record]}
    after=json.loads(json.dumps(ledger));after['records'].append({
        'id':'later_vacuum','stage':2,'row_label':'vacuum_PPP','value':'1',
        'normalization':'unscaled unit-vacuum record coefficient','uncertainty':'exact synthetic',
        'history_model_sha256':model_sha,'reading_model_sha256':reader.MODEL_SHA256})
    assert json.dumps(after['records'][0],sort_keys=True)==frozen
    def validate_ledger(value):
        if value.get('history_model_sha256')!=model_sha:raise ValueError('history model')
        if value.get('schema')!='source-history-evidence-v1':raise ValueError('schema')
        if value.get('records')!=after['records']:raise ValueError('changed historical labels, values or contracts')
    validate_ledger(json.loads(json.dumps(after)))
    rejected=[]
    for label,key,value in [('normalization','normalization','rescaled'),('past_value','value','0'),
                             ('history_stage','stage',1),('uncertainty','uncertainty','unjustified exactness'),
                             ('row_label','row_label','different_reading'),('model_binding','history_model_sha256','wrong-model')]:
        bad=json.loads(json.dumps(after));bad['records'][0][key]=value
        try:validate_ledger(bad)
        except ValueError:rejected.append(label)
        else:raise AssertionError('historical mutation accepted')
    # Coarse observer data do not support this retrodiction without new evidence.
    difference=[Q(1),Q(-1)]
    for i in range(4):
        assert a.apply(B[0,2,i],difference)==[0]*6
        assert a.dot(direct_past,difference)==1
        # No covector on the depth-two carrier represents the full vacuum row.
        assert a.solve(transpose(projection(3,2)),covectors[i],6) is None
    assert a.restrict(expected,[direct_future],[Q(0)]) is None
    true_source=a.apply(mm(D,transitions[0,2]),[Q(1),Q(0)])
    true_readings=a.apply(R,true_source)
    payload={'schema':'seven-dimensional-ideal-readings-v1','model_sha256':reader.MODEL_SHA256,
             'readings':{name:str(value) for name,value in zip(reader.IDS,true_readings)},'terminal_check':'0'}
    reader.reconstruct(json.loads(json.dumps(payload)))
    report={'schema':'history-indexed-observer-coherence-v1','passed':True,'checks':counts,
        'history_model':model,'history_model_sha256':model_sha,
        'source_transitions':[{'from':h,'to':k,'matrix':t.wire_matrix(T)} for (h,k),T in transitions.items()],
        'reading_anchors':{str(h):t.wire_matrix(M) for h,M in reading_anchors.items()},
        'jet_labels':{str(m):labels(m) for m in (1,2,3)},
        'history_by_future_jet_rank_table':history_jet_ranks,
        'effective_past_jet_order':'m-(2-h) for h=0,1; a negative order gives zero. Each prescribed future ideal factor consumes one cut.',
        'observer_anchors_from_seven_readings':{str(m):[t.wire_matrix(M) for M in E[m]] for m in E},
        'evidence_ledger':after,'synthetic_full_reading_payload':payload,
        'refined_history_coordinates':list(map(str,expected[0])),
        'initial_history_dimension':1,'refined_history_dimension':0,
        'negative_controls':{'historical_mutations_rejected':rejected,
            'depth_two_cannot_determine_later_vacuum_or_initial_P_Q_split':True,
            'contradictory_new_evidence_gives_empty_history_not_rewritten_past':True},
        'interpretation':'Observer comparison coherence is natural along the declared actual source-action history. Equivalent routes pull later evidence back to the same correlated history fiber.',
        'scope':'Three synthetic source stages, four rational jet coordinate frames, exact evidence, externally assumed forgotten support. Not arbitrary past realizations, noisy receivers, the historical nonsplit scalar-observer enrichments, or a reconstruction from unavailable measurements.',
        'validator_scope':'The ledger mutation guard checks this pinned fixture only; it is not a general archival or authentication service.'}
    out=ROOT/'results/history-indexed-observer-coherence.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('passed','checks','history_by_future_jet_rank_table','initial_history_dimension','refined_history_dimension','negative_controls','scope')},indent=2))


if __name__=='__main__':main()
