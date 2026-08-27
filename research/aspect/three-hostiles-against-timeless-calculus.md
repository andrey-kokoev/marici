# Three hostile packets against the timeless calculus

## Question

Does the marked-carrier/kernel-descent calculus reproduce known obstructions
outside the mixed-Green example, or was it fitted to that one packet?

## Hostile one: determinant-frame Schur jet

Source packet:
`research/nima/theta-determinant-frame-increment-is-the-schur-complement-first-jet.md`.

The marked carrier contains the retained block `A`, new block `E`, incidences
`B,C`, and all four first jets. The local completion that keeps only the new
diagonal block forgets incidence and retained-state directions. The outer mate
is the logarithmic first jet of the Schur complement.

For the exact scalar fixture

```text
A=2, A'=1, B=3, B'=2, C=5, C'=3, E=11, E'=7,
```

the Schur data are

\[
S=\frac72,
\qquad
S'=\frac54,
\qquad
\frac{S'}S=\frac5{14}.
\]

The diagonal-only jet is `7/11`; deleting the mixed carrier directions leaves
the nonzero residual `43/154`. The calculus therefore chooses relational-first
block sewing and reproduces Nima's complete first-jet law.

## Hostile two: Green--Schwarz product fiber

Source packet:
`research/flavor/flavor-green-schwarz-product-stueckelberg-fiber.md`.

The carrier coordinates are `(k,c)`. Local anomaly completion retains only
their product `A=kc`. The two carrier points

\[
(k,c)=(2,3),
\qquad
(4,3/2)
\]

both complete to `A=6`, but their squared mass factors are `4` and `16`, and
their low-energy exchange factors are `1/4` and `1/16`.

Infinitesimally, `(k,-c)` lies in the kernel of the product differential:

\[
d(kc)(k,-c)=0,
\]

while

\[
d(k^2)(k,-c)=2k^2\ne0.
\]

The calculus therefore refuses to promote anomaly completion into scale,
threshold, or oriented-flux selection. A separate carrier-to-realization
constructor is required.

## Hostile three: Clark tail-lift torsor

Source packet:
`research/kitaev/clark-endpoint-incidence-leaves-an-affine-torsor-of-tail-lifts.md`.

Let endpoint trace retain the first of two finite carrier coordinates. Two
lifts

\[
J_0=(1,0),
\qquad
J_1=(1,1)
\]

have the same endpoint incidence. Their difference `N=(0,1)` lies in the trace
kernel. Pairing against the kernel probe `(0,1)` gives zero for `J_0` and one
for `J_1`.

The endpoint completion therefore leaves an affine torsor of graph lifts, and
the Green relation is not invariant along it. The calculus selects graph-first
sewing and demands source dynamics, decay, covariance, reflection, and cutoff
naturality to choose or reduce the torsor.

## Common proof

All three packets have the same shape:

```text
carrier direction lies in kernel of proposed completion
target relation contracts nontrivially with that direction
therefore target does not descend
therefore relational mate must precede completion
```

No event or temporal order occurs in any proof.

## Result

The calculus survives three hostile packets from determinant geometry, flavor
selection, and graph-valued theta lifting. It predicts each packet's known
failure and its required architectural repair from the same kernel test.

## Claim boundary

The finite fixtures prove the shared obstruction pattern. They do not replace
the source-authority work still open in the full theta matrix, compactification
geometry, or alternating physical polarization.

## Verification

Run:

```text
python research/aspect/checkers/check_three_hostiles_against_timeless_calculus.py
```
