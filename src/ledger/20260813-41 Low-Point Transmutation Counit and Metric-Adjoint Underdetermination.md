# Low-Point Transmutation Counit and Metric-Adjoint Underdetermination

## Record

Date: 2026-08-13

Status: exact four- and five-point field-theory audit complete. The augmented
lowering map is cyclically reference-independent after quotienting by the
annihilator of the canonical Yang--Mills amplitude. It is a transmutation
counit/coframe identity. The proposed metric adjoint is not determined by the
published data and remains a distinct chain-level problem.

Reproducible certificate:

```text
research/nima/check_low_point_transmutation.rs
```

## Question

Entry 40 isolated three possible outcomes for the low-point relation between
scalar scaffolding and the new scaffold differential operators:

1. a genuine metric adjunction;
2. a weaker augmented counit/coframe identity;
3. irreducible dependence on the cyclic scaffold reference.

The proposed adjoint was

\[
J^\dagger_{\rm metric}
=
I_S^{-1}J^{\mathsf T}I_G.
\]

The finite audit gives a sharp, but qualified, answer:

> Outcome 2 is realized on the canonical tree Yang--Mills amplitude at four and
> five points. Outcome 3 is absent after augmentation and the canonical
> amplitude quotient. Outcome 1 is not a matrix that the published
> constructions presently determine.

This is not merely a failure to finish a large matrix computation. The input
needed to define that matrix is absent.

## The intrinsic-looking lowering operator

Backus and Figueiredo define

\[
\mathcal W_{2i}[F]
=
\sum_{j\notin\{2i,2i\pm1\}}
\frac{\partial F}{\partial X_{2i,j}}.
\]

Let

\[
E_n=\{2,4,\ldots,2n\}
\]

be the even scaffold labels. Their tree-level, low-energy theorem states that
for any two distinct labels \(e_1,e_2\in E_n\),

\[
\left(
\prod_{e\in E_n\setminus\{e_1,e_2\}}
\mathcal W_e
\right)
A_n^{\rm YM}
=
X_{e_1,e_2}A_n^{\operatorname{Tr}\phi^3}.
\]

The scalar amplitude on the right depends only on odd--odd variables. Since
\(X_{e_1,e_2}\) occurs with unit coefficient in both \(\mathcal W_{e_1}\)
and \(\mathcal W_{e_2}\), either final action removes the prefactor:

\[
\mathcal W_{e_1}
\prod_{e\notin\{e_1,e_2\}}\mathcal W_e A_n^{\rm YM}
=
\mathcal W_{e_2}
\prod_{e\notin\{e_1,e_2\}}\mathcal W_e A_n^{\rm YM}
=
A_n^{\operatorname{Tr}\phi^3}.
\]

It is therefore convenient to define the full transmuter leaving the even
label \(e_*\) unacted:

\[
T_{e_*}
=
\prod_{e\in E_n\setminus\{e_*\}}\mathcal W_e,
\qquad
T_{e_*}A_n^{\rm YM}
=
A_n^{\operatorname{Tr}\phi^3}.
\]

As differential operators in the original scaffold coordinates the
\(\mathcal W_e\) commute. The order dependence discussed in the source concerns
the convenient sequence of split/polarization loci, not the final operator
identity.

This already supplies a reference-independent augmented lowering operation at
the level of the distinguished field-theory amplitude.

## Four points

Write \([a,b]=\partial_{X_{a,b}}\). Dong--Su--Yang fix the reference derivatives
\([2,8][1,4]\). Their two graph extractors are

\[
D_1=[2,8][1,4][1,6],
\qquad
D_2=[2,8][1,4][3,6],
\]

and obey

\[
D_1A_4^{\rm YM}=\frac1{X_{1,5}},
\qquad
D_2A_4^{\rm YM}=\frac1{X_{3,7}}.
\]

Consequently their cellular augmentation is

\[
(D_1+D_2)A_4^{\rm YM}
=
\frac1{X_{1,5}}+
\frac1{X_{3,7}}
=
A_4^{\operatorname{Tr}\phi^3}.
\]

