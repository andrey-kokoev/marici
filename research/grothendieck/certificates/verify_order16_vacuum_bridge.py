"""Portable order-16 scalar tail square with a pinned A=3,4 source-row bridge.

Needs only sibling verify_source_task_transition.py. Source aggregation is NOT
an equivariant module map. The old observer's packet-support identification and
the owning structural completeness theorem remain explicit external premises.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,combinations,product
import importlib.util,math,sys

spec=importlib.util.spec_from_file_location('task',Path(__file__).with_name('verify_source_task_transition.py'))
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
P=(2,3,5,7,11,13)
CONTRACT={'source_prior':'sum_integer_A_ge_2 A^16 (32 sum_j abs(a_Aj)+8 abs(b_A)) <= M',
          'baseline_vacuum':'chi_2_already_present_no_splitting_claim',
          'old_support':'all_existing_rows_supported_in_the_A2_packet_ending_60060',
          'new_readings':'only_chi_3_and_chi_4_on_the_declared_cubic_source_family',
          'tail_aggregation':'scalar_only_not_source_equivariant',
          'residual_tail':'features_at_A3_and_A4_remain_unmeasured',
          'structural_scope':'new_labelled_blocks_only_not_full_old_observer_identification',
          'acquisition_status':'synthetic_intervals_not_measurements'}

def unit_seed(A,word):
    states=[A]
    for p in word:states.append(states[-1]*p)
    wanted=((A,2*A),(6*A,30*A),(210*A,2310*A))
    return sum(tuple((states[k],states[k+1]) for k in cuts)==wanted for cuts in combinations(range(6),3))

def bridge(b):
    v.fields(b,('artifact','artifact_sha256','rows','measured_scalar_count','reconstructed_saturation'))
    a=b['artifact'];v.require(v.sha(a)==b['artifact_sha256'],'Structural artifact digest mismatch')
    v.fields(a,('passed','increment_dimension','inherited_filtration_dimensions','blocks','old_terminal_bound','checks','conclusion','scope'))
    v.require(a['passed'] is True,'Owning structural audit failed')
    def integers(x):
        if type(x) is list:
            for y in x:integers(y)
        elif type(x) is dict:
            for y in x.values():integers(y)
        else:v.require(type(x) is int,'Structural coefficients/labels must be integers')
    integers(a['inherited_filtration_dimensions'])
    v.require(a['increment_dimension']==30 and a['inherited_filtration_dimensions']==[30,12,2,0], 'Wrong increment')
    v.require(a['old_terminal_bound']==60060,'Wrong old support')
    v.require(type(b['measured_scalar_count']) is int and b['measured_scalar_count']==2 and b['reconstructed_saturation'] is False,
              'Two readings do not reconstruct thirty states')
    v.require(type(b['rows']) is list and len(b['rows'])==2 and len(a['blocks'])==2,'Wrong new rows')
    corners=[];intervals=[(i,j) for i in range(7) for j in range(i+2,7)]
    for A,row,block in zip((3,4),b['rows'],a['blocks']):
        v.fields(row,('background','outer_corner','seams','source','path_cost','gain','retained_feature_degree','observed_basis_interval'))
        integers(row['outer_corner']);integers(row['seams']);integers(row['observed_basis_interval'])
        v.require(row['observed_basis_interval']==[0,6],'Reading is not the full-corner coordinate')
        v.fields(block,('background','chain_vertices','basis','left_forgotten_edge_actions','right_forgotten_edge_actions',
                        'all_other_prime_edge_actions','M_basis_indices','L_basis_indices','prime_edges_audited'))
        for key,value in block.items():
            if key!='all_other_prime_edge_actions':integers(value)
        v.require(block['prime_edges_audited']==192,'Incomplete edge ledger')
        v.require(type(row['background']) is int and row['background']==A,'Wrong background')
        v.require(row['outer_corner']==[A,30030*A] and row['seams']==[[A,2*A],[6*A,30*A],[210*A,2310*A]],'Wrong typed row')
        v.require(row['source']=='forgotten(2,3)*forgotten(5,7)*forgotten(11,13)','Wrong source realization')
        v.require(row['path_cost']=='8' and row['gain']==['1','1'] and type(row['retained_feature_degree']) is int and row['retained_feature_degree']==0,'Wrong unit/degree/cost bridge')
        nonzero=[(word,unit_seed(A,word)) for word in permutations(P) if unit_seed(A,word)]
        v.require(nonzero==[(P,1)],'Vacuum seed is not the canonical coefficient')
        words={}
        for swaps in product((0,1),repeat=3):
            word=tuple(p for k,swap in enumerate(swaps) for p in (P[2*k:2*k+2][::-1] if swap else P[2*k:2*k+2]))
            words[word]=(-1)**sum(swaps)
        v.require(len(words)==8 and sum(abs(c) for c in words.values())==8 and sum(c*unit_seed(A,w) for w,c in words.items())==1,'Cubic realization fails')
        chain=[A]
        for p in P:chain.append(chain[-1]*p)
        basis=[{'index':k,'start':chain[i],'end':chain[j],'interval':[i,j]} for k,(i,j) in enumerate(intervals)]
        v.require(block['background']==A and block['chain_vertices']==chain and block['basis']==basis,'Structural/source labels disagree')
        v.require(block['M_basis_indices']==[k for k,(i,j) in enumerate(intervals) if j-i>=4] and block['L_basis_indices']==[intervals.index((0,6))],'Wrong new-block filtration')
        support={(chain[i],chain[j]) for i,j in intervals}
        v.require(all(60060%end for start,end in support),'A2 support overlap; split theorem not applicable')
        corners.append(support)
        for side in ('left','right'):
            expected={}
            for k in range(6):
                entries=[]
                for col,(i,j) in enumerate(intervals):
                    if side=='left' and i==k+1:entries.append([intervals.index((k,j)),col,1])
                    if side=='right' and j==k:entries.append([intervals.index((i,k+1)),col,1])
                if entries:expected[(chain[k],chain[k+1])]=entries
            records=block[side+'_forgotten_edge_actions']
            actual={tuple(x['edge']):x['entries_row_col_value'] for x in records}
            v.require(len(actual)==len(records) and actual==expected,'Wrong labelled source actions')
        v.require(block['all_other_prime_edge_actions']=='zero, including every retained edge','Changed retained-edge action')
        # Independently evaluate the actual I representatives and all packet edges.
        representatives=[]
        for i,j in intervals:
            word=P[i:j];swapped=(word[1],word[0])+word[2:]
            representatives.append((chain[i],chain[j],{word:1,swapped:-1}))
        def evaluate(start,end,col):
            return [col.get(P[i:j],0) if (start,end)==(chain[i],chain[j]) else 0 for i,j in intervals]
        v.require([evaluate(*rep) for rep in representatives]==[[int(i==j) for j in range(15)] for i in range(15)],'Source representatives are not dual')
        v.require(evaluate(A,30030*A,words)==[int(k==intervals.index((0,6))) for k in range(15)],'Cubic source does not realize the observed top coordinate')
        actions={side:{tuple(x['edge']):x['entries_row_col_value'] for x in block[side+'_forgotten_edge_actions']} for side in ('left','right')}
        for mask in range(64):
            start=A*math.prod(P[k] for k in range(6) if mask&(1<<k))
            for k,prime in enumerate(P):
                if mask&(1<<k):continue
                end=start*prime;left=[];right=[]
                for col,(u,w,coeffs) in enumerate(representatives):
                    lv=evaluate(start,w,{(prime,)+word:c for word,c in coeffs.items()}) if end==u else [0]*15
                    rv=evaluate(u,end,{word+(prime,):c for word,c in coeffs.items()}) if w==start else [0]*15
                    left.extend([row,col,c] for row,c in enumerate(lv) if c)
                    right.extend([row,col,c] for row,c in enumerate(rv) if c)
                v.require(left==actions['left'].get((start,end),[]) and right==actions['right'].get((start,end),[]),'Actual source multiplication disagrees')
    v.require(corners[0].isdisjoint(corners[1]),'New block supports overlap')


def parts(base,node,readings):
    v.fields(node,('parts',));rows=node['parts']
    v.require(type(rows) is list and 1<=len(rows)<=3,'Wrong aggregate count')
    B=v.q(base['budget']);next_start=3
    for i,row in enumerate(rows):
        v.fields(row,('start','end','kind','data','gain'))
        start,end=row['start'],row['end']
        v.require(type(start) is int and start==next_start,'Missing/overlapping background')
        v.require((start,end) in ((3,None),(3,3),(4,None),(3,4),(5,None),(4,4)),'Unsupported background group')
        v.require(row['gain']==['1','1'],'Vacuum/aggregate coordinate must be unit calibrated')
        data=v.box(row['data'])
        if row['kind']=='acquired':
            v.require(start==end and start in (3,4) and row['data']==readings[str(start)],'Unbound acquisition')
        else:
            v.require(row['kind']=='prior' and data==(-B/(8*start**16),B/(8*start**16)), 'Unacquired tail must use prior, not a sensor')
        if end is None:v.require(i==len(rows)-1,'Infinite tail must be last');next_start=None
        else:v.require(type(end) is int and end>=start,'Bad end');next_start=end+1
    v.require(next_start is None,'Missing infinite remainder')
    return rows

def expected(base,node,readings):
    rows=parts(base,node,readings)
    raw,gains,sigma,D,B,outer,weights,local=v.problem(base)
    lower=local+sum(8*r['start']**16*v.minimum(v.box(r['data'])) for r in rows)
    if lower>B:return lower,None,None
    R=B-lower;first=min(r['start'] for r in rows if r['kind']=='prior')
    tv=R/(8*first**16);tr=R*D/(32*3**16) # NEVER move the residual tail to 5!
    u=list(outer['vacuum'])
    for row in rows:
        if row['kind']=='acquired':
            lo,hi=v.box(row['data']);u[0]+=lo;u[1]+=hi
    x=v.mul(sigma['positive'],outer['positive']);y=v.mul(sigma['crossed'],outer['crossed'])
    bounds={'vacuum':(u[0]-tv,u[1]+tv),'residual':(x[0]+y[0]-tr,x[1]+y[1]+tr)}
    tail={'remaining_budget':str(R),'vacuum_first_unacquired':first,'residual_first_unacquired':3,
          'vacuum_l1_upper':str(tv),'residual_l1_upper':str(tr),
          'joint_vacuum_weight':str(8*first**16),'joint_residual_weight':str(Q(32*3**16)/D)}
    return lower,bounds,tail

def node(base,n,c,readings):
    v.fields(c,('node_sha256','status','necessary_cost','bounds','tails','witness','positive_task'))
    v.require(c['node_sha256']==v.sha(n),'Node digest mismatch')
    lower,bounds,tail=expected(base,n,readings);B=v.q(base['budget'])
    v.require(v.q(c['necessary_cost'])==lower,'Wrong joint cost')
    v.require(type(c['positive_task']) is bool,'Bad task flag')
    if lower>B:
        v.require(c['status']=='CERTIFIED_INFEASIBLE' and c['bounds'] is None and c['tails'] is None and c['witness'] is None and not c['positive_task'],'Missing contradiction or vacuous claim');return
    v.require(c['status'] in ('CERTIFIED_FEASIBLE','UNRESOLVED'),'Bad nonempty status')
    v.fields(c['bounds'],bounds)
    v.require(all(v.box(c['bounds'][k])==b for k,b in bounds.items()) and c['tails']==tail,'Wrong universal bounds or residual background')
    if c['status']=='CERTIFIED_FEASIBLE':
        w=c['witness'];v.fields(w,('local','parts','other_coefficients'))
        v.fields(w['local'],v.N);v.require(type(w['parts']) is list and len(w['parts'])==len(n['parts']),'Wrong witness dimension')
        v.require(w['other_coefficients']=='zero; each aggregate realized at its first background','Missing source realization')
        raw,gains,sigma,D,B,outer,weights,_=v.problem(base)
        cost=sum(weights[k]*abs(v.q(w['local'][k])) for k in v.N)
        for k in v.N:
            value=v.q(w['local'][k]);v.require(v.subset(raw[k],v.mul(gains[k],(value,value))),'Local witness fails')
        for row,value in zip(n['parts'],w['parts']):
            value=v.q(value);lo,hi=v.box(row['data']);v.require(lo<=value<=hi,'Vacuum witness fails')
            cost+=8*row['start']**16*abs(value)
        v.require(cost<=B,'Joint source witness over budget')
    else:v.require(c['witness'] is None,'Unresolved node has unexpected witness')
    v.require(c['positive_task']==(c['status']=='CERTIFIED_FEASIBLE' and all(b[0]>0 for b in bounds.values())),'Vacuous task positivity')

def edge(base,old,new,e,readings):
    v.fields(e,('old_sha256','new_sha256','groups'))
    v.require(e['old_sha256']==v.sha(old) and e['new_sha256']==v.sha(new),'Edge digest mismatch')
    a=parts(base,old,readings);b=parts(base,new,readings);groups=e['groups']
    v.require(type(groups) is list and len(groups)==len(a),'Wrong partition length')
    flat=[]
    for row,group in zip(a,groups):
        v.require(type(group) is list and group and all(type(j) is int and 0<=j<len(b) for j in group),'Bad partition')
        flat+=group;children=[b[j] for j in group]
        v.require(group==sorted(group) and children[0]['start']==row['start'] and children[-1]['end']==row['end'],'Changed background restriction')
        for left,right in zip(children,children[1:]):v.require(left['end'] is not None and left['end']+1==right['start'],'Noncontiguous restriction')
        v.require(all(x['start']>=row['start'] for x in children),'Understated cost')
        if row['kind']=='acquired':v.require(len(children)==1 and children[0]==row,'Acquired constraint discarded')
        # Prior rows contain [-M/weight,M/weight]; weighted triangle inequality
        # transports the shared budget even when independent box sums are wider.
    v.require(sorted(flat)==list(range(len(b))),'Missing or duplicated coordinate')

def verify(b):
    v.fields(b,('version','contract','base','base_certificate','bridge','readings','nodes','certificates','edges'))
    v.require(type(b['version']) is int and b['version']==1 and b['contract']==CONTRACT,'Wrong bridge contract')
    v.node(b['base'],b['base_certificate']);bridge(b['bridge'])
    v.fields(b['readings'],('3','4'))
    for interval in b['readings'].values():v.box(interval)
    keys=('00','10','01','11');arrows=('00->10','00->01','10->11','01->11')
    v.fields(b['nodes'],keys);v.fields(b['certificates'],keys);v.fields(b['edges'],arrows)
    layouts={'00':[(3,None,'prior')],'10':[(3,3,'acquired'),(4,None,'prior')],
             '01':[(3,3,'prior'),(4,4,'acquired'),(5,None,'prior')],
             '11':[(3,3,'acquired'),(4,4,'acquired'),(5,None,'prior')]}
    for key in keys:
        n=b['nodes'][key]
        node(b['base'],n,b['certificates'][key],b['readings'])
        v.require([(r['start'],r['end'],r['kind']) for r in n['parts']]==layouts[key],'Unsupported acquisition node')
    for name in arrows:
        start,end=name.split('->');edge(b['base'],b['nodes'][start],b['nodes'][end],b['edges'][name],b['readings'])
    def compose(first,second):return [sorted(k for j in group for k in b['edges'][second]['groups'][j]) for group in b['edges'][first]['groups']]
    left=compose('00->10','10->11');right=compose('00->01','01->11')
    v.require(left==right==[[0,1,2]],'Restriction routes disagree')
    direct={'old_sha256':v.sha(b['nodes']['00']),'new_sha256':v.sha(b['nodes']['11']),'groups':left}
    edge(b['base'],b['nodes']['00'],b['nodes']['11'],direct,b['readings'])
    return True

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python verify_order16_vacuum_bridge.py bundle.json')
    verify(v.load(sys.argv[1]))
    print('VALID order-16 vacuum acquisition square; source/calibration/acquisition/support premises external; no equivariant tail aggregation or full-state reconstruction')
