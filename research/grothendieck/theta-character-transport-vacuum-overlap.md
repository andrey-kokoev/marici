# Mellin character transport derives the completed theta readout

Author: `marici.Grothendieck`

## 1. Source-local spectral deformation

On the completed source space

\[
 \mathcal H_\Phi=L^2(\mathbb R,Z^{-1}\Phi(u)\,du),
\]

define the character transport

\[
 (U_zf)(u)=e^{izu}f(u).
\]

For real (z), (U_z) is a unitary one-parameter group.  The doubly
exponential theta tails make all matrix coefficients between the analytic
vectors used below entire in (z).  The group law

\[
 U_zU_w=U_{z+w}
\]

is fixed before inspecting the scalar readout.

Let

\[
 A_\Phi=-\partial_u^2-(\log\Phi)'\partial_u.
\]

Transporting the completed diffusion gives

\[
 A_{\Phi,z}=U_zA_\Phi U_z^{-1}
 =A_\Phi+2iz\partial_u+z^2+iz(\log\Phi)'.
\]

This is the canonical source-local (z)-deformation requested by the
completion-first programme.  It is a flat gauge transport, not a fitted
potential.

## 2. The readout follows as a vacuum overlap

The normalized constant ground state is

\[
 \Omega(u)=1,
 \qquad A_\Phi\Omega=0.
\]

Its transported ground state is

\[
 \Omega_z=U_z\Omega=e^{izu},
 \qquad A_{\Phi,z}\Omega_z=0.
\]

Their overlap is

\[
 \langle\Omega,\Omega_z\rangle
 =Z^{-1}\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

Up to the fixed normalization convention for the completed theta Fourier
kernel, this is (X(z)).  Therefore the derivational direction is correct:

\[
 \boxed{
 \Phi\longrightarrow A_\Phi
 \longrightarrow U_z,A_{\Phi,z}
 \longrightarrow\langle\Omega,U_z\Omega\rangle=X(z)/X(0).}
\]

No zero data and no previously supplied (X) enter the operator construction.

## 3. Determinant-line interpretation

Let (P_0=|\Omega\rangle\langle\Omega|) be the ground-line projection.  The
compressed transport

\[
 P_0U_zP_0:\operatorname{Ran}P_0\to\operatorname{Ran}P_0
\]

is multiplication by

\[
 \langle\Omega,U_z\Omega\rangle.
\]

Hence its one-dimensional determinant section is the normalized completed
readout.  A zero is precisely failure of the transported vacuum to have a
nonzero component in the original vacuum channel.

This is more structured than the universal rank-one encoding: (U_z) obeys
an independently forced character group law and (A_{\Phi,z}) is its
covariant source dynamics.

## 4. Hostile multiplier exclusion

An artificial replacement

\[
 X(z)\mapsto P_a(z)X(z)
\]

cannot be produced by multiplying the same character transport by (P_a),
because

\[
 \widetilde U_z=P_a(z)U_z
\]

fails the transport law unless

\[
 P_a(z+w)=P_a(z)P_a(w).
\]

Holomorphic scalar solutions of this multiplicative Cauchy equation are
exponentials (e^{cz}), hence nowhere zero.  A quartet polynomial is not a
transport gauge.  Thus source transport provenance excludes (P_a) without
examining its zeros.

This proves only a **scalar-gauge rigidity** theorem for the fixed character
transport.  It does not exclude a more elaborate change of source object whose
induced readout happens to contain (P_a).  Full provenance rigidity still
requires classifying the morphisms of the labelled theta-source groupoid.

## 5. What remains exactly RH-strength

The group law does not imply

\[
 \langle\Omega,U_z\Omega\rangle\ne0
 \qquad(\operatorname{Im}z\ne0).
\]

Characteristic functions of positive even measures can have complex zeros.
The diffusion, ground line, and flat character transport therefore explain
the construction and protect its provenance, but do not supply off-seam
coercivity.

The remaining theorem is now the source-specific statement

\[
\boxed{
 P_0U_zP_0\ \text{is invertible whenever }\operatorname{Im}z\ne0.}
\]

For the theta ground-state measure this is RH in the centered coordinate.  It
must follow from additional structure of (Phi), most plausibly the labelled
Poisson/modular coherence that was forgotten when the source was reduced to
the scalar density.

## 6. Interaction with canonical compression

The source-diffusion projections give finite transport matrices

\[
 U_z^{(N)}=E_NU_zE_N.
\]

They preserve reflection typing and the vacuum channel.  However, the
relevant scalar is the distinguished matrix coefficient

\[
 \langle\Omega,U_z^{(N)}\Omega\rangle,
\]

not the full determinant of (U_z^{(N)}).  Since (E_N\Omega=\Omega), this
matrix coefficient already equals the exact overlap whenever the compression
is applied only to the output vacuum channel.  Consequently finite matrices
do not approximate away the hard scalar question.

Their proper use is to test a future source-derived energy identity, not to
recompute (X).

## 7. Explanation gained

The completed theta readout is a survival amplitude:

\[
 X(z)/X(0)
 =\text{amplitude for the theta vacuum to survive Mellin-character transport}.
\]

Zeros mean complete destructive interference in that distinguished channel.
The critical-line conjecture says such complete cancellation can occur only
for unitary transport (z\in\mathbb R), never for its nonunitary complex
continuation.

This gives precise content to the operator's two-plane interference intuition:
the two descriptions are the original and character-transported vacuum
lines, and the observed zero is loss of their overlap.  What remains
unexplained is why theta modular coherence confines orthogonality to the
unitary axis.

## 8. Scope

The character transport, conjugated diffusion on its natural analytic
domains, vacuum-overlap formula, ground-line determinant, and exclusion of
polynomial *scalar* transport gauges are exact.  For nonreal (z), (U_z) is
not a bounded operator on all of (mathcal H_\Phi); the entire matrix
coefficient and conjugated differential expression are the presently typed
objects.  Off-axis nonvanishing and full source-groupoid provenance rigidity
are not proved.  The construction supplies the missing source-derived
transport operator but not the load-bearing coercivity law, and therefore
does not prove RH.
