# Minimal endpoint–forcing incidence is direction-sensitive

## Bounded question

What is the smallest algebraic incidence that makes a scalar endpoint
displacement observable and controllable together with an already faithful
two-coordinate reciprocal forcing port?

## Frozen state decomposition

Let

\[
X=Y\oplus F,
\qquad
\dim_{\mathbf C}Y=1,
\]

where \(Y\) is endpoint displacement and \(F\) is the forcing port. Assume
\(J:F\to Z\) is injective. The diagonal observation

\[
C_0=(0,J)
\]

is faithful on forcing but has the entire endpoint line \(Y\) as kernel.
Adding more rows that factor only through \(F\) cannot change this kernel.

## Static incidence theorem

Add one source row

\[
\ell=(\alpha,r):Y\oplus F\to\mathbf C.
\]

Then the stacked observation \(\binom{C_0}{\ell}\) is injective exactly when
\(\alpha\ne0\). Indeed, zero forcing output gives \(c=0\), after which the new
row gives \(\alpha y=0\). One scalar row is therefore the minimal static repair,
but only if it actually contains the endpoint coordinate.

If \(J^*J>0\), the resulting feature Gramian is positive definite exactly
under the same condition. Its positivity is feature-space faithfulness, not
yet dynamical or completion-stable observability.

## Dynamic direction theorem

Write the state operator in blocks

\[
A=
\begin{pmatrix}
a&p\\
q&A_F
\end{pmatrix},
\]

where \(p:F\to Y\) and \(q:Y\to F\). With output \(C_0=(0,J)\), the two-step
observability matrix is

\[
\mathcal O_2=
\begin{pmatrix}
C_0\\
C_0A
\end{pmatrix}.
\]

It is injective exactly when \(q\ne0\). The proof is immediate: \(C_0(y,c)=0\)
forces \(c=0\), and then \(C_0A(y,0)=Jqy\). Since \(J\) is injective and
\(Y\) is one-dimensional, this vanishes for nonzero \(y\) exactly when
\(q=0\).

The opposite block \(p\) does not help observability. A forcing-to-endpoint
coupling can be nonzero while a pure endpoint state remains forever hidden from
forcing sensors.

## Dual controllability theorem

Assume the forcing coordinates have a surjective input port

\[
B_0=\binom{0}{I_F}.
\]

Then the two-step reachability matrix \((B_0\;AB_0)\) is surjective onto
\(Y\oplus F\) exactly when \(p\ne0\). Thus the two directions have different
jobs:

\[
q:Y\to F \quad\text{reveals endpoint displacement},
\]

\[
p:F\to Y \quad\text{actuates endpoint displacement}.
\]

A finite minimal realization with full forcing observation and actuation needs
both nonzero. Mere existence of an unspecified off-diagonal block is
insufficient.

## Hostile fixtures

1. **Diagonal direct sum:** \(p=q=0\). The forcing Gramian is positive, but
   the endpoint line is unobservable and unreachable.
2. **Wrong-way coupling:** \(p\ne0,q=0\). The endpoint is reachable from the
   forcing input but remains unobservable from forcing outputs.
3. **Duplicated forcing rows:** arbitrarily many rows of the form \((0,r_j)\)
   retain the endpoint kernel.
4. **Cutoffwise observability collapse:** with \(q_N=(1/N,0)^{\mathsf T}\),
   every finite two-step observability matrix has full rank, but the normalized
   endpoint state has observation energy \(1/N^2\to0\).
5. **Unauthorized static repair:** choosing \(\alpha\ne0\) because it makes the
   Gramian invertible does not derive a theta endpoint row.

## Transmission-zero consequence

The reciprocal forcing storage may be uniformly faithful on \(F\) while being
completely non-orienting for endpoint transmission zeros. An RH-bearing
realization must contain source-derived incidence in the endpoint-to-forcing
direction \(q\), or a direct endpoint sensor \(\alpha\ne0\). A fully minimal
input-output realization also needs the dual forcing-to-endpoint direction
\(p\).

This theorem identifies the type, direction, and minimum rank of the missing
constructor. It does not choose its coefficients. Grothendieck must derive them
from tail, seam, primitive, square, and archimedean boundary data.

## Carrier geometry versus coefficient lens

The decomposition \(Y\oplus F\), block directions, and incidence domains are
Carrier geometry. The adjoint, Gramian, positivity, source sensor, and physical
actuation interpretation belong to the coefficient/interface lens. Rank repair
alone cannot authorize either map.

## Exact audit and falsifiers

The checker exhausts small rational \(p,q\), verifies the static, observability,
and reachability equivalences, and requires all hostile fixtures. The
completion claim is falsified by the normalized endpoint sequence whose output
energy tends to zero. Source typing is falsified if the only nonzero incidence
was selected after observing the desired rank.

## Claim boundary

This is a finite-dimensional compiler theorem. It does not derive theta/Tate
incidence, prove uniform observability, build a physical controller, establish
passivity, orient zeros, or prove RH.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
9/10. The alternatives were direction-insensitive coupling and distinct
observability/controllability directions. Static rank, two-step ranks, wrong-way
and duplicate hostiles, and a collapsing family were frozen measurements.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Incidence split into two directional constructors with separate jobs;
one endpoint-sensitive row was proved statically minimal; and cutoffwise full
rank was separated from uniform observability. Theta source coefficients remain
unconstructed.
