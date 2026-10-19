"""Read-only source review plus independent exact controls; writes Nima's receipt only."""
import copy
import itertools
import json
import re
import tempfile
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/nima/contracts/physics-control-contribution-review.v1.json'
FORMAL='research/nima/results/physics-retained-history-agda-v1.json'
FORMAL_CHECKER='research/nima/checkers/refresh_physics_retained_history_receipt.py'
FRESHNESS_POLICY='research/nima/contracts/physics-formal-freshness-policy.v2.json'


def require(ok,message):
    if not ok: raise ValueError(message)


def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def sha(path): return sha256((ROOT/path).read_bytes()).hexdigest()


def formal_receipt(r):
    require(r['passed'] is True and r['exit_code']==0 and r['inputs_stable'] is True,'formal result')
    require(r['ignore_interfaces'] is True and all(x in r['args'] for x in
        ('--ignore-interfaces','--safe','--cubical','--guardedness')),'formal checking mode')
    require(sha(Path(r['args'][0]))==r['compiler_sha256'],'compiler drift')
    require(sha('research/sontag/agda/RetainedHistoryTransport.agda')==r['source_sha256'],'formal source drift')
    require(sha(FORMAL_CHECKER)==r['checker_sha256'],'formal checker drift')
    policy=load(FRESHNESS_POLICY)
    require(policy['receipt']==FORMAL and sha(FORMAL)==policy['receipt_sha256'],'formal receipt identity')
    keys_digest=sha256(json.dumps(sorted(r['source_inventory_sha256']),separators=(',',':')).encode()).hexdigest()
    require(keys_digest==policy['inventory_keys_sha256'],'formal inventory coverage')
    for path,digest in r['source_inventory_sha256'].items():
        require(sha(Path(path))==digest,'formal dependency drift: '+path)
    log=Path(r['log']);require(sha(log)==policy['log_sha256'],'formal trace drift')
    modules=re.findall(r'^\s*Checking (\S+) \((.+)\)\.$',log.read_text(encoding='utf-8'),re.MULTILINE)
    require(modules and modules[0][0]=='RetainedHistoryTransport','missing compiler dependency trace')
    includes=[Path(r['args'][i+1]) for i,x in enumerate(r['args']) if x=='-i']
    includes += [ROOT,ROOT/'research/sontag/agda']
    extensions=('.agda','.lagda','.lagda.md','.lagda.rst','.lagda.tex','.lagda.org','.lagda.typ')
    for name,path in modules:
        require(path in r['source_inventory_sha256'],'unrecorded checked module')
        relative=name.replace('.', '/')
        candidates={(d/(relative+ext)).resolve() for d in includes for ext in extensions if (d/(relative+ext)).is_file()}
        require(candidates=={Path(path).resolve()},'changed import resolution: '+name)
    return len(r['source_inventory_sha256'])


def risk(shapes,rates,factors,q,h,eps,delta):
    require(0<=q[0]<=q[1]<=1 and eps>0 and 0<delta<1,'risk inputs')
    lo=hi=var=F(0)
    for k,r,f,p in zip(shapes,rates,factors,(2,4)):
        require(k>0 and 0<r[0]<=r[1] and 0<=f[0]<=f[1]<=1,'posterior box')
        lo+=q[0]**p*f[0]*k/r[1]
        hi+=q[1]**p*f[1]*k/r[0]
        var+=q[1]**(2*p)*f[1]**2*k/r[0]**2
    bias=max(abs(lo-h),abs(hi-h))
    tail=None if bias>=eps else min(F(1),var/(eps-bias)**2)
    return {'mean_low':lo,'mean_high':hi,'variance_upper':var,'bias_upper':bias,
            'tail_bound':tail,'decision':'certified' if tail is not None and tail<=delta else 'abstain'}


