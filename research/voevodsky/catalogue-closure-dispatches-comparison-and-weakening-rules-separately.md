# Catalogue closure dispatches comparison and weakening rules separately

Fresh `check_catalogue_edge_type_dispatch.py` validates all four packets on the synthetic generation-2 square. P proves x<=2 and Q x<=3 with identical x-upper weights and increasing surplus: P->Q passes typed weakening but fails comparison because targets differ. S and R independently prove x<=4 with different multipliers: S->R passes same-target comparison but fails the exact weakening rule requiring unchanged weights and bound/surplus increment. A generic 'both endpoints valid' gate accepts too much; edge rules must be dispatched by declared type.

The fixture does not authenticate observed history, source issuer or an analytic role assignment. Next test UNKNOWN or ambiguous edge labels: a candidate with valid endpoint packets must reject unknown rule types rather than defaulting to a permissive comparison or weakening interpretation; require exact rule-version binding.
