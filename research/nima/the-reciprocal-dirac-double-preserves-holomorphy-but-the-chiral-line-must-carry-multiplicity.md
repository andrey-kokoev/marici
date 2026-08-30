# The reciprocal Dirac double preserves holomorphy but the chiral line must carry multiplicity

## The obstruction in the ordinary normal operator

For a holomorphic boundary pencil \(D(s)\), the ordinary positive normal
operator

\[
D(s)^*G(s)D(s)
\]

is generally not holomorphic in \(s\). It is therefore suitable for coercive
kernel exclusion but not for transporting the divisor multiplicity of
\(\xi(s)\).

The reciprocal source geometry supplies a different first-order construction.
It pairs the \(s\)-sheet with the \(1-s\)-sheet before imposing the real
structure.

## Reciprocal dual pencil

Let

\[
D_+(s):X_+\longrightarrow X_-
\]

be the ordered boundary cone, holomorphic in \(s\). Let

\[
D_-(s):X_-\longrightarrow X_+
\]

be its source-authorized reciprocal dual, also holomorphic in \(s\), with the
sewing law

\[
D_-(s)=J_-^{-1}D_+(1-s)^\vee J_+.
\]

Here \(\vee\) is the algebraic or bilinear dual dictated by the polarized
source pairing. It is not the conjugate Hilbert adjoint. Conjugation enters
only after restricting to the reciprocal real locus.

Define the reciprocal Dirac double

\[
\mathscr D(s)
=
\begin{pmatrix}
0&D_-(s)\\
D_+(s)&0
\end{pmatrix}.
\]

This is a holomorphic first-order pencil on \(X_+\oplus X_-\).

## Square and kernel

Its square is block diagonal:

\[
\mathscr D(s)^2
=
\begin{pmatrix}
D_-(s)D_+(s)&0\\
0&D_+(s)D_-(s)
\end{pmatrix}.
\]

Consequently,

\[
\ker\mathscr D(s)
=
\ker D_+(s)\oplus\ker D_-(s).
\]

On the reciprocal real locus, the source involution may identify the two
summands and turn the corresponding polarized square into the positive Green
energy. This gives a legitimate route from the holomorphic reciprocal Dirac
pencil, through its polarized square, to the positive Green form.

The first arrow preserves the ordered first-order data. The second performs
coercive confinement.

## Determinant doubling trap

In finite rank,

\[
\det\mathscr D(s)
=
(-1)^n\det D_+(s)\det D_-(s).
\]

Thus the determinant of the full doubled pencil carries both reciprocal
divisors. On a fixed point of the reciprocal involution it can double the
multiplicity seen by one chiral boundary cone.

Therefore the full Dirac determinant must not be identified directly with
\(\xi(s)\). The multiplicity carrier is the chiral determinant line

\[
\operatorname{Det}D_+
=
\det\ker D_+\otimes
\det\operatorname{coker}D_+^\vee,
\]

or its Fredholm analogue. The reciprocal line is its sewn dual. The doubled
pencil supplies the metric and symmetry, while one oriented chiral line
supplies the holomorphic divisor.

## Required source factorization

The useful theorem is not merely that some off-diagonal double exists. The
complete polarized first-order Green pencil must admit source-derived
intertwiners

\[
\mathcal P_{\mathrm{first}}(s)
=
E(s)\mathscr D(s)F(s),
\]

where \(E\) and \(F\) are holomorphic, invertible, and uniformly bi-bounded on
compact off-seam sets.

Its positive Green realization must then be obtained by imposing the
source real structure and the source metric:

\[
\mathfrak G_s(x,y)
=
\bigl\langle
\mathcal P_{\mathrm{first}}(s)x,\,
G_{\mathrm{src}}(s)
\mathcal P_{\mathrm{first}}(s)y
\bigr\rangle.
\]

This identity must hold after radical descent on the full stratified carrier,
including primitive, square, connected, wall, endpoint, and archimedean
ports.

## Multiplicity theorem

Suppose:

1. \(D_+(s)\) is a holomorphic Fredholm family of index zero;
2. its determinant line is source-trivialized by
   \[
   \det_{\mathrm{rel}}D_+(s)=u(s)\xi(s),
   \qquad u(s)\ne0;
   \]
3. \(E(s)\) and \(F(s)\) are holomorphic invertible families;
4. the reciprocal double is formed with the algebraic dual, not an
   antiholomorphic adjoint;
5. the positive Green form is coercive after the declared radical quotient.

Then:

- the chiral first-order pencil has the same local Fitting data and
  holomorphic multiplicities as \(\xi\);
- the reciprocal Dirac double has the correct symmetric kernel set but carries
  the product of the two reciprocal determinant lines;
- the positive normal form has the same kernel set but carries no independent
  holomorphic multiplicity statement.

The three roles are therefore separate:

- chiral determinant line: holomorphic divisor and multiplicity;
- reciprocal Dirac double: functional-equation symmetry and first-order
  kernel;
- positive Green normal form: coercivity and seam confinement.

## Completion gates

The finite construction survives completion only if:

1. the chiral boundary cones converge as a holomorphic Fredholm family;
2. the reciprocal duality maps converge on one fixed stratified carrier;
3. the intertwiners and their inverses remain compact-uniformly bounded;
4. the chiral determinant sections converge locally uniformly;
5. the doubled kernels acquire no extra completion states;
6. the positive source metrics retain compact-uniform coercivity.

A finite reciprocal double can be perfectly symmetric while its chiral
determinant line loses continuity at completion.

## Hostiles

1. Replace the algebraic reciprocal dual by the Hilbert adjoint and silently
   destroy holomorphy.
2. Use the determinant of the full double and count every zero twice.
3. Prove kernel equality for the double but never identify the chiral
   determinant section.
4. Obtain positivity only after an unbounded comparison map.
5. Let reciprocal sewing exchange determinant lines with an unauthorized
   phase.
6. Verify the square only on diagonal vectors and lose the ordered
   polarization.

## Verdict

The reciprocal geometry provides a canonical holomorphic linearization of the
positive Green mechanism: the reciprocal Dirac double.

It does not eliminate the multiplicity problem. It localizes multiplicity to
one oriented chiral determinant line, while the doubled pencil carries
functional-equation symmetry and the positive normal form carries coercive
zero exclusion.

The next source calculation is therefore the fully polarized off-diagonal
identity that identifies the two chiral blocks of the boundary cone with the
primitive-to-square and reciprocal square-to-primitive Green constructors.