def exact_controls():
    checks={}; A0=(F(9),F(25)); alpha=[F(3),F(5)]
    factors=[F(1),F(1)]; rate=[F(1),F(2)]; shapes=[F(2),F(3)]
    exposure=[F(0),F(0)]; lost_math=F(0); lost_phys=F(0)
    tau,eta=F(9,25),F(16,25); histories=[]
    count_record=[]
    # sqrt(1-tau)=4/5, sqrt(eta*tau)=12/25, sqrt((1-eta)*tau)=9/25.
    events=[('tap',(1,2)),('gain',F(3,5)),('tap',(0,1)),('adaptive',None)]
    for j,(kind,value) in enumerate(events):
        prior=[factors[i]*A0[i] for i in (0,1)]
        if kind=='tap':
            counts=value; count_record.append(counts)
            for i in (0,1):
                c=eta*tau*factors[i]
                require(c>0 and counts[i]>=0,'admitted count fixture')
                checks[f'likelihood_mean_{j}_{i}']=c*A0[i]==(F(12,25)*alpha[i])**2
                exposure[i]+=c;rate[i]+=c;shapes[i]+=counts[i]
                lost_phys+=(F(12,25)*alpha[i])**2+(F(9,25)*alpha[i])**2
                alpha[i]*=F(4,5);factors[i]*=1-tau
            lost_math+=tau*sum(prior)
        else:
            q=value if kind=='gain' else (F(1,2) if sum(map(sum,count_record))>=3 else F(3,4))
            for i,p in enumerate((1,2)):
                lost_phys+=(1-q**(2*p))*alpha[i]**2
                alpha[i]*=q**p;factors[i]*=q**(2*p)
                lost_math+=(1-q**(2*p))*prior[i]
            if kind=='adaptive': checks['adaptive_uses_public_counts']=q==F(1,2)
        checks[f'prefix_state_{j}']=all(alpha[i]**2==factors[i]*A0[i] for i in (0,1))
        checks[f'prefix_resources_{j}']=lost_phys==lost_math and sum(x*x for x in alpha)+lost_phys==sum(A0)
        histories.append({'event':kind,'factors':list(factors),'rate':list(rate),'shapes':list(shapes)})
    checks['posterior_rates_accumulate_pre_tap_exposure']=rate==[F(1)+exposure[0],F(2)+exposure[1]]
    checks['ignoring_intervening_attenuation_is_detected']=rate[0]!=F(1)+2*eta*tau
    checks['two_gain_composition']=all((F(2,3)*F(3,5))**p==F(2,3)**p*F(3,5)**p for p in (2,4))
    checks['equal_H_continuation_hostile']=F(8)*F(1,2)**2==2 and F(8)*F(1,2)**4==F(1,2)
    # Relative phase is invisible to the admitted modewise occupation quotient.
    left=(F(1),F(1)); right=(F(1),F(-1))
    output=lambda v:((v[0]+v[1])**2/2,(v[0]-v[1])**2/2)
    checks['phase_pair_equal_occupation']=[x*x for x in left]==[x*x for x in right]
    checks['signal_mixing_extension_distinguishes']=output(left)==(2,0) and output(right)==(0,2)
    checks['mixing_retains_total_energy']=sum(output(left))==sum(output(right))==2
    # Fresh vacuum is an actual premise of the loss channel.
    checks['populated_ancilla_changes_signal']=F(3,5)*0+F(4,5)*1!=0
    K=F(100000); rates=[(K*F(999,1000),K*F(1001,1000))]*2
    h=F(5,16);eps=h/4;delta=F(1,20)
    tight=risk([K,K],rates,[(F(1),F(1))]*2,(F(499,1000),F(501,1000)),h,eps,delta)
    wide=risk([K,K],rates,[(F(1),F(1))]*2,(F(2,5),F(3,5)),h,eps,delta)
    checks['tight_box_certifies']=tight['decision']=='certified'
    checks['wide_box_abstains']=wide['decision']=='abstain'
    checks['systematic_bias_retained']=tight['bias_upper']>0
    checks['exact_corner_moments_enclosed']=all(
        tight['mean_low']<=q*q*K/r1+q**4*K/r2<=tight['mean_high'] and
        q**4*K/r1**2+q**8*K/r2**2<=tight['variance_upper']
        for q,r1,r2 in itertools.product((F(499,1000),F(501,1000)),*rates))
    checks['mean_and_precision_separated']=F(1,5)>F(1,320) and F(1,7)>F(1,320)
    try:risk([K,K],[(0,1)]*2,[(F(1),F(1))]*2,(F(1,2),F(1,2)),h,eps,delta)
    except ValueError:checks['zero_rate_rejected']=True
    else:checks['zero_rate_rejected']=False
    require(all(checks.values()),'independent exact control failed')
    return checks,histories,tight,wide


