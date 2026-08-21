# The instrument capability fiber

## Generalization of the UDW–QND comparison

For every outcome map with a single Kraus operator, polar decomposition gives

[
K_x=U_xsqrt{E_x},
qquad E_x=K_x^dagger K_x.
]

The effect (E_x) determines every single-use outcome probability,

[
p(x|ho)=operatorname{Tr}(E_xho),
]

but it forgets the partial isometry (U_x). That forgotten datum determines
the successor state.

For the fixed click effect from the UDW–QND test,

[
E_1=s^2|1anglelangle1|,
]

every normalized successor vector (|psiangle) defines a compatible click
map

[
K_1(psi)=-is|psianglelangle1|.
]

Its click probability is always (s^2ho_{11}), while its conditional
successor is always (|psiangle). Overall phase is immaterial, so the
click-capability fiber is the projective qubit space

[
oxed{mathbb{CP}^1simeq S^2.}
]

UDW and QND are merely the two poles:

[
|psi_{m UDW}angle=|0angle,
qquad
|psi_{m QND}angle=|1angle.
]

A rational great-circle family is

[
|psi(t)angle=
rac{1-t^2}{1+t^2}|0angle+
rac{2t}{1+t^2}|1angle,
]

all with the identical click effect. Its immediate repeat-click probability is

[
p(1mid1;t)=
s^2rac{4t^2}{(1+t^2)^2}.
]

## What sequential records recover

A single-use record law projects away the capability fiber. Sequential
experiments do not. After the first click, insert known analyzer unitaries and
ask for a second click. Three analyzer directions (X,Y,Z) measure the Bloch
coordinates of (|psiangle). The checker verifies distinct exact
signatures for the absorptive, QND, (X+), and (Y+) successors.

Thus the distinction is not metaphysical or permanently hidden:

[
oxed{
	ext{single-use observation forgets capability;}
quad
	ext{controlled sequential observation can reconstruct it}.
}
]

## Marici interpretation

The architecture is a fibration rather than a single map:

[
egin{array}{c}
	ext{interaction capabilities}\
downarrow\
	ext{effect algebra / public one-use records}.
end{array}
]

The projection sends an instrument to its effects. Its fibers contain
physically inequivalent write semantics. A sector-specific lens that records
only effects is therefore a lossy view. Sequential composition probes the
fiber because it exposes the successor state to another interaction.

This yields a sharper Carrier question: does Marici supply merely the base
effect algebra, or does its calculus also constrain a distinguished subspace
and composition law in each capability fiber?

Exact artifacts:

- `research/nima/checkers/check_instrument_capability_fiber.py`
- `research/nima/results/instrument_capability_fiber.json`
