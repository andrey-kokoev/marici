# Pentachoron contact: exact ground binding and transparent dark sector

[Branch audit](BRANCH-EVIDENCE.md) · [exact checker](check_pentachoron_ground_sector.py) · [receipt](results/pentachoron-ground-sector.v1.json)

## Scope and source binding

This is an exact auxiliary certificate for the existing autonomous **20+20 point-contact model**, not the geometric entrance, a new physical channel or an automatically admitted C12. C1–C11 and their outcomes remain unchanged.

The checker verifies both archive manifests and the pinned nested symbolic receipt/script hashes. It reads the archived symbolic `L_original`, `L_connected`, `cycle_X` and `matching_P` strings, defining

```
H_O = L_original + cycle_X
H_C = L_connected + cycle_X
P   = matching_P
```

No archived Python is executed. No float NPZ or numerical eigensolver supplies the matrices. A restricted expression parser and exact rational arithmetic in Q(sqrt(2),sqrt(3),sqrt(5),i) suffice; no new package is installed. Square-root signs in the positive-semidefinite certificate are decided by rational enclosures, not floating tolerances.

The model remains `(L2(R) tensor C20)_O direct-sum (C20)_C`, with form

```
integral (||psi'||^2 + psi* H_O psi) dx
  + chi* H_C chi + 2 ||P(psi(0)-chi)||^2.
```

All parameters here are the source fixture epsilon=ell=hbar=kappa=1. The coefficient inner product is the source Euclidean one; it is not imported from another branch.

## Exact finite result

For `theta=(11-2 sqrt(6)-sqrt(5))/2`:

- H_O and H_C are Hermitian; P is an orthogonal rank-two projector.
- H_O-theta I is positive semidefinite of rank sixteen. Thus theta is the actual lowest native energy and its ground eigenspace G has dimension four.
- The map P restricted to G has rank two; D=G intersect ker(P) therefore has dimension two.
- The receipt provides exact ground/dark bases and the ambient orthogonal projector Q_D, checking

```
Q_D* = Q_D,  Q_D^2 = Q_D,
P Q_D = Q_D P = 0,
H_O Q_D = Q_D H_O = theta Q_D.
```

The PSD calculation uses exact Hermitian Schur congruences with certified positive pivots and a zero final block. Kernel generation and residual checks are separate exact calculations. The result does not assume the source's numerical eigenvalue multiplicity.

## Why a uniform all-ground vanishing-transmission claim is false

On `L2(R) tensor D`, the contact term vanishes and the core record is zero. The projector `diag(Q_D,0)` reduces the full form: its mixed H_O terms and its mixed contact terms vanish by the identities above. The restricted Hamiltonian is simply `-d_x^2 + theta` on two free channels. H_C need not preserve D, because the decoupled state has no core component.

Consequently, for every k>0 the dark incoming channel at E=theta+k^2 has

```
t_dark(k)=I2,  r_dark(k)=0,  chi=0.
```

These equal-velocity channels have unit transmission in the source flux convention. Every normalized incoming dark packet supported in `(theta,theta+epsilon)` also transmits with probability one. Such packets exist for arbitrarily small epsilon. Thus neither an all-ground `||t(k)||=O(k)` bound nor an all-ground uniform O(epsilon) transmission-packet bound can hold here. C1/C4 are not contradicted: they refer to the different two-rim fixture.

This is a source-bound sharpening of the previously numerical dark-preparation report, not a no-go for all pentachoron contacts or richer constructions. It also does not establish capture, photon channels or a physical meaning for these two modes.

## The remaining threshold test is now well-typed

Use the contact-active ground complement B=G orthogonal-minus D, of dimension two. A successor may ask whether its transmission is O(k), and whether the ground scattering limits are `t -> Q_D` and `r -> -(I_G-Q_D)`, with uniform packet consequences **on B only**.

The [machine-readable bright-threshold draft](contracts/pentachoron-bright-threshold-draft.v1.json) fixes that statement, its spaces, quantifiers, falsifier and conditional packet corollary. The draft remains frozen as formulation history. The same statement is now explicitly admitted as **open C12 in v5**, with a bounded live planner card; this certificate does not resolve it. It requires checking the threshold boundary system with all closed continuum and finite-core coordinates retained, including any threshold resonance or invisible/core kernel. The unreduced forty-coordinate threshold block is already singular on `(D,0)`; those two automatic dark null directions must be separated before testing for bright lead-visible resonances. Do not invert a singular eliminated core matrix or assert that rank-two P proves regularity. If the proposed bright limit fails, record the actual resonance/limit instead; the dark theorem remains valid.

## Verification and limits

```sh
python research/scattering/low-energy/check_pentachoron_ground_sector.py --check
python -m unittest discover -s research/scattering/low-energy -p test_pentachoron_exact.py
```

Controls reject perturbed/dependent dark bases and executable or out-of-field expressions. The checker does not replay ancestor geometry or the archived numerical scattering solver, classify the complete bound spectrum, prove bright regularity, or modify any high-energy protocol/budget.
