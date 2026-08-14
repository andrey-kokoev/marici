# Alternating Fusion Conductor Symbol and the First Cross-Normal Relation

## Record

Date: 2026-08-13

Status: exact integral coefficient-symbol theorem. The two alternating
scalar-scaffolded three-gluon residues canonically derive the six-point QTDS
contact matrix and its marked-theta Ward-kernel lift. A scalar BRST/kinetic
chain realization and physical Cut naturality remain open.

The result is the first explicit algebraic relation between two distinct
normal constructions on the scalar master. It is not a relation between final
amplitudes. It is a conductor symbol on the union of two complementary fusion
strata.

## Alternating fusion strata

Use the six short planar variables

\[
x_j=X_{j+1,j+3},
\qquad j\in\mathbb Z/6,
\]

and the three long variables

\[
y_0=X_{14},
\qquad
y_1=X_{25},
\qquad
y_2=X_{36}.
\]

Momentum conservation identifies \(X_{26}=X_{62}=x_5\).

The scaffold pairing

\[
\mathfrak f_+=(12)(34)(56)
\]

has fusion-normal ideal

\[
I_+=(x_0,x_2,x_4).
\]

One-step cyclic rotation gives the complementary pairing

\[
\mathfrak f_-=(23)(45)(61)
\]

with ideal

\[
I_-=(x_1,x_3,x_5).
\]

Let

\[
F_\pm=V(I_\pm),
\qquad
F=F_+\cup F_-,
\qquad
Z=F_+\cap F_-.
\]

The normalization of the reducible fusion carrier is

\[
\nu:\widetilde F=F_+\sqcup F_-\longrightarrow F,
\]

and \(Z\) is its conductor locus.

## The two scalar-derived three-gluon residues

The documented three-gluon multi-normal residue on \(F_+\) is

\[
A_3^+
=
y_0x_5+y_2x_1+y_1x_3
-
(y_0y_1+y_0y_2+y_1y_2).
\]

Cyclic rotation gives

\[
A_3^-
=
y_1x_0+y_0x_2+y_2x_4
-
(y_0y_1+y_0y_2+y_1y_2).
\]

These are sections of the ordered multi-residue lines

\[
L_+
=
N^\vee_{13}\otimes N^\vee_{35}\otimes N^\vee_{51},
\]

\[
L_-
=
N^\vee_{24}\otimes N^\vee_{46}\otimes N^\vee_{62}.
\]

One-step rotation maps the ordered fusion-normal list

\[
(x_0,x_2,x_4)
\longmapsto
(x_1,x_3,x_5)
\]

position by position. It therefore identifies the ordered residue lines with
positive orientation. No arbitrary scalar trivialization is introduced.

On the conductor,

\[
A_3^+|_Z
=
A_3^-|_Z
=
A_0
=
-(y_0y_1+y_0y_2+y_1y_2).
\]

Thus the two branch sections glue at order zero.

## The intrinsic conductor symbol

Inside \(F_+\), the conductor \(Z\) has normal coordinates
\((x_1,x_3,x_5)\). Inside \(F_-\), it has normal coordinates
\((x_0,x_2,x_4)\). Define the polarity-odd relative normal symbol

\[
\boxed{
\sigma_{\rm alt}(A_3^+,A_3^-)
=
d_{Z/F_+}A_3^+
-
d_{Z/F_-}A_3^-.
}
\]

Explicitly,

\[
\boxed{
\sigma_{\rm alt}
=
y_2\,dx_1+y_1\,dx_3+y_0\,dx_5
-y_1\,dx_0-y_0\,dx_2-y_2\,dx_4.
}
\]

This symbol is intrinsic to the normalized union. It uses only derivatives in
directions that exist on the corresponding branch. It does not extend
\(A_3^+\) into the missing even directions or \(A_3^-\) into the missing odd
directions.

Algebraically, if

