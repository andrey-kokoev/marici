"""Exhaust every schedule of two cancellations and four consuming boundary reads."""
import contextlib, io, json
from copy import deepcopy
from pathlib import Path
from four_cell_query_net import construct_queries
with contextlib.redirect_stdout(io.StringIO()):
    import check_four_cell_continuation_rewrite_probe as source
initial=construct_queries(source.records)
expected=initial.meanings()
leaves=edges=intermediate=0
terminal_signatures=set()
def visit(net):
    global leaves,edges,intermediate
    assert net.meanings()==expected
    enabled=net.enabled()
    if not enabled:
        assert net.completed()==4
        assert all(k in ('ANSWER','OUT') for k,_ in net.nodes.values())
        terminal_signatures.add(repr(sorted(net.meanings().items())))
        leaves+=1
        return
    if 0<net.completed()<4:intermediate+=1
    for pair in enabled:
        child=deepcopy(net)
        before_answers=child.completed()
        is_read=child.nodes[pair[0]][0]=='VALUE'
        child.step(pair)
        assert child.completed()==before_answers+int(is_read)
        try:child.step(pair)
        except ValueError:pass
        else:raise AssertionError('consumed source used twice')
        edges+=1
        visit(child)
visit(initial)
assert leaves==80 and len(terminal_signatures)==1 and intermediate>0
# Port linearity forbids attaching a second read to one VALUE.
net=deepcopy(initial);net.step(net.enabled()[0])
value=next(n for n,(k,_) in net.nodes.items() if k=='VALUE')
try:net.link((value,'p'),(value,'p'))
except ValueError:pass
else:raise AssertionError('value duplicated')
# An erased pending channel breaks live semantics even if another answer exists.
net=deepcopy(initial);net.step(net.enabled()[0])
net.step(next(p for p in net.enabled() if net.nodes[p[0]][0]=='VALUE'))
assert net.completed()==1
pending=next(n for n,(k,_) in net.nodes.items() if k=='VALUE')
net.nodes[pending][1]['value']=(0,0)
assert net.meanings()!=expected
report={'passed':True,'complete_schedules':leaves,'schedule_tree_edges':edges,
 'intermediate_partial_answer_occurrences':intermediate,
 'terminal_answer_semantics_unique':True,'live_channel_meanings_preserved':True,
 'consumed_queries_cannot_be_replayed':True,'pending_channel_erasure_detected':True,
 'rules':['EB--FB -> VALUE + VALUE (one original record per value)',
          'VALUE--READ -> ANSWER (consume value and query)'],
 'scope':'Two families, four one-shot queries, exact attributed payloads at one target. No duplicator, arbitrary-query reuse, full fermionic semantics or physical contour selection.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/four-cell-query-net.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