For the same reference, the Backus--Figueiredo transmuter is

\[
T_8=\mathcal W_2\mathcal W_4\mathcal W_6.
\]

The three factors contain, respectively,

\[
[2,8],\qquad [1,4],\qquad [1,6]\ \text{or}\ [3,6].
\]

Thus \(D_1\) and \(D_2\) are literally two monomials in the coordinate
expansion of \(T_8\). But they are not the whole operator. The exact expansion
has

\[
5^3=125
\]

raw selections and 124 distinct derivative monomials. Both \(D_i\) occur with
coefficient one. Therefore

\[
R_{4,0}
=
T_8-D_1-D_2
\]

is a nonzero differential operator with 122 distinct monomials and total
coefficient weight 123. Nevertheless the two source theorems imply

\[
R_{4,0}A_4^{\rm YM}=0.
\]

This is already enough to distinguish an operator equality from an equality
after evaluation on the canonical amplitude.

## Five points

For the reference derivatives \([2,10][1,4]\), the five pentagon
triangulations and their complete extractors are

| Cell | Scalar diagram | Complete differential monomial |
|---|---|---|
| \(\Gamma_1\) | \(1/(X_{1,5}X_{1,7})\) | \([2,10][1,4][1,6][1,8]\) |
| \(\Gamma_2\) | \(1/(X_{3,7}X_{3,9})\) | \([2,10][1,4][3,6][3,8]\) |
| \(\Gamma_3\) | \(1/(X_{1,5}X_{5,9})\) | \([2,10][1,4][1,6][5,8]\) |
| \(\Gamma_4\) | \(1/(X_{1,7}X_{3,7})\) | \([2,10][1,4][1,8][3,6]\) |
| \(\Gamma_5\) | \(1/(X_{3,9}X_{5,9})\) | \([2,10][1,4][3,8][9,6]\) |

The ray and fan cases are explicit examples or immediate specializations of
the Dong--Su--Yang rules; the remaining two follow mechanically from their
connected-sequence prescription. Together they give

\[
\sum_{a=1}^{5}D_{\Gamma_a}A_5^{\rm YM}
=
A_5^{\operatorname{Tr}\phi^3},
\]

where

\[
\begin{aligned}
A_5^{\operatorname{Tr}\phi^3}
={}&
\frac1{X_{1,5}X_{1,7}}
+\frac1{X_{3,7}X_{3,9}}
+\frac1{X_{1,5}X_{5,9}}\\
&+\frac1{X_{1,7}X_{3,7}}
+\frac1{X_{3,9}X_{5,9}}.
\end{aligned}
\]

The corresponding full transmuter is

\[
T_{10}
=
\mathcal W_2\mathcal W_4\mathcal W_6\mathcal W_8.
\]

Every listed \(D_{\Gamma_a}\) selects one coordinate derivative from each of
these four factors. Hence the full Catalan coframe is again contained
monomial-by-monomial in \(T_{10}\).

The exact expansion now has

\[
7^4=2401
\]

raw selections and 2370 distinct derivative monomials. Each of the five graph
extractors occurs with coefficient one. The residual

\[
R_{5,0}
=
T_{10}-\sum_{a=1}^{5}D_{\Gamma_a}
\]

has 2365 distinct monomials, total coefficient weight 2396, and satisfies

\[
R_{5,0}A_5^{\rm YM}=0.
\]

The coframe is therefore a very sparse cellular resolution of the full
transmutation operator on this particular amplitude. It is not an equality of
free differential operators.

## The exact quotient statement

Let \(\operatorname{Diff}_n\) denote the algebra generated by scaffold
coordinate derivatives and define

\[
\operatorname{Ann}(A_n^{\rm YM})
=
\{D\in\operatorname{Diff}_n:D A_n^{\rm YM}=0\}.
\]

At four and five points the low-point result is

