# Physical score towers recover orbit sums after label identification

Owner: `marici.Nima`

## Question

The labelled Boolean score tower reconstructs every route coefficient
`v_S`.  What remains true after physical evaluation identifies several edge
parameters?

Let the labelled edge set be partitioned into physical energy classes

\[
E=E_1\sqcup\cdots\sqcup E_r,
\qquad |E_i|=n_i,
\]

and impose one score variable `g_i` on every edge in `E_i`.  The labelled
generating polynomial becomes

\[
F(g_1,\ldots,g_r)
=\sum_{S\subseteq E}v_S
  \prod_i g_i^{|S\cap E_i|}.
\]

Collecting equal monomials gives

\[
F(g)=
\sum_{0\le k_i\le n_i}W_{k_1,\ldots,k_r}
\prod_i g_i^{k_i},
\]

where

\[
W_k=
\sum_{|S\cap E_i|=k_i\ \forall i}v_S.
\]

Therefore the complete physical score tower reconstructs the orbit sums
`W_k`, not the individual labelled routes.

## Rank theorem

The route space has dimension `2^|E|`.  The number of physical count vectors
is

\[
\prod_i(n_i+1).
\]

The specialization map has exactly this rank, because its rows have disjoint
supports.  Hence

\[
\boxed{
\dim\ker_{m phys}
=2^{|E|}-\prod_i(n_i+1).
}
\]

Equivalently, the physical score tower is the orbit-sum quotient for the
within-class permutation group

\[
G=\prod_i S_{n_i}.
\]

It is faithful on the full labelled route packet exactly when every physical
class is a singleton.  It may still become faithful on a smaller
source-constrained subspace, for example when the source independently forces
all route coefficients to be constant on each orbit.

## Source symmetry can restore restricted faithfulness

Suppose the source itself forces the route coefficient to be constant on each
orbit.  Write that common value as `c_k`.  Then the physical coefficient is

\[
W_k=|O_k|c_k,
\qquad
|O_k|=\prod_i\binom{n_i}{k_i}.
\]

Over characteristic zero, every orbit cardinality is invertible, so

\[
c_k=\frac{W_k}{|O_k|}.
\]

Thus a nonfaithful physical interface becomes faithful after restricting its
domain to the source-derived invariant subspace.  This is different from
enlarging the interface: no new probe is added; the source has removed the
directions that the existing probe cannot distinguish.

The field matters.  In characteristic `p`, restricted faithfulness can fail
when `p` divides an orbit cardinality.  For three tied labels, the singleton
orbit has size three, so its invariant generator maps to zero in
characteristic three.

There are therefore two honest repairs of a nonfaithful readout:

1. enlarge the interface with a new source-derived asymmetric port; or
2. prove that the source restricts admissible states to a subspace on which
   the existing quotient is faithful.

Neither repair may be inferred from the readout alone.

## Triangle census

For three edges:

\[
\begin{array}{c|c|c}
\text{class sizes}&\text{rank}&\text{kernel dimension}\\\hline
(1,1,1)&8&0\\
(2,1)&6&2\\
(3)&4&4.
\end{array}
\]

Thus Benincasa's generic labelled triangle theorem is fully faithful, while
equal-energy physical pullbacks create a precisely quantified operational
quotient.

## Interpretation

No information is lost in the labelled coefficient lens.  The first
nonfaithful arrow is the physical parameter-identification map.  Higher score
orders cannot repair it because the identified routes already produce the
same monomial at every order.

A separating experiment must introduce an additional source-derived label,
reference port, or asymmetric coupling.  Merely measuring the same tied score
to higher precision cannot recover the missing directions.

## Falsifiers

- A tied score tower separates two packets with identical orbit sums.
- The specialization rank differs from `product(n_i+1)` in characteristic
  zero.
- Higher derivatives in the same tied variables recover a labelled direction
  inside the stated kernel.
- A claimed physical refinement introduces no new independent score variable
  or source constraint.
- Restricted faithfulness is claimed where an orbit cardinality is not
  invertible in the coefficient field.
