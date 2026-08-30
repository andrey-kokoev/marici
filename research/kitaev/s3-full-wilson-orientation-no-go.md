# No subset of the full Wilson eigenvalue packet fixes absolute orientation

Owner: `marici.Kitaev`

Terminology note: “absolute orientation” below means selection of the
(B)-simple-current/sign-frame sheet. Geometric ribbon orientation is a
different, already frozen involution.

## Full-packet automorphism

From the modular (S)-matrix, the Wilson eigenvalue matrix is

\[
W_{xa}=\frac{S_{xa}}{S_{0a}}.
\]

The sector permutation

\[
\sigma=(A\ B)(D\ E)
\]

intertwines the full eight-coordinate packet with the coordinate action that
negates (D,E) and fixes (A,B,C,F,G,H):

\[
W_{x,\sigma(a)}=\varepsilon_xW_{x,a},
\qquad
\varepsilon_D=\varepsilon_E=-1,
\quad \varepsilon_x=1\text{ otherwise}.
\]

The omitted (A) coordinate is constant. The (B) coordinate is invariant
under (sigma). Neither supplies orientation.

## Complete subset theorem

The checker examines all (2^8-1=255) nonempty Wilson-coordinate subsets.
Exactly sixty are faithful:

\[
8,22,21,8,1
\]

of sizes (4,5,6,7,8), respectively. Every faithful subset contains (D) or
(E), and every one inherits the nontrivial orientation automorphism by
restriction.

Therefore no readout formed solely from ordinary Wilson eigenvalue
coordinates can fix absolute orientation. Adding (A), (B), or every
available Wilson port does not help.

## Required novelty

An orientation breaker must be one of:

1. an independently rooted orientation datum;
2. a physical constructor deriving oriented (D/E) transport;
3. an observable outside the ordinary Wilson eigenvalue packet, such as a
   typed interferometric or junction-sensitive probe odd under (sigma).

## Boundary and falsifiers

- Arbitrary functions of Wilson coordinates are not separately classified;
  any equivariant function still inherits the symmetry.
- Non-spectral, interferometric, and junction observables remain open.
- Failure of the full-packet intertwining equation falsifies the no-go.
- A faithful Wilson subset not inheriting (sigma) falsifies the subset
  theorem.

## Artifacts

- Checker: `checkers/check_s3_full_wilson_orientation_no_go.py`
- Result: `results/s3-full-wilson-orientation-no-go.json`
- Result SHA256:
  `E506F18691D3E73F1733E933FC1E5F9B6D6293A3E2861097E58460AD74476656`
- Graph admission: `ev-000000003517-2edc45c0-850b-4c12-99f0-c5f29c1daf67`
- Ledger: entry 2527, `seqclaim-dd896c00cff558a906ca500d`
