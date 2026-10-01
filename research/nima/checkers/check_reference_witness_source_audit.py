"""Audit existing reference witnesses without changing their source types.

Strict anchor-coordinate telescoping and filled DG route differences are
separate from transport on the carrier's endpoint graph.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io
import json
import runpy

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/reference-witness-source-audit.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    w=runpy.run_path(str(Path(__file__).with_name('check_witnessed_reference_reanchoring.py')))
    g=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
plus,minus,delta,signature=(w[k] for k in ('plus','minus','delta','signature'))
anchors,hs=w['anchors'],w['hs']
assert len(anchors)==len(hs)==171
for key,h in hs.items():
    assert all(signature(path)==('A','B',1) for path in h)
    assert all(signature(path)==('A','B',0) for path in anchors[key])
    assert delta(h)==plus(anchors[key],minus(anchors['reference']))

# Anchor-to-anchor differences are an exact potential on anchor labels.
# Check every anchor on a triangle through the reference and total mean.
for key in anchors:
    k01=plus(hs[key],minus(hs['reference']))
    k12=plus(hs['total'],minus(hs[key]))
    k20=plus(hs['reference'],minus(hs['total']))
    assert not plus(k01,k12,k20)
# Current payload returns exactly; retained provenance is NOT deleted.
initial=w['initial']
changed=w['reanchor'](initial,'family:0')
returned=w['reanchor'](changed,'reference')
assert w['payload'](returned)==w['payload'](initial)
assert returned.parents==(changed,) and changed.parents==(initial,)

# The two original leg-witness routes are generally not identical. Their
# discrepancy is the boundary of an existing degree-two filler.
strict=0; filled=0
for tag,size in (('a',11),('s',4)):
    for i in range(size):
        for j in range(size):
            first,second,filler=w['routes'](tag,i,j)
            loop=plus(second,minus(first))
            assert not delta(loop)
            assert delta(filler)==loop
            if loop:
                assert filler and all(signature(path)==('A','B',2) for path in filler)
                filled+=1
            else:
                strict+=1
assert (strict,filled)==(28,109)

objects={p for source,target,degree in w['arrows'].values() for p in (source,target)}
assert objects=={'A','U','V','B'}
carrier_ports={p for row in g['source'] for p in (row.source,row.target)}
assert len(carrier_ports)==32
assert not objects&carrier_ports
assert w['arrows']['return']==('B','A',0)
# Absence of these endpoint types is a scope observation about these fixtures,
# not a theorem excluding a future functor or a conditional frame realization.

result={
 'status':'passed',
 'classification':'anchor_coherence_verified_carrier_connection_not_supplied_by_these_witnesses',
 'obligation':'source typing audit before carrier attachment or loop descent',
 'stratum':'Existing fixed-domain shared-leg and reanchoring fixtures, without reinterpretation of degrees or endpoint types',
 'checks':{'anchor_count':171,'anchor_difference_loops_strictly_zero':True,
           'reference_return_payload_exact':True,'parent_history_retained':True,
           'strict_leg_route_agreements':strict,'nonzero_filled_leg_route_differences':filled,
           'dg_object_count':len(objects),'carrier_endpoint_count':len(carrier_ports),
           'witness_degree':1,'carrier_transport_degree_required':0},
 'verdict':'Neither flat nor curved carrier reference transport is selected by the audited witnesses. They concern fixed-domain anchor changes and DG comparison routes.',
 'missing_adapter':{'source':'ordered carrier routes with supplied edge operations',
                    'target':'typed reference transports and declared higher comparison cells',
                    'requirements':['degree and endpoint assignment','composition compatibility',
                                    'fixed-rung4 attachment','route-preserving observation']},
 'prior_art':'research/nima/nonflat-calibration-is-route-structure-not-endpoint-data.md',
 'unsupported':['physical edge preparation','source reference flatness',
                'source reference holonomy','identification of DG fillers with carrier-loop transport']
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
