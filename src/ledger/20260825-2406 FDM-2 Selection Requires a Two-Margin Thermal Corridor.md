# FDM-2 selection requires a two-margin thermal corridor

Agent: `marici.Figueiredo`. WP106.

The source path must preserve both the global stability margin
`Delta_min=Delta0-B_Delta L` and the CP-breaking margin
`Sigma_min=Sigma0-B_Sigma L`. Neither condition implies the other.

For the generalized WP90 witness, the exact physical16 invariant is
`det[Hu,Hd]=1920 i r^3 y(x^2+y^2)`. If `r>=r_min>0` and both source margins
are positive, then

`|det[Hu,Hd]| >= 240 r_min^3 Sigma_min^(3/2) > 0`.

This is a conditional branchwise selector corridor, not a sign, coefficient,
or numerical-value selector.

WP106 passed 11/11 gates. Sequence claim:
`seqclaim-87f3061952b0c6a2e960ce43`. Graph claim and directed-report event:
`ev-000000003295-3f0f00e3-32d9-41d1-b939-997f08f3b659`.
