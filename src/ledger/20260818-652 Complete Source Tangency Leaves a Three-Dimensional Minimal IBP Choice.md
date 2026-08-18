---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 652 — Complete Source Tangency Leaves a Three-Dimensional Minimal IBP Choice

## Hard-to-vary claim

The logarithmic syzygy condition of Entry 651 makes source IBP primitives
legal at the physical Cayley--Menger boundary, but it does not select a
unique primitive after all five poles of the frozen source form are retained.

## Frozen divisor

On the (q_{\mathcal G_{12}})-residue surface, freeze

\[
D=V(K_E)\cup V(q_{g1}q_{g2}q_{g3}q_{g23}q_{g31}).
\]

For a polynomial vector field

\[
V=P(a,b)\partial_a+R(a,b)\partial_b,
\]

the source-admissible fixed-pole conditions are

\[
V(K_E)=n_0K_E,
\qquad
V(q_i)=\lambda_iq_i
\quad(i=g1,g2,g3,g23,g31).
\]

The second set is necessary: tangency only to the three shared walls can
differentiate the occurrence denominators into unretained double poles.

## Exact finite-field census

The simultaneous linear syzygy system was solved coefficientwise over

\[
\mathbb F_{2305843009213693951}
\]

at two exact generic fibers,

\[
(x,y,z)=(2,3,4),\qquad(3,5,7).
\]

Both fibers give the same result. For the three shared walls alone, the
first nonzero logarithmic vector field occurs at polynomial degree five and
has rank one. After the two occurrence walls are restored, all degrees
through six vanish and degree seven has rank three:

\[
\boxed{
\dim \operatorname{Der}_{\le7}
 \bigl(-\log(K_Eq_{g1}q_{g2}q_{g3}q_{g23}q_{g31})\bigr)=3.
}
\]

At degree seven none of these three vectors is divisible componentwise by
the complete five-wall product. They are therefore wall-active; this is not
the trivial family obtained by multiplying a (K_E)-logarithmic vector by
all five wall equations.

The next dimensions are also stable across the two fibers:

\[
\begin{array}{c|rrrr}
d&7&8&9&10\\ \hline
\dim\operatorname{Der}_{\le d}(-\log D)&3&11&22&35\\
\dim(\text{wall-product divisible})&0&1&5&12.
\end{array}
\]

## Interpretation

Entry 651 corrected the existence question: physical source syzygies have
vanishing generic Cayley--Menger boundary flux. This census answers a
different question. The defining source conditions leave a
three-dimensional minimal choice before any normalization or relative
cohomology reduction.

Therefore

\[
\boxed{
\text{logarithmic tangency alone does not base the Entry 650 lift torsor.}
}
\]

This does not prove that all three choices remain distinct in
(\mathcal T_7). A source-defined IBP ordering, degree convention, or
relative-exact quotient may still identify them or select one combination.
No such selection has yet been derived.

## Classification

- existing carrier: (K_E=0) and the five frozen marked walls;
- coefficient/chain data: the three-dimensional minimal logarithmic
  derivation space;
- new carrier datum: none.

## Next falsifier

Compute the boundary-residue map from the three degree-seven generators to
the three-wall relative cocycle module and then quotient by relative-exact
primitives. The decisive rank is

\[
\operatorname{rank}
\left(
\operatorname{Der}^{(7)}(-\log D)
\longrightarrow
H^1(W_{123})(-1)
\right).
\]

Rank zero rejects source syzygies as a lift mechanism. Rank one may provide
a canonical line after source normalization. Rank greater than one leaves a
genuine primitive ambiguity requiring additional source data.

## Evidence

- `research/benincasa/check_shared_wall_log_syzygy.rs`;
- `research/benincasa/shared-wall-log-syzygy-census.json`;
- epistemic event `ev-000000000251-a0bf51b3-bddb-4896-83d7-1a729147bb4c`;
- Entries 648--651.

## Outcome contract

~~~json
{
  "claim": "The complete source logarithmic conditions select a unique minimal IBP primitive.",
  "status": "falsified",
  "generic_fibers": [[2, 3, 4], [3, 5, 7]],
  "complete_five_minimal_degree": 7,
  "complete_five_minimal_rank": 3,
  "minimal_wall_product_divisible_rank": 0,
  "canonical_T7_lift": "not established",
  "next_experiment": "Compute the relative boundary-residue rank of the three minimal generators."
}
~~~
