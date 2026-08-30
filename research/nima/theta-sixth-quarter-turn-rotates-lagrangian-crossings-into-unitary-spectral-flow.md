# The sixth theta quarter-turn rotates Lagrangian crossings into unitary spectral flow

## Ordered-port correction

The Cayley and spectral-flow construction in this packet acts on the unframed
full Weyl rank divisor. The current theta scalar is a flagged cross-transfer
entry and can vanish while the full Weyl matrix remains invertible. Retain this
packet as a full-port theorem only. Applying it to RH requires a prior
source-derived relation between the bordered transmission pencil and the full
Weyl determinant.

Exact Cayley and Maslov-path theorem. The Lagrangian graph, reference plane,
symplectic form, Plücker data, and crossing form remain fixed. The sixth
rotation sends the Hermitian Weyl path to a unitary scattering path whose
eigenphase flow records the oriented characteristic crossings. This supplies
global counting and coherence, not the missing scalar-to-determinant bridge.

## Fixed crossing package

Retain

\[
\left(
\Gamma(W(\lambda)),
\mathcal L_0,
\Omega,
Q_\lambda,
\operatorname{Pl}(\Gamma(W(\lambda)))
\right).
\]

For the selfadjoint feedback Weyl family,

\[
W(\lambda)
=
A-\lambda I
-
B^*(D_H-\lambda)^{-1}B,
\]

the real path is Hermitian between poles and its crossing form is strictly
negative.

## Cayley quarter-turn

Define

\[
U_W(\lambda)
=
\bigl(W(\lambda)-iI\bigr)
\bigl(W(\lambda)+iI\bigr)^{-1}.
\]

For real \(\lambda\) away from poles, \(W(\lambda)=W(\lambda)^*\), so

\[
U_W(\lambda)^*U_W(\lambda)=I.
\]

The Cayley transform rotates the Hermitian port relation into a unitary
scattering relation without changing the fixed internal Dirac system.

## Characteristic crossing becomes a phase crossing

If

\[
W(\lambda_0)v=0,
\]

then

\[
U_W(\lambda_0)v=-v.
\]

Thus a Lagrangian intersection with \(\mathcal L_0\) becomes an eigenphase
crossing through \(-1\) on the unit circle.

The identity

\[
I+U_W
=
2W(W+iI)^{-1}
\]

gives

\[
\det(I+U_W)
=
2^r
\frac{\det W}{\det(W+iI)},
\]

where \(r=\dim\mathcal U\). On the real axis, the denominator is nonzero.
Therefore the Cayley phase crossing and exterior determinant crossing have the
same real divisor and geometric multiplicity.

## Direction of phase travel

Let \(\mu_j(\lambda)\) be an eigenvalue branch of \(W(\lambda)\). The fixed
crossing theorem gives

\[
\mu_j'(\lambda_0)<0
\]

at every characteristic crossing. Its Cayley phase

\[
u_j(\lambda)
=
\frac{\mu_j(\lambda)-i}{\mu_j(\lambda)+i}
\]

therefore crosses \(-1\) in one fixed orientation.

Each local Maslov contribution has the same sign, weighted by the crossing
corank.

## Spectral flow and Maslov index

On a real interval containing no poles at its endpoints, the signed count of
\(-1\) phase crossings of \(U_W\) equals the Maslov index of

\[
\Gamma(W(\lambda))
\]

relative to \(\mathcal L_0\). It also equals the spectral flow of the
selfadjoint feedback pencil through zero.

Because all crossing forms are negative, the signed count reduces to the
negative of the total geometric multiplicity:

\[
\operatorname{Mas}
=
-\sum_{\lambda_0}
\dim\ker W(\lambda_0)
\]

with the chosen orientation convention.

This is a global coherence invariant assembled from the local crossing forms.

## Pole crossings and interlacing

At poles of \((D_H-\lambda)^{-1}\), the Weyl path leaves a finite chart. The
Cayley path may nevertheless have a controlled unitary continuation when the
source residue packet is retained.

The global spectral-flow theorem must distinguish:

- zero crossings of \(W\);
- poles inherited from \(D_H\);
- pole-zero cancellations;
- embedded spectral points;
- essential-spectrum thresholds.

Dropping the primitive or prime-square residue layers can change this count.

## Relation to local Tate phases

The local Tate sewing factors are unitary on the critical seam. The Cayley
transform shows the operator type required for a global interpretation: local
phases should be components or relative determinants of the completed unitary
path \(U_W\).

The first two non-trace-class currents then belong to phase renormalization and
boundary spectral flow, while the trace-class tail can contribute an ordinary
determinant. This matches the previously derived three-level filtration.

The equality remains a construction target. Local phase multiplication alone
does not produce the global Weyl path or its reference plane.

## Real-axis counting is not complex zero confinement

The Maslov index counts crossings of an already constructed real Hermitian
path. It does not prove that the original scalar theta section equals the
exterior determinant of that path.

Nor does coarse spectral-flow data determine the full complex divisor. Two
analytic scalar sections may have the same real crossing count and orientation
while differing by off-axis divisor packets if only their Maslov data, rather
than their complete analytic values, are retained.

Therefore spectral flow cannot replace the source-level determinant bridge.

## Source-normalized phase

The determinant

\[
\det U_W(\lambda)
\]

is a unit-modulus phase on the real axis. Its winding records the total
spectral flow, but only after a source-fixed determinant-line trivialization is
chosen. A fitted phase origin can shift winding assignments across poles and
cutoffs.

The tensor unit, vacuum line, endpoint orientation, and primitive-current
normalization are candidate sources of that trivialization. None may be
selected from the desired zero count.

## Finite compiler

At cutoff \(X\), form

\[
U_{W,X}(\lambda)
=
\bigl(W_X(\lambda)-iI\bigr)
\bigl(W_X(\lambda)+iI\bigr)^{-1}.
\]

Verify:

1. exact unitarity for real nonsingular \(\lambda\);
2. equivalence of \(-1\) eigenspace and \(\ker W_X(\lambda)\);
3. crossing-form sign;
4. determinant identity for \(I+U_{W,X}\);
5. pole and residue typing;
6. equality of Maslov, spectral-flow, and determinant counts;
7. cutoff transition coherence;
8. preservation of lower Plücker and Smith data.

## Falsifiers

The unitary-path route fails if:

1. a real Cayley matrix is not unitary;
2. a \(-1\) phase crossing has no Weyl-kernel state;
3. a crossing travels in the wrong direction;
4. a pole is silently counted as a zero;
5. phase trivializations differ between cutoffs without a comparison cell;
6. the local Tate product has a residual phase not represented by \(U_W\);
7. essential-spectrum winding is assigned a discrete multiplicity;
8. theta scalar zeros disagree with the exterior/Cayley divisor.

## Sixth fixed object

The next invariant layer is

\[
\left(
U_W(\lambda),
\det U_W(\lambda),
\operatorname{Mas},
\operatorname{Sf},
\mathcal R
\right).
\]

Here \(\mathcal R\) denotes the residue filtration as separately typed mathematical state
data; it must remain separately typed rather than compressed into the phase.

## Verdict

The sixth quarter-turn converts the oriented Lagrangian crossings into unitary
spectral flow. It supplies a coherent global counting mechanism and a natural
home for local Tate phases. But it remains downstream of the decisive source
question: whether the completed theta scalar is the determinant-line section
of the fixed Weyl relation. Without that bridge, the Maslov index counts the
spectrum of a beautiful constructed system rather than the zeros of \(\Xi\).
