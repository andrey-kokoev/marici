# Pairwise Trace Sectors and the Cyclic Transmutation Counit

## Record

Date: 2026-08-13

Status: all-arity tree-level field-theory theorem, conditional only on two
published scalar-scaffold inputs: the Backus--Figueiredo pair-transmutation
theorem and even-label multilinearity of the canonical scaffolded Yang--Mills
amplitude. The support identities were independently enumerated through seven
points. The relation to the complete Dong--Su--Yang graph coframe is verified at
four and five points but remains conditional at general multiplicity.

Reproducible certificate:

```text
research/nima/check_transmutation_counit_all_arity.rs
```

## Result

The amplitude-level lowering operation has a reference-free all-arity form.
It is not necessary to choose a cubic graph, a Parke--Taylor basis, or a metric
adjoint.

Let

\[
E_n=\{2,4,\ldots,2n\},
\qquad
O_n=\{1,3,\ldots,2n-1\},
\]

and write

\[
\mathcal W_e
=
\sum_{j\notin\{e,e\pm1\}}
\partial_{X_{e,j}}.
\]

For distinct \(e,f\in E_n\), define

\[
P_{ef}
=
\prod_{g\in E_n\setminus\{e,f\}}\mathcal W_g,
\qquad
V_{ef}
=
\partial_{X_{e,f}}P_{ef}.
\]

Backus and Figueiredo prove at tree level and at leading low energy that

\[
P_{ef}A_n^{\rm YM}
=
X_{e,f}A_n^{\operatorname{Tr}\phi^3}.
\]

Consequently,

\[
V_{ef}A_n^{\rm YM}
=
A_n^{\operatorname{Tr}\phi^3}.
\]

The new point is that \(V_{ef}\) has a universal, much smaller representative.
Set

\[
B_g
=
\sum_{\substack{o\in O_n\\o\notin\{g-1,g+1\}}}
\partial_{X_{g,o}},
\]

and

\[
U_{ef}
=
\partial_{X_{e,f}}
\prod_{g\in E_n\setminus\{e,f\}}B_g.
\]

Then

\[
\boxed{
U_{ef}A_n^{\rm YM}
=
A_n^{\operatorname{Tr}\phi^3}
}
\]

for every unordered pair \(\{e,f\}\subset E_n\).

Thus every edge of the complete graph on the even scaffold labels carries the
same scalar transmutation counit.

## Exact proof of the odd-target reduction

The canonical scaffold amplitude is multilinear in every gluon polarization.
In scalar variables this implies the stronger support statement used explicitly
by Dong--Su--Yang: in each term an even label occurs in at most one
\(X\)-coordinate. Equivalently, any differential monomial containing two
derivatives whose coordinates share the same even label annihilates the
amplitude.

Expand \(V_{ef}\). Suppose the \(\mathcal W_g\) factor chooses an even target
\(h\).

- If \(h=e\) or \(h=f\), that label already occurs in
  \(\partial_{X_{e,f}}\).
- If \(h\notin\{e,f\}\), then \(h\) is itself one of the sources of another
  \(\mathcal W_h\) factor.

In either case the differential monomial contains two coordinates sharing
even label \(h\), so it vanishes on \(A_n^{\rm YM}\). Every surviving choice
therefore sends every remaining even source to an allowed odd target. Those
choices are exactly the monomials in \(U_{ef}\). Hence

\[
V_{ef}-U_{ef}
\in
\operatorname{Ann}(A_n^{\rm YM}),
\]

which proves the boxed identity.

This is an amplitude-quotient statement. It does not assert equality of the
two differential operators on arbitrary functions.

## Support counts

Each \(\mathcal W_g\) has \(2n-3\) possible targets. Each restricted \(B_g\)
has \(n-2\) possible odd targets. Since \(V_{ef}\) contains \(n-2\)
\(\mathcal W\)-factors,

\[
\#\text{ raw choices in }V_{ef}
=(2n-3)^{n-2},
\]

while

\[
\boxed{
|\operatorname{supp}U_{ef}|
=(n-2)^{n-2}.
}
\]

The monomials are distinct: an even--odd coordinate remembers its unique even
source. Supports belonging to distinct pairs \(\{e,f\}\) are disjoint because
each \(U_{ef}\) monomial contains exactly one even--even coordinate, namely
\(X_{e,f}\).

