"""Bind the accepted Bool witness to the registered retained source, not to optics."""
import argparse
import copy
import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from check_physics_source_register import ROOT, P, SID, load, sha, require, encode, decode, compose, M

sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from admit_structural_overlap import check as check_live_overlap
from check_structural_pilot_transport import identity, zeros, add, scale, mul, transpose, realify
from check_programme_overlap import coefficient_audit

CONTRACT='research/nima/contracts/physics-structural-pilot-binding.v1.json'


def image(path,occurrence_id):
    require(isinstance(occurrence_id,str) and occurrence_id,'missing occurrence identity')
    return {'source_id':SID,'occurrence_id':occurrence_id,'registered_record':encode(path),
            'complex_state':P.basis(path.target),'real_state':P.basis(path.target)+(0,)*4}


def recover(record):
    require(record['source_id']==SID,'foreign binding source')
    path=decode(record['registered_record'])
    require(image(path,record['occurrence_id'])==record,'corrupt binding image')
    return path


def action(a,x):return tuple(sum(row[j]*x[j] for j in range(len(x))) for row in a)


def phase(q,re,im):return realify(add(identity(4),scale(re-1,q)),scale(im,q))


def validate(c):
    reg=load(c['register']);interface=load(c['pilot_interface'])
    source=next(s for s in reg['sources'] if s['id']==c['source_instance_id'])
    view=next(v for v in reg['views'] if v['id']==c['registered_view'])
    mapping=next(m for m in reg['maps'] if m['id']==c['registered_map'])
    require(c['source_instance_id']==SID==interface['source_instance'],'wrong source')
    require(source['version']==interface['id']==c['source_version'],'source version')
    require(view['source_instance_id']==mapping['source']==SID and mapping['target']==view['id'],'wrong registered map')
    require(c['decision']=='accept_scoped_programme_binding' and 'common physical witness' in c['excluded'],'scope promotion')
    require(c['maps']['scale']=='theta=pi*t; H_j=pi Q_j; z*H_j z=2 E_Hj(r(z)). pi is the accepted shared symbolic scale, not a measured clock or energy unit.','scale drift')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=load(CONTRACT);validate(c)
    paths={CONTRACT,c['accepted_import'],c['register'],c['pilot_interface'],
           'research/conjecture_net/contracts/structural-overlap-acceptance.v1.json',
           'research/conjecture_net/pilot_carrier.py','research/conjecture_net/admit_structural_overlap.py',
           'research/conjecture_net/check_structural_pilot_transport.py','research/conjecture_net/check_programme_overlap.py',
           'research/nima/checkers/check_physics_source_register.py',
           'research/nima/standard-spectral-correspondence.md','research/nima/spectral-whole-return-proof.md'}
    pinpath=ROOT/c['source_pins']
    if args.pin:
        require(not pinpath.exists(),'refusing implicit re-pin')
        pinpath.write_text(json.dumps({'source_sha256':{p:sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=load(c['source_pins']);require(set(pins['source_sha256'])==paths,'pin coverage')
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source drift: '+p)
    live=check_live_overlap()
    npaths=nsplits=0
    for n in range(7):
        for word in itertools.product(tuple(M),repeat=n):
            for source in P.LABELS:
                path=P.PathRecord(source,word);record=image(path,'pilot-occurrence')
                require(recover(record)==path,'record inverse')
                require(action(realify(M[P.Operation.LEFT],zeros(4)),record['real_state'])==
                        P.basis(P.apply(P.Operation.LEFT,path.target))+(0,)*4,'registered action real square')
                for k in range(n+1):
                    before=P.PathRecord(source,word[:k]);after=P.PathRecord(before.target,word[k:])
                    require(compose(encode(before),encode(after))==record['registered_record'],'registered composition')
                    nsplits+=1
                npaths+=1
    ident=identity(4);zero=zeros(4);j=realify(zero,scale(-1,ident))
    qs={op:scale(F(1,2),add(ident,scale(-1,m))) for op,m in M.items()}
    phases=((F(1),F(0)),(F(0),F(-1)),(F(-1),F(0)),(F(3,5),F(-4,5)))
    nphase=0
    for op,q in qs.items():
        hessian=realify(q,zero);generator=realify(zero,scale(-1,q))
        require(generator==mul(j,hessian),'normalized generator/scale transport')
        for re,im in phases:
            u=phase(q,re,im)
            require(mul(transpose(u),u)==identity(8),'phase norm')
            require(mul(mul(transpose(u),j),u)==j,'phase symplectic transport')
            require(mul(mul(transpose(u),hessian),u)==hessian,'energy transport')
            nphase+=1
    nticks=0
    for source in P.LABELS:
        for tags in itertools.product(tuple(P.Schedule),repeat=2):
            tick=P.TickFragment.rebuild(source,tags)
            require(P.TickFragment.rebuild(source,tick.tags)==tick and tick.swap().swap()==tick,'Tick tags')
            target=tick.routes[0].target
            for schedule,seam in zip(tags,tick.seam_labels):
                reverse=tuple(reversed(P.schedule_word(schedule)))
                path=P.PathRecord(target,reverse)
                require(path.trace[1]==seam and path.target==source,'positive return attachment')
                require(recover(image(path,'return'))==path,'return record binding')
                first,second=reverse
                start=P.basis(target)+(0,)*4
                middle=action(phase(qs[first],F(-1),F(0)),start)
                finish=action(phase(qs[second],F(-1),F(0)),middle)
                require(middle==P.basis(seam)+(0,)*4 and finish==P.basis(source)+(0,)*4,'return endpoint square')
            if tags[0]!=tags[1]:require(tick.seam_labels[0]!=tick.seam_labels[1],'seam identity collapsed')
            nticks+=1
    path=P.PathRecord((False,False),(P.Operation.LEFT,P.Operation.RIGHT))
    repeated=image(path,'first');second=image(path,'second')
    require(repeated['real_state']==second['real_state'] and repeated!=second,'occurrence identity collapsed')
    controls=[]
    for name in ('foreign-source','corrupt-real-state','missing-occurrence','erased-word'):
        bad=copy.deepcopy(repeated)
        if name=='foreign-source':bad['source_id']='passive-port-fock-memory.v1'
        elif name=='corrupt-real-state':bad['real_state']=(0,)*8
        elif name=='missing-occurrence':bad['occurrence_id']=''
        else:bad['registered_record']['word']=()
        try:recover(bad)
        except ValueError:controls.append(name)
        else:raise AssertionError('accepted '+name)
    readouts=coefficient_audit()
    for p,h in pins['source_sha256'].items():require(sha(p)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','node':c['node'],'source_instance_id':SID,
         'registered_view':c['registered_view'],'live_accepted_import':live,
         'record_inverse_cases':npaths,'registered_composition_splits':nsplits,
         'tick_bindings':nticks,'phase_controls':nphase,'readout_coefficients':readouts,
         'rejected_hostiles':controls,'occurrence_identity_preserved':True,
         'verification_level':c['verification_level'],'physical_recovery':False,'new_kernel_theorem':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('source_sha256','live_accepted_import')},indent=2))

if __name__=='__main__':main()