\[
\boxed{
[T_{e_*}]
=
\left[\sum_{\Gamma}D_{\Gamma}^{(e_*)}\right]
\quad\text{in}\quad
\operatorname{Diff}_n/\operatorname{Ann}(A_n^{\rm YM})
}
\]

for every cyclic scaffold reference \(e_*\). Evaluation gives

\[
T_{e_*}A_n^{\rm YM}
=
\sum_\Gamma D_\Gamma^{(e_*)}A_n^{\rm YM}
=
A_n^{\operatorname{Tr}\phi^3}.
\]

This annihilator quotient is a precise low-point quotient. It should not be
silently identified with the full gauge-cohomological or PT/KK/BCJ quotient;
constructing a comparison to those representation-independent quotients is
additional work.

## Every cyclic scaffold reference

Let

\[
\rho_r(i)=i+2r\pmod{2n}
\]

with labels returned to \(\{1,\ldots,2n\}\). Rotate the base reference,
operators, and cells by \(\rho_r\), and set

\[
e_*^{(r)}=\rho_r(2n).
\]

The Rust certificate checks every reference rather than assuming covariance.

At four points:

| \(r\) | Rotated fixed even pair | \(e_*^{(r)}\) | Cell permutation |
|---:|---|---:|---|
| 0 | \((2,8)\) | 8 | \((1)(2)\) |
| 1 | \((2,4)\) | 2 | \((12)\) |
| 2 | \((4,6)\) | 4 | \((1)(2)\) |
| 3 | \((6,8)\) | 6 | \((12)\) |

Every rotated coframe is contained in the corresponding
\(T_{e_*^{(r)}}\) expansion. Each expansion has the same
125/124 raw/distinct count and the same 122-support residual.

At five points:

| \(r\) | Rotated fixed even pair | \(e_*^{(r)}\) | Cell permutation |
|---:|---|---:|---|
| 0 | \((2,10)\) | 10 | \(1\to1\to\cdots\) |
| 1 | \((2,4)\) | 2 | \(1\to2\to3\to4\to5\to1\) |
| 2 | \((4,6)\) | 4 | the square of that 5-cycle |
| 3 | \((6,8)\) | 6 | the cube of that 5-cycle |
| 4 | \((8,10)\) | 8 | the fourth power of that 5-cycle |

Every expansion has the same 2401/2370 raw/distinct count and the same
2365-support residual. Rotation permutes the five scalar diagrams, so their
augmentation is unchanged.

The stronger omitted-pair audit also passes:

- at four points there are 6 omitted pairs, 12 labelled choices of final
  \(\mathcal W\), and 4 distinct full transmuters \(T_{e_*}\);
- at five points there are 10 omitted pairs, 20 labelled choices of final
  \(\mathcal W\), and 5 distinct full transmuters.

Every \(T_{e_*}\) appears \(n-1\) times among the pair/final-action choices and
has the same scalar output. Thus raw coordinates remain reference-dependent,
but no reference defect survives the augmentation/annihilator quotient at
these arities.

## Why the metric adjoint cannot be computed

For a genuine adjunction one needs an actual linear map

\[
J^+:S_{2n}^+
\longrightarrow
G_n^+\otimes L_{\mathfrak f}
\]

on specified paired spaces, not only a rule sending one distinguished scalar
master amplitude to one Yang--Mills amplitude.

In the most favorable generic twisted-cohomology model,

\[
\dim S_{2n}=(2n-3)!,
\qquad
\dim G_n=(n-3)!
\]

before including the external gauge-state fiber. The low-point counts are:

| \(n\) | \(\dim S_{2n}\) | \(\dim G_n\) | Entries of full \(J\) | Free after one master-section value | Optimistic free count after \(n\) independent cyclic values |
|---:|---:|---:|---:|---:|---:|
| 4 | 120 | 1 | 120 | 119 | at least 116 |
| 5 | 5040 | 2 | 10080 | 10078 | at least 10070 |

The last column is deliberately overgenerous: the cyclic values are related by
relabeling, so they need not supply \(n\) independent constraints. Even under
that favorable fiction the matrix is overwhelmingly undetermined.

