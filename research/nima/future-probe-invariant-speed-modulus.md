# From future-probe cones toward (c)

## Question

Can the future-probe causal-cone idea recover the relativistic invariant
speed, rather than merely some finite graph propagation bound?

## Minimal composition family

Assume a homogeneous one-dimensional velocity parameter and test the
associative family

[
uoplus_kappa v
=
rac{u+v}{1+kappa uv}.
]

The exact checker verifies associativity, identity (0), and inverse (-u).
A nonzero velocity (L) is invariant under composition with every (v) when

[
Loplus_kappa v=L.
]

Exactly,

[
Loplus_kappa v-L
=
rac{v(1-kappa L^2)}{1+kappa Lv},
]

so a finite invariant speed exists precisely on the positive branch:

[
oxed{c=rac1{sqrt{kappa}},qquad kappa>0.}
]

The other branches remain mathematically available:

[
egin{array}{c|c}
kappa>0 & 	ext{finite Lorentz-like invariant speed}\
kappa=0 & 	ext{Galilean composition; }c=infty\
kappa<0 & 	ext{no real fixed limiting speed in this family}
end{array}
]

## What has and has not emerged

The preceding future-probe result supplies an operational causal cone:
information has reached a probe when the probe can distinguish a source
event. Local composition bounds cone growth. Homogeneity and associative
frame composition then permit a finite invariant-speed modulus.

But they do not select the positive branch. Future probing plus locality is
compatible with both finite-speed and Galilean worlds.

Nor can the numerical SI value of (c) be derived without a unit convention.
Under a velocity-coordinate rescaling (u'=a u),

[
kappamapstorac{kappa}{a^2},
qquad
cmapsto ac.
]

Thus (299,792,458 {m m,s^{-1}}) is partly a statement about meter and
second calibration. The invariant physical content is:

1. a finite rather than infinite causal speed;
2. the universality of the same cone across sectors;
3. dimensionless ratios between causal propagation and other sector scales.

## Sharp Marici frontier

The Carrier would need to explain at least three additional facts:

1. **branch selection:** why (kappa>0), excluding the Galilean branch;
2. **universality:** why every admissible sector transport preserves the same
   causal cone;
3. **normalization:** how the cone relates to independently defined clocks
   and rods, or why those standards are themselves Carrier-derived.

Therefore the strongest current statement is

[
oxed{
	ext{future probes + locality define causal propagation;}
quad
	ext{relativity may promote its rate to a universal modulus }c.
}
]

They do not yet derive the finite branch or its calibration.

## Next falsifier

Search the existing cross-sector transport laws for a common finite fixed
boundary under composition. If scattering, radiative gravity, and cosmology
all preserve the same cone without importing a background metric separately,
that would support Carrier-level universality. If each sector requires an
independent causal normalization, (c) belongs to the sector lens rather than
the shared Carrier.

Exact artifacts:

- `research/nima/checkers/check_future_probe_invariant_speed_modulus.py`
- `research/nima/results/future_probe_invariant_speed_modulus.json`
