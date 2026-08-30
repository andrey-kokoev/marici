# Balanced fourth-order coupling gate

## Question

WP983 specializes the WP982 balance condition to the natural same-coupling
mass pattern

\[
a=A g,qquad b=B g^2,qquad c=C g^2.
\]

If \(\gamma=\Gamma g^s\), then

\[
E=2s+4-2-10=2s-8.
\]

The unique balanced exponent is therefore

\[
s=4.
\]

Thus a one-coupling completion can remove the live \(g\)-fiber only if the
quartic mediator coefficient is generated at fourth order in that coupling.

## Magnitude gate

After balance,

\[
\widehat\rho=\frac{\Gamma^2A^4}{BC^5}.
\]

For unit normalized coefficients this equals \(1\). Retaining the WP977
choice \(\Gamma=8\) with \(A=B=C=1\) gives \(64\). Both lie below the
WP978 crossing \(24696\).

If \(A=B=C=1\) and \(\Gamma\) is restricted to a positive integer source
multiplicity, the strict crossing condition is

\[
\Gamma^2>24696.
\]

The smallest admissible integer is \(158\), because

\[
157^2=24649<24696<24964=158^2.
\]

## Interpretation

Fourth-order generation is an exponent rigidifier, not a numerical selector.
It removes dependence on the common coupling but transfers the entire burden
to the independently derived normalized prefactor. A large multiplicity,
group factor, threshold enhancement, or non-unit normalized coefficient could
cross the boundary, but none is supplied by the current source grammar.

This packet does not identify \(s=4\) with a specific loop order or claim
perturbative realizability. Such a physical interpretation requires an
explicit mediator model, its matching calculation, and uncertainty control.

The smallest falsifier is an admitted source calculation deriving
\(s=4\) and a prefactor strictly above \(24696\), followed by the coupled
vacuum and instrument checks.

## Reproduction

Run:

    python research/flavor/checkers/wp983_balanced_fourth_order_coupling_gate.py

The generated result is
research/flavor/results/wp983_balanced_fourth_order_coupling_gate.json.
