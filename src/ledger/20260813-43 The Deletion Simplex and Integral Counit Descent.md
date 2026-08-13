# The Deletion Simplex and Integral Counit Descent

## Record

Date: 2026-08-13

Status: all-arity field-theory algebra proved from scaffold polarization
multilinearity and commutativity of constant-coordinate derivatives. The
Backus--Figueiredo pair theorem identifies its complete one-skeleton at the
last two deletion grades. This supplies integral, coherent descent of the
scalar counit. Compatibility with a physical factorization Cut is reduced to
a one-bridge comparison problem but is not yet fully proved.

Reproducible certificate:

```text
research/nima/check_transmutation_counit_all_arity.rs
```

## The larger object behind the complete graph

Entry 42 found pairwise trace operators \(U_{ef}\) indexed by the edges of
\(K_n\). The complete graph is not the whole geometry. It is the one-skeleton
of a canonical \((n-1)\)-simplex whose faces record which even scaffold labels
have not yet been deleted.

For every subset \(K\subseteq E_n\), define

\[
\mathcal A_n(K)
=
\left(
\prod_{g\in E_n\setminus K}\mathcal W_g
\right)
A_n^{\rm YM}.
\]

Thus \(K\) is the set of retained even labels. If \(e\in K\), deletion of
\(e\) is the face map

\[
d_e:\mathcal A_n(K)\longrightarrow\mathcal A_n(K\setminus\{e\}),
\qquad
d_e=\mathcal W_e.
\]

Because the \(\mathcal W_e\) are constant-coordinate differential operators,

\[
\mathcal W_e\mathcal W_f
=
\mathcal W_f\mathcal W_e.
\]

Because every term in the scaffold amplitude contains a given even label in
at most one \(X\)-coordinate,

\[
\mathcal W_e^2\mathcal A_n(K)=0.
\]

The same statement holds after any other deletions. The operations therefore
act through the square-free commutative deletion algebra

\[
\Bbbk[w_e:e\in E_n]/(w_e^2).
\]

Its basis is the Boolean lattice of subsets of \(E_n\).

## Alternating totalization

Choose the cyclic order on \(E_n\). For

\[
K=\{e_0<e_1<\cdots<e_k\},
\]

define the oriented boundary

\[
\partial_K
=
\sum_{i=0}^{k}(-1)^i\mathcal W_{e_i}.
\]

More explicitly, its \(i\)-th term lands in the copy indexed by
\(K\setminus\{e_i\}\). Commutativity gives pairwise cancellation:

\[
\partial^2=0.
\]

For every pair \(i<j\), deleting \(e_i\) and then \(e_j\) occurs with the
opposite sign from deleting \(e_j\) and then \(e_i\). This is an exact
Koszul/semi-simplicial identity; it does not depend on an amplitude formula.

The Rust certificate enumerates every face and verifies \(\partial^2=0\)
through twelve even labels. The enumeration is a bounded audit of the sign
convention; the proof is all-arity.

## The final two deletion grades

Let

\[
S_n=A_n^{\operatorname{Tr}\phi^3}.
\]

The Backus--Figueiredo theorem identifies every retained edge and vertex:

\[
\mathcal A_n(\{e,f\})
=
X_{e,f}S_n,
\]

\[
\mathcal A_n(\{e\})
=
S_n,
\]

and

\[
\mathcal A_n(\varnothing)=0.
\]

The two faces of every retained edge agree after forgetting their formal
vertex labels:

\[
\mathcal W_e\mathcal A_n(\{e,f\})
=
\mathcal W_f\mathcal A_n(\{e,f\})
=
S_n.
\]

With orientations retained, the edge boundary is

\[
\partial\bigl(X_{e,f}S_n[ef]\bigr)
=
S_n[f]-S_n[e].
\]

The boundaries of the edges of \(K_n\) span all differences among the
\(n\) formal vertex copies. Since \(K_n\) is connected,

\[
H_0(\text{final deletion complex})
\cong
\Bbbk\cdot S_n.
\]

This gives an integral formulation of reference independence. No average and
no division by \(n\) are required. The cyclic and complete-graph averages of
entry 42 are convenient representatives of the same descent class, not the
mechanism that creates it.

## Higher coherence

For three retained labels \(e,f,h\), the object

\[
\mathcal A_n(\{e,f,h\})
=
\prod_{g\notin\{e,f,h\}}\mathcal W_g A_n^{\rm YM}
\]

is a canonical triangular filler whose three faces are the pair objects

\[
X_{e,f}S_n,
\qquad
X_{e,h}S_n,
\qquad
X_{f,h}S_n.
\]

Four retained labels supply tetrahedral coherence, and so on. Their explicit
functions need not be reconstructed to prove coherence: they already exist as
successive actions of commuting \(\mathcal W\)-operators. The alternating
face identities ensure that all reference-change paths agree up to the next
specified filler.

Thus the correct statement is stronger than pairwise equality:

> Scalar transmutation is the degree-zero descent of a complete
> semi-simplicial deletion object carried by the scaffolded Yang--Mills
> amplitude.

This is the natural home of the “no curvature” observed in bounded reference
checks. Flatness is expected here: it is enforced by the commuting face maps.
Nonzero curvature could only appear when this deletion object is compared with
another operation, such as a physical Cut, a normal jet, or modular sewing.

## Relation to the pairwise trace and DSY operators

On a retained edge, the derivative

\[
\partial_{X_{e,f}}
\]

contracts the edge coefficient:

