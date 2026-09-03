# Relative logarithmic Gårding remainder criterion

## Question

Is absolute boundedness of the interval boundary remainder necessary, or can a strict relative logarithmic bound still preserve the signed tail?

## Claim boundary

This packet weakens the prior bounded-remainder criterion to a strict relative-form estimate. It does not prove that the Weil boundary remainder satisfies that estimate.

## Relative criterion

Let

\[
g_L(f)=\langle f,\log(1+D_L)f\rangle,
\qquad D_L=\sqrt{-\Delta_D}.
\]

Write \(\Gamma_L=g_L+k_L\). Assume

\[
|k_L(f,f)|\le\eta g_L(f)+C_L\lVert f\rVert^2
\]

with \(0\le\eta<1\). On the complement of the first \(M\) Dirichlet modes,

\[
\Gamma_L(f,f)
\ge
\left[(1-\eta)
\log\left(1+\frac{\pi(M+1)}{2L}\right)-C_L\right]
\lVert f\rVert^2.
\]

After subtracting a prime-sector bound \(C_{\rm prime}(L)\), the tail is nonnegative once

\[
(1-\eta)
\log\left(1+\frac{\pi(M+1)}{2L}\right)
\ge C_L+C_{\rm prime}(L).
\]

Thus a boundary remainder may grow logarithmically, provided its relative coefficient remains strictly below one.

## Boundary case

At \(\eta=1\), the logarithmic reserve disappears. A remainder \(k_L=-g_L\) satisfies the unit relative bound and cancels the principal growth exactly. Therefore strictness is necessary for this route.

## Relation to the prior criterion

The absolute bounded-remainder theorem is the special case \(\eta=0\). This packet supersedes it as the broadest sufficient condition currently established; the earlier theorem remains valid but may be unnecessarily strong for boundary pseudodifferential effects.

Finite-tail coupling still requires the independent Schur budget

\[
b_M^2\le m_Ma_M.
\]

## Disposition

The interval source gate is now a disjunction:

1. prove an absolute order-zero remainder bound, or
2. prove a strict relative logarithmic bound with \(\eta<1\).

The cheapest falsifier is a normalized high-mode sequence for which \(|k_L|/g_L\to1\) or exceeds one after lower-order subtraction.

## Verification

- `research/voevodsky/checkers/check_relative_log_garding_remainder.py`
- `research/voevodsky/results/relative_log_garding_remainder.json`
