"""Independent API verifier. Expected state/query MUST come from the caller.

Passing the packet's own descriptor as the expected history defeats this trust
boundary. Digests bind statements; they do not authenticate frame truth.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,gzip,copy
from verify_symbolic_tail_interface import support,lift,check_lp
if not __debug__:raise RuntimeError('Verification requires assertions enabled')
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rational(value):
    assert type(value) in (int,str,Q), 'EXACT_RATIONAL_REQUIRED'
    return str(Q(value))
def pair(values):
    assert isinstance(values,(tuple,list)) and len(values)==2, 'UNDECLARED_OBSERVABLE'
    return [rational(v) for v in values]
def canonical_state(state):
    assert set(state)=={'schema','source_rule','source_binding','m','frames'}
    assert isinstance(state['frames'],(tuple,list))
    assert state['schema']=='retained-tail-state-v1' and type(state['m']) is int and state['m']>=2
    assert type(state['source_binding']) is str and state['source_binding']
    rule={'cap':'100+2j','slope':'128^-j','range':'0<=j<m'};assert state['source_rule']==rule
    frames=[]
    for row in state['frames']:
        assert set(row)=={'a','b'}
        frames.append({'a':pair(row['a']),'b':rational(row['b'])})
    return {'schema':'retained-tail-state-v1','source_rule':rule,'source_binding':state['source_binding'],'m':state['m'],'frames':frames}
def canonical_query(query):
    kind=query['kind'];assert kind in ('point-membership','linear-maximum')
    field='point' if kind=='point-membership' else 'objective';assert set(query)=={'kind',field}
    return {'kind':kind,field:pair(query[field])}
def verify_certificate(expected_state,expected_query,packet):
    state=canonical_state(expected_state);query=canonical_query(expected_query)
    assert set(packet)=={'schema','state','state_digest','query','query_digest','result'}
    assert packet['schema']=='state-bound-tail-query-v1'
    assert packet['state']==state and packet['query']==query
    assert packet['state_digest']==digest(state)
    assert packet['query_digest']==digest({'state_digest':digest(state),'query':query})
    frames=[(tuple(map(Q,row['a'])),Q(row['b'])) for row in state['frames']];result=packet['result']
    if query['kind']=='linear-maximum':
        check_lp({'m':state['m'],'frames':state['frames'],'objective':query['objective'],'result':result},frames)
        return {'verified':True,'kind':query['kind'],'status':result['status'],
                'value':result.get('value')}
    point=tuple(map(Q,query['point']));assert type(result['admitted']) is bool
    if result['reason']=='RETAINED_FRAME':
        assert set(result)=={'admitted','reason','frame_index','lhs','upper'} and not result['admitted']
        i=result['frame_index'];assert type(i) is int and 0<=i<len(frames)
        a,b=frames[i];lhs=sum(x*y for x,y in zip(a,point))
        assert Q(result['lhs'])==lhs>b==Q(result['upper'])
    else:
        assert all(sum(x*y for x,y in zip(a,point))<=b for a,b in frames)
        if result['reason']=='SOURCE_LIFT':
            assert set(result)=={'admitted','reason','lift','vertical_bounds'} and result['admitted']
            lo,hi=lift(state['m'],point,result['lift']);assert list(map(Q,result['vertical_bounds']))==[lo,hi]
        else:
            assert result['reason']=='SOURCE_SEPARATOR' and not result['admitted']
            assert set(result)=={'admitted','reason','separator'}
            a,b=support(state['m'],result['separator']);assert sum(x*y for x,y in zip(a,point))>b
    return {'verified':True,'kind':query['kind'],'admitted':result['admitted'],'reason':result['reason']}

def main():
    cp=OUT/'state-bound-tail-query-contract.json';rp=OUT/'state-bound-tail-query.json';pp=OUT/'state-bound-tail-query-packet.json.gz'
    c=json.loads(cp.read_text());r=json.loads(rp.read_text())
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    assert sha(Path(__file__).with_name('check_symbolic_tail_interface.py'))==c['engine_sha256']
    assert sha(ROOT/'grothendieck/results/two-moment-tail-complexity.json')==c['source_sha256']
    with gzip.open(pp,'rt') as f:p=json.load(f)
    binding=c['source_binding'];frames=[(('1','0'),'50'),(('-1','0'),'-25'),(('-1/2','1'),'0'),(('0','-1'),'-30')]
    # Build expected histories from the frozen contract, NOT certificate data.
    states={}
    for m in c['m_values']:
        for stage in range(5):
            states[m,stage]={'schema':'retained-tail-state-v1','source_rule':{'cap':'100+2j','slope':'128^-j','range':'0<=j<m'},
              'source_binding':binding,'m':m,'frames':[{'a':list(a),'b':b} for a,b in frames[:stage]]}
    expected_cases={(m,s,kind,i) for m in c['m_values'] for s in range(5)
                    for kind,count in (('point-membership',len(c['points'])),('linear-maximum',len(c['objectives']))) for i in range(count)}
    assert len(p['cases'])==len(expected_cases) and {(x['m'],x['stage'],x['kind'],x['query_index']) for x in p['cases']}==expected_cases
    for case in p['cases']:
        state=states[case['m'],case['stage']]
        expected=({'kind':'point-membership','point':c['points'][case['query_index']]} if case['kind']=='point-membership'
                  else {'kind':'linear-maximum','objective':c['objectives'][case['query_index']]})
        result=verify_certificate(state,expected,case['certificate'])
        assert result['verified']
    attacks=0
    assert {a['name'] for a in p['attacks']}==set(c['attack_requests'])
    for attack in p['attacks']:
        assert {k:attack[k] for k in ('expected_m','expected_stage','expected_query')}==c['attack_requests'][attack['name']]
        state=states[attack['expected_m'],attack['expected_stage']]
        expected=attack['expected_query']
        # The attack specification is a fixed replay request, not a claimed history.
        if attack['name']=='foreign_source_binding':state={**state,'source_binding':binding+':another-run'}
        try:verify_certificate(state,expected,attack['certificate'])
        except (AssertionError,ValueError,KeyError,IndexError,TypeError,ZeroDivisionError):attacks+=1
        else:raise AssertionError('accepted attack '+attack['name'])
    assert attacks==len(p['attacks'])==10
    control=next(x for x in p['cases'] if (x['m'],x['stage'],x['kind'],x['query_index'])==(2,0,'point-membership',0))['certificate']
    state=states[2,0];query={'kind':'point-membership','point':['0','0']}
    malformed=[(state,{'kind':'point-membership','point':v}) for v in ([False,0],[0.0,0],'00',[0,0,0])]
    malformed.append(({**state,'hidden_atom_constraint':'t_0=1'},query))
    malformed.append((state,{**query,'audit':'t_0<=0'}))
    bad_state=copy.deepcopy(state);bad_state['frames']=[{'a':['0','0'],'b':'0','hidden_audit':True}]
    malformed.append((bad_state,query));bad_state=copy.deepcopy(state);bad_state['frames']=[{'a':['0','0','1'],'b':'0'}]
    malformed.append((bad_state,query))
    for expected_state,expected_query in malformed:
        try:verify_certificate(expected_state,expected_query,control)
        except (AssertionError,ValueError,KeyError,IndexError,TypeError,ZeroDivisionError):pass
        else:raise AssertionError('malformed expected context admitted')
    result={'passed':True,'report_sha256':sha(rp),'valid_query_certificates':len(p['cases']),'binding_and_proof_attacks_rejected':attacks,
      'malformed_expected_contexts_rejected':len(malformed),
      'trust_boundary':'Expected history and request reconstructed independently of the certificate; immutable state initialization and frame truth still require trust.',
      'scope':c['scope']}
    (OUT/'state-bound-tail-query-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
