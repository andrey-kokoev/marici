# The fourth theta quarter-turn separates cross-zero from exterior rank loss

## Status

Exact determinant-line theorem and finite divisor-separation hostile. With the
history Dirac core and two-port Weyl matrix fixed, the fourth rotation passes
from port coordinates to the top exterior power. This yields a real-spectral
invariant for a selfadjoint feedback extension, but it does not preserve the
zero set of the current cross-port scalar readout.

## Fixed three-layer object

Retain:

\[
D_H
=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix},
\]

the two typed ports

\[
B=
\begin{pmatrix}
b_f&b_0
\end{pmatrix},
\]

and the matrix Weyl function

\[
W(\lambda)
=
A-\lambda I
-
B^*(D_H-\lambda)^{-1}B.
\]

No fourth-round operation may redefine \(D_H\), identify the two ports, or fit
the direct term \(A\) from scalar zeros.

## Exterior rotation

For a two-dimensional port space, the top exterior action is one-dimensional:

\[
\Lambda^2W(\lambda)
=
\det W(\lambda).
\]

Under a unitary port rotation

\[
W\longmapsto U^*WU,
\]

the determinant is invariant:

\[
\det(U^*WU)=\det W.
\]

A zero of \(\det W\) means that the full port relation loses rank:

\[
\det W(\lambda)=0
\quad\Longleftrightarrow\quad
\ker W(\lambda)\ne\{0\}.
\]

This is a coordinate-independent relationship defect, unlike the zero of one
chosen matrix entry.

## Selfadjoint feedback confinement

Assume

\[
D_H=D_H^*,
\qquad
A=A^*.
\]

For \(\lambda=x+iy\) with \(y>0\), the resolvent identity gives

\[
\operatorname{Im}(D_H-\lambda)^{-1}
=
y(D_H-\lambda)^{-*}(D_H-\lambda)^{-1}.
\]

Hence

\[
\operatorname{Im}W(\lambda)
=
-y
\left[
I
+
B^*(D_H-\lambda)^{-*}(D_H-\lambda)^{-1}B
\right].
\]

This form is strictly negative definite. Therefore

\[
W(\lambda)v=0
\]

with \(v\ne0\) is impossible when \(y>0\). The lower half-plane follows by
adjoint symmetry.

Consequently every zero of the feedback determinant lies on the real
\(\lambda\)-axis, apart from separately typed pole cancellations and
essential-spectrum boundary phenomena.

## Block determinant identity

For the selfadjoint extension

\[
\mathbb A
=
\begin{pmatrix}
D_H&B\\
B^*&A
\end{pmatrix},
\]

the finite-dimensional Schur identity is

\[
\det(\mathbb A-\lambda)
=
\det(D_H-\lambda)
\det W(\lambda).
\]

Thus determinant zeros of \(W\) are characteristic values of the fixed
selfadjoint feedback system, with multiplicities controlled by the complete
block pencil rather than by one transfer entry.

## Exact divisor-separation hostile

Reuse the selfadjoint internal matrix

\[
D=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

and ports

\[
b_f=\binom{1}{1},
\qquad
b_0=\binom{1}{-i}.
\]

Let

\[
B=
\begin{pmatrix}
1&1\\
1&-i
\end{pmatrix}
\]

and take the resolvent port matrix

\[
Q(z)=B^*(D-z)^{-1}B.
\]

Its endpoint-to-source cross entry is

\[
Q_{0f}(z)
=
\frac1{-1-z}
+
\frac{i}{1-z},
\]

which vanishes at

\[
z=-i.
\]

But

\[
\det Q(z)
=
\frac{|\det B|^2}{(-1-z)(1-z)}.
\]

Since

\[
\det B=-1-i\ne0,
\]

the determinant is nonzero at \(z=-i\). Therefore

\[
Q_{0f}(-i)=0,
\qquad
\det Q(-i)\ne0.
\]

The scalar cross zero is destructive port interference while the full
relationship volume remains nonzero.

## Exterior geometry

Let \(w_f(\lambda)\) and \(w_0(\lambda)\) be the two columns of \(W(\lambda)\).
Then

\[
\det W(\lambda)
\]

is the coefficient of

\[
w_f(\lambda)\wedge w_0(\lambda)
\]

in the oriented port-area line. A determinant zero means the two complete port
responses become dependent.

A cross-entry zero means only that one selected component of one response
vanishes. These are different geometric events.

## Relation to the theta scalar

The current source-tail construction realizes the completed scalar through a
source-to-endpoint pairing. That places it naturally in a cross-transfer
coordinate. The fourth rotation cannot simply declare this scalar to be
\(\det W\), because the hostile above proves that cross and exterior divisors
are generally different.

A legitimate determinant promotion needs a source theorem of the form

\[
\Xi\!\left(\frac12+i\lambda\right)
=
u(\lambda)\det W(\lambda),
\qquad
u(\lambda)\ne0.
\]

The construction of \(W\), its direct term, and its determinant line must
precede this comparison.

## Lower-minor data remain necessary

Even equality of characteristic determinants does not identify the complete
pencil. Buzzard's exact polynomial-pencil hostile shows that equal
characteristic polynomials can hide different first determinantal ideals and
unipotent structure.

The determinant bridge must therefore preserve:

- port rank;
- first and higher determinantal ideals;
- Smith profile where the coefficient ring permits it;
- kernel and adjoint-kernel variance;
- factorization residue flags;
- spectral type under completion.

## Fourth-round alternatives

The rotation leaves three sharply typed possibilities.

### Cross-entry verdict

If \(\Xi\) remains only a cross-entry, the selfadjoint/exterior route supplies
provenance but no zero confinement.

### Exterior-section theorem

If the source constructs \(\Xi\) as the top exterior section of the complete
port relation, selfadjoint feedback confines its characteristic zeros.

### Higher port rank

If endpoint, primitive, square, seam, and archimedean channels require a port
space of rank greater than two, use the top nonzero exterior power and retain
the whole determinantal-ideal filtration. A fitted two-port compression is not
admissible.

## Finite falsifiers

The exterior route fails if:

1. the scalar and determinant divisors differ at one cutoff;
2. a zero-free comparison factor develops a zero or pole in completion;
3. equal determinants hide different lower-minor profiles;
4. port dimension grows beyond the declared exterior degree;
5. the direct term is chosen after scalar inspection;
6. hostile prime perturbations preserve the proposed exterior identity;
7. a completed determinant zero belongs only to essential spectrum without an
   authorized characteristic state.

## Verdict

The fourth quarter-turn produces the first invariant whose zeros are genuinely
confined by selfadjointness: the top exterior determinant of the complete port
Weyl relation. It simultaneously proves that the current cross-port theta zero
cannot be promoted to that invariant for free. The next decisive calculation
is a source-level divisor comparison between the completed scalar section and
the exterior determinant, with every lower-minor and spectral-type field
retained.
