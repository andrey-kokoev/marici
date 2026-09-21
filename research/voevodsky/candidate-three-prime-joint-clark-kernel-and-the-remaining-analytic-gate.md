# Candidate three-prime joint Clark kernel and the remaining analytic gate

The passed three-prime cut diagram fixes the only viable finite candidate for the cross-cut pairing.

For a route with event features `g1,g2,g3`, retain the ordered tensor record before any cut deletion and use

    q_joint = q_cut ⊗ q_rec,
    q_rec|degree r = tau^(2r) C_Clark^(⊗r).

Equivalently, after sheet reduction, replace each occurrence of `C_Clark` by `J` and pair the ordered event slots before applying any rejoining map. The pairing is block-diagonal in the retained vertex-chain label, but not in the record degrees: all cross terms inside each tensor degree are retained.

The three-prime checker verifies the corresponding finite identities:

- the joint carrier has rank 48;
- the two marginal ghosts have nonzero joint pairing;
- deleting either cut and then taking the transpose gives the rejoin mate;
- the two possible rejoin orders have equal contragredient composites;
- opposite polarity changes the lower carrier to `-C_Clark` and commutes with rejoining.

This candidate cannot be obtained by pulling back a terminal Clark form: both marginal ghosts lie in the terminal kernel, while their joint pairing matrix is

    [[6,0],[0,-18]].

## Remaining analytic gate

To identify `q_joint` with the arithmetic Clark Green form, expand the actual sewn kernel for three ordered events before terminal aggregation. For every pair of marked histories `h,k`, compute the full cross-cut coefficient

    q_Clark(h,k)
      = sum over retained shell ports and tensor degrees
          tau^(2r) < C_Clark^(⊗r) L_r(h), L_r(k) >,

including the affine-origin correction on each translated moment and the seam transports at both internal cuts.

The required comparison is the matrix identity on the 48 source columns

    K_arithmetic = R_joint^* Q_joint R_joint,

where `R_joint` is the ordered, typed, sheet-reduced receiver. It must be checked before either cut is forgotten. The two alternating marginal ghosts are the negative control: the left side must pair them as the joint matrix above, rather than annihilate them as every terminal pullback does.

No sampled theta value can certify this equality. The calculation must retain the analytic spectral family (or prove equality of the corresponding holomorphic kernels), use the already established moment-origin transport, and include all endpoint and first-moment cross terms.

Thus the next implementation is not another rank test. It is an explicit three-event Clark kernel expansion followed by a symbolic/holomorphic equality check against `R_joint^* Q_joint R_joint`. Until that expansion exists, the coefficient candidate is established but its identification with the full arithmetic Green form remains open.