The certificate enumerates every raw choice for every pair through \(n=7\),
checks the closed counts with overflow-safe arithmetic through \(n=25\), and
verifies exact covariance under rotation by two scalar labels.

## A second theorem: vertex plus incident edges

The pair sectors expose a stronger decomposition of the full
Backus--Figueiredo transmuter. For an omitted even label \(e\), define

\[
T_e
=
\prod_{g\in E_n\setminus\{e\}}\mathcal W_g,
\qquad
R_e
=
\prod_{g\in E_n\setminus\{e\}}B_g.
\]

Any multi-affinity-surviving term in \(T_e\) is of precisely one of two kinds.

1. Every source chooses an odd target. These terms comprise \(R_e\).
2. Exactly one source \(f\) chooses the only even label not already used as a
   source, namely \(e\). All other sources choose odd targets. These terms
   comprise \(U_{ef}\).

No other even target can occur, and two sources cannot both target \(e\).
Therefore

\[
\boxed{
T_e
\equiv
R_e+\sum_{f\in E_n\setminus\{e\}}U_{ef}
\pmod{\operatorname{Ann}(A_n^{\rm YM})}.
}
\]

Backus--Figueiredo transmutation gives

\[
T_eA_n^{\rm YM}=A_n^{\operatorname{Tr}\phi^3},
\]

whereas every one of the \(n-1\) incident edge operators gives the same scalar
amplitude. It follows immediately that the previously unidentified all-odd
vertex sector obeys

\[
\boxed{
R_eA_n^{\rm YM}
=
-(n-2)A_n^{\operatorname{Tr}\phi^3}.
}
\]

Its support has size

\[
|\operatorname{supp}R_e|=(n-2)^{n-1}.
\]

The complete surviving support of \(T_e\) therefore has size

\[
(n-2)^{n-1}+(n-1)(n-2)^{n-2}
=(2n-3)(n-2)^{n-2}.
\]

The Rust certificate verifies the disjoint support decomposition for every
omitted label through seven points.

## Complete-graph incidence form

Let \(Q\) be the signless vertex--edge incidence matrix of \(K_n\):

\[
Q_{e,\{a,b\}}
=
\begin{cases}
1,&e\in\{a,b\},\\
0,&e\notin\{a,b\}.
\end{cases}
\]

Collecting the operators into vectors gives

\[
T=R+QU
\qquad
\text{in }
\operatorname{Diff}/\operatorname{Ann}(A_n^{\rm YM}).
\]

The scalar augmentation has weights

\[
\epsilon(U_{ef})=1,
\qquad
\epsilon(R_e)=-(n-2),
\qquad
\epsilon(T_e)=1.
\]

Since each row of \(Q\) contains \(n-1\) ones, the incidence equation is
numerically exact:

\[
-(n-2)+(n-1)=1.
\]

This is the first nontrivial finite algebra seen directly among the lowering
operators. The reference labels do not disappear by an unexplained
cancellation; they organize into the vertices and edges of \(K_n\), while the
canonical amplitude quotient collapses every normalized representative to one
counit class.

## Manifestly cyclic representatives

Let \(e_i=2i\), with \(i\) cyclic modulo \(n\). Several reference-free
operators now follow without further amplitude input:

\[
\epsilon_n^{\rm cycle}
=
\frac1n\sum_{i=1}^{n}U_{e_i,e_{i+1}},
\]

\[
\epsilon_n^{\rm edge}
=
\frac{2}{n(n-1)}
\sum_{1\leq i<j\leq n}U_{e_i,e_j},
\]

\[
\epsilon_n^{\rm vertex}
=
-\frac{1}{n(n-2)}
\sum_{i=1}^{n}R_{e_i},
\]

and

\[
\epsilon_n^{W}
=
\frac1n\sum_{i=1}^{n}T_{e_i}.
\]

For \(n\geq3\), all four send \(A_n^{\rm YM}\) to
\(A_n^{\operatorname{Tr}\phi^3}\), are invariant under cyclic rotation, and
represent the same class in
\(\operatorname{Diff}/\operatorname{Ann}(A_n^{\rm YM})\).

The cycle representative is particularly economical: it uses the Hamiltonian
cycle selected by the planar order rather than averaging over all edges of
\(K_n\).

## Location of the Dong--Su--Yang coframe

Dong--Su--Yang conventionally fix

\[
\partial_{X_{2,2n}}
\qquad\text{and}\qquad
\partial_{X_{1,4}}.
\]

