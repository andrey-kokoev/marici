---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 732 — The Mu-Two Trace Gate Has No Local Resonant Input

## Comparison of Entries 730 and 731

Entry 730 derives the mandatory finite-trace gate on the stack chart of the
weighted rational edge:

\[
\mathcal E_{23}^{+}\xrightarrow{\operatorname{Tr}}\mathcal E_{23,\mathbb Q},
\qquad
\mathcal E_{23}^{-}\xrightarrow{\operatorname{Tr}}0.
\]

Entry 731 independently derives the transformed-frame overlap

\[
T_{uy}=\operatorname{diag}(1,1,s^{-4},s^{-2}).
\]

Because the original connection is pulled back from the rational base and all
new exponents are even, the transformed exceptional lattice has trivial
(\mu_2)-character.  The shear introduces no hidden odd line.

## Resonant input

The exact weighted calculation gives

\[
\ker R_{23}=0
\]

and, for the algebraic--elliptic extension indicial complex,

\[
\ker L_m(R_{23})=0,
\qquad 1\le m\le10.
\]

Hence

\[
\boxed{
(\ker R_{23})^+=(\ker R_{23})^-=0,
\qquad
(\ker L_m)^+=(\ker L_m)^-=0.
}
\]

The trace gate is therefore vacuous on the local exceptional resonance
spaces: there is no even survivor to push with multiplicity two and no odd
survivor killed by trace.

## What remains

The coefficient (2e_{23}) in

\[
\gamma_0=(e_{12}^++e_{12}^-)-(e_{13}^++e_{13}^-)+2e_{23}
\]

is still canonically typed by the unnormalized degree-two trace.  What fails
is the stronger proposal that this rational edge obtains its coefficient from
a local exceptional extension-resonance kernel.

This does not delete the full nonresonant edge coefficient object.  A global
Čech class could only arise from the restriction/Gysin differential among
the strict-transform coefficient objects and this nonresonant edge—not from
an unaccounted local kernel on (E_{23}).

## Narrow conclusion

\[
\boxed{
\text{The local exceptional-resonance route to the rational invariant cycle
is falsified.}
}
\]

No new carrier datum is indicated.

## Evidence

- Entries 728, 730, and 731;
- `research/benincasa/marici-gm/gysin-weighted-crossing-conventions.md`;
- allocator claim `seqclaim-8c5202736303757472376737`.
- epistemic event
  `ev-000000000345-377386eb-5049-4b2f-9131-b87c508bb7e4`.

## Next falsifier

Construct the actual resolved coefficient Čech differential.  Its invariant
block must use the unnormalized trace on the nonresonant (e_{23}) object.
If that block has zero cofiber, the entire pairwise-resonant-divisor route to a
rational extension class closes.
