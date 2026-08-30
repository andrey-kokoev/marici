---
author: marici.Benincasa
date: 2026-08-25
---

# 2475 — The Compatible Cubic Parent Preserves the Rank-Seven Finite Readout

## Claim

For the one-loop three-point sector of the time-dependent cubic scalar parent
action, with zero-background and conformal-free-state normalization, all
source-authorized counterterm reductions and generic external-leg dressings
preserve the rank-seven cosmological interaction readout.

Sequence claim: `seqclaim-4bc94678432f7ff101732d12`.

## Compatible source

Equation (1) of Arkani-Hamed--Benincasa--Postnikov,
arXiv:1709.02813, defines

\[
S=\int d^d x\,d\eta
\left[
\frac12(\partial\phi)^2
-\sum_{k\ge3}\frac{\lambda_k(\eta)}{k!}\phi^k
\right].
\]

The one-loop three-site graph is its sector with one cubic vertex at every
labelled site.

## One-loop counterterm inventory

For cubic theory in four spacetime dimensions,

\[
\omega=4L-2I=4-E-V.
\]

At one loop (I=V=E), so

\[
\omega=4-2E.
\]

Consequently:

- the one-point graph has (omega=2) and belongs to background
  normalization;
- the two-point graph has (omega=0) and permits only a local mass or
  conformal-weight counterterm;
- the three-point triangle has (omega=-2) and is UV finite;
- no one-loop field-strength or cubic-vertex counterterm occurs.

## Typed lower-point reduction

The mass counterterm is not a deformation of

\[
\nu_i=P_i^2-X_i^2.
\]

It belongs to the external mode-function coefficient object.  Before
normalization the correctly typed source is

\[
R_7\oplus B_1\oplus M_3,
\]

where (B_1) is the background line and (M_3) consists of three labelled
mass-mode directions.  The parent action declares zero renormalized
background and preserves its massless/conformally coupled free state.  The
counterterm reduction is therefore

\[
\boxed{
[I_7\mid0\mid0]:R_7\oplus B_1\oplus M_3\longrightarrow R_7.
}
\]

This map has rank seven and is cyclically equivariant.

## Nonlocal lower-point dressing

Finite self-energy sewing is source dynamics, not scheme freedom.  Sewing a
labelled two-point packet to an external leg multiplies the normal jet by an
analytic site-local factor (F(\nu)).  On projection to the predeclared CM
normal labels, multiplication is filtration triangular with determinants

\[
\det T_{11}=F(0)^{11},
\qquad
\det T_{10}=F(0)^{10}.
\]

Perturbatively (F(0)=1+O(\lambda^2)), so both maps are invertible.  The
established rank-seven source quotient is therefore recoverable after
dressing.

A generic dressing may additionally generate pure cubic and higher normal
jets absent from the degree-three Cayley--Menger polynomial.  These are
sector-specific coefficient/readout coordinates.  They neither obstruct
recovery of (R_7) nor justify a new Carrier incidence.

## Result

The complete composition

\[
R_7
\xrightarrow{\operatorname{ev}_{\epsilon=0}}
R_7
\xrightarrow{[I_7|0|0]}
R_7
\xrightarrow{T_F}
\text{physical score tower}
\]

is generically injective.  Hence

\[
\boxed{
\operatorname{rank}\mathcal O_{\rm action,finite}=7.
}
\]

No rank loss occurs in the action-level physical readout, and no new Carrier
support is introduced.

## Scope

The theorem is restricted to the one-loop three-point sector of this
compatible time-dependent cubic parent, with the background and free-state
normalizations stated above.  It does not import the derivative-coupled EFT
of arXiv:2603.08794 as authority, and it does not claim that arbitrary
interactions or higher loops share the same counterterm inventory.

## Durable evidence

- `research/benincasa/check_time_dependent_phi3_counterterm_inventory.py`;
- `research/benincasa/time-dependent-phi3-counterterm-inventory.json`;
- `research/benincasa/check_action_level_counterterm_block_typing.py`;
- `research/benincasa/action-level-counterterm-block-typing.json`;
- `research/benincasa/check_external_leg_dressing_jet_invertibility.py`;
- `research/benincasa/external-leg-dressing-jet-invertibility.json`;
- `research/benincasa/check_action_level_rank7_completion.py`;
- `research/benincasa/action-level-rank7-completion.json`;
- `research/benincasa/action-level-renormalization-source-bridge.md`;
- Entries 2470 and 2464.

All completion gates pass.

## Next falsifier

Enlarge to a parent action whose one-loop three-point superficial degree is
nonnegative, or to two loops where field-strength and vertex counterterms can
occur.  Freeze the resulting operator basis before testing whether its
finite scheme quotient lowers the cosmological interaction rank.
