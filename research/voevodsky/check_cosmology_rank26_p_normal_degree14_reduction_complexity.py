"""Familywise pivot-elimination complexity for degree-14 p-normal reductions."""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(ROOT/'research'/'benincasa'),str(ROOT/'research'/'voevodsky')]
import physical_four_mark_residue_twisted_derham as base
import check_rank26_total_energy_triple_relation_module as rees
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/f'cosmology_rank26_p_normal_degree14_reduction_complexity_p{base.PRIME}.json'

def reduce_steps(row,pivots):
    row=dict(row); steps=0
    while row:
        pivot=max(row); coefficient=row[pivot]; existing=pivots.get(pivot)
        if existing is None: return row,steps
        for column,value in existing.items(): base.add_value(row,column,-coefficient*value)
        steps+=1
    return row,steps

def summarize(rows,pivots,start,end):
    nonzero=zero=total=max_steps=0; histogram={}
    for row in rows[start:end]:
        if row: nonzero+=1
        residue,steps=reduce_steps(row,pivots); assert not residue
        zero+=1; total+=steps; max_steps=max(max_steps,steps); histogram[str(steps)]=histogram.get(str(steps),0)+1
    return {'rows':end-start,'nonzero_input_rows':nonzero,'zero_remainders':zero,'total_pivot_eliminations':total,'max_pivot_eliminations_per_row':max_steps,'pivot_elimination_histogram':histogram}

def main():
    assert rees.AMBIENT==14
    protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); assert protocol['passed']
    point=tuple(protocol['test_point_xyz']); nx=tuple(protocol['integral_unit_normals']['nx']); ny=tuple(protocol['integral_unit_normals']['ny']); t=tuple(protocol['integral_unit_normals']['p_tangent_difference'])
    _,columns=rees.column_packet(); special=list(rees.raw_relations(point,columns)); dx,_=adapter.derivative_rows(columns,point,nx); dy,_=adapter.derivative_rows(columns,point,ny); dt,_=adapter.derivative_rows(columns,point,t)
    pivots={}
    for row in special: base.add_pivot(dict(row),pivots)
    for row in dt: base.add_pivot(dict(row),pivots)
    assert len(pivots)==11603
    ranges={'IBP_derivative_relations':(0,480),'K_multiplication_relations':(480,4704),'marked_q_multiplication_relations':(4704,29904)}
    families={}
    for family,(start,end) in ranges.items(): families[family]={'nx':summarize(dx,pivots,start,end),'ny':summarize(dy,pivots,start,end)}
    out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-degree14-reduction-complexity.v1','status':'familywise_zero_reduction_complexity_measured','field':base.PRIME,'ambient_relation_degree':14,'fixed_S_plus_T_rank':len(pivots),'family_ranges':{k:list(v) for k,v in ranges.items()},'families':families,'interpretation':'All rows reduce to zero; pivot-elimination counts measure finite certificate complexity without retaining coefficient vectors.','limitations':['pivot counts depend on deterministic column and row order','not a basis-independent homotopy length','finite degree 14 only'],'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
