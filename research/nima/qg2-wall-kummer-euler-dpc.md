# `q_g2` wall character and Euler orientation: third conjecture cycle

## Problem

The conductor connecting formula closes the grade `-1` node only if the normalized `q_g2` wall has trivial relative Kummer character and the collision Euler factor enters with the derived negative inverse orientation.

## Bold conjecture

The exact-square wall restriction gives trivial Kummer character, and the global residue orientation fixes

\[
\delta_{\rm cond}=\frac{r_\infty}{\kappa-1}
=-\frac{r_{-1}+r_{-\kappa}}{\kappa-1}.
\]

## Named rivals

1. ambient square-root monodromy induces character `-1` on the wall conductor loop;
2. the wall pullback character is trivial but cannot be transported to the ambient physical chain;
3. the inverse-Euler sign is arbitrary rather than fixed by residue orientation.

## Risky consequences

The wall divisor must have even multiplicity, while an ambient transverse probe must distinguish whether unrestricted transport remains valid. Independently, the residue at infinity divided by the labeled Euler factor must reproduce the required sign.

## Strongest falsification attempt and residual

At `a=p` and `xi=-kappa+s`, execution `structured_command_execution:e_7396_1788303098613631700_9` gives

\[
K_{\rm exc}=16p^4s^2.
\]

The pulled-back divisor has multiplicity two, so the normalized-wall square-root character is `+1`. However,

\[
\left.\frac{\partial K_{\rm exc}}{\partial a}\right|_{a=p,\xi=-\kappa}
=16p^3(\kappa-1)(\kappa+1),
\]

which is generically nonzero. The ambient branch divisor is transverse and a generic ambient meridian has character `-1`. Thus trivial wall character survives, but unrestricted ambient transport is falsified.

The finite-residue theorem gives

\[
r_\infty=-\frac{1}{32p^4(\kappa-1)}.
\]

Dividing by the collision Euler factor `kappa-1` yields

\[
\frac{r_\infty}{\kappa-1}
=-\frac{1}{32p^4(\kappa-1)^2},
\]

fixing both inverse factor and sign without fitting.

## Disposition and residual conjecture

The grade `-1` conductor total complex closes canonically in the normalized-wall pullback local system. This is now an algebraic source-typed result. It does not descend automatically to an ambient physical chain: the wall is quadratically tangent to a generically simple ambient branch divisor. The residual conjecture is that a tangency/nearby-cycle comparison map transports the closed wall class to the physical cut while recording the ambient `-1` character. The next falsifier must construct that map or show the character mismatch obstructs descent.

## Evidence

- `research/nima/checkers/check_qg2_wall_kummer_euler_orientation.py`
- `research/nima/qg2-conductor-connecting-morphism-dpc.md`
