"""Audit Nima's exact prototype in isolation and test retained observation fibers.
No full-source Clifford equivalence or physical-readout selection is inferred.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import importlib.util,contextlib,io,hashlib,json,shutil,sys
base=Path(__file__).resolve().parent;root=base.parent.parent
owner=root/'research/nima'
checker=owner/'checkers/check_clifford_retained_order.py'
source=owner/'agda/RetainedComparisonSeries.agda'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks={}
formal_path=base/'retained-clifford-profiles-formal.json'
formal=json.loads(formal_path.read_text())
checks['fresh_formal']=formal['passed'] and formal['fresh'] and formal['clifford_profiles_mode']
checks['formal_sources_current']=all(sha(Path(p))==h for p,h in formal['source_snapshot_hashes'].items())
checks['formal_checker_current']=sha(base/'check_native_radar_formal.py')==formal['checker_sha256']
# Run the owner's complete checker, but redirect its sole receipt write to our
# private sandbox. All owner files, including the existing receipt, stay intact.
old_receipt=owner/'results/clifford-retained-order.json'
before={p:sha(p) for p in [checker,source,old_receipt]}
spec=importlib.util.spec_from_file_location('nima_clifford_audit',checker)
m=importlib.util.module_from_spec(spec)
saved_bytecode=sys.dont_write_bytecode
sys.dont_write_bytecode=True
try:spec.loader.exec_module(m)
finally:sys.dont_write_bytecode=saved_bytecode
sandbox=root/'temp/voevodsky-clifford-owner-audit'
(sandbox/'agda').mkdir(parents=True,exist_ok=True);(sandbox/'results').mkdir(exist_ok=True)
shutil.copyfile(source,sandbox/'agda/RetainedComparisonSeries.agda')
m.OWNER=sandbox
with contextlib.redirect_stdout(io.StringIO()):m.main()
owner_run=json.loads((sandbox/'results/clifford-retained-order.json').read_text())
checks['owner_full_checker_reran']=owner_run['signed_associativity_cases']==512 and owner_run['parenthesization_controls']==3239
checks['owner_files_unchanged']=all(sha(p)==h for p,h in before.items())
# Independent bit-sign version used in the new formal module.
def mul(g,h):
    e,a,b=g;d,c,f=h
    return (e^d^(b&c),a^c,b^f)
def rev(g):
    e,a,b=g
    return (e^(a&b),a,b)
def act(g):return g[1:]
def action_mul(g,h):return (g[0]^h[0],g[1]^h[1])
def owner_form(g):return (-1 if g[0] else 1,g[1],g[2])
G=list(product((0,1),repeat=3));B=list(product((0,1),repeat=2))
checks['bit_convention_matches_owner']=all(owner_form(mul(g,h))==m.normal_product(owner_form(g),owner_form(h)) for g,h in product(G,repeat=2))
checks['associativity_all_signed_elements']=all(mul(mul(g,h),k)==mul(g,mul(h,k)) for g,h,k in product(G,repeat=3))
checks['reversal_antimultiplicative']=all(rev(mul(g,h))==mul(rev(h),rev(g)) for g,h in product(G,repeat=2))
checks['reversal_involutive_and_inverse']=all(rev(rev(g))==g and mul(g,rev(g))==(0,0,0) and mul(rev(g),g)==(0,0,0) for g in G)
checks['action_descent_composes']=all(act(mul(g,h))==action_mul(act(g),act(h)) for g,h in product(G,repeat=2))
ad=lambda g:tuple(m.mul(m.mul(m.realize(owner_form(g)),q),m.reverse(m.realize(owner_form(g)))) for q in m.BASIS)
checks['action_labels_exactly_classify_adjoint_maps']=all((act(g)==act(h))==(ad(g)==ad(h)) for g,h in product(G,repeat=2))
sections=[]
for signs in product((0,1),repeat=4):
    choose={b:(e,)+b for b,e in zip(B,signs)}
    sections.append(all(choose[action_mul(g,h)]==mul(choose[g],choose[h]) for g,h in product(B,repeat=2)))
checks['no_multiplicative_section_all_16_choices']=not any(sections)
# Full construction trees, with reversal as an extra retained node.
def evaluate(t):
    if t[0]=='unit':return (0,0,0)
    if t[0]=='letter':return (0,1,0) if t[1]==1 else (0,0,1)
    if t[0]=='times':return mul(evaluate(t[1]),evaluate(t[2]))
    if t[0]=='reverse':return rev(evaluate(t[1]))
    raise ValueError(t)
def trees(w):
    if not w:return [('unit',)]
    if len(w)==1:return [('letter',w[0])]
    return [('times',a,b) for k in range(1,len(w)) for a in trees(w[:k]) for b in trees(w[k:])]
retained=[]
for n in range(7):
    for w in product((1,2),repeat=n):
        for t in trees(w):
            assert owner_form(evaluate(t))==m.evaluate(w)
            assert evaluate(('reverse',t))==rev(evaluate(t))
            assert ('reverse',t)[1]==t
            assert ('times',t,('letter',1))[1]==t
            # Entire source tree and both profile indices remain in the group.
            lift=evaluate(t);action=act(lift)
            packet=(action,(lift,t))
            assert packet[1][1]==t and packet[1][0]==lift
            retained.append(packet)
checks['all_3239_trees_retained']=len(retained)==3239
checks['trees_remain_distinct']=len({p[1][1] for p in retained})==3239
lift_fibers=defaultdict(list);action_fibers=defaultdict(list)
for a,(g,t) in retained:lift_fibers[g].append(t);action_fibers[a].append((g,t))
checks['regrouped_action_fibers_recover_all_trees']=sum(map(len,action_fibers.values()))==3239
checks['all_eight_lifts_and_four_actions_seen']=len(lift_fibers)==8 and len(action_fibers)==4
u=('unit',);x=('letter',1);y=('letter',2);lr=('times',x,y);rl=('times',y,x)
checks['same_action_distinct_lifts']=act(evaluate(lr))==act(evaluate(rl)) and evaluate(lr)!=evaluate(rl)
checks['same_lift_distinct_histories']=evaluate(u)==evaluate(('times',x,x)) and u!=('times',x,x)
checks['reversal_node_not_erased']=('reverse',('reverse',lr))!=lr and evaluate(('reverse',('reverse',lr)))==evaluate(lr)
checks['bracketing_not_erased']=('times',lr,x)!=('times',x,('times',y,x)) and evaluate(('times',lr,x))==evaluate(('times',x,('times',y,x)))
# Preserve the owner's hostile distinctions instead of claiming a new residue.
J=m.J;minusJ=m.scale(-1,J)
checks['lift_difference_not_nested_commutator']=m.subtract(J,minusJ)==m.scale(2,J) and m.subtract(m.mul(J,minusJ),m.mul(minusJ,J))==m.ZERO
out=dict(passed=all(checks.values()),checks=checks,owner_rerun=owner_run,
 retained_tree_count=len(retained),lift_fiber_sizes={str(k):len(v) for k,v in lift_fibers.items()},action_fiber_sizes={str(k):len(v) for k,v in action_fibers.items()},
 source_sha256={str(p.relative_to(root)):sha(p) for p in [Path(__file__),formal_path,checker,source,owner/'clifford-retained-order-recursion.md']},
 scope='Formal retention and no multiplicative lift section, exact complete finite-group checks and bounded construction-tree controls. Restricted active-sector Clifford representation; not a full-source equivalence, isometry, physical selection, or arbitrary higher-source coherence theorem.')
(base/'retained-clifford-profiles.json').write_text(json.dumps(out,indent=2)+'\n')
print('passed=',out['passed'],'checks=',len(checks),'retained_trees=',len(retained),'multiplicative_sections=',sum(sections))
raise SystemExit(0 if out['passed'] else 1)
