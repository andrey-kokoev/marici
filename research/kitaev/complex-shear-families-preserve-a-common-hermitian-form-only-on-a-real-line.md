# Complex shear families preserve a common Hermitian form only on a real line

## Bounded question

For which coefficient families \(\mathcal F\subset\mathbf C\) does the shear

\[
S(F)=
\begin{pmatrix}
1&F\\
0&1
\end{pmatrix}
\]

preserve one fixed nondegenerate Hermitian form?

## Exact common-form theorem

Assume \(\mathcal F\) contains a nonzero coefficient. There exists a fixed
nondegenerate Hermitian matrix \(H\) satisfying

\[
S(F)^*HS(F)=H
\qquad\text{for every }F\in\mathcal F
\]

if and only if the real span of \(\mathcal F\) has dimension one. Equivalently,
all nonzero coefficients occupy one real line in \(\mathbf C\).

Write

\[
H=
\begin{pmatrix}
a&b\\
\overline b&d
\end{pmatrix},
\qquad a,d\in\mathbf R.
\]

Direct multiplication gives the two independent invariance laws

\[
aF=0,
\qquad
2\operatorname{Re}(\overline bF)+a|F|^2=0.
\]

One nonzero \(F\) forces \(a=0\). Nondegeneracy then forces \(b\ne0\), and
every coefficient must satisfy

\[
\operatorname{Re}(\overline bF)=0.
\]

The kernel of this nonzero real functional on \(\mathbf C\simeq\mathbf R^2\)
is one real line. Conversely, if \(F=rq\) with \(r\in\mathbf R\) for one
nonzero \(q\), choose \(b=iq\) and any real \(d\). Then

\[
H_q=
\begin{pmatrix}
0&iq\\
-i\overline q&d
\end{pmatrix}
\]

is invariant and has determinant \(-|q|^2\ne0\).

## No positive metric for a nontrivial shear

Every invariant nondegenerate Hermitian form for a family containing a
nonzero shear has \(a=0\) and determinant \(-|b|^2<0\). It therefore has
signature \((1,1)\). No nontrivial shear preserves a positive-definite
Hermitian metric. The theorem concerns an indefinite conserved form, not
passivity or a Hilbert norm.

## Smallest hostile family

The two coefficients

\[
F_1=1,\qquad F_2=i
\]

do not lie on one real line. Invariance under \(F_1\) makes \(b\) purely
imaginary; invariance under \(F_2\) makes \(b\) real. Hence \(b=0\), while
either nonzero shear already forces \(a=0\). The resulting \(H\) is degenerate.
Two non-collinear phases are therefore the minimal common-form obstruction.

## Complex symplectic preservation is different

Let

\[
J=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

For every complex \(F\),

\[
S(F)^{\mathsf T}JS(F)=J.
\]

This uses transpose and the complex bilinear alternating form. Hermitian
preservation uses conjugate transpose. Determinant one gives the former in
rank two; it does not give the latter.

## Holomorphic-family corollary

If \(F(s)\) is holomorphic and nonconstant on a connected open complex domain,
its image cannot lie in one real line. Therefore the shears \(S(F(s))\) admit
no fixed nondegenerate Hermitian invariant form on that domain. A common form
can occur on a real slice where the coefficients share one phase, or after
additional source structure changes the state space or permits an
\(s\)-dependent form.

For the theta/Tate lane this means normal convergence and invertibility of the
completed shear do not construct a conserved Hermitian metric. Such a form
must come from boundary currents, and a fixed rank-two form is already ruled
out wherever the completed transform is holomorphic and nonconstant.

## Carrier geometry versus coefficient lens

The shear composition law and determinant-one complex symplectic form are
algebraic Carrier data. Complex conjugation, Hermitian signature, positivity,
and passivity belong to the coefficient and physical-interface lens. Treating
transpose preservation as conjugate-transpose preservation crosses that
typing boundary.

## Exact audit and falsifiers

The checker derives the full symbolic residual, verifies complex symplectic
preservation for an arbitrary coefficient, constructs a common indefinite form
for several coefficients on one exact rational complex line, and proves the
\(\{1,i\}\) hostile family forces degeneracy.

The theorem is falsified by two non-collinear coefficients preserving one
fixed nondegenerate Hermitian form, or by a collinear family for which the
displayed \(H_q\) fails invariance. A theta metric claim is falsified by any
two source-derived coefficient values with nonzero real determinant
\(\operatorname{Im}(\overline{F_1}F_2)\).

## Claim boundary

This is an exact rank-two algebraic theorem. It does not derive the actual
theta coefficient range, a boundary-current form, an \(s\)-dependent metric,
passivity, conservativity of a larger realization, KYP positivity, or RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
8/10. The alternatives were determinant-one implication of a common metric and
a conjugation-induced phase-line obstruction. The full residual, determinant,
two-phase hostile, and transpose-symplectic identity were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The common-metric branch was reduced exactly to one real coefficient
line; positive-definite invariance was eliminated; and the holomorphic
corollary rules out a fixed rank-two Hermitian form on any nonconstant open
complex family. Larger or parameter-dependent boundary forms remain open.
