"""Retained reflection-orbit observer and exact Z2-graded path products.

Local observer records do not change owning ledger operations or prepare inputs.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, encode
from check_retained_word_transport import RetainedSuccessorLedger
from check_parity_preparation_gate import audit as gate_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/symmetry-orbit-adapter.v1.json'


@dataclass(frozen=True)
class OrbitRecord:
    original: object
    reflected_slots: tuple
    orbits: tuple
    even: tuple
    odd: tuple


class SymmetryOrbitObserver:
    def __init__(self,ledger,edge_map):
        self.ledger=ledger;self.edge_map=dict(edge_map);self.records={}
        registry={(s,t,label) for label,s,t in ledger.packets}
        assert set(self.edge_map)==set(self.edge_map.values())==registry
        assert all(self.edge_map[self.edge_map[e]]==e for e in registry)

    def slots(self,paths):
        lookup={p:i for i,p in enumerate(paths)}
        moved=[tuple(self.edge_map[e] for e in path) for path in paths]
        if any(p not in lookup for p in moved):
            raise ValueError('Reflection-closed word domain required; no silent padding')
        return tuple(lookup[p] for p in moved)

    def split(self,payload):
        payload=self.ledger.resolve_payload(payload);slots=self.slots(payload.paths)
        orbits=tuple((i,) if slots[i]==i else (i,slots[i]) for i in range(len(slots)) if i<=slots[i])
        even=tuple((payload.values[i]+payload.values[j])/2 for i,j in enumerate(slots))
        odd=tuple((payload.values[i]-payload.values[j])/2 for i,j in enumerate(slots))
        record=OrbitRecord(payload,slots,orbits,even,odd)
        self.records[id(record)]=record
        return record

    def reconstruct(self,record):
        if self.records.get(id(record)) is not record:
            raise ValueError('Foreign or substituted observer record')
        self.ledger.resolve_payload(record.original)
        return tuple(a+b for a,b in zip(record.even,record.odd))

    def supplied_component(self,record,parity):
        # API registration accepts these coefficients; it does not derive them.
        self.reconstruct(record)
        if parity not in ('even','odd'):raise ValueError('Explicit parity required')
        return self.ledger.retain_path_payload(record.original.paths,getattr(record,parity))


def audit():
    prior=gate_audit();incidence=incidence_audit()
    primitives=incidence['primitive_order'];packets=[(p['owner']+':'+''.join(p['edge']),*p['edge']) for p in primitives]
    ledger=RetainedSuccessorLedger(packets)
    # Actual source-graph relabelling, not a permutation fitted to payload values.
    relabel={'A':'C','C':'A','B':'B','D':'Ep','Ep':'D','E':'Dp','Dp':'E'}
    edges=[(s,t,label) for label,s,t in packets]
    by_endpoint={(s,t):(s,t,label) for s,t,label in edges}
    edge_map={e:by_endpoint[(relabel[e[0]],relabel[e[1]])] for e in edges}
    observer=SymmetryOrbitObserver(ledger,edge_map)
    root=ledger.root;child=ledger.successor(root);stages=[root,child]
    domain_checks=[]
    for stage in stages:
        payload=ledger.retain_payload(stage,[F(i+1) for i in range(len(stage.paths))])
        record=observer.split(payload)
        assert observer.reconstruct(record)==payload.values
        assert sum(x*x for x in payload.values)==sum(x*x for x in record.even)+sum(x*x for x in record.odd)
        assert all(record.even[j]==record.even[i] and record.odd[j]==-record.odd[i] for i,j in enumerate(record.reflected_slots))
        assert ledger.assembly_history(record.original)==ledger.assembly_history(payload)
        domain_checks.append({'word_length':stage.word_length,'slots':len(stage.paths),'orbits':len(record.orbits),
                              'singleton_orbits':sum(len(o)==1 for o in record.orbits)})
    # Unsupported subsets are rejected without adding missing coefficient slots.
    subset=ledger.retain_path_payload((root.paths[0],),(F(1),))
    try:observer.split(subset)
    except ValueError:pass
    else:raise AssertionError('Nonclosed domain accepted')
    rec=observer.split(ledger.retain_payload(root,[F(1)]*10))
    forged=OrbitRecord(rec.original,rec.reflected_slots,rec.orbits,rec.even,rec.odd)
    try:observer.reconstruct(forged)
    except ValueError:pass
    else:raise AssertionError('Substituted record accepted')

    counts=[];witness=None
    for left_stage,right_stage in [(root,root),(root,child),(child,root),(child,child)]:
        tests=0
        for i in range(len(left_stage.paths)):
            for j in range(len(right_stage.paths)):
                left=ledger.retain_payload(left_stage,[F(k==i) for k in range(len(left_stage.paths))])
                right=ledger.retain_payload(right_stage,[F(k==j) for k in range(len(right_stage.paths))])
                lr=observer.split(left);rr=observer.split(right)
                product=ledger.compose_payloads(left,right);pr=observer.split(product)
                # Simultaneous reflection respects endpoint sewing and cut slots.
                refl_left=ledger.retain_path_payload(left.paths,[left.values[k] for k in lr.reflected_slots])
                refl_right=ledger.retain_path_payload(right.paths,[right.values[k] for k in rr.reflected_slots])
                reflected_product=ledger.compose_payloads(refl_left,refl_right)
                assert reflected_product.paths==product.paths
                assert reflected_product.values==tuple(product.values[k] for k in pr.reflected_slots)
                parts={}
                for a,b in [('even','even'),('odd','odd'),('even','odd'),('odd','even')]:
                    lp=observer.supplied_component(lr,a);rp=observer.supplied_component(rr,b)
                    assert lp.operation==rp.operation=='supplied'
                    p=ledger.compose_payloads(lp,rp);p_record=observer.split(p)
                    assert p.paths==product.paths
                    assert (p_record.odd if a==b else p_record.even)==tuple(F(0) for _ in p.values)
                    parts[a,b]=p
                assert pr.even==tuple(a+b for a,b in zip(parts['even','even'].values,parts['odd','odd'].values))
                assert pr.odd==tuple(a+b for a,b in zip(parts['even','odd'].values,parts['odd','even'].values))
                assert observer.reconstruct(pr)==product.values
                assert ledger.deconstruct_payload(product)[0]==(left,right)
                if witness is None and any(parts['odd','odd'].values):
                    witness={'left_basis_slot':i,'right_basis_slot':j,
                             'left_odd':lr.odd,'right_odd':rr.odd,
                             'product_paths':parts['odd','odd'].paths,
                             'odd_times_odd_even_values':parts['odd','odd'].values}
                tests+=1
        counts.append({'left_length':left_stage.word_length,'right_length':right_stage.word_length,'basis_pairs':tests})
    assert witness is not None
    # Equal-copy successor is different from multiplying two prepared odd inputs:
    # the appended neutral all-ones primitive factor is even.
    neutral=ledger.retain_payload(root,[F(1)]*10)
    assert all(v==0 for v in observer.split(neutral).odd)
    lr=observer.split(ledger.retain_payload(root,[F(k==0) for k in range(10)]))
    odd_input=observer.supplied_component(lr,'odd')
    extension=ledger.compose_payloads(odd_input,neutral)
    assert all(v==0 for v in observer.split(extension).even)
    assert any(extension.values)

    dependencies=list(prior['source_sha256'])+['research/scattering/seed-composition/check_symmetry_orbit_adapter.py']
    return {
        'schema':'marici.scattering.symmetry-orbit-adapter.v1',
        'status':'lossless_parity_observer_constructed_path_product_is_Z2_graded_not_odd_closed',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'adapter':{'kind':'local observer; owning ledger unchanged','split':'(x+Jx)/2, (x-Jx)/2',
                   'original_payload_retained':True,'counting_norm_preserved_with_both_records':True,
                   'nonclosed_domains_rejected':True,'substituted_records_rejected':True,
                   'source_component_operation':'supplied','domains':domain_checks},
        'product_rules':{'simultaneous_reflection':'J(x*y)=(Jx)*(Jy)',
                         'even':'x_even*y_even + x_odd*y_odd',
                         'odd':'x_even*y_odd + x_odd*y_even',
                         'odd_times_odd':'even','odd_subspace_closed_under_bilinear_product':False,
                         'neutral_even_successor_preserves_odd':True,
                         'basis_tests':counts,'exact_bilinear_extension':'basis verification proves identities on these complete domains',
                         'general_argument':'graph reflection preserves endpoints and fixed-cut concatenation; parity signs multiply'},
        'nonzero_odd_product_witness':witness,
        'boundary':{'parity_split_is_multiplicative':False,'physical_preparation_implemented':False,
                    'odd_inputs_independently_prepared':False,'formal_outcome_admitted':False},
        'next_gate':'Audit existing controller masks under graph reflection: determine whether context transitions preserve parity, or require additional paired control records to avoid parity leakage.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale symmetry-orbit receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: retained symmetry-orbit observer recovers coefficients and preserves counting norm with both records.')
    print('PASS: 676 basis-pair tests verify graded product rules; odd times odd is even, neutral successor preserves odd.')
    print('Boundary: cross-word subtraction remains an observer; ledger components are registered as supplied.')


if __name__=='__main__':main()
