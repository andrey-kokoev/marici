"""Explicit source-coupled rational tail task; not the actual prime-tail task."""
from pathlib import Path
from fractions import Fraction as Q
from collections import deque
import json,gzip,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def mode(channel,origin):return 'even_support' if channel==origin else 'adjacent_capacity'
def scale(end):return Q(1,2) if end&4 else Q(1)

def verify_lp(p,cutoff=4):
    assert set(p)=={'mode','m','primal','dual','finite_optimum','uniform_tail_error','full_lower','full_upper'}
    assert type(p['m']) is int and p['m']==cutoff and cutoff in (4,8)
    assert len(p['primal'])==cutoff and len(p['dual'])==cutoff+cutoff*(cutoff+1)//2
    assert p['mode'] in ('even_support','adjacent_capacity')
    values=p['primal']+p['dual']+[p[k] for k in ('finite_optimum','uniform_tail_error','full_lower','full_upper')]
    assert all(type(x) is str and len(x)<=24 for x in values)
    rationals=list(map(Q,values));assert all(abs(q.numerator).bit_length()<=32 and q.denominator.bit_length()<=32 for q in rationals)
    x=list(map(Q,p['primal']));y=list(map(Q,p['dual']));m=cutoff
    assert len(x)==m and len(y)==m+m*(m+1)//2 and all(z>=0 for z in x+y)
    rows=[([i],Q(0 if p['mode']=='even_support' and i%2==0 else 1)) for i in range(m)]
    for a in range(m):
        for b in range(a+1,m+1):
            cap=sum(i%2==1 for i in range(a,b)) if p['mode']=='even_support' else (b-a+1)//2
            rows.append((list(range(a,b)),Q(cap)))
    assert all(sum(x[i] for i in ids)<=cap for ids,cap in rows)
    assert all(sum(y[j] for j,(ids,_) in enumerate(rows) if i in ids)>=Q(1,2**(i+1)) for i in range(m))
    primal=-sum(x[i]/2**(i+1) for i in range(m));dual=-sum(y[j]*cap for j,(_,cap) in enumerate(rows))
    assert primal==dual==Q(p['finite_optimum'])==Q(p['full_upper'])
    eps=Q(1,2**m);assert Q(p['uniform_tail_error'])==eps and Q(p['full_lower'])==dual-eps
    return dual-eps,primal

