# Low-Point Scalar-Grade Audit

## Record

Date: 2026-08-12

Status: reproducible exact-arithmetic audit at four, six, and eight points. The independent
all-multiplicity proof is entry 14.

## Purpose

The reconstruction theorem in entry 11 says that the scalar associated-grade family must descend
through the Parke--Taylor KK/BCJ quotient before inverse pairing can define an intrinsic
half-object. This entry records the first explicit audit of that condition in this repository.

The implementation is

`research/nima/check_j_reconstruction.py`.

It uses only Python's standard library and exact rational arithmetic.

## Direct scalar computation

For each cyclic order, the planar \(\operatorname{Tr}(\Phi^3)\) tree is generated as the sum over
triangulations of the corresponding polygon. Every shifted propagator is expanded in
\(t=\delta^{-1}\), and the coefficient of \(t^{n-2}\) is selected. No NLSM Feynman rule, CHY
formula, or BCJ relation is used to produce the grade.

The number of scalar diagrams checked is

| Multiplicity | Triangulations |
| --- | ---: |
| 4 | 2 |
| 6 | 14 |
| 8 | 132 |

## Four-point normalization

For the canonical order,

\[
a_{R,4}(1234)
=
-(X_{13}+X_{24})
=
s_{13}.
\]

In the same Parke--Taylor basis,

\[
m(1234\mid1234)
=
\frac1{s_{12}}+\frac1{s_{23}}
=
-\frac{s_{13}}{s_{12}s_{23}}.
\]

Thus the reconstructed logarithmic coordinate is

\[
\mathsf J_4
=
-s_{12}s_{23}\,{\rm PT}(1234)
\]

in these conventions. This fixes the overall sign of the audit. Because the cohomology is
one-dimensional, it does not test basis independence.

## Six-point scalar grade

The triangulation expansion gives the following expression directly in canonical planar
variables:

\[
\begin{aligned}
a_{R,6}(123456)
={}&
-(X_{13}+X_{15}+X_{24}+X_{26}+X_{35}+X_{46})\\
&+\frac{(X_{13}+X_{24})(X_{15}+X_{46})}{X_{14}}\\
&+\frac{(X_{15}+X_{26})(X_{24}+X_{35})}{X_{25}}\\
&+\frac{(X_{13}+X_{26})(X_{35}+X_{46})}{X_{36}}.
\end{aligned}
\]

This displays the three allowed three-particle poles. For example,

\[
\operatorname*{Res}_{X_{14}=0}a_{R,6}
=
(X_{13}+X_{24})(X_{15}+X_{46}),
\]

the product of the two corresponding four-point grades, up to the two inherited minus signs.
The other two residues behave cyclically. The remaining line is the six-point contact term.

## BAS pairing implementation

For two cyclic orders \(\alpha,\beta\), the script computes

\[
m(\alpha\mid\beta)
=
(-1)^{w(\alpha\mid\beta)+1}
\sum_{T\in\mathcal G(\alpha)\cap\mathcal G(\beta)}
\frac1{\prod_{e\in T}s_e},
\]

where \(w\) is the relative winding number. This is the standard boundary-intersection formula
for two Parke--Taylor forms. No full singular ordering matrix is inverted.

## Two independent six-point reconstructions

The first reconstruction uses

\[
B_-=
\{(1,\alpha(2,3,4),5,6)\},
\qquad
B_+=
\{(1,\beta(2,3,4),6,5)\},
\]

and the second moves the fixed first label:

\[
\widetilde B_-=
\{(2,\alpha(1,3,4),5,6)\},
\qquad
\widetilde B_+=
\{(2,\beta(1,3,4),6,5)\}.
\]

Each pairing matrix is \(6\times6\) and is inverted exactly. The resulting representatives are
then paired against 27 distinct audit orderings, including orderings outside both input bases.

Result:

\[
I_6({\rm PT}_\gamma,\mathsf J_6^{B})
=
I_6({\rm PT}_\gamma,\mathsf J_6^{\widetilde B})
=
a_{R,6}(\gamma)
\]

for all 27 orderings in the audit, with exact equality of rational numbers.

This is a genuine basis-change test. It would fail if the orderwise scalar grades did not assemble
into one Parke--Taylor cohomology covector at six points.

## Ordering-relation audit

The script first evaluates photon decoupling,

\[
D_n=
a_{R,n}(1,2,\ldots,n)
+\sum_{i=2}^{n-1}
a_{R,n}(2,\ldots,i,1,i+1,\ldots,n),
\]

and finds exact zero in three deterministic generic rational samples at each of
\(n=4,6,8\).

For \(n=4,6,8\), the script evaluates the fundamental relation

\[
\sum_{i=2}^{n-1}
\left(s_{12}+s_{13}+\cdots+s_{1i}\right)
a_{R,n}(2,3,\ldots,i,1,i+1,\ldots,n)
=0.
\]

It vanishes exactly in three deterministic generic rational kinematic samples at each tested
multiplicity. Samples with a zero test denominator are discarded rather than regularized.

It also evaluates the Kleiss--Kuijf shuffle identity

\[
a(1,\alpha,n,\beta)
=
(-1)^{|\beta|}
\sum_{\sigma\in\alpha\shuffle\beta^{\mathsf T}}
a(1,\sigma,n)
\]

for five ordered splits at six points and seven ordered splits at eight points. All vanish
exactly. These KK checks audit the primary-relation closure used in entry 14; that closure is an
all-order algebraic theorem and does not depend on finite sampling.

Finally, the script verifies coefficient by coefficient the exceptional
\(S_6\)-orbit tensor identity used by the quadratic soft-contact lemma in entry 14. This checks
the only six-point case not reduced immediately by a common omitted label or a four-cycle split.

The eight-point check is useful because it sums 132 scalar triangulations for every ordering and
tests an overlapping-channel amplitude. It remains a finite check, not a proof of the full BCJ
ideal.

## Reproduction

From the repository root run:

```text
python research/nima/check_j_reconstruction.py
```

The expected final line is:

```text
all exact low-point checks passed
```

## What this establishes

- the alternating scalar-grade algorithm reproduces the stated four- and six-point formulas;
- normalization is fixed at four points;
- the first nontrivial inverse-pairing reconstruction is independent of two explicit BCJ bases;
- photon decoupling survives exact checks through eight points;
- the fundamental BCJ relation survives exact checks through eight points;
- representative KK shuffles survive exact checks at six and eight points;
- the exceptional six-point quadratic contact identity holds exactly;
- six-point physical residues factorize before any inverse-pairing computation.

## What it does not establish

- by itself, the all-multiplicity proof that the scalar grade annihilates the full KK/BCJ kernel;
  that proof is given analytically in entry 14;
- equality with \((\operatorname{Pf}'A)^2\) without the perfect-pairing/period argument of entry 11;
- a canonical scalar-surface boundary map;
- half-object-level Jordan strictification;
- loop or modular completion.

## Next falsification target

Move from ordering relations to the six-point channel quotient. Verify the leading inverse-BAS
block and the induced \(\mathsf J_4\otimes\mathsf J_4\) residue described in entry 13. This tests
factorization naturality rather than repeating the now-proved descent relation.
