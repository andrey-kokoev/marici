import json
from pathlib import Path

pair=[{2,4},{1,3}]
active=sorted(pair[0]|pair[1])
assert active==[1,2,3,4]

records=[]
for edge in active:
    owner=0 if edge in pair[0] else 1
    partner=next(e for e in pair[owner] if e!=edge)
    other=sorted(pair[1-owner])
    records.append({
      'soft_edge':edge,'owner_wall':owner+1,'same_wall_partner':partner,'other_wall_edges':other,
      'radial_local_form':'q_owner=delta+r*(1+u_partner.n)+O(r^2), r=|ell-C_edge|',
      'physical_measure':'d^3ell=r^2*dr*dOmega',
      'exceptional_direction_equation':'n=-u_partner-lambda*v_other, |n|=1',
      'positive_multiplier_candidate':'lambda=-2*(u_partner.v_other)/|v_other|^2, admitted only when u_partner.v_other<0',
    })

packet={
 'schema':'marici.five_site_region_pair_active_soft_blowup.v1',
 'representative':['g_123','g_125'],
 'active_soft_occurrence_count':4,
 'records':records,
 'generic_radial_division_identity':'r^2/(delta+c*r)=r/c-delta/c^2+delta^2/(c^2*(delta+c*r)), c=1+u_partner.n nonzero',
 'ordinary_log_grades':{'grade_0':0,'grade_1':0,'grade_2':'nonzero delta^2*log(delta)'},
 'first_nonanalytic_normal_order':2,
 'exceptional_polar_section':'c=1+u_partner.n=0; the linear radial coefficient vanishes and requires a separate weighted blowup',
 'exceptional_direction_multiplicity':'at most one positive direction for fixed boundary geometry',
 'carrier_classification':'existing occurrence-resolved edge-soft radial blowup',
 'coefficient_classification':'second-Rees logarithmic endpoint coefficient',
 'new_carrier_datum':False,
 'scope':'generic active-soft chart away from the polar section c=0; existence, polar-section resolution, and source coefficient remain to be solved',
}
Path('research/benincasa/results/five-site-region-pair-active-soft-blowup.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('active_soft_occurrence_count','generic_radial_division_identity','first_nonanalytic_normal_order','exceptional_polar_section','new_carrier_datum')},sort_keys=True))
