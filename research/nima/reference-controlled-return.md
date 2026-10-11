# Reference preparation composes with conservative return, but changes its period

## Declared joint protocol

The preceding preparation supplies A=alpha J and B=beta J, with alpha,beta in {+1,-1}. In this family, B v A^-1=(alpha beta) J v J^-1. Thus the old left bank mixer becomes L_s=s L, where s=alpha beta.

A supplied instruction either flips A, flips B, or does nothing. After that instruction, use the resulting s in the existing positive exchange:

    (x,t) -> E(Rx,s Lt).

The reference signs and instruction history remain part of the retained state. This is an explicit new controlled composition of existing operations, not a source-generated decision about which operation occurs. There is no carrier-to-reference selection rule or autonomous physical clock here.

## Joint inverse and budget

For each reference configuration and each instruction, the body map is an orthogonal transformation. Its inverse first undoes the exchange and rotations using the CURRENT reference signs, then undoes the supplied reference instruction. All sign configurations and all twenty coordinate basis vectors are tested exactly.

The joint coefficient budget

    ||x||^2 + ||t||^2 + ||A||_F^2 + ||B||_F^2

is conserved; the reference contribution is four in this prepared family. This does not account for an external controller's physical implementation or identify the coefficient budget with laboratory energy.

## Recompute return instead of inheriting the old six-step claim

For the specified protocol “flip A before every exchange,” s alternates. For a fixed starting s, two steps return the reference signs and act on the body by T_s=U_s U_-s.

Exact full-space matrix checks give:

- T_s has order six: the numerical joint state has period twelve;
- the observed pair (x,Ct) returns after six steps;
- after six steps the twelve-dimensional observable sector is fixed, but the eight-dimensional residual is negated.

In the fixed coordinates a=Ct, b=CLt, one step at sign s is

    (x,a,b,k) -> (s b,Rx,s a,s Lk).

This explains why observing a six-step return can miss the remaining complement change. The full period is an operator identity, not a statement that the complete history record repeats or that a physical clock has been derived.

The concrete ordinary/twisted fixture traces retain only the prior three allowed advances and then reverse them exactly. The twelve-step identity was checked by matrix powers, not by bypassing the prior retained-state depth policy. All parent states and event labels in the bounded traces remain available.

## Disposition

The conditional reference preparation can be coupled to the existing return without losing invertibility or the joint coefficient budget. It must not inherit the fixed-reference period uncritically. The remaining source obligation is the control/attachment rule selecting these interventions, not another guessed exchange gain.

This result applies only to the explicit +/-J family and supplied protocol. It does not establish a uniquely WG-generated autonomous response, a general evolving-reference law, a gravitational coefficient, or a relation between the numerical period twelve and the old gravitational prefactor.

## Verification

`python research/nima/checkers/check_reference_controlled_return.py` passed. Results: `results/reference-controlled-return.json`, containing exact inverse, orthogonality, period, observed-return and bounded-history checks with source digests.

No prior dynamics implementation was modified. No ledger entry, commit or publication is claimed.
