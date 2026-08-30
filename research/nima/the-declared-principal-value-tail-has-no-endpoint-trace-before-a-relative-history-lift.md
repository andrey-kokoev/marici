# The declared principal-value tail has no endpoint trace before a relative history lift

## Audit result

The current source packets do not define the principal-value tail as an element of the interval history graph
[
mathcal G_L=H^1([L,2L];mathcal H).
]
They define it as a Fourier/Hilbert-transform boundary distribution whose translated response has an algebraic moment tail. Consequently
[
Gamma_LJ_{mathrm{tail},p}
]
is presently undefined: neither zero nor nonzero endpoint trace has source authority.

The canonical projector
[
Pi_{0,L}=I-R_LGamma_L
]
is therefore an exact theorem on already-constructed history maps, but it cannot yet be applied to the declared principal-value distribution.

## Why arbitrary projection is unsafe

The primitive principal-value lane requires a source-derived relative moment cancellation before arithmetic aggregation. If one first chooses an arbitrary lift (widetilde J_{mathrm{PV},p}) and replaces it by
[
Pi_{0,L}widetilde J_{mathrm{PV},p},
]
the removed affine component
[
R_LGamma_Lwidetilde J_{mathrm{PV},p}
]
may contain exactly the boundary moments needed for that cancellation. Zero endpoint trace prevents leakage into the endpoint coordinates, but does not prove preservation of the relative sewing law.

Thus two quotients must not be conflated:

- history trace quotient, removing affine endpoint data;
- principal-value moment quotient, removing the algebraic Hilbert tail by authorized relative sewing.

They commute only after a comparison theorem.

## Required comparison square

The next constructor must provide a relative history lift (J^{mathrm{rel}}_{mathrm{PV},p}) and prove
[
Gamma_LJ^{mathrm{rel}}_{mathrm{PV},p}=0
]
from the source sewing identity, or an authorized comparison
[
J^{mathrm{rel}}_{mathrm{PV},p}
=
Pi_{0,L}widetilde J_{mathrm{PV},p}
]
together with preservation of every required moment subtraction.

Equivalently, if (M_p) is the declared principal-value moment map and (S_p) its source subtraction, one needs the commutative relation
[
M_pPi_{0,L}widetilde J_{mathrm{PV},p}
=
M_pwidetilde J_{mathrm{PV},p}-S_p.
]

Without this identity, the projector is a convenient normalization rather than the declared tail constructor.

## Hostile

Choose two history lifts of the same boundary distribution differing by an affine path:
[
widetilde J_2=widetilde J_1+R_L(a,b).
]
They represent the same zero-trace projection,
[
Pi_{0,L}widetilde J_2=Pi_{0,L}widetilde J_1,
]
while their endpoint moments differ. Hence the projected history alone cannot recover which source boundary moment was subtracted.

## Consequence

The endpoint lower bound is conditionally protected once a relative zero-trace lift exists. The earliest missing arrow is now
[
	ext{principal-value boundary distribution}
longrightarrow
	ext{source-relative interval history}
]
with simultaneous trace and moment compatibility.

No tail Schur elimination, odd causal return, or completion margin should be instantiated before that lift is constructed.