"""Exploratory arithmetic, not a fitted nuclear model or physical validation."""
import json
from pathlib import Path
from fractions import Fraction
from math import comb

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/strominger/results/reciprocal-tetrahedral-numerology/arithmetic.json'

def main():
    moves=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    h=lambda v:sum(v)
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    primitives=[(0,2,2),(2,0,2),(2,2,0)]
    u=sub(primitives[0],primitives[1]);v=sub(primitives[0],primitives[2])
    checks={
      'mutual_centroid_displacements_sum_zero':all(sum(t[j] for t in moves)==0 for j in range(3)),
      'A_primitive_height_step_four':all(h(t)==4 for t in primitives),
      'B_offset_height_three':h((1,1,1))==3,
      'one_plus3_three_minus1':sorted(map(h,moves))==[-1,-1,-1,3],
      'horizontal_basis_is_equilateral_triangular':h(u)==h(v)==0 and dot(u,u)==dot(v,v)==8 and dot(u,v)==4,
      'ABC_stack_repeats_after_three_A_layers':sub(tuple(3*x for x in primitives[0]),(4,4,4))==tuple(a+b for a,b in zip(u,v)),
      'tetrahedron_all_six_squared_edges_eight':all(dot(sub(a,b),sub(a,b))==8 for i,a in enumerate(moves) for b in moves[i+1:])}
    assert all(checks.values())
    nuclei=[('deuterium2',1,1),('helium4',2,2),('oxygen16',8,8),('calcium40',20,20),('calcium48',20,28),('iron56',26,30),('lead208',82,126),('uranium238',92,146)]
    table=[]
    for name,P,N in nuclei:
        table.append({'nucleus':name,'P':P,'N':N,'A':P+N,'N_minus_P':N-P,
          'N_side_missing_slots_minus_P_side_missing_slots':4*(N-P),
          'minimum_fraction_of_all_fourfold_slots_missing':str(Fraction(abs(N-P),P+N)),
          'minimum_missing_slot_percent':round(100*abs(N-P)/(P+N),3)})
    # Approximate familiar empirical inputs, not new measurements or sourced precision data.
    mp,mn,me=938.272,939.565,0.511
    magic=[2,8,20,28,50,82,126]
    tetrahedral=[comb(k+2,3) for k in range(1,8)]
    result={'status':'arithmetic_passed_not_physics','checks':checks,
      'height_coordinate':'h=x+y+z; orthonormal vertical distance is h/sqrt(3)',
      'layers':[{'h':h,'family':'A (N center/P vertex)' if h%4==0 else 'B (P center/N vertex)'} for h in range(12) if h%4 in (0,3)],
      'gaps':'3,1,3,1,... in h; not equally spaced occupied planes',
      'tetrahedral_site_counts':tetrahedral,'twice_tetrahedral_counts':[2*x for x in tetrahedral],
      'empirical_nuclear_magic_numbers':magic,
      'first_failure_of_twice_tetrahedral_shell_hypothesis':{'ordinal':4,'predicted':40,'reference':28},
      'spin_warning':'Sites were whole nucleons; treating each as a two-spin orbital is an additional, unconstructed occupation rule.',
      'fourfold_bipartite_occupancy':table,
      'helium4_obstruction':'Connected2P2N with only source nearest-neighbor links must be a length3 path: source is bipartite with girth6, so no4-cycle or tetrahedral K4 bonding graph.',
      'approximate_empirical_mass_inputs_MeV':{'proton':mp,'neutron':mn,'electron':me},
      'mass_split_MeV_approx':round(mn-mp,3),'fractional_mass_split_percent_approx':round(100*(mn-mp)/mp,4),
      'free_neutron_beta_Q_MeV_approx':round(mn-mp-me,3),
      'scope':'Exploratory known-constraint arithmetic. No fitted interaction, physical P/N assignment, nuclear stability prediction or completion of the separate flag-family iteration.'}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
