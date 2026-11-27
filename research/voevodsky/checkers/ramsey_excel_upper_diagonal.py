"""Use the Excel fresh upper squares BEFORE graph lookup to mark a body diagonal."""
from ramsey_excel_mirror_core import D,runpy,permutations,product,combinations,json
from ramsey_excel_successor_chart_audit import local,mirror
from ramsey_table_cube_differences import analyze

def run():
    patches=analyze(9)['pieces'][1:];upper=[];lower=[]
    for z in patches:
        a=z['start'];b=[9-i for i in reversed(a)];upper.append({local(a,r) for r in z['new']});lower.append({local(b,mirror(r)) for r in z['new']})
    top,=set.intersection(*upper);bottom,=set.intersection(*lower);word=lambda k:''.join(map(str,k));diagonal=tuple(sorted([word(top),word(bottom)]));assert diagonal==('000','111')
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));C=g['cells'];E=frozenset(tuple(sorted((C[i],C[j]))) for i,j in combinations(range(26),2) if g['G'][i]>>j&1)
    def move(e,p,b):
        def cell(s):return ''.join('*' if s[j]=='*' else str(int(s[j])^k) for j,k in zip(p,b))
        return frozenset(tuple(sorted((cell(s),cell(t)))) for s,t in e)
    zero=(0,0,0);orbit={move(E,p,b) for p in permutations(range(3)) for b in product(range(2),repeat=3)}
    ds=[tuple(sorted((s,''.join(str(1-int(x)) for x in s)))) for s in C if '*' not in s and s.startswith('0')];assert all(sum(d in e for d in ds)==1 for e in orbit);pair=[e for e in orbit if diagonal in e];assert len(pair)==2
    M=lambda e:move(e,(2,1,0),(1,1,1));assert M(pair[0])==pair[1]
    stabilizers={''.join(map(str,p)):sum(move(e,p,zero)==e for e in pair) for p in permutations(range(3))};assert sorted(stabilizers.values())==[0,0,0,2,2,2]
    # Face normal i at the all-high corner vs the edge along axis j at all-high.
    # Read the full matrix so that we do not pick one distinguishing edge post hoc.
    def matrix(e):
        return [[int(tuple(sorted((''.join('1' if k==i else '*' for k in range(3)),''.join('*' if k==j else '1' for k in range(3))))) in e) for j in range(3)] for i in range(3)]
    mats=sorted([matrix(e) for e in pair]);assert not any(any(row) for m in mats for row in m)
    # Instead inspect the disjoint edge at i=0 and the remaining coordinate high.
    def across(e):
        return [[0 if i==j else int(tuple(sorted((''.join('1' if k==i else '*' for k in range(3)),''.join('*' if k==j else '0' if k==i else '1' for k in range(3))))) in e) for j in range(3)] for i in range(3)]
    cycles=sorted(across(e) for e in pair);assert cycles==[[[0,0,1],[1,0,0],[0,1,0]],[[0,1,0],[0,0,1],[1,0,0]]];out=dict(across_face_matrices=cycles,upper_intersection=word(top),lower_intersection=word(bottom),extra_graph_condition='color the line between the two intersection corners red',all_completions=len(orbit),compatible=len(pair),mirror_exchanges=True,axis_permutations_fixing_individual_counts=stabilizers,high_face_to_high_edge_matrices=mats,shared_red=len(pair[0]&pair[1]));print(out);dest=D.parent/'results/ramsey_excel_upper_diagonal_orientation.json';text=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==text;dest.write_text(text)
if __name__=='__main__':run()
