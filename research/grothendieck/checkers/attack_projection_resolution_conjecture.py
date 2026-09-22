"""Attempt: doubling the proof-only projection resolves the frozen middle task.

Never rewrites deployed inputs or promotes a failed conjecture. Reuses the
owning window functions via AST extraction to avoid their deployment side effects.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import floor,isqrt
import ast,importlib.util,json,hashlib,copy
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE.parent/'results'
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r=module('projection',HERE/'refine_fixed_bin_response.py');t=module('task',HERE/'three_channel_source_task.py')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ends(x):return Q(str(x.lower().fmpq())),Q(str(x.upper().fmpq()))
def ball(x):return arb(x.numerator)/x.denominator
def enc(x):
    lo,hi=ends(x);return {'lower':str(lo),'upper':str(hi),'display':x.str(24)}
protected=[OUT/n for n in ('three-channel-source-task-calibration-bulk-norm.json','bulk-response-norm-refinement.json',
 'calibration-refinement-frozen-inputs.json','time-bin-cubic-observer.json','three-channel-cubic-protocol.json')]
hashes={p.name:sha(p) for p in protected}
parent=t.SourceTask(protected[0]);norm=json.loads(protected[1].read_text(encoding='utf-8'))
frozen=json.loads(protected[2].read_text(encoding='utf-8'))
ctx.prec=6144
bounds=[ball(Q(side['new_squared_norm']['upper'])) for side in norm['sides']]
print('Computing 272-dimensional proof-only projection...',flush=True)
C,h,diagnostics=r.refine(bounds,subdivisions=16,bits=6144)
new_C=ends(C)
old_C=tuple(t.pair(parent.cal['refinement_evidence'][key]) for key in ('C_bin_lower','C_bin_upper'))
assert old_C[0]<new_C[0]<new_C[1]<old_C[1]
print('C:',C.str(24),flush=True)
# Import ONLY the owning function definitions; no runpy, output writes or
# expensive unrelated deployment regeneration. Mathematical quadrature unchanged.
source=HERE/'certify_robust_cubic_template_measurement.py'
parsed=ast.parse(source.read_text(encoding='utf-8'))
names={'pos_ball','sym_ball','primes_to','window'}
functions=[node for node in parsed.body if isinstance(node,ast.FunctionDef) and node.name in names]
assert {node.name for node in functions}==names
ctx.prec=192
PI=arb.pi();s=arb(7)/2
namespace={'arb':arb,'floor':floor,'isqrt':isqrt,'PI':PI,'V':arb(32),'CELLS':262144,'step':arb(32)/262144}
exec(compile(ast.Module(body=functions,type_ignores=[]),str(source),'exec'),namespace)
print('Replaying unchanged whole-cell theta enclosures...',flush=True)
A=namespace['window'](2,2,'A1');B=namespace['window'](12,5,'B1')
partial=arb(0);N=4096
for p in namespace['primes_to'](N):
    n=p
    while n<=N:partial+=arb(p).log()*arb(n)**(-s);n*=p
n=arb(N);tail=n**(1-s)*(n.log()/(s-1)+1/(s-1)**2)
L=1/s+1/(s-1)-PI.log()/2+(s/2).digamma()/2-partial-namespace['pos_ball'](tail)
assert A['mu']-L>0 and B['mu']-L>0 and h>0

def gain(c):return 2*A['X']*B['X']*(c+h*(A['mu']-L))*(c+h*(B['mu']-L))
G=gain(C);gl,gu=ends(G)
# Recheck the parent gain from the SAME window/L boxes and its stored C range.
parent_replay=ends(gain(ball(old_C[0]).union(ball(old_C[1]))))
for mode in ('private','reuse'):
    before=parent.calibrations(mode)['positive']
    assert before[0]<=gl<gu<=before[1]
    # Roundoff at different working precision may differ at tiny endpoints;
    # the reconstructed parent and archived parent must overlap tightly.
    assert max(before[0],parent_replay[0])<min(before[1],parent_replay[1])
    assert abs(before[0]-parent_replay[0])+abs(before[1]-parent_replay[1])<(before[1]-before[0])/1000000
lo=t.interval(frozen['cases']['private']['middle_threshold']['raw']['positive'])[0]
threshold=lo/Q(499,400)
low_gain=gain(ball(new_C[0]));high_gain=gain(ball(new_C[1]))
# Monotonicity in C follows from positive X,h and both positive factors.
# If BOTH inequalities hold, every exact C in this new interval still has a
# Cartesian gain enclosure straddling the threshold with the frozen windows/L.
floor_proved=ends(high_gain)[0]<threshold<ends(low_gain)[1]
cal=copy.deepcopy(parent.cal)
cal['parent_calibration_file']=protected[0].name;cal['parent_calibration_sha256']=sha(protected[0])
for mode in ('private','reuse'):
    cal['diagonal_refinements'][mode]['positive']={'lower':[str(gl.numerator),str(gl.denominator)],'upper':[str(gu.numerator),str(gu.denominator)]}
cal['refinement_evidence']={'method':'272-dimensional-proof-only-fixed-hat-projection','projection_dimension':272,
 'projection_bits':6144,'theta_cells':262144,'theta_bits':192,'scaled_cutoff':32,
 'deployed_filter_sha256':sha(protected[3]),'frozen_inputs_sha256':sha(protected[2]),
 'norm_evidence_sha256':sha(protected[1]),'window_code_sha256':sha(source),
 'C_bin_lower':[str(new_C[0].numerator),str(new_C[0].denominator)],
 'C_bin_upper':[str(new_C[1].numerator),str(new_C[1].denominator)]}
cal_path=OUT/'three-channel-source-task-calibration-projection272.json'
cal_path.write_text(json.dumps(cal,indent=2)+'\n',encoding='utf-8');engine=t.SourceTask(cal_path)
results={mode:engine.certify(frozen['cases'][mode]['middle_threshold']) for mode in ('private','reuse')}
resolved=all(x['status']!='UNRESOLVED' for x in results.values())
assert hashes=={p.name:sha(p) for p in protected}
report={'conjecture':'272-dimensional proof-only projection resolves both frozen middle cases without changing theta quadrature',
 'verdict':'supported_by_certificates' if resolved else 'refuted_for_this_declared_method_and_precision',
 'protected_file_hashes':hashes,'calibration_file':cal_path.name,'calibration_sha256':sha(cal_path),
 'C_before':list(map(str,old_C)),
 'C_after':{'lower':str(new_C[0]),'upper':str(new_C[1]),'display':C.str(24)},'C_width_reduction':str((old_C[1]-old_C[0])/(new_C[1]-new_C[0])),
 'gain_after':enc(G),'threshold':str(threshold),'fixed_box_floor_proved':floor_proved,
 'gain_at_low_C':enc(low_gain),'gain_at_high_C':enc(high_gain),
 'windows':{name:{key:enc(obj[key]) for key in ('X','mu','tail_bound')} for name,obj in (('A1',A),('B1',B))},
 'L':enc(L),'h':enc(h),'projection_diagnostics':diagnostics,'middle_cases':results,
 'scope':'Fresh whole-cell theta/rigorous projection computation; floor concerns the current Cartesian enclosures, not physical ambiguity. No acquisition or detector/prior change.'}
(OUT/'projection-resolution-conjecture-attack.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':report['verdict'],'C':C.str(24),'gain':G.str(24),'fixed_box_floor_proved':floor_proved,
                  'statuses':{m:x['status'] for m,x in results.items()}},indent=2))
