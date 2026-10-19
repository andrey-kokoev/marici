"""Three explicit native import adapters; ONE protocol and energy assembler."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import hashlib,json
from assemble_metric_coefficient_protocol import ROOT,A,ONE,ZERO,assemble,encode,decode,read_operator,sharp,product,tr
OUT=ROOT/'research/strominger/results/common-three-carrier-protocol'


def coefficient(values,masks):
    c=[F(0)]*16
    for v,m in zip(values,masks):c[m]=F(v)
    return A(tuple(c))


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    proton_path=ROOT/'research/nima/results/twelve-triangle-1836-arrows.json'
    neutron_path=ROOT/'research/strominger/results/neutron-arrow-native-bridge.json'
    electron_path=ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
    proton=json.loads(proton_path.read_text());neutron=json.loads(neutron_path.read_text());electron=json.loads(electron_path.read_text())
    assert neutron['status']=='passed'
    for p,h in neutron['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    labels=sorted({':'.join(r['source'][1:]) for r in proton});pops=[{} for _ in range(3)]
    for r in proton:
        s=['raw','local','aligned'].index(r['source'][0]);assert r['target'][0]==['local','aligned','raw'][s]
        i=labels.index(':'.join(r['target'][1:]));j=labels.index(':'.join(r['source'][1:]))
        pops[s][i,j]=coefficient([r['weight_real'],r['weight_imag_sqrt3']],[0,10])
    nops=[{} for _ in range(3)];d=[F(c['d']) for c in neutron['coordinates']]
    for r in neutron['arrows']:
        s='LGN'.index(r['stage']);i,j=r['target'],r['source']
        nops[s][i,j]=coefficient(r['numerator'],[0,1,10,11])/A(d[j])
    eops=[{} for _ in range(3)]
    for r in electron['arrows']:
        eops['LGN'.index(r['stage'])][r['target'],r['source']]=coefficient([v for pair in r['weight'] for v in pair],[0,2,8,10])
    inputs=[('proton',labels,[F(1)]*36,pops,proton_path),
            ('neutron',[f"triangle-{r['triangle']}:axis-{r['axis']}" for r in neutron['coordinates']],[1/x for x in d],nops,neutron_path),
            ('electron',[f'face-{i//2}:spin-{i%2}' for i in range(8)],[F(1)]*8,eops,electron_path)]
    summaries={};packets=[];checks={}
    for name,coordinates,metric,ops,path in inputs:
        source={'schema':'marici.metric-coefficient-source.v1','coordinates':coordinates,'metric':list(map(str,metric)),
                'local':encode(ops[0]),'alignment':encode(ops[1]),
                'provenance':{'input':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                              'adapter':'native labelled coefficient import; metric numerator conversion explicit; global return withheld from assembler'}}
        result=assemble(source);n=len(metric)
        checks[name+'_return_derived_not_supplied']=read_operator(result['operators']['N'],n)==ops[2]
        checks[name+'_expected_count']=result['measures']['protocol_transfer_count']==(144 if name=='electron' else 1836)
        checks[name+'_expected_rank']=result['measures']['return_rank']==(2 if name=='electron' else 1)
        # Rational diagonal chart rescaling is non-unitary in Euclidean slots.
        # Correct metric transport preserves physical adjoints and energy.
        scales=[F(2) if i%2 else F(3) for i in range(n)]
        transformed=deepcopy(source);transformed['metric']=[str(metric[i]/scales[i]**2) for i in range(n)]
        for key,m in [('local',ops[0]),('alignment',ops[1])]:
            transformed[key]=encode({(i,j):v*A(scales[i]/scales[j]) for (i,j),v in m.items()})
        alternative=assemble(transformed)
        checks[name+'_metric_chart_invariant_measures']=alternative['measures']==result['measures']
        aN=read_operator(alternative['operators']['N'],n);aH=read_operator(alternative['operators']['H_in_pi_over_four_units'],n)
        N=read_operator(result['operators']['N'],n);H=read_operator(result['operators']['H_in_pi_over_four_units'],n)
        checks[name+'_metric_chart_covariant_operators']=aN=={(i,j):v*A(scales[i]/scales[j]) for (i,j),v in N.items()} and aH=={(i,j):v*A(scales[i]/scales[j]) for (i,j),v in H.items()}
        path=OUT/(name+'.json');path.write_text(json.dumps(result,indent=2)+'\n');packets.append(path)
        summaries[name]=result['measures']
    # Small independent rejection probes, without rerunning the large cases.
    small={'schema':'marici.metric-coefficient-source.v1','coordinates':['a','b'],'metric':['1','1'],'local':encode({(0,0):ONE}),'alignment':encode({(0,0):ONE}),'provenance':{}}
    def reject(label,bad,message):
        try:assemble(bad)
        except ValueError as e:checks[label]=message in str(e)
        else:checks[label]=False
    bad=deepcopy(small);bad['metric'][0]='0';reject('singular_metric_rejected',bad,'metric')
    bad=deepcopy(small);bad['local']=encode({(0,0):A(2)});reject('nonprojector_rejected',bad,'projector')
    bad=deepcopy(small);bad['alignment']=encode({(i,j):A(F(1,2)) for i in range(2) for j in range(2)});reject('noncommuting_projections_rejected',bad,'commute')
    bad=deepcopy(small);bad['local']=encode({(0,0):ONE,(0,1):ONE});reject('nonorthogonal_projection_rejected',bad,'projector')
    # Orthonormal two-coordinate example: basis changes need not preserve
    # sparsity, even when the physical projector and energy are equivalent.
    baseline=assemble(small)
    rotated=deepcopy(small);dense={(0,0):A(F(9,25)),(0,1):A(F(12,25)),(1,0):A(F(12,25)),(1,1):A(F(16,25))}
    rotated['local']=rotated['alignment']=encode(dense);other=assemble(rotated)
    checks['transfer_count_is_not_a_physical_invariant']=baseline['measures']['protocol_transfer_count']==3 and other['measures']['protocol_transfer_count']==12 and baseline['measures']['constraint_spectrum_in_pi_over_four_units']==other['measures']['constraint_spectrum_in_pi_over_four_units']
    bindings=[Path(__file__).resolve(),Path(__file__).with_name('assemble_metric_coefficient_protocol.py'),ROOT/'research/voevodsky/checkers/check_pentachoron_spin_interfaces.py',proton_path,neutron_path,electron_path]
    report={'status':'passed' if all(checks.values()) else 'failed','checks':checks,'carriers':summaries,
            'scope':'One L/G-to-return constructor and one projector-defect energy rule; native import adapters remain explicit. This is not native triangle-operation energy, five-cell electron transport, a unified arrow-only frontend, or physical mass calibration.',
            'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in bindings},
            'packet_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in packets}}
    (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'checks':checks,'carriers':summaries},indent=2))
    if not all(checks.values()):raise SystemExit(1)

if __name__=='__main__':main()
