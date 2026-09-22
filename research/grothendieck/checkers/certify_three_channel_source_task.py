"""Fresh gamma=1 task calibration and three-valued synthetic certificates."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
import runpy,importlib.util,json,hashlib,copy
from flint import arb,ctx

HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'results'
protocol_build=runpy.run_path(str(HERE/'certify_three_channel_cubic_protocol.py'))
exact=protocol_build['exact']
ctx.prec=384
qp=lambda q:[str(q.numerator),str(q.denominator)]
bounds=lambda x:{'lower':qp(x.lower().fmpq()),'upper':qp(x.upper().fmpq())}
L=exact['L'];log2=arb(2).log();pi=arb.pi()
assert L>0 and log2*(3*log2).tanh()>L
constant=(1+arb(6).log())*(1+arb(210).log())/18
assert constant<1
assert arb(16)>2/(1+arb(3).log())
multiplier=(1+arb(3).log())**2
# Owning completed-theta H4 tail majorant, also needed for actual-letter admissibility.
q0=4*pi
H0=1+16*(-3*q0).exp()/(1-(arb(3)/2)**4*(-5*q0).exp())
forcing=8*pi**(-arb(9)/2)*H0**2*(-2*q0).exp()*sum(
    (arb(comb(10,k)*factorial(k))*q0**(10-k)/(2**(k+1)) for k in range(11)),arb(0))
assert forcing<arb(1)/4
protocol_path=OUT/'three-channel-cubic-protocol.json'
calibration={'schema':'marici.grothendieck.three-channel-source-task-calibration.v1',
             'protocol_file':protocol_path.name,'protocol_sha256':hashlib.sha256(protocol_path.read_bytes()).hexdigest(),
             'source_functional':{'positive':bounds(exact['S0']),'crossed':bounds(exact['Sx'])},
             'residual_tail_multiplier_upper':qp(multiplier.upper().fmpq()),
             'uniform_bounds':{'residual_coefficient':'abs(sigma0(A)),abs(sigmax(A)) <= (1+log A)^2, A>=2',
                               'coefficient_bound_constant':str(constant),
                               'complete_forcing_H4_squared_upper':str(forcing)},
             'source_domain':'Real coefficients in the 270 two-feature cubic products V_A plus the line spanned by k_A, at each admitted integer A>=2; all corner labels retained.',
             'prior':'sum_A A^16 [32 sum_j |a_(A,j)|+8|b_A|] <= M. This is an external assumption, not inferred from measurements.',
             'target':'u_A=b_A, t_A=sigma0(A)*a_(A,0)+sigmax(A)*a_(A,x); T=sum_A t_A is per w_seam^2.',
             'scope':'Source functional unchanged; receiver calibration is the gamma=1 bin-filter protocol, not gamma=2 private residual data.'}
(OUT/'three-channel-source-task-calibration.json').write_text(json.dumps(calibration,indent=2)+'\n',encoding='utf-8')
spec=importlib.util.spec_from_file_location('source_task',HERE/'three_channel_source_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
engine=t.SourceTask();results={};fixtures={}
for mode in ('private','reuse'):
    E=engine.calibrations(mode)
    mid={n:(E[n][0]+E[n][1])/2 for n in t.NAMES}
    data={'mode':mode,'budget':str(t.DEFAULT_BUDGET),
          'raw':{'positive':{'center':str(mid['positive']),'radius':str(mid['positive']/10)},
                 'crossed':{'center':'0','radius':str(mid['crossed']/100)},
                 'vacuum':{'center':'1/100','radius':'1/1000'}},
          'witness':{'positive':'1','crossed':'0','vacuum':'1/100'}}
    good=engine.certify(data)
    assert good['status']=='CERTIFIED_FEASIBLE' and good['nonvacuous_positive_task_certificate']
    assert Q(good['witness_check']['moment_cost'])==Q(52559872,25)
    bad=copy.deepcopy(data);bad.pop('witness');bad['raw']['vacuum']={'center':'2','radius':'1/1000'}
    bad_result=engine.certify(bad)
    assert bad_result['status']=='CERTIFIED_INFEASIBLE'
    parts={n:Q(v) for n,v in bad_result['necessary_cost_by_channel'].items()}
    assert parts['positive']+parts['crossed']<t.DEFAULT_BUDGET and parts['vacuum']<t.DEFAULT_BUDGET
    assert sum(parts.values())>t.DEFAULT_BUDGET
    withheld=copy.deepcopy(data);withheld.pop('witness')
    unknown=engine.certify(withheld)
    assert unknown['status']=='UNRESOLVED' and not unknown['nonvacuous_positive_task_certificate']
    rejected=copy.deepcopy(data);rejected['witness']['positive']='2'
    rejected_result=engine.certify(rejected)
    assert rejected_result['status']=='UNRESOLVED' and not rejected_result['witness_check']['accepted']
    fixtures[mode]={'feasible':data,'infeasible':bad,'witness_withheld':withheld}
    results[mode]={'feasible':good,'infeasible':bad_result,'witness_withheld':unknown,
                   'rejected_witness':rejected_result}
# Edge cases: exact zero is feasible even with zero budget; malformed bounds are not certificates.
zero={'raw':{n:{'center':'0','radius':'0'} for n in t.NAMES},'budget':'0','witness':{n:'0' for n in t.NAMES}}
z=engine.certify(zero)
assert z['status']=='CERTIFIED_FEASIBLE' and not z['nonvacuous_positive_task_certificate']
invalid=copy.deepcopy(zero);invalid['raw']['vacuum']['radius']='-1'
try:engine.certify(invalid)
except ValueError:pass
else:raise AssertionError('Negative measurement radius accepted')
for value in ('1/3','-1/3','1/10000000000','-1/10000000000'):
    q=Q(value)
    assert Q(t.outward_decimal(q,8,False))<=q<=Q(t.outward_decimal(q,8,True))
report={'schema':'marici.grothendieck.three-channel-source-task-certificate.v1','passed':True,
        'input_kind':'Explicit synthetic exact-rational intervals, not experimental measurements',
        'prior_order':16,'common_budget':str(t.DEFAULT_BUDGET),'cases':results,
        'scope':'Sound sufficient feasibility witnesses and necessary budget contradictions; not a complete feasibility solver. Aggregate bounds are universal outer bounds, and their nonvacuity requires the witness.'}
(OUT/'three-channel-source-task-fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n',encoding='utf-8')
(OUT/'three-channel-source-task-certificate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'cases':{mode:{'statuses':{k:v['status'] for k,v in case.items()},
                                        'feasible_aggregate_bounds':case['feasible']['aggregate_readout_enclosures']}
                                   for mode,case in results.items()}},indent=2))
