# Finite probe horizon plus frame naturality selects the Lorentz branch

## Selection mechanism

The preceding calculations left three ingredients separate:

1. future probes give propagation an operational meaning;
2. local constructor composition bounds propagation in one frame;
3. homogeneous frame changes compose through
   [
   uoplus_kappa v=rac{u+v}{1+kappa uv}.
   ]

Let (L) be the finite nonzero boundary of the probe-reachable velocities in
one frame. If physical causal support is natural under changes of inertial
frame, every frame transport must preserve that boundary:

[
Loplus_kappa v=L
qquad	ext{for every admissible }v.
]

Exactly,

[
Loplus_kappa v-L
=
rac{v(1-kappa L^2)}{1+kappa Lv}.
]

Therefore

[
oxed{kappa=rac1{L^2}>0,qquad c=L.}
]

The Galilean branch fails sharply:

[
Loplus_0 v=L+v
eq L.
]

It cannot preserve any finite universal probe horizon.

## What this explains

The positive branch does not need to be selected by declaring “there is an
invariant speed.” It follows from two independently typed requirements:

- **local finiteness:** elementary interaction composition produces a finite
  reachability horizon in any one operational frame;
- **naturality:** the physical distinction between reachable and unreachable
  probes is not changed by re-presenting the experiment in another inertial
  frame.

Thus:

[
oxed{
	ext{finite local probe horizon}
+	ext{frame naturality}
Longrightarrow
	ext{Lorentz-like positive branch}.
}
]

This is a genuine explanatory improvement. It identifies which structural
principle excludes Galilean kinematics: not future probing alone, but the
requirement that its finite causal boundary be a natural object.

## Current Marici typing gap

The derivation is conditional because the repository currently obtains these
premises from sector inputs rather than from the shared Carrier:

- the Machian discrete-wave proxy builds a finite cone into its
  nearest-neighbor hyperbolic update;
- the scattering/helicity construction admits a Lorentz metric, time
  orientation, and future null ray as source data;
- no established comparison map derives both the finite probe horizon and
  inertial-frame transport from the common Carrier calculus.

Accordingly, this is not yet a derivation of (c) from Marici. It is a
minimal contract that such a derivation must satisfy.

## Sharp next test

Construct a Carrier-to-causal comparison

[
mathfrak C_{m Carrier}^{m local}
longrightarrow
mathfrak C_{m probe}^{m spacetime}
]

that sends local composition depth to probe-support growth and intertwines
Carrier transport with inertial-frame transport. Then verify:

1. finite nonzero support radius per generator;
2. closure under sequential composition;
3. naturality of the support boundary;
4. the same boundary in scattering, radiative gravity, and cosmology.

If that map exists without importing the Lorentz metric, the positive branch
is Carrier-derived. If it requires the metric as input, (c) remains part of
the spacetime sector lens.

Exact artifacts:

- `research/nima/checkers/check_finite_horizon_frame_covariance_selection.py`
- `research/nima/results/finite_horizon_frame_covariance_selection.json`
