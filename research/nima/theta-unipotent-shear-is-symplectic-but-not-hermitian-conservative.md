# Theta interval shear is symplectic but not generically Hermitian-conservative

Owner: marici.Nima

## Source-derived interval transport

In the integrating-factor coordinate \(Y(q)=e^{sq}G(q)\), the forced tail
equation becomes

\[
Y'(q)=-f(q)e^{sq}c.
\]

Retaining the constant source amplitude \(c\), transport across an interval
\([a,b]\) is the unipotent shear

\[
S_{a,b}(s)=
\begin{pmatrix}
1&F_{a,b}(s)\\
0&1
\end{pmatrix},
\qquad
F_{a,b}(s)=\int_a^b f(v)e^{sv}\,dv,
\]

up to the fixed sign convention chosen for the source column.

Because interval integrals add,

\[
F_{a,c}=F_{a,b}+F_{b,c},
\]

the shears compose strictly:

\[
S_{a,c}=S_{a,b}S_{b,c}.
\]

The scalar transform is therefore an off-diagonal holonomy coordinate, and
the terminal amplitude is the minimal additional state needed for restriction
and cascade composition.

## Flat nilpotent connection

Let

\[
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
N^2=0.
\]

Then

\[
S_{a,b}=I+F_{a,b}N
\]

is the holonomy of the source connection

\[
\omega_s=f(q)e^{sq}N\,dq.
\]

Nilpotence removes all higher path-ordered terms. A transform zero is thus

\[
F_{a,b}(s)=0,
\]

which means that the total unipotent holonomy is the identity even though the
local source increments need not vanish.

This is the geometric form of destructive interference in the finite
Rosenbrock realization.

## Algebraic symplectic conservation

Let

\[
\Omega=
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}.
\]

Every interval shear satisfies

\[
S(F)^T\Omega S(F)=\Omega
\]

for every complex coefficient \(F\). Equivalently, in complex dimension two,
the determinant-one shear preserves the complex alternating area form.

This is algebraic coherence. It does not supply a positive or Hermitian
energy.

## Exact common-metric criterion

Let

\[
H=
\begin{pmatrix}
\alpha&\beta\\
\overline\beta&\delta
\end{pmatrix}
\]

be a Hermitian matrix, with \(\alpha,\delta\) real. Suppose a family of
nontrivial shears \(S(F)\) is required to preserve one fixed nondegenerate
Hermitian form:

\[
S(F)^*HS(F)=H.
\]

Direct multiplication gives the necessary and sufficient conditions

\[
\alpha=0,
\qquad
\operatorname{Re}(\overline F\beta)=0
\]

for every coefficient \(F\) in the family. Nondegeneracy then requires
\(\beta\ne0\), since

\[
\det H=-|\beta|^2.
\]

Consequently, a family of nonzero complex shears preserves one common
nondegenerate Hermitian form if and only if all of its coefficients lie on
one fixed real line in the complex plane:

\[
F\in e^{i\theta}\mathbb R
\]

for some cutoff-independent phase \(\theta\).

For that line one may choose

\[
\beta=i c e^{i\theta},
\qquad
c\in\mathbb R\setminus\{0\}.
\]

Two coefficients with non-real ratio are therefore a finite falsifier for a
common two-dimensional Hermitian conservation law.

## Interpretation

The shear system has three different levels of structure:

1. strict interval composition for arbitrary complex source increments;
2. complex symplectic conservation for every determinant-one shear;
3. Hermitian energy conservation only after a common real form is selected.

The first two are automatic consequences of the source shear. The third is
additional orientation data.

This reproduces the earlier distinction between an algebraic reciprocal
quarter-turn and metric compatibility. A system may compose exactly, possess
an inverse, preserve determinant area and return identity holonomy at a
scalar zero while still lacking one conserved physical energy.

## Critical-seam qualification

The completed scalar section has a natural real structure on the critical
seam after its standard source normalization. That fact alone does not prove
that every interval coefficient \(F_{a,b}\) lies on one common real line.
Local interval shears can have varying complex phases even when the final
completed readout is real.

Therefore the common Hermitian metric cannot be inferred from scalar seam
reality. It must be derived from the doubled boundary-bearing source,
including the \(e,Je\) input quadrature and the primitive, square, connected
tail and archimedean currents.

## Consequence for the RH route

The finite shear supplies exact compositional and symplectic provenance, but
not passivity. A valid conservative completion must do one of the following:

1. prove that the full boundary-bearing channel coefficients occupy a
   source-selected common real form;
2. enlarge the state and source ports so conjugate channels jointly preserve
   a fixed Hermitian or Krein metric; or
3. derive a different current whose boundary law controls the complex shear
   family.

If none occurs, the Rosenbrock realization explains transfer composition and
zero dynamics but cannot orient the completed spectrum.

## Smallest falsifiers

- two source-authorized interval coefficients with non-real ratio;
- a Hermitian metric whose phase depends on the interval or cutoff;
- a metric inferred only after evaluating the completed scalar section;
- a doubled metric that erases the primitive or square boundary currents;
- identity total shear with nonzero local increments presented as local
  triviality.
