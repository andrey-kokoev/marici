# Two-matrix mixed-quartic grammar: WP732

## Question

Which mixed quartics must accompany the simultaneous singlet–triplet scalar
source, and can a source symmetry retain a relation between the two Yukawa
sectors while keeping WP731's radial norm truncation closed?

## Two symmetry choices

Let (A=S_A) and (B=S_B) be complex three-by-three matrix scalars.

Under independent chiral flavor groups,

\[
A\mapsto L_AAR_A^\dagger,
\qquad
B\mapsto L_BBR_B^\dagger,
\]

the only degree-four mixed invariant is the product of norms

\[
I_1=\operatorname{Tr}(A^\dagger A)
\operatorname{Tr}(B^\dagger B).
\]

This makes WP731's mixed radial grammar complete. It also leaves no flavor
intertwiner relating the two Yukawa tensors or their products. An equality
such as (q_A=q_B) is then an additional source assertion, not a consequence
of the independent flavor symmetry.

To relate the two Yukawa sectors, introduce a common biunitary flavor frame,

\[
A\mapsto LAR^\dagger,
\qquad
B\mapsto LBR^\dagger.
\]

Retain independent sector (Z_3) gradings. These allow each determinant
cubic while forbidding quadratic scalar mixing and quartics with unequal
numbers of a field and its conjugate. The balanced mixed degree-four invariant
space then has four generators:

\[
\begin{aligned}
I_1&=\operatorname{Tr}(A^\dagger A)
     \operatorname{Tr}(B^\dagger B),\\
I_2&=\operatorname{Tr}(A^\dagger B)
     \operatorname{Tr}(B^\dagger A),\\
I_3&=\operatorname{Tr}(A^\dagger A B^\dagger B),\\
I_4&=\operatorname{Tr}(AA^\dagger BB^\dagger).
\end{aligned}
\]

They arise from the four left/right index-contraction pairings for one copy of
each of (A,B,A^\dagger,B^\dagger).

## Exact independence

Let (E_{ij}) denote the three-by-three matrix unit. At (A=E_{11}), evaluate
the invariants on

\[
B\in\{E_{22},E_{12},E_{21},E_{11}\}.
\]

The evaluation matrix is

\[
\begin{pmatrix}
1&0&0&0\\
1&0&0&1\\
1&0&1&0\\
1&1&1&1
\end{pmatrix},
\]

whose determinant is (-1). Hence the four invariants are exactly linearly
independent already on real matrices.

On the radial identity slice (A=xI_3,B=yI_3), however,

\[
(I_1,I_2,I_3,I_4)
=x^2y^2(9,9,3,3).
\]

The slice collapses the four-dimensional coupling space to one readout. A
radial fixed-point calculation therefore cannot certify the tensor stability
matrix or exclude relevant directions in the three hidden mixed channels.

## Source-symmetry tradeoff

The checker verifies that all four invariants are unchanged under a common
left/right transformation. It also gives independent left and right
transformations of (A) alone that leave (I_1) fixed while changing
(I_2,I_3,I_4). Thus the alternatives are exact:

- independent flavor groups retain only (I_1), but supply no common flavor
  intertwiner fixing the Yukawa-product relation;
- a common flavor frame can support such an intertwiner, but enlarges the
  mixed scalar grammar from one to four couplings.

Spurion intertwiners produced by the common Standard Model lepton channel have
the same effect: once admitted, they must be included when testing which mixed
tensor counterterms are generated.

## Disposition

WP732 rules out using the radial direct-sum system as the completed RG source
whenever a common flavor intertwiner is invoked to repair WP729's Yukawa
cancellation fiber. The smallest exact falsifier is the determinant-(-1)
evaluation matrix: three independent mixed tensor directions are invisible on
the radial identity slice.

The next constructive choice is now explicit. Either derive the Yukawa-product
relation from a source structure that preserves independent flavor groups, or
admit the common frame and compute the beta functions for all four mixed
quartics. No authority exists to impose the relation while retaining only
(I_1).

Reproduce with: `uv run --with sympy python research/flavor/checkers/wp732_two_matrix_mixed_quartic_grammar.py`

Generated result: `results/wp732_two_matrix_mixed_quartic_grammar.json`.