def main():
    source=OUT/'causal-interface-construction.json';base=OUT/'causal-interface-construction-contract.json'
    tail=ROOT/'grothendieck/results/tail-witness-separator.json';carrier=ROOT/'voevodsky/results/decomposition-coherence-carriers.json.gz'
    runtime=OUT/'relational-live-witness-runtime.json'
    data=load(source);parent=load(base);numeric=load(tail);compiled=load(runtime)
    with gzip.open(carrier,'rt') as f:decomposed=json.load(f)
    task={'objective':'F=sum_n -2^-n (x_n+y_n)','threshold':'-31/32','strict_test':'certified lower > threshold',
      'origin_zero':['even_support','adjacent_capacity'],'origin_one':['adjacent_capacity','even_support'],
      'initial_tail_carrier':'Independent normalized carriers in the two source-selected modes; any admitted pair may initialize.',
      'scale':'1 before accepted source(2,m), 1/2 afterwards; all atom and interval bounds scale together.',
      'tail_update':'Accepted source(2,m) multiplies BOTH infinite tails by 1/2. Every other accepted or rejected base action leaves tails unchanged.',
      'tail_continuity':'Normalized atoms <=1 give per-channel absolute suffix <=2^-m; scaled suffix <=scale*2^-m.',
      'calibration_constructor':'A truthful accepted audit-origin(b) binds the channel mode to b and the current source cut. An LP packet proves a universal bound on that carrier, not an observation of a chosen extremizer.',
      'publication_constructor':'New publish-tail-bound output, not reinterpretation of base issue(0/1). Requires a delivered source-origin receipt at a post-cut state, coherent calibration witnesses and a strict combined lower bound.'}
    contract={'schema':'mixed-source-tail-certificate-v1','task':task,'task_sha256':digest(task),
      'base_context':parent['context'],'input_sha256':{str(p.relative_to(ROOT)):sha(p) for p in (source,base,tail,carrier,runtime)},
      'frozen_controls':['opposite-origin even/even packets','coherent packets with suffix omitted','coherent half-scale control','reverse-scaling authorization attempt'],
      'bounds':{'channels':2,'cutoff':4,'primal_entries_per_channel':4,'dual_entries_per_channel':14,'rational_numerator_denominator_bits':32,
        'origin_possibility_mask_bits':2,'source_cut_bits':6,'retained_behavioral_rows':70,'retained_transition_cells':1260},
      'trust':'Truthful calibration audits, delivered receipts, fixed run/task/cut bindings and existing atomic source authorization. Hash equality is not authentication.',
      'scope':'Explicit rational control coupling. No actual-prime or signed-kernel calibration correspondence is asserted.'}
    cp=OUT/'mixed-source-tail-certificate-contract.json';save(cp,contract)
    context={'base':parent['context'],'mixed_task_sha256':digest(task)};threshold=Q(task['threshold'])
    templates={(p['mode'],p['m']):p for p in numeric['packets']}
    for name in ('even_support','adjacent_capacity'):
        for m in (4,8):verify_lp(templates[name,m],m)
    rows={(tuple(r['views']),r['origin']):r for r in compiled['lifted_rows']}
    views=[tuple(data['naive_local_partitions'][n][i] for n in ('source','acquisition','recipient')) for i in range(70)]
    def make_packet(channel,origin,end):
        return {'context':context,'channel':channel,'origin':origin,'cut':end,'scale':str(scale(end)),
                'accepted_calibration_audit':['audit-origin',origin],
                'lp':copy.deepcopy(templates[mode(channel,origin),4])}
    def validate_partial(p,end):
        assert set(p)=={'context','channel','origin','cut','scale','accepted_calibration_audit','lp'}
        assert p['context']==context and type(p['cut']) is int and p['cut']==end and p['scale']==str(scale(end))
        assert type(p['channel']) is int and p['channel'] in (0,1) and type(p['origin']) is int and p['origin'] in (0,1)
        assert p['accepted_calibration_audit']==['audit-origin',p['origin']]
        assert p['lp']['mode']==mode(p['channel'],p['origin'])
        lo,hi=verify_lp(p['lp']);return scale(end)*lo,scale(end)*hi
    def assemble(v,mask,packets):
        possible=[b for b in (0,1) if mask&(1<<b) and (tuple(v),b) in rows]
        if not possible:return {'status':'INVALID_INITIAL_FIBER'}
        out=rows[tuple(v),possible[0]]['output'];end,received=out[1:3]
        try:
            assert len(packets)==2 and sorted(p['channel'] for p in packets)==[0,1]
            bounds=[validate_partial(p,end) for p in packets]
        except (AssertionError,ValueError,KeyError,ZeroDivisionError):return {'status':'INVALID_PACKET'}
        # Intersect with the same source witness, not a new witness per packet.
        live=[b for b in possible if all(p['origin']==b for p in packets)]
        lower=sum(lo for lo,hi in bounds);result={'lower':str(lower),'live_origins':live}
        if not live:result['status']='INCOMPATIBLE_SOURCE'
        elif not end&8 or any(received!=b for b in live):result['status']='NOT_AUTHORIZED'
        elif lower<=threshold:result['status']='NO_STRICT_CERTIFICATE'
        else:result['status']='CERTIFIED'
        return result
    def initial_mask(v):return sum(1<<b for b in (0,1) if (tuple(v),b) in rows)
    cases=[]
    for b in (0,1):
        weak=data['states'].index([11,b,b,b,None]);strong=data['states'].index([15,b,b,b,None])
        incompatible=[make_packet(0,0,11),make_packet(1,1,11)]
        coherent=[make_packet(ch,b,11) for ch in (0,1)]
        good=[make_packet(ch,b,15) for ch in (0,1)]
        for name,i,packets,expected in [('opposite_origins',weak,incompatible,'INCOMPATIBLE_SOURCE'),
              ('coherent_unscaled',weak,coherent,'NO_STRICT_CERTIFICATE'),('compatible_scaled',strong,good,'CERTIFIED')]:
            result=assemble(views[i],initial_mask(views[i]),packets);assert result['status']==expected
            cases.append({'name':name,'actual_origin':b,'source_state':i,'views':list(views[i]),'packets':packets,'result':result})
        assert sum(validate_partial(p,11)[0] for p in incompatible)==-Q(3,4)>threshold
        assert sum(validate_partial(p,11)[1] for p in coherent)==-Q(15,16)>threshold
        # A real globally admitted zero-extended counterexample, not a merely
        # hypothetical infimum, refutes both naive positive classifications.
        actual=[templates[mode(ch,b),8] for ch in (0,1)]
        value=sum(verify_lp(p,8)[1] for p in actual);assert value==-Q(255,256)<threshold
    # Single-purpose mutations reject even when scalar inequalities still pass.
    valid=copy.deepcopy(cases[2]);v=tuple(valid['views']);negative_controls={}
    for mutation in ('wrong_context','wrong_cut','wrong_mode','missing_tail','corrupt_dual'):
        pp=copy.deepcopy(valid['packets'])
        if mutation=='wrong_context':pp[0]['context']['mixed_task_sha256']='foreign'
        elif mutation=='wrong_cut':pp[0]['cut']=11
        elif mutation=='wrong_mode':pp[0]['lp']['mode']='adjacent_capacity'
        elif mutation=='missing_tail':pp[0]['lp']['uniform_tail_error']='0'
        else:pp[0]['lp']['dual'][1]=str(Q(pp[0]['lp']['dual'][1])+1)
        result=assemble(v,initial_mask(v),pp);assert result['status']=='INVALID_PACKET';negative_controls[mutation]=result
    # Bind the infinite-tail constructor to every actual base transition.
    scaled_steps=0
    for i,s in enumerate(data['states']):
        for label,(accepted,j) in zip(parent['labels'],data['transitions'][i]):
            t=data['states'][j];factor=Q(1,2) if accepted and label[0]=='source' and label[1]==2 else Q(1)
            assert s[1]==t[1] and scale(t[0])==factor*scale(s[0]);scaled_steps+=factor!=1
    a=data['states'].index([11,0,0,0,None]);b=data['states'].index([15,0,0,0,None]);action=parent['labels'].index(['source',2,0])
    assert data['transitions'][a][action]==[True,b]
    assert data['transitions'][b][action]==[False,b]
    # Regrouping checks evaluate the mixed constructor on each independently
    # generated carrier, then check its verdicts through all comparison maps.
    index={tuple(s):i for i,s in enumerate(data['states'])};verdicts=[]
    for carrier_data in decomposed['carriers']:
        results=[]
        for s in carrier_data['canonical_states']:
            i=index[tuple(s)];packets=[make_packet(ch,s[1],s[0]) for ch in (0,1)]
            results.append(assemble(views[i],initial_mask(views[i]),packets))
        verdicts.append(results)
    comparisons=0
    for mapping in decomposed['comparisons']:
        a,b=mapping['from'],mapping['to']
        for i,j in enumerate(mapping['map']):
            assert verdicts[a][i]==verdicts[b][j];comparisons+=1
    packet={'cases':cases,'negative_controls':negative_controls,
      'counterexamples':[{'origin':b,'scale':'1','channels':[templates[mode(ch,b),8] for ch in (0,1)],'total':'-255/256','extension':'zero after n=8'} for b in (0,1)],
      'regrouping_verdicts':verdicts,'reverse_control':{'label':['source',2,0],'predecessor_state':data['states'].index([11,0,0,0,None]),
          'successor_state':data['states'].index([15,0,0,0,None]),'backward_compatible':True,'forward_reexecution_accepted':False}}
    pp=OUT/'mixed-source-tail-certificate-packet.json';save(pp,packet)
    report={'verdict':'MIXED_CONTROL_PASSES','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'threshold':str(threshold),'incompatible_scalar_lower':'-3/4','coherent_without_tail':'-15/16',
      'coherent_full_lower':'-17/16','admitted_counterexample':'-255/256','compatible_scaled_lower':'-17/32',
      'source_tail_transition_checks':1260,'accepted_halving_transitions':scaled_steps,
      'independent_decompositions':52,'mixed_verdict_transport_checks':comparisons,
      'retained_per_channel_rationals':18,'scope':contract['scope'],
      'conclusion':'Joint source admission and certified remainder are independently necessary in this mixed control; a compatible source-authorized positive certificate survives all ownership regroupings.'}
    for path,h in contract['input_sha256'].items():assert sha(ROOT/path)==h
    save(OUT/'mixed-source-tail-certificate.json',report);print(json.dumps(report,indent=2))
if __name__=='__main__':main()
