# Generic completion-kernel comparison interface

Owner: `marici.Strominger`

## Question

What exact conditions let completion reveal an ordinary kernel without
manufacturing it?

## Interface

Start with separated topological vector spaces and a densely embedded source
core

\[
\iota_X:X\hookrightarrow\widehat X,
\qquad
\iota_Y:Y\hookrightarrow\widehat Y,
\]

an operator `A:X->Y`, and a candidate extension
`A_hat:Dom(A_hat) subset X_hat -> Y_hat`. A completion contract contains:

1. the source and completed spaces;
2. the chosen Hausdorff topology;
3. the dense embedding and its evidence;
4. the completion map and universal-property evidence;
5. the target embedding `i_Y:Y->Y_hat` and the source and extended operators;
6. one canonical extension mechanism;
7. the commuting operator square
   \[
   \widehat A\iota_X=\iota_Y A.
   \]

The admitted mechanisms are a unique bounded continuous extension, closure of
a closable graph, or the Friedrichs generator of a closed nonnegative form.
Merely completing `X` does not choose `A_hat`.

## Comparison theorem

Assume:

- `i_X` and `i_Y` are injective and `i_X(X)` is dense;
- `A_hat` is the unique extension supplied by one of the declared canonical
  mechanisms;
- the operator square commutes;
- each proposed completion-only zero mode is represented by a graph-limit
  sequence `i_X x_n -> x_hat` with `i_Y A x_n -> 0`;
- any claimed derived obstruction is separately represented by an evidenced
  `Tor` object.

Then restriction of the operator square gives a canonical comparison

\[
\begin{CD}
\ker A @>{\ker\iota_X}>> \ker\widehat A\\
@VVV @VVV\\
X @>{\iota_X}>> \widehat X .
\end{CD}
\]

Its image consists of the classes that descend from `X`. The ordinary new
kernel is the quotient

\[
K_{\mathrm{new}}
=\ker\widehat A/\operatorname{im}(\ker\iota_X).
\]

This quotient is not a completion defect. A derived completion obstruction is
a different typed object, present only when a failure of exactness produces a
nonzero evidenced Tor grade. Thus the completed kernel partitions into:

\[
\dim\ker\widehat A
=d_{\mathrm{descends}}+d_{\mathrm{completion\ only}}
 +d_{\mathrm{derived\ obstruction}}.
\]

Completion does not manufacture the ordinary new classes because both the
extended operator and the graph-limit test are fixed independently of the
desired kernel. If extension uniqueness, square commutativity, or graph-limit
evidence is missing, the classification is unauthorized.

## Finite linear observation fiber

For a finite-dimensional kernel `K`, an observation fiber declares available
ports `ell_i`, their exact matrix

\[
O:K\longrightarrow F^r,
\qquad x\mapsto(\ell_1x,\ldots,\ell_rx),
\]

and independent execution authority for every port. Faithfulness is
`rank(O)=dim(K)`. Minimality is stronger: deleting every individual row lowers
the rank below `dim(K)`.

Consequences:

- the number of ports need not equal the kernel dimension; redundant faithful
  families exist;
- an unavailable port is absent from `O`, while an available port may evaluate
  to zero on a particular state;
- shared geometric support does not authorize port execution.

## Magnetic application

For finite signed atomic spin-two measures completed weak-star to finite Radon
measures, distributional differentiation gives the continuous extension

\[
\widehat{\mathcal A}_3:
\mathcal M(S^2)_{\sigma(\mathcal M,C^0)}
\longrightarrow
\mathcal D'(S^2)_{\sigma(\mathcal D',C^\infty)}.
\]

The finite-atomic kernel is zero: a distributional zero of the elliptic paired
operator is smooth, while a finite atomic measure cannot be a nonzero smooth
section. In the completed Radon space elliptic regularity and the exact
harmonic multiplier give

\[
\ker\widehat{\mathcal A}_3
=\mathcal H_2\oplus\mathcal H_3\oplus\mathcal H_4,
\qquad
\dim=5+7+9=21.
\]

All three harmonic blocks are completion-only ordinary kernel classes with
zero derived-defect dimension. The 21 low-harmonic projections have identity
observation matrix. Every one-port deletion has rank 20, so this family is
faithful and deletion-minimal. The local characteristic locus `p^4-q^4=0`
remains a separate support object.

## Grothendieck test packet

For the positive completed theta density, take the dense core
`C_c^infinity(R)` in

\[
\mathcal H_\Phi=L^2(\mathbb R,Z^{-1}\Phi\,du).
\]

The nonnegative Dirichlet form has the canonical Friedrichs generator

\[
A_\Phi=-\Phi^{-1}(\Phi f')'.
\]

The constant ground mode is absent from the compactly supported core and is a
one-dimensional completion-only ordinary kernel class. Compact resolvent
authorizes the finite spectral projections `E_N`, retaining complete
eigenspaces and converging strongly to the identity. This is a reusable source
compression packet only. It makes no claim about an RH-bearing Fredholm
kernel.

## Evidence

- Sector-neutral schema:
  `contracts/generic-completion-interface.v1.schema.json`.
- Generic validator: `generic_completion_interface.py`.
- Magnetic contract: `contracts/magnetic-generic-completion.v1.json`.
- Three-way classification fixture:
  `contracts/generic-completion-classification-fixture.v1.json`.
- Theta test packet:
  `contracts/grothendieck-theta-completion-test.v1.json`.
- Checker: `checkers/generic_completion_interface_checks.py`.
- Results: `results/generic_completion_interface.json`.
