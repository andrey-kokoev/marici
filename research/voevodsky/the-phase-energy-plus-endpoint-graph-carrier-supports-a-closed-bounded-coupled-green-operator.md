# The phase-energy plus endpoint-graph carrier supports a closed bounded coupled Green operator

## Augmented carrier

Use the source-reached direct sum

\[
\mathscr K_S
=
\mathscr E_S
\oplus
\mathscr H_{end,S},
\]

where:

- \(\mathscr E_S\) is the local phase-energy completion on which the normalized
  Tate multiplier \(\mathcal A_S\) is bounded self-adjoint;
- \(\mathscr H_{end,S}\) is the completed second-order endpoint graph carrying
  the bounded endpoint trace \(\Gamma_S\).

This augmentation is forced by the vertical endpoint sequence; the endpoint
sector cannot be absorbed into the unaugmented Plancherel bulk.

## Coupling

Let

\[
B_S:\mathscr E_S\to\mathscr H_{end,S}
\]

be the source Green-trace coupling on the common source-generated core. If it
extends boundedly in the augmented norms, define

\[
\mathbb G_S
=
\begin{pmatrix}
\mathcal A_S&B_S^*\\
B_S&J_{end}
\end{pmatrix},
\qquad
J_{end}=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

on \(\mathscr K_S\).

Because all four blocks are bounded and the off-diagonal blocks are adjoints,
\(\mathbb G_S\) is bounded self-adjoint. Its form is therefore closed on the
entire augmented carrier.

## Source construction of the coupling

On the second-order relative graph, endpoint value and flux traces are bounded.
The Green boundary expression

\[
\omega((M,J),(\widetilde M,\widetilde J))
=J\widetilde M-M\widetilde J
\]

is consequently bounded. Pulling this expression back through the Volterra
source map and the phase-energy embedding gives the candidate \(B_S\). Proving
that these two pullbacks agree on their common source core is the remaining
mixed Green identification; once equality is known, bounded extension is
unique.

## Canonical positive majorant

Although \(\mathbb G_S\) need not be positive, bounded self-adjoint functional
calculus supplies the canonical positive Gram

\[
|\mathbb G_S|
\]

and the two polarity legs

\[
(\mathbb G_S)_+^{1/2},
\qquad
(\mathbb G_S)_-^{1/2}.
\]

This is packet-independent and closed. It does not prove Weil positivity,
because the negative leg may be nonzero. It does place bulk, Green coupling,
and completed endpoints inside one legitimate operator rather than in separate
formal sectors.

## Positive rung-four criterion on the augmented carrier

After endpoint parity diagonalization, positivity reduces to the genuine block
Schur conditions. If the even endpoint line is retained positively and the odd
line is eliminated, the remaining condition is

\[
B_{odd,S}^*B_{odd,S}
\preceq
\mathsf B_{aug,S},
\]

where \(\mathsf B_{aug,S}\) is the positive bulk-plus-even-endpoint block.
Unlike the rejected unaugmented inequality, both sides are now continuous in
the same graph topology.

## Advance

The augmented carrier removes the topological obstruction and constructs a
closed coupled operator conditional only on equality of the two source
Green-trace pullbacks. It does not settle the final positivity inequality.
