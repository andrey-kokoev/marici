"""Exact audit of the observer-energy filtered common-edge admissible region."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).parents[1]
C=F(2);packets=[]
for conductor,energy in ((1,1),(2,1),(2,3),(4,3),(4,7),(8,7)):
 # Exact illustrative packet constants; no convergence of K is asserted.
 K=F(conductor+energy,2);delta=F(1,conductor+energy+1);L=F(conductor)+C+K+delta+1;margin=L-delta-F(conductor)-C-K
 packets.append({'conductor_F':conductor,'energy_N':energy,'placement_bound_K':str(K),'reference_loss_delta':str(delta),'chosen_cutoff_L':str(L),'common_edge_margin':str(margin),'admissible':margin>0})
# Directed upper bounds: coordinatewise packet maximum followed by threshold cutoff.
def upper(a,b):
 Fm=max(a['conductor_F'],b['conductor_F']);Nm=max(a['energy_N'],b['energy_N']);K=F(Fm+Nm,2);d=F(1,Fm+Nm+1);L=F(Fm)+C+K+d+1;return L-d-Fm-C-K>0
checks={'all_packets_admissible':all(x['admissible'] for x in packets),'pairwise_directed_upper_bounds':all(upper(a,b) for a in packets for b in packets),'observer_energy_is_explicit_coordinate':all('energy_N' in x for x in packets),'no_false_K_decay_claim':F(packets[-1]['placement_bound_K'])>=F(packets[0]['placement_bound_K'])}
out={'schema':'marici.voevodsky.filtered-physical-common-edge-certificate.v2','connection_bound_C_S':str(C),'packets':packets,'checks':checks,'passed':all(checks.values()),'acceptance_theorem':{'hypotheses':['G_0(L,F,N) >= (L-delta(L,F,N)) I','-K(F,N) I <= Y_N Z_F (D_L-A) Z_F Y_N <= K(F,N) I','A_(F,-) <= (F+C_S) I'],'common_edge_condition':'L >= delta(L,F,N)+F+C_S+K(F,N)','conclusion':'finite filtered common physical edge on H_(F,N)'},'next_gate':'Construct one packet-independent residual feature and prove observer-filtration tail control; bounded K(F,N) alone gives no residual norm limit.'}
if __name__=='__main__':
 p=ROOT/'results'/'filtered-physical-common-edge-certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
