"""Small exact geometry checks prompted by the two new PDFs; not model validation."""
from fractions import Fraction as Q
from itertools import permutations,product
from hashlib import sha256
from pathlib import Path
from datetime import datetime,timezone
import json

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve()
OUT=ROOT/'research/strominger/results/new-nuclear-pdf-relevance/geometry-audit.json'

def main():
    D=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    second=[[Q(sum(v[i]*v[j] for v in D),3) for j in range(3)] for i in range(3)]
    transverse=[[4*int(i==j)-second[i][j] for j in range(3)] for i in range(3)]
    check1=transverse==[[Q(8,3)*int(i==j) for j in range(3)] for i in range(3)]
    def fourth(n):return Q(sum(sum(a*b for a,b in zip(v,n))**4 for v in D),9*sum(x*x for x in n)**2)
    axis,diagonal=fourth((1,0,0)),fourth((1,1,1))
    check2=axis==Q(4,9) and diagonal==Q(28,27) and axis!=diagonal
    nn=sorted({v for p in set(permutations((1,1,0))) for s in product((-1,1),repeat=3) for v in [tuple(a*b for a,b in zip(p,s))]})
    representatives=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
    group={v:int(i>=2) for i,v in enumerate(representatives)}
    grouping=[]
    for v in representatives:
        same=sum(group[tuple((a+b)%2 for a,b in zip(v,delta))]==group[v] for delta in nn)
        grouping.append({'fcc_coset':v,'same_group_neighbors':same,'opposite_group_neighbors':len(nn)-same})
    check3=len(nn)==12 and all(r['same_group_neighbors']==4 and r['opposite_group_neighbors']==8 for r in grouping)
    def same_row_steps(direction):
        k=1
        while sum(k*x for x in direction)%2:k+=1
        return k, sum((k*x)**2 for x in direction)
    rows={name:same_row_steps(direction) for name,direction in [('110',(1,1,0)),('111',(1,1,1))]}
    check4=rows=={'110':(1,2),'111':(2,12)}
    threshold=Q('938.272')+Q('0.511')-Q('939.565')
    checks={'tetrahedral_quadratic_transverse_identity_true':check1,'quadratic_identity_does_not_establish_higher_order_isotropy':check2,
      'grouping_four_FCC_cosets_into_two_does_not_produce_six_coordinate_rocksalt_graph':check3,
      'FCC_110_close_packed_row_is_not_111_row':check4,'literal_proton_electron_binding_deficit_is_negative':threshold==Q('-0.782')}
    assert all(checks.values())
    marton=ROOT/'references/preprints202604.0421.v1.pdf'
    migal=next(p for p in (ROOT/'references').glob('*.pdf') if '72-1_' in p.name)
    result={'status':'exact_geometry_audit_passed_not_physical_model_validation','recorded_at':datetime.now(timezone.utc).isoformat(),'checks':checks,
      'source_sha256':{p.relative_to(ROOT).as_posix():sha256(p.read_bytes()).hexdigest() for p in [HERE,marton,migal]},
      'tetrahedral_second_moment':[[str(x) for x in row] for row in second],
      'sum_transverse_projectors':[[str(x) for x in row] for row in transverse],
      'normalized_fourth_directional_moments':{'cube_axis':str(axis),'body_diagonal':str(diagonal)},
      'two_group_FCC_neighbor_counts':grouping,'first_FCC_site_along_rows_step_multiplier_and_squared_distance':rows,
      'illustrative_empirical_mass_inputs_MeV':{'proton':'938.272','electron':'0.511','neutron':'939.565'},
      'mp_plus_me_minus_mn_MeV':str(threshold),
      'scope':'Only stated geometry and arithmetic implications checked. Does not prove or disprove every dynamical claim, infer actual neutron constituents, or identify quantum spin with a lattice angle.'}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'checks':len(checks),'fourth_moments':[str(axis),str(diagonal)],'FCC_group_neighbor_counts':'4 same,8 opposite; not6 opposite','binding_deficit_MeV':str(threshold),'receipt':OUT.relative_to(ROOT).as_posix()}))

if __name__=='__main__':main()
