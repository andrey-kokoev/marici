# Radiative exit-Higgs portal: WP686

## Shared fermion endpoint

The ordinary quark Yukawa and messenger exit Yukawa share the right-handed
quark:

\[
q_L\mathbin{-}H\mathbin{-}q_R,
\qquad
B_L\mathbin{-}X\mathbin{-}q_R.
\]

On the corresponding two-state fermion block,

\[
M=\begin{pmatrix}
y_qh&0\\
y_Xx&M_B
\end{pmatrix}.
\]

The one-loop fermion invariant contains

\[
\operatorname{Tr}[(MM^\dagger)^2]
\supset 2y_q^2y_X^2h^2x^2
\]

per color. Therefore the quadratic portal from WP684 is required as a
counterterm whenever (y_qy_X\neq0).

## What is selected

The zero-portal truncation is not RG invariant. The admitted source vertices
radiatively generate portal support, so inclusion of the operator is no longer
optional in the quantum source grammar.

This does not select a numerical (lambda_p). A renormalized boundary value
can cancel the running contribution at one chosen scale, and finite threshold
terms remain scheme dependent until matched. The durable result is operator
support and radiative rigidification, not a flavor value.

## Remaining gate

The full one-scheme beta coefficient, orientation-dependent scalar invariants,
and finite messenger threshold must be derived together. Only then can one ask
whether the portal is bounded away from zero at an experimental scale with
uncertainties.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp686_radiative_exit_higgs_portal.py

Generated result: results/wp686_radiative_exit_higgs_portal.json.
