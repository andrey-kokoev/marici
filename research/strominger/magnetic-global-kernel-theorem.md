# Global combinatorial classification of the magnetic kernel

This packet joins the component, initialization, transfer, and boundary
lemmas.  Its scope is purely the exponent-lattice operator with a full target
lattice.  It uses no potentials, residues, logarithms, or physical
interpretation.

## The theorem

Let `g>=2`, let the admitted even pole depths be

\[
A_k=\{0,2,\ldots,2k\},
\]

and impose arbitrary finite source Laurent cutoffs while retaining every
target row.  Then every kernel vector is the restriction of one of the
following classes whose complete support is admitted:

\[
D_{g,a}=z^{-a}\bar z^{-(g+a-1)},\qquad a\in A_k,
\]

and, only at grade two,

\[
E_1=1-\bar z^{-2},
\qquad
E_2=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}.
\]

The second exceptional class requires `k>=3`.  No source truncation creates
a new class, since restricting the source merely deletes columns of a fixed
map into the full target lattice.

For automatically sufficient cutoffs this gives

\[
\boxed{
\dim\ker M_g=k+1+\epsilon(g,k),
}
\]

where

\[
\epsilon(2,k)=1+\mathbf 1_{k\ge3},
\qquad
\epsilon(g,k)=0\quad(g\ge3).
\]

The minimal lower cutoff that displays every tower is

\[
m_{\min}\le-(g+2k-1).
\]

## Why the classification is unbounded

The lattice reflection label

\[
q=|a+m-(1-g)|
\]

splits the matrix into independent components.  The fixed component `q=0`
consists of zero columns by antisymmetry and gives exactly the towers.

For `q>0`, initialization and continuation separate.

1. `q=1` is covered by its symbolic transfer theorem; its unique singular
   initialization is `(g,q)=(2,1)`, giving `E_1`.
2. In the high-grade cone `g>=q>1`, the initialization determinant is a
   nonzero endpoint product for arbitrary `g,q`.
3. In the low-grade cone `q>g`, put `d=q-g`.  The adjacent stratum `d=1` has
   endpoint determinant
   \[
   -g(g+3)(2g-1)g!(g+3)!/3,
   \]
   hence is always injective.  For even `d`, the apparent zero `d=g+8` is a
   preferred-chart boundary repaired by the transverse row.  For odd `d>=3`,
   the residual determinant can vanish only at `(g,d)=(2,5)`, by the proved
   Diophantine lemma; this is `(g,q)=(2,7)` and gives `E_2`.
4. The growing low-grade plus tail is triangular in two charts.  Its
   collision reconstruction uses only depths left of the collision, while
   boundary-visible tail columns lie strictly to the right.  Thus
   \[
   CA^{-1}B=0,
   \]
   so the fixed local collision block is the literal Schur complement.
5. The symbolic odd/even stable pivots extend every nonsingular
   initialization block to arbitrary pole cutoff.  Their factors do not
   vanish in the stable domain, so no late relation can be born.

Thus every nonzero component is injective except the two stated grade-two
components.  The distinction between mechanisms is exact: towers are zero
columns on the reflection-fixed locus, whereas `E_1,E_2` are primitive
circuits among nonzero columns.

## Boundary classification

With a full target lattice there are only visibility effects:

- a tower is absent if its single source vertex is outside the cutoff;
- `E_1` or `E_2` is absent if any vertex in its support is outside;
- moving either source boundary outward can reveal a listed class but cannot
  create any other dependence;
- target truncation is a different operator and is not covered here.

The theorem therefore classifies interior classes and both source-boundary
visibility effects for arbitrary grade, pole-depth cutoff, and Laurent
cutoff.

## Proof dependencies

The symbolic ingredients are recorded in:

- `magnetic-lattice-classification.md`;
- `magnetic-q1-transfer-theorem.md`;
- `magnetic-high-grade-base.md`;
- `magnetic-low-grade-core.md`;
- `magnetic-odd-core-diophantine.md`;
- `magnetic-plus-chain-triangular.md`;
- `magnetic-plus-boundary-compatibility.md`;
- `magnetic-even-pivot-symbolic.md` and `magnetic-schur-normal-form.md`.

The bounded checkers are falsification audits of the symbolic identities, not
the source of the arbitrary-parameter quantifiers.
