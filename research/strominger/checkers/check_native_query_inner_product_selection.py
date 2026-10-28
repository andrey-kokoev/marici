"""General positive pairings defeat transport-only selection; query projections repair it."""
from pathlib import Path
from fractions import Fraction as F
import contextlib, io, runpy, json, hashlib
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
with contextlib.redirect_stdout(io.StringIO()):
    p=runpy.run_path(str(BASE/'checkers/check_native_query_pairing_selection.py'))
group=p['group']; compose=p['compose']; features=p['features']; n=len(group)
def inner(x,y,lam):
    return (sum(a*b for a,b in zip(x,y))+lam*sum(x)*sum(y))/(3+9*lam)
def event(state,e,lam):
    q=state[:n];r=list(state[n:]);names=list(features);i=names.index(e);f=features[e]
    seen=inner(f,q,lam);delta=r[i]-seen;r[i]=seen
    return tuple(a+b*delta for a,b in zip(q,f))+tuple(r)
responses=[]
for lam in (F(0),F(1,9)):
    # I+lambda J is strictly positive for lambda>=0 by its displayed form.
    assert lam>=0
    for h in p['generators']:
        perm=[group.index(compose(h,g)) for g in group]
        for i in range(n):
            for j in range(n):
                assert F(i==j)+lam==F(perm[i]==perm[j])+lam
    for f in features.values(): assert inner(f,f,lam)==1
    initial=(F(0),)*n+tuple(F(e=='AB') for e in features)
    first=event(initial,'AB',lam)
    assert first==features['AB']+(F(0),)*6
    final=event(first,'BA',lam)
    response=final[n+list(features).index('BA')]
    assert response==(1+9*lam)/(3+9*lam)
    # Whole-domain involution and budget preservation via basis-pair tests.
    basis=[tuple(F(i==j) for i in range(n+6)) for j in range(n+6)]
    def budget_pair(x,y):return inner(x[:n],y[:n],lam)+sum(a*b for a,b in zip(x[n:],y[n:]))
    for e in features:
        cols=[event(b,e,lam) for b in basis]
        assert all(event(c,e,lam)==b for c,b in zip(cols,basis))
        assert all(budget_pair(cols[i],cols[j])==budget_pair(basis[i],basis[j])
                   for i in range(n+6) for j in range(n+6))
    responses.append(str(response))
assert responses==['1/3','1/2']
# Self-adjoint multiplication P_e requires (f_e(g)-f_e(k))*H[g,k]=0.
# Left isometries propagate these zeros across simultaneous translations.
locally_unseparated=[];witnesses=[]
for i,g in enumerate(group):
    for j,k in enumerate(group):
        if i==j:continue
        if all(f[i]==f[j] for f in features.values()):locally_unseparated.append((i,j))
        witness=next(((h,e) for h in group for e,f in features.items()
                      if f[group.index(compose(h,g))]!=f[group.index(compose(h,k))]),None)
        assert witness is not None
        witnesses.append(witness)
assert len(locally_unseparated)==6
report={'status':'pass','responses':responses,'positive_pairings':'H_lambda=(I+lambda J)/(3+9lambda), lambda=0 or 1/9',
        'transport_isometry_in_both':True,'off_diagonal_entries_forced_zero_with_translated_queries':len(witnesses),
        'ordered_pairs_not_separated_by_untranslated_six_queries':len(locally_unseparated),
        'repair':'Native generator isometries plus self-adjoint multiplication by six native queries force H=cI.',
        'scope':'Exact finite algebra and written general classification; no physical projector authority or new Agda theorem.'}
files=[Path(__file__).resolve(),BASE/'native-query-inner-product-selection-v1.md',
       ROOT/'research/nima/agda/NativeSeedTransitionProbe.agda']
report['sha256']={str(f.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
out=BASE/'results/native-query-pairing-selection/general-inner-product.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sha256'}))
