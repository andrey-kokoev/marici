"""Source-only numerical check of the theta-kernel Rouché inequality."""
import json,math
from pathlib import Path
from reduced_source_pick_hostile_scan import eta_pair

def zeta(s,depth):
    eta,_=eta_pair(s,depth);return (eta/(1-2**(1-s))).real
def xi(s,depth):return .5*s*(s-1)*math.pi**(-s/2)*math.gamma(s/2)*zeta(s,depth)
center=xi(.5,80);edge=xi(1.5,80);center_control=xi(.5,72);edge_control=xi(1.5,72)
variation=edge-center;margin=center-variation
result={'Xi_one_half':center,'Xi_three_halves':edge,'theta_variation_majorant':variation,
        'rouche_margin_Xi_half_minus_variation':margin,'Xi_three_halves_less_than_twice_Xi_half':edge<2*center,
        'depth_72_80_max_discrepancy':max(abs(center-center_control),abs(edge-edge_control)),
        'implication':'certified inequality Xi(3/2)<2 Xi(1/2) implies Xi has no zeros for |s-1/2|<=1',
        'interval_certified':False,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'xi-centered-unit-disk-rouche.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