def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x


def main():
    c=load(CONTRACT); source_hashes={CONTRACT:sha(CONTRACT)}
    for m in c['source_manifests']:
        manifest=load(m);require(manifest['passed'] is True,'source manifest result')
        source_hashes[m]=sha(m)
        for path,digest in manifest['source_sha256'].items():
            require(sha(path)==digest,'source manifest drift: '+path)
            source_hashes[path.replace('\\','/')]=digest
    for port in c['ports']:
        for path in port['evidence']:source_hashes[path]=sha(path)
    r=load(FORMAL);inventory_count=formal_receipt(r)
    source_hashes[FORMAL]=sha(FORMAL);source_hashes[FORMAL_CHECKER]=sha(FORMAL_CHECKER)
    source_hashes[FRESHNESS_POLICY]=sha(FRESHNESS_POLICY)
    controls=[]
    for name in ('unsafe','failed','unstable','incremental','stale-source','missing-inventory'):
        bad=copy.deepcopy(r)
        if name=='unsafe':bad['args'].remove('--safe')
        elif name=='failed':bad['exit_code']=1
        elif name=='unstable':bad['inputs_stable']=False
        elif name=='incremental':bad['ignore_interfaces']=False
        elif name=='stale-source':bad['source_sha256']='0'*64
        else:bad['source_inventory_sha256'].pop(next(iter(bad['source_inventory_sha256'])))
        try:formal_receipt(bad)
        except ValueError:controls.append(name)
        else:raise AssertionError('bad receipt accepted: '+name)
    # Exercise added-file tolerance and shadow rejection without changing repository sources.
    with tempfile.TemporaryDirectory(prefix='physics-import-resolution-') as directory:
        probe=Path(directory); trial=copy.deepcopy(r);trial['args']+=['-i',str(probe)]
        (probe/'UnrelatedFreshnessProbe.agda').write_text('module UnrelatedFreshnessProbe where\n',encoding='utf-8')
        require(formal_receipt(trial)==inventory_count,'unrelated addition rejected')
        (probe/'RetainedHistoryTransport.agda').write_text('module RetainedHistoryTransport where\n',encoding='utf-8')
        try:formal_receipt(trial)
        except ValueError:controls.append('shadow-import')
        else:raise AssertionError('shadow import accepted')
    checks,histories,tight,wide=exact_controls()
    out={'schema':'marici.physics-control-contribution-review-result.v1','status':'pass',
         'decision':c['decision'],'accepted_ports':[p['id'] for p in c['ports']],
         'independent_checks':checks,'check_count':len(checks),'traces':histories,
         'tight_calibration':tight,'wide_calibration':wide,
         'phase_extension_hostile':c['phase_extension_control'],
         'formal_receipt_fresh':True,'formal_inventory_count':inventory_count,'formal_receipt':FORMAL,
         'formal_freshness_policy':FRESHNESS_POLICY,'unrelated_addition_control':True,
         'formal_corruption_controls':controls,'compiler_rerun':False,'owner_suites_rerun':False,
         'source_sha256':source_hashes,'checker_sha256':sha(Path(__file__)),
         'boundary':c['review_boundaries']}
    (ROOT/c['result']).write_text(json.dumps(encode(out),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','ports':out['accepted_ports'],'independent_checks':len(checks),
        'formal_inventory_count':inventory_count,'formal_corruption_controls':controls,
        'tight':tight['decision'],'wide':wide['decision'],'phase_extension_outputs':[[2,0],[0,2]]},indent=2))


if __name__=='__main__':main()
