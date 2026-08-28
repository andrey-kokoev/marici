# Source prime-chain optical Schur jet

## What was tested

The synthetic reciprocal quartet has now been replaced at the local rung by
Nima's source-derived prime valuation chain. For one labelled prime, the
finite operator uses the nilpotent shift `S_N`, the primitive incidence `e_0`,
and the augmentation row assigning one to every valuation state. Its bordered
determinant produces the geometric Euler truncation rather than inserting that
factor as a fitted scalar.

Adding valuation state `e_(N+1)` is an exact block extension. When the retained
coordinates are the old valuation states followed by the boundary port, the
new diagonal block is constant `E=1`. The incoming block carries the
augmentation of the new state, and the outgoing block carries its `-q`
incidence from `e_N`.

## Result

For the additions `N=1 -> 2` and `N=2 -> 3`, the checker proves symbolically:

- the complete Schur logarithmic first jet equals the determinant increment;
- it equals the independently source-derived logarithmic increment of the
  geometric prime-chain current;
- the two increments telescope exactly;
- the new diagonal block's own logarithmic jet is zero;
- consequently the entire nonzero increment is carried by mixed incidence and
  retained-state transport.

At `q=1/2`, the two successive jets are `10/21` and `34/105`; their sum is
`4/5`, exactly the direct `N=1 -> 3` determinant-frame increment.

This is the first non-synthetic optical Schur/current match in the branch. It
also confirms the earlier warning: reading only the newly added mode's
diagonal trace misses the whole arithmetic increment.

## Boundary

This qualifies one source-local valuation chain, not the completed theta
operator. The local chain is acyclic in the open contraction sector and does
not contain RH-strength zeros. The next block must couple the two reciprocal
valuation cones while retaining primitive renormalization, prime-square,
seam, endpoint, and archimedean channels. That coupled extension is where a
root-local optical normal-current test can first bear on the critical line.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_source_prime_chain_optical_schur_jet.py
```
