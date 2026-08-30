# The Bockstein horizontality stencil crosses a rank jump

The proposed projective-variation precheck samples the x-direction through `(1,3,4)`. At that point the exported exact-relation dimension is 11 and the Bockstein image rank is 11. At `(3,3,4)` they are respectively 2 and 1.

Consequently these samples do not belong to one constant-rank family. There is no rank-one Bockstein subbundle across the displayed stencil, so differentiating normalized representatives cannot test its horizontality. The varying normal-form support is not merely a frame nuisance; the fiber type itself changes.

The corrected order is:

1. derive the discriminant or Fitting locus on which the relation and Bockstein ranks jump;
2. restrict to one source-defined constant-rank open stratum;
3. construct the Bockstein line and ambient quotient there;
4. compute both connection residuals modulo the transported line;
5. separately study specialization toward the rank-jump locus.

The lightweight audit is `checkers/check_bockstein_stencil_rank_stratum.py`.
