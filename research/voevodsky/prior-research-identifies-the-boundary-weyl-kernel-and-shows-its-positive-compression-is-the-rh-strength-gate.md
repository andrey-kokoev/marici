# Prior research identifies the boundary Weyl kernel and shows its positive compression is the RH-strength gate

## Search result

The prior research does not contain a completed boundary-triple construction with a proved positive Weyl function. It contains the canonical candidate kernel and an exact classification of its negative defect.

This is enough to identify the logical strength of the remaining theorem.

## Canonical strip kernel

Let

\[
\Theta_S(z)
=
\frac{E_S^\#(z)}{E_S(z)}
\]

be the completed reflected multiplier in the selected strip or conformally equivalent half-plane.

The canonical two-variable boundary kernel is

\[
K_S(z,w)
=
\frac{
1-
\Theta_S(z)
\overline{\Theta_S(w)}
}{
2\pi i(\bar w-z)
}.
\]

Before division by the outer factors, this is the de Branges kernel

\[
K_{E_S}(z,w)
=
\frac{
E_S(z)\overline{E_S(w)}
-
E_S^\#(z)
\overline{E_S^\#(w)}
}{
2\pi i(\bar w-z)
}.
\]

This is the natural Weyl-kernel candidate for any boundary-triple realization of the reflected contour differential.

## Boundary data

The real-boundary diagonal gives the logarithmic phase current, up to orientation and normalization.

The endpoint lines carry the poles and residues responsible for the completed swap-polarized endpoint block.

Thus the kernel already has the correct continuous and endpoint boundary data.

The missing issue is positivity, not identification of the candidate.

## Exact positivity criterion

The kernel is positive exactly when \(\Theta_S\) is Schur in the chosen domain.

Equivalently, one needs the Hermite--Biehler inequality

\[
|E_S^\#(z)|
\le
|E_S(z)|.
\]

For the globally completed multiplier, this condition is equivalent in strength to the required zero-location theorem. It cannot be obtained from a local factorwise estimate because individual prime ratios change orientation across the strip.

Therefore a positive boundary-triple realization on the unrestricted completed carrier would already contain the main arithmetic theorem.

## Krein--Langer classification

If the meromorphic reflected ratio has finite negative index, write its Krein--Langer factorization as

\[
\Theta=B^{-1}S,
\]

where \(S\) is Schur and \(B\) is the Blaschke product of the forbidden pole divisor.

Then the kernel has the exact decomposition

\[
K_\Theta(z,w)
=
\frac{
K_S(z,w)-K_B(z,w)
}{
B(z)\overline{B(w)}
}.
\]

Thus every negative square lies in the model space

\[
K_B=H^2\ominus BH^2.
\]

There is no unidentified analytic remainder.

## Physical compression

Let \(M\) be the source-derived observation subspace. Positivity after physical compression is equivalent to contractive absorption of the divisor feature:

\[
\|A_Bf\|
\le
\|A_Sf\|
\qquad
(f\in M).
\]

Douglas factorization rewrites this as

\[
A_B|_M
=C A_S|_M
\]

for a contraction \(C\).

This is the nonlocal version of the rank-one endpoint leverage inequality.

## Endpoint index one

The bare endpoint swap block contributes one negative parity line. Hence the minimally faithful local boundary kernel starts in generalized Nevanlinna class \(N_1\).

If the only forbidden divisor direction is the endpoint line, the desired physical compression is the cancellation

\[
N_1
\longrightarrow
N_0.
\]

If additional Blaschke directions occur, their model-space dimension records additional negative squares. A finite-rank endpoint feature cannot absorb them unless the source observation annihilates or contractively absorbs those directions.

## Why higher coherence cannot help

A centered negative square persists under source-preserving successor maps. Higher lattice coherence can transport a positive or negative observation, but cannot change its sign without changing the source reading or quotienting out the witness.

Therefore the boundary-kernel contraction is the terminal substantive positivity gate.

## What the Clifford bicomplex contributes

The four-component Clifford operator provides:

1. a common closed carrier;
2. compact-resolvent oscillator bulk;
3. separate current and endpoint-orientation channels;
4. the correct resolvent denominator for endpoint residues.

It does not provide positivity of the extracted kernel. Its extraction matrices are indefinite, and endpoint evaluation remains a nonlocal resolvent residue.

Thus the bicomplex types the boundary triple but does not solve its Schur problem.

## Most precise remaining theorem

Construct the source observation map into the de Branges/Krein--Langer feature space without using the unknown divisor, and prove that its image satisfies

\[
K_S|_M\succeq0.
\]

Equivalently, construct the source-derived Douglas contraction absorbing the Blaschke defect on \(M\).

For the parity-reduced endpoint model, this specializes to the leverage inequality

\[
c_k
\|C_k^{\dagger/2}v_k\|^2
\le1.
\]

## Circularity warning

Constructing the contraction from the Blaschke product \(B\) is classification, not proof. The factor \(B\) encodes the forbidden divisor whose absence or absorption is being tested.

A valid proof must obtain the same contraction from source operations such as convolution squares, the canonical/dual pairing, the Green trace, or another independently positive carrier.

## Disposition

Prior research already identifies the prospective boundary Weyl kernel and its exact negative model space. The unresolved theorem is not construction of a candidate boundary kernel. It is source-derived contractive absorption of its Krein--Langer defect.

This is the RH-strength rung-four positivity gate. No further categorical filling can replace it.
