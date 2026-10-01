"""Exact gate: native DG witness retention versus writable record amplitudes."""
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import io
import json
import runpy
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
ROOT=HERE.parents[2]
out=ROOT/'research/nima/results/witness-record-memory-gate.json'
out.unlink(missing_ok=True)
with redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(HERE/'check_shared_leg_dg_realization.py'))
plus=source['plus']; word=source['word']; evaluate=source['evaluate']
rank=source['rank']; Z=source['Z']; values=source['values']
results=[]
for roots in ({'a':(0,0),'s':(0,0)},{'a':(3,7),'s':(2,1)}):
    arrows,delta,bases,rectangles,routes=source['build'](roots)
    assigned=dict(values)
    for a,(_,_,degree) in arrows.items():
        if degree==1: assigned[a]=evaluate(delta(word(a)),values)
    indexes={k:{p:i for i,p in enumerate(bases[k])} for k in (0,1,2)}
    d1=[{indexes[0][p]:v for p,v in delta(word(*path)).items()} for path in bases[1]]
    d2=[{indexes[1][p]:v for p,v in delta(word(*path)).items()} for path in bases[2]]
    r1=rank(d1); r2=rank(d2)
    assert (len(bases[1]),r1,r2)==(246,137,109)
    assert len(bases[1])-r1-r2==0
    # The actual degree-one reading factors through its boundary, on a full basis.
    for path in bases[1]:
        assert evaluate(word(*path),assigned)==evaluate(delta(word(*path)),values)
    cycles=[]
    for path in bases[2]:
        cycle=delta(word(*path))
        assert cycle and not delta(cycle)
        assert evaluate(cycle,assigned)==Z
        cycles.append(cycle)
    assert len(cycles)==109
    # Fixed-boundary witness changes cannot supply an independently changed reading.
    for tag,size in (('a',11),('s',4)):
        for i,j in product(range(size),repeat=2):
            first,second,_=routes(tag,i,j)
            altered=plus(first,{p:F(7,3)*c for p,c in cycles[0].items()})
            assert altered!=first and delta(altered)==delta(first)
            assert evaluate(altered,assigned)==evaluate(first,assigned)
            assert evaluate(first,assigned)==evaluate(second,assigned)
    # Keeping a filler is not zeroing it: its degree-two reading can be nonzero,
    # while its degree-one boundary reading vanishes.
    assert any(evaluate(word(*path),assigned)!=Z for path in bases[2])
    # Attempting a direct primitive witness write breaks the current response rule.
    h=next(a for a,(_,_,degree) in arrows.items() if degree==1 and 'h' in a)
    bad=dict(assigned); bad[h]=source['add'](bad[h],source['I'])
    assert evaluate(word(h),bad)!=evaluate(delta(word(h)),values)
    # Explicit OPTIONAL extension:137 new closed degree-one memory generators,
    # no new degree-two fillers. Its H1 has137 new scalar directions.
    extended_d1=d1+[{} for _ in range(137)]
    assert rank(extended_d1)==r1
    assert len(extended_d1)-r1-rank(d2)==137
    results.append({'roots':roots,'H1_original':0,'H1_with_declared_memory':137})

result={
 'status':'passed',
 'classification':'native_boundary_response_has_no_independent_witness_memory_declared_extension_required',
 'arithmetic':'exact rational',
 'checks':{'native_DG_checker_rerun':True,'complete_degree1_boundary_factorization':True,
           'all109_cycle_readings_zero':True,'all137_fixed_boundary_route_controls':True,
           'nonzero_retained_degree2_readings':True,'primitive_write_rejected':True,
           'explicit_closed_memory_extension_rank':True},
 'root_checks':results,
 'conclusion':'The existing additive boundary-response readout cannot turn retained witness choices into independently writable exchange records. Adding137 closed unfilled memory generators is a sufficient new chain-level extension, not information already supplied by the native witness model.',
 'scope':'The finite free shared-leg DG fixture and its present matrix response. Nonlinear history readings, other native structures and physical instrument memory are not ruled out.',
 'next_falsifier':'Locate an existing source or instrument memory realization with an independently specified preparation, response and update rule; verify whether it supplies the declared extension rather than merely retaining more equivalent witness paths.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
