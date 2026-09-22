"""Exact decoder for the declared seven-dimensional forgotten ideal slice.

Usage: python reconstruct_seven_dimensional_ideal_slice.py READINGS.json
       python reconstruct_seven_dimensional_ideal_slice.py --model

Standard library only. No source archive, discovery script or stored source
coefficients are consulted. The source-domain assumption is NOT inferred
from these seven values. This exact interface accepts rational strings only.
"""
from fractions import Fraction
from pathlib import Path
from math import prod
import hashlib,json,sys

IDS=('vacuum_PPP','vacuum_QQQ','first_block_P','blocks_1P_2P',
     'blocks_1P_3P','blocks_1Q_2P','blocks_1Q_3P')
SEAMS=(
 ((0,1),(3,7),(15,31)),
 ((0,2),(3,11),(15,47)),
 ((0,1),(1,3)),
 ((0,1),(3,7)),
 ((0,1),(15,31)),
 ((0,2),(3,7)),
 ((0,2),(15,31)))
PRIMES=(2,3,5,7,11,13)
# Each row gives one of the eight path coefficients in reading order IDS.
INVERSE=(
 (1,0,0,0,0,0,0),
 (0,1,1,0,0,1,1),
 (-1,0,0,0,1,0,0),
 (0,-1,-1,0,0,-1,0),
 (-1,0,0,1,0,0,0),
 (0,-1,-1,0,0,0,-1),
 (1,0,1,-1,-1,0,0),
 (0,1,0,0,0,0,0))
def vertex(mask):return 2*prod(p for i,p in enumerate(PRIMES) if mask&(1<<i))
def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'))
def path(bits):
    events=[]
    for i in range(3):
        pair=(2*i,2*i+1)
        events.extend(reversed(pair) if bits&(1<<i) else pair)
    return tuple(events)
MODEL={
 'id':'background-two-forgotten-three-diamond-ideal-v1',
 'source_domain':{'background':2,'outer_corner':[2,60060],
   'ordered_blocks':[[2,3],[5,7],[11,13]],'marks':'all forgotten',
   'support':'the eight blockwise P/Q paths only','constraint':'sum of eight path coefficients = 0',
   'dimension':7,'assumption':'domain membership must be justified externally'},
 'path_order':'integer bit mask 0..7; bit i reverses block i+1',
 'readings':[{'id':name,'cut_order':len(seams),
   'mask_seams':[['e',a,b,0] for a,b in seams],
   'arithmetic_seams':[[vertex(a),vertex(b)] for a,b in seams],
   'outer_corner':[2,60060],'buffers':'vacuum','normalization':'unscaled unit-vacuum record coefficient'}
   for name,seams in zip(IDS,SEAMS)],
 'inverse_matrix_path_coefficients_from_readings':[list(row) for row in INVERSE]}
MODEL_SHA256=hashlib.sha256(canonical(MODEL).encode()).hexdigest()

def require(ok,message):
    if not ok:raise ValueError(message)
def rational(x):
    require(type(x) is str,'readings must be exact rational strings, not JSON numbers')
    try:return Fraction(x)
    except (ValueError,ZeroDivisionError) as exc:raise ValueError('invalid rational reading') from exc

def reconstruct(payload):
    require(type(payload) is dict,'expected object')
    required={'schema','model_sha256','readings'}
    require(required.issubset(payload) and set(payload)<=required|{'terminal_check'},'unexpected or missing fields')
    require(payload['schema']=='seven-dimensional-ideal-readings-v1','schema mismatch')
    require(payload['model_sha256']==MODEL_SHA256,'source/reading model digest mismatch')
    readings=payload['readings']
    require(type(readings) is dict and set(readings)==set(IDS),'exactly the seven labelled readings required')
    y=[rational(readings[name]) for name in IDS]
    if 'terminal_check' in payload:
        require(rational(payload['terminal_check'])==0,'nonzero terminal check contradicts the ideal-domain assumption')
    a=[sum((c*v for c,v in zip(row,y)),Fraction(0)) for row in INVERSE]
    require(sum(a)==0,'internal ideal reconstruction error')
    # These coordinate equations check consistency of the decoder, NOT
    # whether the unknown physical source is within the asserted domain.
    forward=(a[0],a[7],a[0]+a[2]+a[4]+a[6],a[0]+a[4],
             a[0]+a[2],a[1]+a[5],a[1]+a[3])
    require(list(forward)==y,'internal reading reconstruction error')
    moments=[sum((a[b] for b in range(8) if b&t==t),Fraction(0)) for t in range(8)]
    terms=[]
    for b,c in enumerate(a):
        if not c:continue
        events=path(b);vertices=[2]
        for event in events:vertices.append(vertices[-1]*PRIMES[event])
        terms.append({'reversed_blocks':[i+1 for i in range(3) if b&(1<<i)],
           'event_primes':[PRIMES[i] for i in events],'marks':[0]*6,
           'vertices':vertices,'coefficient':str(c)})
    nonzero_orders=[t.bit_count() for t,m in enumerate(moments) if m]
    return {'schema':'seven-dimensional-ideal-reconstruction-v1','model_sha256':MODEL_SHA256,
      'source_terms':terms,'path_coefficients':[str(c) for c in a],
      'interaction_coefficients':{str(t):str(c) for t,c in enumerate(moments)},
      'ideal_order_in_declared_slice':min(nonzero_orders) if nonzero_orders else 'zero belongs to every ideal power',
      'filtration_membership':{'I':True,'I_squared':all(not moments[t] for t in (1,2,4)),
        'I_cubed':all(not moments[t] for t in (1,2,3,4,5,6)),
        'I_fourth':not any(a)},
      'terminal_check_supplied':'terminal_check' in payload,
      'scope':'Unique exact source conditional on the declared support and ideal constraint. Neither seven-reading agreement nor a zero terminal check certifies that support. Not a global source inverse.'}

def no_duplicates(items):
    out={}
    for k,v in items:
        require(k not in out,'duplicate JSON key');out[k]=v
    return out
def invalid_constant(value):raise ValueError('nonfinite JSON number')
def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=no_duplicates,parse_constant=invalid_constant)
if __name__=='__main__':
    try:
        require(len(sys.argv)==2,'usage: reconstruct_seven_dimensional_ideal_slice.py READINGS.json | --model')
        result=({'model':MODEL,'model_sha256':MODEL_SHA256} if sys.argv[1]=='--model' else reconstruct(load(sys.argv[1])))
        print(json.dumps(result,indent=2))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print('REJECTED: '+str(exc),file=sys.stderr);sys.exit(1)