\[
J_+=(x_1,x_3,x_5)\subset\mathcal O(F_+),
\qquad
J_-=(x_0,x_2,x_4)\subset\mathcal O(F_-),
\]

then

\[
\sigma_{\rm alt}
=
[A_3^+-A_0]_{J_+/J_+^2}
-
[A_3^--A_0]_{J_-/J_-^2}.
\]

Changing an ambient representative of \(A_3^+\) by \(I_+\), or of \(A_3^-\)
by \(I_-\), changes neither branch function and hence neither relative normal
symbol. The executable audit verifies this on all fifty-four quadratic ideal
monomials at the degree relevant to \(A_3\).

## Shared-longitudinal symbol

Take the linear symbol in the common \(y\)-directions. With columns ordered as

\[
(dx_0,dx_1,dx_2,dx_3,dx_4,dx_5),
\]

the three coefficient rows are

\[
d_0=dx_5-dx_2,
\]

\[
d_1=dx_3-dx_0,
\]

\[
d_2=dx_1-dx_4.
\]

Equivalently,

\[
d_y\sigma_{\rm alt}
=
\begin{pmatrix}
0&0&-1&0&0&1\\
-1&0&0&1&0&0\\
0&1&0&0&-1&0
\end{pmatrix}.
\]

The three long channels are the vertices opposite the three roads of the
oriented channel triangle. Its Ward-star incidence is

\[
\partial_\triangle(d_0,d_1,d_2)
=
(d_2-d_1,\ d_0-d_2,\ d_1-d_0).
\]

Therefore

\[
\boxed{
C_{\rm QTDS}
=
\partial_\triangle d_y\sigma_{\rm alt}
=
\begin{pmatrix}
1&1&0&-1&-1&0\\
0&-1&-1&0&1&1\\
-1&0&1&1&0&-1
\end{pmatrix}.
}
\]

This is exactly the six-point QTDS contact matrix independently obtained from
the scalar rank-jump presentation. Every column lies in

\[
A_2=\widetilde H_0(R_3;\mathbb Z).
\]

No \(GL(6)\) fit or adjustable normalization occurs.

## The complete cross-normal formula

Entry 64 supplies the integral suspension

\[
\Gamma_3:A_2\xrightarrow{\sim}H_1(K_{2,3};\mathbb Z),
\]

and entry 59 supplies the integral Ward bridge

\[
\Theta:H_1(K_{2,3};\mathbb Z)\xrightarrow{\sim}\ker d_{\rm Ward}.
\]

The complete coefficient relation is therefore

\[
\boxed{
M_{\rm Ward}
=
\Theta\,
\Gamma_3\,
\partial_\triangle\,
d_y\,
\sigma_{\rm alt}
\left(
\mathbb J_{\mathfrak f_+}A_{\rm scalar},
\mathbb J_{\mathfrak f_-}A_{\rm scalar}
\right).
}
\]

It gives

\[
M_{\rm Ward}
=
\begin{pmatrix}
0&-1&-1&0&1&1\\
-1&-1&0&1&1&0\\
0&1&1&0&-1&-1\\
1&1&0&-1&-1&0\\
-1&-1&0&1&1&0\\
0&1&1&0&-1&-1\\
1&0&-1&-1&0&1
\end{pmatrix}.
\]

All six columns are annihilated by the exact marked-theta Ward contact
differential.

This closes the coefficient-level gap left in entry 64.

## Why both fusion branches are necessary

A single residue cannot contain this relation.

The \(F_+\) residue is independent of its own fusion normals

\[
x_0,\ x_2,\ x_4,
\]

while the \(F_-\) residue is independent of

\[
x_1,\ x_3,\ x_5.
\]

Each branch is therefore blind to exactly three columns of
\(C_{\rm QTDS}\). The six-column source exists only as the polarity-odd
relative symbol of the normalized two-branch carrier.

This is structurally important:

> The first cross-normal relation is not a unary operator on one fusion
> residue. It is descent data attached to the intersection of two alternating
> fusion charts.