\[
\partial_{X_{e,f}}\mathcal A_n(\{e,f\})=S_n.
\]

Entry 42 showed that even-label multilinearity reduces this contraction to the
universal odd-target operator \(U_{ef}\). Consequently \(U_{ef}\) is a sparse
representative of either endpoint augmentation of the edge object, modulo the
annihilator of \(A_n^{\rm YM}\).

The Dong--Su--Yang cubic-diagram derivatives then refine one chosen edge into
a Catalan cellular coframe. The hierarchy is now

\[
\text{deletion simplex}
\supset
\text{pair edge}
\supset
\text{odd-target trace sector}
\supset
\text{fixed planar slice}
\supset
\text{Catalan graph coframe}.
\]

This removes the apparent tension between a fully symmetric \(W\)-operation
and reference-dependent graph extractors: the latter are coordinates on a
chosen one-simplex of a coherent symmetric object.

## What this says about Cut naturality

Output factorization is automatic:

\[
\operatorname{Res}_D(U_{ef}A_n^{\rm YM})
=
\operatorname{Res}_D S_n
=
S_LS_R.
\]

This alone does not define a coproduct on \(U_{ef}\). The scaffolded
Yang--Mills factorization formula has the schematic form

\[
\operatorname{Res}_D A_n^{\rm YM}
=
\sum_{j,J}
C_{jJ}(X)
\,\partial_{X_{x,j}}A_L^{\rm YM}
\,\partial_{X_{x',J}}A_R^{\rm YM},
\]

where \(C_{jJ}(X)\) is linear and implements the internal polarization
coevaluation.

There is nevertheless a sharp degree consequence. If the cut divides the
external gluons into \(p\) and \(q\), with \(p+q=n\), then the two lower
counits have total differential order

\[
p+q=n.
\]

The factorization formula already supplies one derivative on each lower
amplitude. The global \(U_{ef}\) has order \(n-1\). Therefore a scalar
factorized term has the required total lower order only when exactly one of
the global derivatives hits the linear kernel \(C_{jJ}\):

\[
(n-1)-1+2=n.
\]

Two derivatives cannot hit \(C_{jJ}\) because it is linear. If none hits it,
the lower factors are over-differentiated in polarization degree and vanish.

This proves a support-level **one-bridge principle**:

> Every nonzero term in the Cut of the transmutation counit contains exactly
> one derivative that contracts the internal Yang--Mills coevaluation; after
> removing that bridge, the remaining derivatives distribute across the two
> lower deletion objects.

It does not yet determine the complete signed bridge sum.

## Three edge orbits under a Cut

The channel partitions the even labels as

\[
E_n=E_L\sqcup E_R.
\]

Accordingly,

\[
E(K_n)
=
E(K_{|E_L|})
\sqcup
E(K_{|E_R|})
\sqcup
(E_L\times E_R).
\]

A chain-level Cut coaction must therefore specify three cases:

1. the retained trace edge lies entirely on the left;
2. it lies entirely on the right;
3. it crosses the channel.

In the crossing case, \(\partial_{X_{e,f}}\) can hit the
\(+X_{j,J}\) term of the gluing kernel. The two built-in derivatives then
become the two trace edges joining \(e\) and \(f\) to the internal scaffold
labels on the lower factors. This strongly predicts

\[
U_{ef}^{(n)}
\longmapsto
U_{e,\iota_L}^{(L)}
\otimes
U_{\iota_R,f}^{(R)}
\qquad
(e\in E_L,\ f\in E_R)
\]

modulo the lower amplitude annihilators.

For a same-side edge, the unique bridge must instead come from one of the
odd-target \(B_g\) derivatives. Its contraction converts a built-in internal
derivative into the trace edge of the opposite factor. Gauge identities can
move this bridge among several coordinate representatives, so a canonical
formula cannot be asserted without an explicit comparison calculation.

## Current verdict

The deletion simplex is a genuine enlargement of the emerging operation
algebra:

\[
\boxed{
\text{commuting square-zero deletions}
\longrightarrow
\text{semi-simplicial descent}
\longrightarrow
\text{scalar transmutation counit}.
}
\]

It explains all-arity reference independence and supplies every higher
reference-change coherence. It does not by itself prove physical-Cut
naturality. That comparison introduces one new ingredient: contraction of the
internal polarization coevaluation.

This is structurally consistent with the broader Marici picture. A theory-
producing operation is not only a map on final amplitudes; it is a map of the
appropriate compositional objects. Here the underlying object is now visible,
and the missing datum has been reduced to one bridge map.

## Next executable test

At the first nontrivial five-point channel, expand the published scaffolded
factorization formula and sort every surviving \(U_{ef}\) term by:

- left edge;
- right edge;
- crossing edge;
- which unique derivative hits \(C_{jJ}\).

Then test whether the signed bridge sum equals the tensor product of the lower
three- and four-point counits modulo their annihilator ideals. A failure only
in the same-side edge orbits would identify the precise gauge-homotopy term
needed for a chain-level coaction.

## Primary sources

- Backus and Figueiredo, *Surface Gauge Invariance, Soft Limits and the
  Transmutation of Gluons into Scalars*, arXiv:2505.17179, sections 6--8:
  <https://arxiv.org/abs/2505.17179>.
- Dong, Su, and Yang, *On differential operators for scalar-scaffolded
  gluons*, arXiv:2512.15882v2, especially equations (2.16)--(2.24) and section
  3: <https://arxiv.org/abs/2512.15882>.

