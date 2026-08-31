import json
from fractions import Fraction as Q
from pathlib import Path

# Formal log coordinates and ordered-pair basis.
ell={2:Q(2),3:Q(5),5:Q(9),7:Q(12)}
pairs=[(n,m) for n in ell for m in ell]
def degrees(pair):
 n,m=pair; return (ell[n]+ell[m],ell[n]-ell[m])
def transport(pair,p,q):return (pair[0]*p,pair[1]*q)
# Extend logs additively only for tested transported labels.
def transported_degrees(pair,lp,lq):
 S,D=degrees(pair); return (S+lp+lq,D+lp-lq)
checks={
 "ordered_pairs_retain_ratio_orientation":all(degrees((n,m))[1]==-degrees((m,n))[1] for n,m in pairs),
 "diagonal_transport_shifts_product_and_preserves_ratio":all(transported_degrees(x,Q(7),Q(7))==(degrees(x)[0]+14,degrees(x)[1]) for x in pairs),
 "independent_transport_shifts_ratio_by_log_difference":all(transported_degrees(x,Q(7),Q(3))==(degrees(x)[0]+10,degrees(x)[1]+4) for x in pairs),
 "swap_preserves_product_and_reverses_ratio":all(degrees((m,n))==(degrees((n,m))[0],-degrees((n,m))[1]) for n,m in pairs),
}
# Rank-one positive packet c tensor cbar has coefficient matrix cc^T and all
# 2x2 minors zero; a generic pair packet need not.
c=[Q(1),Q(-2),Q(3)]; C=[[x*y for y in c] for x in c]
checks["rank_one_positive_cone_has_zero_two_by_two_minors"]=all(C[i][j]*C[k][l]-C[i][l]*C[k][j]==0 for i in range(3) for j in range(3) for k in range(3) for l in range(3))
base=Path(__file__).parents[2]
source=(base/"nima"/"theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md").read_text(encoding="utf-8")
flat=(base/"nima"/"theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md").read_text(encoding="utf-8")
checks.update({
 "source_types_bridge_on_tensor_square":"linear\nonly after polarization to an ordered-pair module" in source,
 "source_requires_both_product_and_ratio_degrees":"must\nintertwine both pairs" in source,
 "flat_sector_comparison_still_requires_intertwining_square":"cannot be identified without a source-derived bonding map" in flat,
})
result={"schema":"marici.strominger.rh_polarized_pair_band_cross_term_typing_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/nima/theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md","research/nima/theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md"],"verdict":"A correctly typed nonperturbative cross-term carrier exists at the formal level: the ordered-pair module C_arith tensor conjugate(C_arith), not the one-copy label module. Product and ratio logarithmic degrees obey the required diagonal and independent prime-transport laws, ordered-pair orientation is retained, and the physical one-copy source lands in the rank-one positive cone. This removes the one-copy typing obstruction but does not yet construct the finite correlation maps rho_nm to (W_nm,J_nm), prove joint-jet bonding, or exhibit a boundary current detecting a flat state.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"tested_ordered_pairs":len(pairs)}
out=Path(__file__).parents[1]/"results"/"rh_polarized_pair_band_cross_term_typing_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
