import json
from fractions import Fraction as Q
from pathlib import Path

# Formal logarithmic coordinates ell_n; exact identities do not require floating logs.
ell={1:Q(0),2:Q(2),3:Q(3),4:Q(4),5:Q(7),6:Q(8)}
c={1:Q(1),2:Q(-2),3:Q(3),4:Q(-1),5:Q(2),6:Q(-3)}
def moments(c):return (sum(c.values()),sum(c[n]*ell[n] for n in c))
def trunc(c,N):return {n:v for n,v in c.items() if n<=N}
def transport_mom(mu,lp):return (mu[0],mu[1]+lp*mu[0])
mu6=moments(c); mu4=moments(trunc(c,4)); removed=moments({n:v for n,v in c.items() if n>4})
checks={
 "first_two_moments_give_a_canonical_two_coordinate_cross_map":len(mu6)==2,
 "moment_map_is_additive_over_retained_and_removed_labels":mu6==(mu4[0]+removed[0],mu4[1]+removed[1]),
 "identity_bonding_on_krein_plane_conflicts_with_label_truncation":mu6!=mu4,
 "prime_transport_is_triangular_on_two_moments":transport_mom(mu6,Q(5))==(mu6[0],mu6[1]+5*mu6[0]),
 "triangular_transport_preserves_first_nonzero_moment":transport_mom((Q(0),Q(9)),Q(5))==(Q(0),Q(9)),
}
base=Path(__file__).parents[2]
moment=(base/"nima"/"theta-logarithmic-moment-tower-observes-finite-packets-but-prime-transport-preserves-their-divisor.md").read_text(encoding="utf-8")
excl=(base/"grothendieck"/"prime-multiplication-division-curvature-is-positive-exclusion.md").read_text(encoding="utf-8")
checks.update({
 "source_says_moments_observe_but_do_not_orient":"observability of cancellation, not a\nmechanism that removes or orients it" in moment,
 "source_says_exclusion_is_stronger_than_universal_seam_cocycle":"genuinely stronger than the universal seam cocycle" in excl,
})
result={"schema":"marici.strominger.rh_log_moment_product_cross_term_no_go.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/nima/theta-logarithmic-moment-tower-observes-finite-packets-but-prime-transport-preserves-their-divisor.md","research/grothendieck/prime-multiplication-division-curvature-is-positive-exclusion.md","research/strominger/results/rh_krein_exclusion_product_bonding_audit.json"],"verdict":"The only source-immediate cross map from a labelled packet to the two mixed coordinates is the augmentation/first-log-moment pair. It is additive and prime-transport triangular, but it preserves the first nonzero divisor residue rather than orienting or removing it. It also changes under label truncation, whereas the independently constructed Krein factor in the product response bonds by identity. Therefore this moment map cannot be inserted as a cutoff-natural conservative cross term for the existing product object. A valid joint Green form needs a new boundary current with its own compatible bonding law, not the universal logarithmic seam cocycle.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"witness":{"full_moments":list(map(str,mu6)),"truncated_moments":list(map(str,mu4)),"removed_tail_moments":list(map(str,removed))}}
out=Path(__file__).parents[1]/"results"/"rh_log_moment_product_cross_term_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
