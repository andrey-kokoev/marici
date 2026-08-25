# The theta matrix coefficient lives on a metaplectic geodesic, not a fixed Zak torus

Author: `marici.Grothendieck`

## 1. Question

The Fourier transform is a quarter-turn of phase space, and the integer comb
is self-dual. Does the Zak transform on one fixed lattice torus provide the
natural geometry for the dilation matrix coefficient

\[
 \mathcal A(u)
 =\langle\Delta_{\mathbb Z},R_uf\rangle?
\]

Not by itself. Continuous dilation changes the underlying phase-space lattice.
The closed object is the metaplectic orbit of the lattice, equivalently a
geodesic in an arithmetic homogeneous space.

## 2. Metaplectic generators

Let

\[
 (R_uf)(x)=e^{u/2}f(e^ux)
\]

be unitary dilation. It represents the diagonal symplectic element

\[
 a_u=
 \begin{pmatrix}
 e^u&0\\
 0&e^{-u}
 \end{pmatrix}.
\]

Let

\[
 w=
 \begin{pmatrix}
 0&1\\
 -1&0
 \end{pmatrix}
\]

be the symplectic quarter-turn, represented metaplectically by Fourier
transformation. Then

\[
\boxed{
 wa_uw^{-1}=a_{-u}}
\]

and therefore

\[
 \mathcal FR_u\mathcal F^{-1}=R_{-u}.
\]

This is the geometric origin of reciprocal scale reflection.

## 3. The fixed Zak torus does not close

The Zak transform resolves a function relative to the fixed lattice
\(\mathbb Z^2\) in phase space. Under \(a_u\), that lattice becomes

\[
 \Lambda_u
 =
 a_u\mathbb Z^2
 =
 e^u\mathbb Z\oplus e^{-u}\mathbb Z.
\]

For generic real \(u\),

\[
 \Lambda_u\ne\mathbb Z^2.
\]

Thus continuous dilation is not an internal motion of a single Zak torus. It
moves through the moduli of covolume-one lattices. A fixed Zak chart can
describe a local presentation, but the faithful carrier is the family
\(\{\Lambda_u\}\).

The operator's sensed rotation therefore points beyond one torus to the
metaplectic homogeneous space.

## 4. The comb is an automorphic distribution

Let

\[
 \Delta_{\mathbb Z}
 =\sum_{n\in\mathbb Z}\delta_n.
\]

Poisson summation gives

\[
 \mathcal F\Delta_{\mathbb Z}
 =\Delta_{\mathbb Z}.
\]

There is a second exact coherence. Let the even shear act by the quadratic
phase

\[
 (T_2h)(x)=e^{2\pi ix^2}h(x).
\]

Then

\[
\boxed{
 T_2\Delta_{\mathbb Z}
 =
 \sum_ne^{2\pi in^2}\delta_n
 =
 \Delta_{\mathbb Z}.}
\]

Hence the comb is fixed not only by the Fourier generator \(w\), but also by
the integral even shear. Up to the standard metaplectic phase convention,
these generate the theta modular subgroup.

A generic Fourier-fixed distribution need not satisfy this second coherence.
This is the first additional source law exposed by the rotated picture.

## 5. Theta as an automorphic matrix coefficient

For any Schwartz state \(h\), define

\[
 \Theta_h(g)
 =
 \langle\Delta_{\mathbb Z},\omega(g)h\rangle,
\]

where \(\omega\) is the metaplectic representation. Invariance of the comb
under the theta subgroup makes \(\Theta_h\) an automorphic distributional
matrix coefficient.

For the minimally derived state

\[
 f=D(D+1)e^{-\pi x^2},
\]

restriction to the diagonal geodesic gives

\[
\boxed{
 \Theta_f(a_u)
 =
 \langle\Delta_{\mathbb Z},R_uf\rangle
 =
 \mathcal A(u).}
\]

Fourier fixation of both endpoints and
\(wa_uw^{-1}=a_{-u}\) imply

\[
 \Theta_f(a_u)=\Theta_f(a_{-u}).
\]

The completed theta source is therefore the restriction of an automorphic
metaplectic matrix coefficient to a Weyl-reflected geodesic.

## 6. The 90-degree conceptual rotation

The old coordinates were

\[
 \text{labels}\longrightarrow\text{sum}\longrightarrow\mathcal A(u).
\]

The rotated coordinates are

\[
\boxed{
\begin{array}{c}
\text{automorphic boundary distribution }\Delta_{\mathbb Z}\\
+\text{minimal metaplectic state }f\\
+\text{diagonal transport }a_u\\
\downarrow\\
\text{relational matrix coefficient }\Theta_f(a_u).
\end{array}}
\]

Poisson summation, reciprocal reflection, and integral sampling are different
shadows of this single representation-theoretic object.

## 7. Why this may replace the invented arithmetic boundary operator

The earlier block-operator programme sought an infinite arithmetic boundary
space by assembling all label and prime seam blocks. The metaplectic picture
suggests that this infinity is already organized as the orbit of one
automorphic distribution:

\[
 \Delta_{\mathbb Z}
 \quad\text{inside}\quad
 \mathcal S(\mathbb R)\subset L^2(\mathbb R)\subset\mathcal S'(\mathbb R).
\]

The arithmetic dynamics need not be separately fitted as
\(A_{\mathrm{arith}}\). It may be the restriction of the oscillator
representation to the theta modular subgroup, while the free quarter operator
is the Casimir/diagonal generator seen in logarithmic coordinates.

This is a proposed retyping, not yet an operator equivalence theorem.

## 8. Hostile discrimination

The earlier higher-Hermite perturbations remain Fourier-fixed, but they fail
the minimal-Casimir condition on the state. Shifted or twisted combs may remain
valid distributions, but they fail invariance under the even shear or acquire
a nontrivial character.

Thus the source pair is constrained on both sides:

\[
\begin{array}{c|c}
\text{state }f&
\text{minimal }D(D+1)\text{ descendant of the Gaussian}\\
\text{boundary }\Delta_{\mathbb Z}&
\text{fixed by Fourier and the integral even shear}.
\end{array}
\]

The next hostile census should vary pairs while retaining both conditions.
If a large family survives, metaplectic automorphy still explains only the
functional equation. If the pair is rigid up to scale and phase, the remaining
zero-orientation problem has been sharply localized to one automorphic matrix
coefficient.

## 9. New proof target

Mellin transformation along the diagonal geodesic is spectral decomposition
for the self-adjoint dilation generator. The exact identity is

\[
 2\xi\!\left(\frac12+iz\right)
 =
 \int_{\mathbb R}\Theta_f(a_u)e^{izu}\,du.
\]

The RH-strength question becomes:

\[
\boxed{
\text{Which positivity or orientation theorem for this automorphic
metaplectic matrix coefficient forbids complex spectral nulls?}}
\]

The theorem must use both the minimal state condition and the automorphic comb
condition. Weyl symmetry alone gives only evenness.

## 10. Scope

The metaplectic conjugation of dilation, moving lattice family, Fourier and
even-shear invariance of the comb, and restriction formula for the theta
source are exact, modulo the conventional harmless metaplectic phase choice.
The replacement of the arithmetic boundary block by an automorphic
representation, and any positivity theorem for its cross-spectrum, remain
conjectural. RH is not proved.
