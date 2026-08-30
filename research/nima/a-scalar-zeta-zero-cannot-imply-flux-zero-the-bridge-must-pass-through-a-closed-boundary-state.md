# A scalar zeta zero cannot imply flux zero; the bridge must pass through a closed boundary state

## Universal implication is false

Let

\[
F(z)=1+2e^z.
\]

At

\[
z_0=-\log2+i\pi,
\]

one has \(F(z_0)=0\). The positive-source odd seam flux is

\[
\mathcal K(z)=4\sinh z,
\]

and

\[
\mathcal K(z_0)=3\ne0.
\]

Thus positivity, reciprocal two-port retention, exact moving-seam geometry,
and scalar cancellation do not imply flux cancellation.

The missing bridge cannot be a universal identity of Mellin transforms.

## Native jet obstruction

For a value--flux jet \((M,J)\), multiplication by a nonvanishing source
factor \(g\) acts as

\[
S_g=
\begin{pmatrix}
g&0\\
g'&g
\end{pmatrix}.
\]

The scalar readout \(r(M,J)=M\) propagates zeros because

\[
rS_g=g\,r.
\]

But its kernel is the invariant pure-flux line

\[
\ker r=\{(0,J)\}.
\]

Therefore a scalar zero is compatible with a permanently nonzero flux state.
No iteration of the native multiplicative jet removes this ambiguity.

## Functional-equation insufficiency

Reciprocal symmetry also does not force derivative or flux vanishing. If

\[
\Xi(s)=\Xi(1-s),
\]

then

\[
\Xi'(s)=-\Xi'(1-s).
\]

At an off-seam zero \(s_0\), this relates the derivative at two distinct
points. It does not imply \(\Xi'(s_0)=0\). Demanding both value and derivative
to vanish would additionally force multiple zeros and is stronger than RH.

Hence the desired zero-to-flux implication cannot be extracted from the scalar
functional equation alone.

## Correct intermediate object

The required bridge has the form

\[
\Xi(s_0)=0
\Longrightarrow
\exists\,0\ne h\in\ker\mathcal D(s_0)
\Longrightarrow
\mathfrak F_{\partial}(h;s_0)=0.
\]

Here:

- \(\mathcal D(s)\) is a source-derived operator pencil or boundary
  colligation;
- its determinant section is exactly \(\Xi(s)\);
- \(h\) is a genuine kernel state, not the scalar value--flux jet of \(\Xi\);
- the domain of \(\mathcal D(s)\) imposes a maximal isotropic or closed
  reciprocal boundary condition;
- Green's identity then forces the oriented boundary flux of \(h\) to vanish.

The second implication is a standard domain theorem once the boundary
condition is constructed. The first is the spectral identification theorem.

## Determinant theorem required

A scalar equality

\[
\det\mathcal D(s)=c(s)\Xi(s)
\]

is sufficient only when:

1. \(c(s)\) is nonvanishing on the region;
2. \(\mathcal D(s)\) is Fredholm or determinant-class in the declared
   topology;
3. determinant zero is equivalent to noninvertibility;
4. noninvertibility produces a kernel state in the Green domain rather than
   only a cokernel or completion defect;
5. cutoff determinants converge without spectral pollution;
6. the endpoint domain is preserved in the limit.

Without these points, scalar determinant agreement does not authorize a
zero-state flux law.

## Boundary closure, not derivative zero

For a kernel state \(h\), the closed boundary condition should pair reciprocal
endpoint data through a Lagrangian relation

\[
\Lambda_s\subset E_{\partial,+}\oplus E_{\partial,-}.
\]

If the Green boundary form is \(\Omega_\partial\), maximal isotropy gives

\[
\Omega_\partial(\operatorname{Tr}h,\operatorname{Tr}h)=0.
\]

This is flux zero for the operator state. It does not say that
\(\Xi'(s_0)=0\).

The distinction removes the apparent contradiction with expected simple
zeros: simple scalar determinant zeros may correspond to one-dimensional
operator kernels whose boundary traces are isotropic.

## Relation to the Birman--Schwinger defect

The earlier normalized defect

\[
I-K(s)
\]

is a candidate pencil. The needed equivalence is

\[
\Xi(s)=0
\quad\Longleftrightarrow\quad
1\in\sigma(K(s)),
\]

with the collision eigenvector lying in the complete polarized Green domain
and satisfying the reciprocal boundary relation.

Finite-cutoff eigenvalue collisions are insufficient. One needs convergence
of the pencils and exclusion of eigenvalues drifting to one without a
completed kernel state.

## Exact research order

The zero-to-flux programme must proceed as:

1. construct the complete operator pencil on the three-stratum source domain;
2. construct its maximal isotropic reciprocal endpoint condition;
3. prove the Green flux identity on that domain;
4. prove Fredholm and determinant-class control;
5. identify its determinant section with completed \(\Xi\);
6. infer that a scalar zero supplies a closed kernel state;
7. apply the oriented positivity theorem to force the seam.

Items 1--5 are constructor and spectral-identification obligations. Item 6 is
then legitimate and noncircular.

## Hostiles

1. Infer flux zero directly from \(\Xi(s_0)=0\).
2. Replace operator-state flux by \(\Xi'(s_0)\).
3. Use a determinant with an uncontrolled vanishing prefactor.
4. Let determinant zero produce only a cokernel state.
5. Impose flux-zero boundary conditions after locating the zeros.
6. Prove the equivalence only at finite cutoff.

## Verdict

There is no universal scalar zero-to-flux law. The two-atom hostile and the
invariant pure-flux jet line rule it out.

The valid bridge is spectral:

\[
\text{completed zeta zero}
\longrightarrow
\text{kernel state of a source-derived closed boundary pencil}
\longrightarrow
\text{vanishing Green flux}.
\]

The earliest unresolved RH-bearing theorem is therefore the determinant and
kernel-state identification for the complete polarized operator pencil.
