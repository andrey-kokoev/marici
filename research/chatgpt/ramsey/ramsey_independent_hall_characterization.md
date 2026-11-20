# Beyond pair labels: exact independent-Hall characterization

Fix a vertex v of a 6-regular triangle-free graph on 22 vertices. Put U=N(v) (six independent vertices), W=V minus (U union {v}) (fifteen vertices), H=G[W], and S(w)=N(w) intersect U.

Then G has independence number <=6 iff BOTH:
1. H has independence number <=5;
2. for every independent J in H, |union_{w in J} S(w)| >= |J|.

Proof: an independent set containing v is {v} plus an independent set of H. An independent set not containing v consists of an independent J in H together with any subset of U avoiding the union of its signatures; the maximum such size is |J|+6-|union S(J)|. This proves both directions. Since every subset of an independent J is independent, condition 2 is precisely Hall's marriage condition on the signatures of every independent J. Each independent J admits a distinct representative in U for each of its members. It is NOT a matching of all fifteen W vertices into six U vertices.

Regularity gives each label u in U exactly five occurrences among signatures, sum |S(w)|=30, and deg_H(w)=6-|S(w)|; H has 30 edges. Triangle-freeness says H is triangle-free and every H edge joins disjoint signatures. Condition 2 excludes empty signatures. These facts also give an exact reverse construction: choose H and signatures satisfying these conditions and add v,U and signature incidences. This generates a 6-regular (3,7;22) witness. It is a characterization, not yet a simpler search algorithm or explanation of which assignments exist.

The original Hall-center family is the special case of fifteen distinct size-two signatures. General witnesses allow mixtures and repeated signatures; injective duad labels are not universal. Singleton/triple variations preserve the average signature size two but must still satisfy the independent-Hall condition; balance alone is insufficient.

Independent check: ramsey_independent_hall_signatures.py tested 97,043 independent sets over all 220 rooted regular catalogue records. Output JSON records the roots minimizing sum_w (|S(w)|-2)^2. Records 182..191 have respective minima 4,6,8,6,6,8,8,8,0,0. Minimum profiles of counterexamples use balanced singleton/triple defects; some have repeated signatures. This is descriptive evidence, not a proof that all roots or all generalized constructions have only sizes 1,2,3.

Next structural test: do valid degree-preserving local graph switches connect the regular counterexamples to the pair-signature family while staying triangle-free and excluding independent sevens? This would test whether uniform pairs are a useful starting configuration for a broader transition mechanism, rather than a necessary static form.
