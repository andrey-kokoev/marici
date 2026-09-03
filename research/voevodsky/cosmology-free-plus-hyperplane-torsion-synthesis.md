# Free and hyperplane-torsion degree correction

## Question

Do the primitive free class and `H*(-1)` form two components of one obstruction group?

## Claim boundary

No. The prior direct-sum synthesis conflated total degrees. The free class is represented by `{u,v}` in motivic degree two and by `Xi_log` in de Rham degree two. The isolated divisor-sign cycle represents `H*(-1)` in `CH^2(P2,1)=H_M^3(P2,Z(2))`, one motivic degree higher.

The full tame tuple `(v^-1,u,-v/u)` is a Gersten boundary of `{u,v}`. Splitting it into monomial and constant-sign pieces is not a splitting by cocycles: the isolated sign piece can represent `H*(-1)` only because the complementary nonconstant piece carries the opposite Gersten class. Their sum is exact in the Gersten complex.

Therefore `Z plus Z/2` is at most bookkeeping for split representatives, not the cohomology group of the horn target. Rationalization forgets signs, but the sign does not constitute an independent degree-two horn obstruction.

## Disposition

This packet supersedes the earlier free-plus-torsion direct-sum claim. The valid result is narrower: `H*(-1)` obstructs isolating the sign as a residue with no compensating data. The next leaf reconstructs the correctly graded localization total complex.

## Verification

- Degree check against `CH^2(P2,1)=H_M^3(P2,Z(2))`
- The prior synthesis checker is superseded and must not be used as verification.