The first derivative selects the edge sector \(U_{2,2n}\). The second fixes
one odd target in that sector. The resulting fixed slice contains

\[
(n-2)^{n-3}
\]

monomials. Their graph rules select a much sparser Catalan family of size

\[
\mathcal C_{n-2}
\]

inside that slice.

The hierarchy is therefore

\[
(2n-3)^{n-2}
\longrightarrow
(n-2)^{n-2}
\longrightarrow
(n-2)^{n-3}
\longrightarrow
\mathcal C_{n-2},
\]

corresponding respectively to:

1. the raw pair transmuter;
2. its universal odd-target representative;
3. a fixed trace/reference slice;
4. the planar cubic-diagram coframe.

At four points the sizes are

\[
25\longrightarrow4\longrightarrow2\longrightarrow2,
\]

and at five points they are

\[
343\longrightarrow27\longrightarrow9\longrightarrow5.
\]

The complete published four- and five-point DSY coframes were checked
monomial by monomial to lie in the stated slice. The paper proves its general
graph rules only for specified families, so this ledger does not promote the
all-graph Catalan selection to a theorem.

## Interpretation

This changes the operator-algebra picture in three ways.

First, lowering is an augmented trace operation, not presently a metric
adjoint of the scalar-to-YM jet. Its universal primitive is the pairwise trace
sector \(U_{ef}\).

Second, cyclic-reference independence is now an all-arity theorem at amplitude
level. It does not rely on the bounded four- and five-point cancellations of
entry 41.

Third, the planar DSY graph operators are best viewed as a sparse normal form
for one edge of a larger, fully symmetric incidence object. The complete graph
is supplied by the choice of the two polarizations left for the final trace;
the planar ordering then selects a Hamiltonian cycle and a Catalan chart.

This is precisely the sort of small native grammar sought by Marici:

\[
\text{gauge first-jet object}
\xrightarrow{\text{pairwise trace counit}}
\text{scalar object},
\]

with the apparently large graph family resolving one morphism rather than
defining many unrelated operations.

## What is proved and what is not

Proved here, from the cited published inputs:

- \(U_{ef}A_n^{\rm YM}=A_n^{\operatorname{Tr}\phi^3}\) for every pair and all
  tree multiplicities;
- the exact support counts and pair-sector disjointness;
- the vertex--edge incidence decomposition of \(T_e\);
- \(R_eA_n^{\rm YM}=-(n-2)A_n^{\operatorname{Tr}\phi^3}\);
- manifestly cyclic averaged representatives and their equality in the
  canonical amplitude quotient.

Not proved:

- that every DSY cubic graph has the proposed derivative at arbitrary
  multiplicity;
- that the Catalan graph family is a canonical basis before quotienting by the
  Yang--Mills annihilator;
- that this counit is adjoint to the scalar fusion jet under an intrinsic
  gauge-sector metric;
- that \(U_{ef}\) has a canonical chain-level lift;
- that the lower-point counits obtained after a physical Cut obey the required
  tensor/coaction law.

Constant-coefficient differentiation in even-containing coordinates commutes
formally with extraction of a residue in an independent odd--odd physical
channel. This is weaker than factorization naturality: after the cut one must
still identify how the retained trace pair and all remaining even labels
distribute across the two factors.

## Next falsification target

The next sharp question is the cut coaction of the edge class.

For a physical odd--odd channel \(D\), determine whether there is a canonical
formula of the form

\[
\operatorname{Cut}_D\,U_{ef}^{(n)}
=
\sum_{\sigma}
U_{e_Lf_L}^{(L,\sigma)}
\otimes
U_{e_Rf_R}^{(R,\sigma)},
\]

where \(\sigma\) accounts for the internal polarization/trace allocation and
where the formula is compatible with the complete-graph incidence relation.

A positive result would promote the amplitude counit to a factorization
counit. A failure would locate precisely where the lowering operation requires
extra chain or state-sum data.

## Primary sources

- Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*, arXiv:2505.17179, especially equations
  (68), (108)--(109), and the all-arity low-energy proof in section 7.3:
  <https://arxiv.org/abs/2505.17179>.
- Dong, Su, and Yang, *On differential operators for scalar-scaffolded
  gluons*, arXiv:2512.15882v2, especially equations (2.16)--(2.18), section 3,
  and the stated scope of the factorization proofs:
  <https://arxiv.org/abs/2512.15882>.

