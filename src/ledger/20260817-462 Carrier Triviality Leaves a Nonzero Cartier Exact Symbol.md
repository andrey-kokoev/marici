---
id: 462
date: 2026-08-17
title: Carrier Triviality Leaves a Nonzero Cartier Exact Symbol
---

# Carrier Triviality Leaves a Nonzero Cartier Exact Symbol

Entry 461 trivializes the full carrier by writing

\[
K=F^2=u^2z^2,
\]

where

\[
F=a^2+\frac u2(1-b^2)-\frac54u^2+\frac12u^3.
\]

The original exact operators differentiate at fixed (u).  Hence

\[
K_a=4aF=4ua z,
\qquad
K_b=-2ubF=-2u^2b z.
\]

Every term proportional to (K=u^2z^2) vanishes after dividing by one
Cartier factor (z) and restricting to the reduced section (z=0).  The
terms involving (K_a) and (K_b), however, retain one factor of (z) and
survive that operation.

For a sector with (e_a=2-s_a), (e_b=2-s_b), and source coefficient (f),
the first Cartier symbols are therefore

\[
\sigma_z(p)
=-3u^2b\,fL_1^{e_a}L_2^{e_b},
\]

and

\[
\sigma_z(q)
=-6ua\,fL_1^{e_a}L_2^{e_b}.
\]

Thus algebraic triviality of the carrier does not trivialize the exact-form
complex.  The reduced carrier has identity monodromy, but its first nilpotent
Cartier neighborhood supports a nonzero differential.  This is the precise
location where resonance transport may survive.

The formulas do not yet give a finite cokernel: their visible powers of (u),
(a), (L_1), and (L_2) must be divided by the degreewise source and target
Rees shifts of Entry 460.  Performing that normalization before specialization
is essential; setting (u=0) in the displayed unnormalized symbols would
incorrectly erase them.

The next gate is to normalize these two symbols in every homogeneous block and
compute the resulting exceptional cokernel and its action on the resonant
bidegrees.

The executable audit is
research/voevodsky/check_soft_axis_translated_exact_symbols.py.
