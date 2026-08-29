# The coefficient-valued window history is the first comparison-map candidate

## Carrier order

The source already distinguishes two histories:

[
mathfrak h_p:tlongmapsto[W_t]inmathcal F_{mathrm{cell}},
]

and its analytic multiplication representation

[
operatorname{Mult}([W_t])=M_{W_t}.
]

The comparison from arithmetic incidence should be constructed in
(mathcal F_{mathrm{cell}}) before applying (operatorname{Mult}). This
preserves the one-dimensional wall direction and avoids representing it
prematurely as the infinite-rank identity.

## Finite candidate

Let (e_{p,1}) and (e_{p,2}) be the labelled primitive and square
valuation/Fock atoms. Define the unweighted finite feature candidate

[
J_p^{mathrm{cell}}e_{p,1}=[W_{log p}],
qquad
J_p^{mathrm{cell}}e_{p,2}=[W_{2log p}].
]

Then the oriented Adams boundary is

[
J_p^{mathrm{cell}}(e_{p,2}-e_{p,1})
=
[W_{2log p}-W_{log p}].
]

Applying the analytic representation gives exactly

[
operatorname{Mult}
J_p^{mathrm{cell}}(e_{p,2}-e_{p,1})
=
D_p.
]

Thus the candidate has the correct finite location, grade, orientation, and
raw propagator without embedding an arithmetic delta directly into (L^2).

## Arithmetic weights remain external

The source coefficients attach to the incidence atoms:

[
e_{p,1}longmapsto p^{-1/2-sigma-it}e_{p,1},
]

[
e_{p,2}longmapstorac12p^{-1-2it}e_{p,2}.
]

They should not be absorbed into a rescaling of ([W_t]). Keeping coefficient
weight and cell feature separate preserves Adams naturality and allows the
Euler half-density to be audited independently.

## What this candidate solves

At finite cutoff it supplies:

1. a direct prime-labelled map;
2. grade (1	o2) boundary orientation;
3. the exact adjacent-window difference;
4. wall typing before analytic representation;
5. automatic compatibility with the multiplication history.

It also makes prime diagonality formal before completion because each
(J_p^{mathrm{cell}}) lands in its labelled cell fiber.

## What remains missing

A vector-space assignment is not yet a Green lift. The source must still
provide a cell-feature form

[
g_p^{mathrm{cell}}
]

such that its represented image agrees with the analytic relative Green
boundary form. The required identity is

[
g_p^{mathrm{cell}}
left(
J_p^{mathrm{cell}}e_{p,1},
J_p^{mathrm{cell}}e_{p,2}
ight)
=
b_p(e_{p,1},e_{p,2})
]

with the correct adjoint orientation.

Without (g_p^{mathrm{cell}}), the norms of the candidate lifts, their
radicals, and the mixed coefficient cannot be calculated.

## Representation-intertwining theorem

The decisive square is

[
operatorname{Mult}
left(
partial_tmathfrak h_p
ight)
=
partial_t
operatorname{Mult}
left(
mathfrak h_p
ight)
]

on a common analytic core, together with

[
operatorname{Mult}
left(
mathfrak h_p(2L)-mathfrak h_p(L)
ight)
=
M_{W_{2L}-W_L}.
]

The second equality is finite and formal. The first must be checked in the
topology used by the Green form.

## Minimal hostile

Choose a feature-space inner product that makes the two endpoint vectors
orthogonal, although their multiplication representations have the desired
difference. The finite comparison map and scalar window identity both pass,
but the pulled-back mixed Green block vanishes. This proves that the feature
form, not the feature assignment alone, carries the remaining content.

## Refined frontier

The first comparison-map candidate is now explicit:

[
e_{p,k}longmapsto[W_{klog p}],
qquad k=1,2.
]

The next source theorem is narrower:

> Construct the polarized cell-feature Green form for which this
> coefficient-valued window history is a cutoff-natural, radical-compatible,
> oriented lift, and prove that multiplication represents its Green boundary
> identity.

If successful, the arithmetic--analytic comparison arrow is no longer
missing; only its completion bounds remain.