There are four independent missing pieces:

1. the published fusion residue gives the image of the distinguished scalar
   master section, not the action of \(J\) on a complete source basis;
2. no chain-level physical gauge pairing \(I_G\), including transverse-state
   coevaluation, is supplied;
3. \(J^\dagger\) returns to a \(2n\)-point normal object carrying
   \(L_{\mathfrak f}^\vee\), whereas \(T_{e_*}\) is an arity-preserving
   \(n\)-point transmutation;
4. the diagram derivatives are specified through their values on the canonical
   amplitude, not as a map on an arbitrary gauge cohomology class.

If a smaller fusion-normal source is intended instead of the global
twisted-cohomology space, that source and its perfect pairing must first be
defined. Merely restricting both constructions to their distinguished
one-dimensional lines makes an adjoint tautological and normalization-dependent;
it does not compute the claimed intrinsic adjoint.

Therefore

\[
I_S^{-1}J^{\mathsf T}I_G
\]

is presently undefined as an explicit low-point matrix. Invertible choices of
\(I_S\) and \(I_G\) would transport, not remove, the large ambiguity in \(J\).

## Three-way verdict

### 1. Genuine adjunction

Not established and not presently evaluable. The literal identification with
the published \(D_\Gamma\) or \(T_{e_*}\) is type-incompatible. A future
normal-line-corrected Gysin/Thom comparison could still produce a genuine
adjunction theorem, but it would be new structure.

### 2. Weaker counit/coframe identity

Established at tree field theory for \(n=4,5\) on the canonical amplitude:

\[
T_{e_*}
\equiv
\sum_\Gamma D_\Gamma^{(e_*)}
\pmod{\operatorname{Ann}(A_n^{\rm YM})},
\]

and both sides evaluate to the complete planar scalar amplitude. The
\(D_\Gamma\) are sparse Catalan coordinates of the transmutation counit.

### 3. Irreducible reference dependence

Falsified at the augmented canonical-amplitude level through five points. All
cyclic references give the same scalar output and differ only by a permutation
of the cellular presentation plus an amplitude-annihilating operator. Raw
operator representatives remain reference-dependent.

## Conceptual update

The correct emerging algebra is not yet a metric raising/lowering algebra.
What is actually visible is

\[
\text{scalar master}
\xrightarrow{\text{fusion normal residue}}
\text{YM distinguished section}
\xrightarrow{\text{transmutation counit}}
\text{scalar amplitude},
\]

with the second arrow admitting a Catalan cellular coframe. The composite may
eventually be recognized as a counit, trace, or Frobenius-type contraction, but
calling it an adjoint now would erase the arity, normal-line, and pairing data
that remain missing.

The next non-tautological task is consequently not another low-point derivative
expansion. It is to construct a full chain-level fusion map and physical gauge
pairing, then ask whether its Verdier/Gysin adjoint descends to the already
identified transmutation class.

## Reproduction

```powershell
rustc --edition=2021 -O research/nima/check_low_point_transmutation.rs `
  -o "$env:TEMP\marici-low-point-transmutation.exe"
& "$env:TEMP\marici-low-point-transmutation.exe"
```

The certificate checks:

- both four-point and all five five-point graph/operator pairs;
- membership with coefficient one in the appropriate full \(W\) expansion;
- all four and five cyclic scaffold references;
- exact graph permutations and augmentation invariance;
- raw, distinct, and residual operator-support counts;
- every omitted-even-pair/final-action choice;
- the low-point matrix-identifiability bounds.

## Sources

- [Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*](https://arxiv.org/html/2505.17179)
- [Dong, Su, and Yang, *On differential operators for scalar-scaffolded
  gluons*, v2](https://arxiv.org/html/2512.15882v2)
- [Arkani-Hamed et al., *Scalar-Scaffolded Gluons and the Combinatorial Origins
  of Yang--Mills Theory*, v3](https://arxiv.org/html/2401.00041v3)
- Entries 08, 11, 13, 36, and 40 of this ledger.
