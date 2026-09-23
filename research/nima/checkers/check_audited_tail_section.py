"""Explicit audit-aware extension; the ordinary two-coordinate API is unchanged."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from check_symbolic_tail_interface import Generator
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')

class AuditedGenerator(Generator):
    def __init__(self,m,pins):
        super().__init__(m);self.pins=dict(pins)
        if len(self.pins)!=len(pins):raise ValueError('DUPLICATE_AUDIT')
        for j,h in self.pins.items():
            if type(j) is not int or not 0<=j<m or not 0<=h<=100+2*j:raise ValueError('INVALID_AUDIT')
    def mass(self,k):
        return Generator.mass(k)-sum(Q(100+2*j) for j in self.pins if j<k)
    def weighted(self,k):
        return Generator.weighted(k)-sum(Q(100+2*j,128**j) for j in self.pins if j<k)
    def section(self,point):
        if len(point)!=2:raise ValueError('UNDECLARED_OBSERVABLE')
        offset=(sum(self.pins.values(),Q(0)),sum(h*Q(1,128**j) for j,h in self.pins.items()))
        residual=tuple(v-w for v,w in zip(point,offset));answer=super().member(residual)
        return {'pins':[[j,str(h)] for j,h in sorted(self.pins.items())],'offset':list(map(str,offset)),
                'residual_point':list(map(str,residual)),'residual_membership':answer}
    def coordinate(self,section,j):
        if j in self.pins:return self.pins[j]
        witness=section['residual_membership']['lift'];k=witness['high_prefix'];p=Q(witness['high_partial'])
        l=witness['complement_prefix'];r=Q(witness['complement_partial']);theta=Q(witness['theta']);cap=Q(100+2*j)
        high=cap if j<k else p if j==k else Q(0);comp=cap if j<l else r if j==l else Q(0)
        return (1-theta)*(cap-comp)+theta*high

def main():
    engine=Path(__file__).with_name('check_symbolic_tail_interface.py');parent=OUT/'symbolic-tail-interface.json'
    contract={'schema':'audited-tail-section-v1','engine_sha256':sha(engine),'owning_report_sha256':sha(parent),
      'source':'The same admitted independent atom-cap face. Euclidean paths are explicitly the comparison identity notion.',
      'audits':'All rational threshold predicates on each declared pinned atom. Preserving its exact coordinate preserves every such audit.',
      'construction':'Subtract pinned observable contributions; remove pinned capacities from both cumulative sums; apply the existing greedy section to the remaining box.',
      'observer':'(U,V,all pinned atom values). Pins are supplied observations or proposed coordinates, not inferred from an old representative lift.',
      'contraction':'H_A(x,t)=(1-t)x+t*s_A(U(x),V(x),x_A), preserving the same enlarged observation.',
      'm_values':[2,3,4,8,16,64,1024],'times':['0','1/4','1/2','1'],
      'controls':['no pins','first atom','middle atom','first and last atoms','all but last/all atoms for small m','impossible common audit at a target base'],
      'scope':'Conditional fibers of the owning normalized box. No actual-source selection, authenticated observations, arbitrary hidden restrictions or inverse physical operation.'}
    cp=OUT/'audited-tail-section-contract.json';save(cp,contract)
    cases=[];nontrivial=0
    for m in contract['m_values']:
        x={0:Q(3),m//2:Q(5),m-1:Q(7)}
        u=sum(x.values());v=sum(h*Q(1,128**j) for j,h in x.items())
        audit_sets={(),(0,),(m//2,),tuple(sorted({0,m-1}))}
        if m<=4:audit_sets.update([tuple(range(m-1)),tuple(range(m))])
        for indices in sorted(audit_sets):
            pins=[(j,x.get(j,Q(0))) for j in indices];model=AuditedGenerator(m,pins);section=model.section((u,v))
            assert section['residual_membership']['admitted'] and model.section((u,v))==section
            # All dense reads are verification work, not stored by the section.
            dense=[model.coordinate(section,j) for j in range(m)]
            assert all(0<=h<=100+2*j for j,h in enumerate(dense))
            assert sum(dense)==u and sum(h*Q(1,128**j) for j,h in enumerate(dense))==v
            assert all(dense[j]==h for j,h in pins)
            changed=[j for j in range(m) if dense[j]!=x.get(j,Q(0))];nontrivial+=bool(indices and changed)
            times=[]
            for t in map(Q,contract['times']):
                point=[(1-t)*x.get(j,Q(0))+t*dense[j] for j in range(m)]
                assert all(0<=h<=100+2*j for j,h in enumerate(point))
                assert sum(point)==u and sum(h*Q(1,128**j) for j,h in enumerate(point))==v
                assert all(point[j]==h for j,h in pins)
                # These stand for any frames depending only on the enlarged observation.
                assert sum(point)<=u+1 and -sum(point)<=-u
                times.append({'time':str(t),'moments':[str(u),str(v)],'audits':[[j,str(point[j])] for j,h in pins]})
            cases.append({'m':m,'source_sparse':[[j,str(h)] for j,h in sorted(x.items())],'point':[str(u),str(v)],
                          'section':section,'changed_unpinned_count':len(changed),'contraction_checks':times})
    # The old section need not preserve the new audit. The new section does.
    x=(Q(0),Q(1),Q(0));point=(Q(1),Q(1,128));base=Generator(3).member(point);assert base['admitted']
    old=AuditedGenerator(3,[]);old_section=old.section(point);assert old.coordinate(old_section,0)>0
    audited=AuditedGenerator(3,[(0,Q(0))]);new_section=audited.section(point)
    assert new_section['residual_membership']['admitted'] and audited.coordinate(new_section,0)==0
    # A target base may admit source witnesses but none with the same audit.
    fixed=AuditedGenerator(3,[(2,Q(0))]);target=(Generator.mass(3),Generator.weighted(3))
    assert Generator(3).member(target)['admitted'];rejected=fixed.section(target)
    assert not rejected['residual_membership']['admitted']
    sep=rejected['residual_membership']['separator'];a=list(map(Q,sep['normal']));rhs=Q(sep['upper'])+sum(z*h for z,h in zip(a,map(Q,rejected['offset'])))
    assert sum(z*h for z,h in zip(a,target))>rhs
    for invalid in ([(0,Q(-1))],[(3,Q(0))],[(0,Q(0)),(0,Q(1))]):
        try:AuditedGenerator(3,invalid)
        except ValueError:pass
        else:raise AssertionError('invalid audit accepted')
    packet={'cases':cases,'old_section_audit_failure':{'source':list(map(str,x)),'point':list(map(str,point)),
        'old_section':old_section,'new_section':new_section,'audit':'t_0<=0'},
      'target_without_common_audit':{'m':3,'point':list(map(str,target)),'section':rejected,
        'full_separator':{'normal':list(map(str,a)),'upper':str(rhs)}},
      'identity':'Ordinary paths inside each fixed enlarged-observation fiber, not pointwise equality of distinct source witnesses.'}
    pp=OUT/'audited-tail-section-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'AUDIT_PRESERVING_CONDITIONAL_SECTION_PASSES','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'section_cases':len(cases),'contraction_checks':sum(len(t['contraction_checks']) for t in cases),
      'nontrivial_audited_contractions':nontrivial,'missing_common_audit_fiber_rejected':True,
      'scope':contract['scope'],'storage_boundary':'Pinned indices/values and run-specific evidence remain retained information; contraction does not erase them.'}
    save(OUT/'audited-tail-section.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
