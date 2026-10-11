# Iteration 1: common-frame naturality selects the current one-factor mixer

## Fresh starting state and objective

The current retained-memory model supplies an exchange and record lineage, but leaves mixer, physical frame and gravitational normalization unresolved. This iteration freshly inspected `retained-memory-reference.md`, the current Clifford implementation, and the local-frame audit before attempting selection.

The result below is a conditional mathematical selection theorem, not a claim that the actual Boolean seed has already admitted every orthogonal frame transformation.

## Selection policy tested

Keep the existing algebra M2(R), its positive counting/Frobenius metric, normalized multiplication port C and one-factor lift L=T tensor I. Require T to be:

1. real-linear and unit preserving;
2. an algebra automorphism;
3. natural under simultaneous orthogonal change of the COMMON two-dimensional frame;
4. capable of exposing an orthogonal hidden port: C L C^T=0.

The frame condition means T(QXQ^T)=Q T(X) Q^T for every Q in O(2). This is a precise candidate admission policy, not a consequence of free directed-path incidence. In particular, it is stronger than invariance under the two Boolean permutations alone.

## Exhaustive reduction, not a sampled search for mixers

Under conjugation by O(2), M2(R) splits into scalar, skew and symmetric-traceless sectors. The exact checker computes commutation constraints for one rational rotation and one reflection. Their coefficient matrix has rank thirteen on the sixteen-dimensional space of linear operators; its kernel is exactly the three-dimensional family

    T(s,q,p,z)=(a*s,c*q,c*p,b*z).

The three displayed sector projectors form an independent kernel basis, so this is a complete necessary classification over R as well as Q. Full O(2) naturality implies these two particular commutation constraints.

Unit preservation forces a=1. Applying multiplicativity to e1 squared equals 1 gives c squared equals 1. Applying it to e1*e2=J gives b=c squared=1. Therefore the only possible real operators are identity and

    R(s,q,p,z)=(s,-q,-p,z).

Both really are natural for all O(2), not just the two matrices used in the rank certificate. The nonidentity candidate has the coordinate-free formula

    R(X)=tr(X) I-X^T=J X J^-1.

Trace and metric adjoint commute with orthogonal conjugation, proving its full covariance. No choice between J and -J is needed: both induce the same R.

## Hidden-port gate selects the nonidentity candidate

For identity, C L C^T=I, so it does not supply an orthogonal hidden readout. For R tensor I the compression is zero. Thus the policy uniquely selects the existing one-factor mixer.

The earlier Ad_e1 alternative fails this stronger common-frame naturality condition. Although it was observationally conjugate after an appropriate bank-adapter transport, it singles out an axis if the common algebra/frame interpretation is held fixed.

## What has and has not been selected

Within the stated class, the current mixer is selected, and its orientation sign is unnecessary. This is stronger than conservation-only selection, but does NOT classify arbitrary sixteen-dimensional mixers, derive the metric or one-factor architecture, select an external physical frame, or determine a gravitational coupling.

Most importantly, common-frame conjugation differs from independent changes at source and target ports. The original tetrahedral adapter uses maps between different marked vertices. It cannot automatically treat those maps as endomorphisms of one canonically identified physical space. The previous local-frame obstruction remains relevant.

Gravitational normalization has not been addressed by this selector. No amplitude scale, clock, matter coupling or dimensionless mass ratio is produced by the rank calculation.

## Next executable continuation

Test the selected mixer on genuinely separate endpoint fibers: determine whether its hidden readout can be natural under independent endpoint-frame changes, or exactly what source-retained identification/reference it requires. This is nonredundant with the common-frame theorem and precedes any physical normalization claim.

## Verification

`python research/nima/checkers/check_natural_mixer_selection.py` passed with exact rational commutant rank, sector-basis, multiplication, covariance and hidden-port checks. Results: `results/natural-mixer-selection.json`, with source digests.

The reduction of c squared equals 1 to c=+/-1 and the all-O(2) covariance argument are written real-algebra proofs above. No claim of a new Agda theorem, fitted gravitational value, ledger entry, commit or publication is made.
