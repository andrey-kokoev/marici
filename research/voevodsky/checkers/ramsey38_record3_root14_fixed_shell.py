"""Same array, same release, different minimum mesh size for two particular shells."""
from ramsey38_record3_polygon_trial import pf,cf,rows,fmt,json
from ramsey38_global_shell import sub
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary

def check():
    r=rows(14);released=r[25];P=set.union(set(),*r.values());bad=frozenset(map(frozenset,json.loads(pf.read_text())['predictions']['14']['25']['shell']));w=frozenset(map(frozenset,json.loads(cf.read_text())['certificates']['14']['25']));good=boundary(w);ears=[r[i] for i in (2,15,20)]
    assert released=={12,17} and shelling(w) and bad^good==sub(ears[0],3)
    # Two boundary faces of a tetrahedron close the entire fan at their common edge.
    locked={frozenset.intersection(*(bad&sub(t,3))):t for t in ears};assert set(locked)==set(map(frozenset,((13,17),(1,17),(3,12))))
    tips={v for v in P-released if all(not e<=(released|{v}) or released|{v}<=t for e,t in locked.items())};assert tips=={18,22} and not any(released<=f for f in bad)
    # Peel three ears, cone the residual sphere, then introduce the required
    # interior edge by a 2-to-3 move. Reattach the observed ears unchanged.
    residual=bad
    for t in ears:residual=residual^sub(t,3)
    x=28;mesh={f|{x} for f in residual};joint=frozenset((x,18,22));old={joint|{v} for v in released};assert old<=mesh and not any(released<=t for t in mesh)
    mesh=(mesh-old)|{released|e for e in sub(joint,2)}|set(ears)
    order=shelling(frozenset(mesh));assert order and boundary(mesh)==bad
    assert all(any(s<=t for t in mesh) for s in r.values()) and {v for v,s in r.items() if len(s)<4 and not any(s<=f for f in boundary(mesh))}=={25}
    print('boundary change:',fmt(good-bad),'->',fmt(bad-good));print('locked edges:',fmt(locked),'available link vertices:',sorted(tips));print('fixed-shell filling:',len(mesh),'cells, row 25 link:',fmt(t-released for t in mesh if released<=t),'shelling:',[sorted(t) for t in order]);return mesh
if __name__=='__main__':check()
