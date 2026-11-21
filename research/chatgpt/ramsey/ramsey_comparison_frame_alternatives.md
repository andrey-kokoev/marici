# Typed row meaning determines a canonical re-lift and a transport phase

ramsey_comparison_frame_alternatives.py explicitly compares the two specifications after center transfer G->B:
- Keep the original22-vertex permutation R: R(B) changes ten of the fifteen duad-to-label neighborhood signatures in the new-center presentation and replaces25 red edges.
- Conjugate comparison by any of the five K:G->B: (KRK)(B)=K(RG). This preserves EVERY new duad-to-label signature, replaces five red edges, and fixes the transported pole marks.
The two resulting graphs are different for every K (25 edge replacements separate the comparison outputs). Thus the choice is operational, not a coordinate synonym. The earlier commuting graph-update square remains true, but its fixed-R lower arrow is not a pure row move within the new incidence chart.

There is a natural additional rule that resolves even the fivefold marking ambiguity:
**Preserve R's action on the six NEW label vertices, and lift that action canonically to their fifteen pairs.**

Given B, new center v and its six neighbors U, each outside vertex w has unique signature S(w), a two-subset of U. Define Rhat(v)=v, Rhat(u)=R(u) for u in U, and Rhat(w) to be the unique outside vertex with signature R(S(w)). This is determined without searching marking transports. It agrees with R on the new label vertices but corrects its action on the fifteen pair vertices.

Exactly ONE of the five transports satisfies KRK=Rhat: phase3 in the deterministic stored list. This gives a unique reversible marking map once the typed-row preservation rule is imposed. It is NOT the previously proposed selected-duad-exchange convention (phase4). For phase3, old entry selected7 becomes11, with new partition[6,11,14]; old exit selected14 becomes20, with new partition[4,7,20]. Both transported poles are stationary under Rhat, not under the uncorrected R.

Interpretation: if 'row change' means retaining the same six-label action and only changing the matching, the correct lower operation is the canonical re-lift, not the unchanged vertex permutation. That principle selects the transport and restores pole stationarity. This is a semantic specification of what row change must preserve, not a proof that the original strings already supplied that specification.

Evidence: companion JSON contains every comparison permutation, chart-change list, edge distances, canonical re-lift and selected phase. The recorded five-K transport lists and incidence labels are prerequisites.