The scalar master supplies the two local sections, their cyclic line
transport, their common conductor value, and their complementary relative
normal directions.

## What has now been proved

Proved exactly:

1. the two scaffold residues are scalar-derived and related by cyclic
   rotation;
2. their ordered conormal residue lines are cyclically identified with
   positive orientation;
3. their restrictions agree on the conductor;
4. their polarity-odd relative normal symbol is independent of ambient
   representatives;
5. its common-\(y\) linear symbol followed by road incidence is exactly the
   QTDS contact matrix;
6. suspension and the Ward bridge give the exact seven-by-six Ward-kernel
   matrix;
7. every resulting column is Ward closed.

Still open:

1. a morphism of scalar multi-normal residue/kinetic complexes whose associated
   symbol is \(\sigma_{\rm alt}\);
2. compatibility with gauge/BRST descent;
3. one complete-pair separating Cut square;
4. one nonseparating Cut with explicit internal-state coevaluation;
5. extension beyond the three-gluon/six-scalar local model.

Thus the result is intrinsic at coefficient-symbol level but not yet a
physical chain-level natural transformation.

## Consequence for the operation algebra

The relation cannot be written using only a list of unary operators such as
\(\operatorname{gr}_R\) and \(\mathbb J_{\mathfrak f}\). It uses incidence
between strata:

\[
F_+\longleftarrow Z\longrightarrow F_-.
\]

The new primitive operation is a bivariant normal symbol on the conductor of a
reducible normal carrier,

\[
\sigma_{\rm alt}:
\left(
\mathbb J_{\mathfrak f_+}\mathcal S,
\mathbb J_{\mathfrak f_-}\mathcal S
\right)
\longrightarrow
N^\vee_{Z/\widetilde F}\otimes\operatorname{sgn}_{\rm pol}.
\]

This is exactly the kind of operation expected in a Cousin, Cech, or
exit-path description of a stratified master geometry. It is further evidence
that the emerging structure is a derived incidence calculus rather than a
strict operator algebra on amplitudes.

## Next falsifier

Construct a chain map

\[
\boldsymbol{\sigma}_{\rm alt}:
\operatorname{Tot}
\check C
\left(
\{F_+,F_-\};
\mathbb J_{\mathfrak f}\mathcal S
\right)
\longrightarrow
\mathcal W_{\rm Ward}
\]

whose associated coefficient symbol is the matrix above.

It must:

1. carry the ordered residue lines rather than trivialize them silently;
2. intertwine the scalar kinetic differential with the Ward differential;
3. reproduce \(\Theta\Gamma_3\partial_\triangle d_y\sigma_{\rm alt}\) on the
   associated grade;
4. commute with a Cut that partitions complete fusion pairs;
5. include the physical coevaluation when a Cut creates an internal gluon;
6. survive one nonseparating Cut modulo the declared hereditary
   total-derivative ideal.

Failure at step 2 would make the exact coefficient relation kinematic but not
gauge-cohomological. Failure at steps 4--6 would make it local but not a
self-factorizing physical dictionary.

## Reproducible certificate

Run:

```text
rustc --edition=2021 -D warnings -O research/nima/check_three_gluon_qtds_transgression.rs -o "$env:TEMP\\marici-three-gluon-transgression.exe"
& "$env:TEMP\\marici-three-gluon-transgression.exe"
```

The certificate checks the two branch formulas, conductor gluing, cyclic
residue-line orientation, independence from all relevant quadratic ambient
representative changes, the exact QTDS contact matrix, the complete Ward
matrix, and Ward closure of all six columns.

## Internal dependencies

- Entry 08: Yang--Mills as a multidegree-\((1,\ldots,1)\) normal residue.
- Entry 20: the scalar-derived six-point QTDS contact matrix.
- Entries 59 and 64: the integral Ward bridge and suspension.
- `research/nima/check_three_gluon_qtds_transgression.rs`: exact certificate.