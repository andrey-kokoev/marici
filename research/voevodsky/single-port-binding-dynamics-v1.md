# Candidate dynamics and a conditional binding model

## What is now constructed

The port bridge now has two explicitly different dynamical continuations:

1. A reciprocal Hermitian completion of the directed transfer. It has exact
   reversible, norm-preserving finite-sector dynamics, but fails the retained
   central spin symmetry for a scalar coupling. It is not particle binding.
2. A separately declared quadratic pair-sector interaction with a relative
   half-line kinetic operator. It produces an exact spatially localized bound
   state above a calculable coupling threshold. An isotropic extension preserves
   the entire electron doublet and admits bound witnesses in every potential fold.

**These are conditional models, not source-derived physical hydrogen.**
The interaction sign, relative kinetic law, location of the attractive defect,
strength and optional orientation averaging are stated additions. None is
selected by the existing coefficient transfers.

## 1. The original directed arrow cannot be a closed-system Hamiltonian alone

Let h=N_proton e_(AB,x), ell be the electron face0spin0 row of E, and

    eta=||h||²=1/180,
    b=ell^dagger, d=(-ell1,ell0),
    delta=||b||²=||d||²=1/2+sqrt3/6.

In the retained basis (h,Eb,Ed), the metric is

    M=diag(eta,2delta,2delta).

The original forward arrow has only the coefficient A_(p,bright)=delta.
It is not self-adjoint in M. A closed Hamiltonian completion requires its
metric adjoint, corresponding to one additional reverse raw transfer:

    H(g)=[[0, g delta, 0],
          [conjugate(g) eta/2, 0, 0],
          [0, 0, 0]].

The arbitrary complex g is not an inferred energy scale. The checked relation
is H^dagger M=M H, not ordinary symmetry in an unnormalized basis.
The bright energies are

    +/-sqrt(|g|² eta delta/2),

and the dark direction has energy zero.

The checker constructs Cayley updates

    U(s)=(I-isH)(I+isH)^(-1)

and verifies U^dagger M U=M and exact energy conservation for nine complex
coupling/step controls. This is a declared reversible discrete update, not a
conversion of the native assembly clock into physical time or a claim that
Cayley updates equal the exact exponential at finite step.

## 2. Why that reciprocal model is not the desired pair interaction

The native proton selected line is central-even; the electron doublet is
central-odd. With S=diag(1,-1,-1),

    S H(g) S=-H(g).

A fixed scalar nonzero g therefore violates this central symmetry. It would
need additional transforming interaction data or a carrier enlargement.
Adding the reverse transfer alone does not resolve that obstruction.

Also, C_proton direct-sum C²_electron describes amplitude mixing between
sectors. It is not the tensor product containing one proton and one electron.
Its negative finite level is an internal bonding eigenvalue, not proof of
spatial localization below a separated-particle continuum. No interaction
between a physical proton spin doublet and an electron spin doublet is derived.

## 3. A distinct pair-sector quadratic interaction

Use the tensor product of the existing selected proton line with the logical
electron doublet. Its internal dimension is 1 times 2, not 1 plus 2.
This is a declared sector using the present carriers, not a derivation of the
physical proton spin or hydrogen total spin.

The projected normalized-encoder port map C satisfies

    K=C^dagger C=(eta/2) b b^dagger=k Q,
    Q=b b^dagger/delta,
    k=eta delta/2=1/720+sqrt3/2160.

Q is a rank-one orthogonal projector. It fixes b and annihilates d.
K is the same positive quadratic port observable; converting it into an
attractive energy requires the **new rule** -kappa K, kappa>0. The source
transfer supplies K but does not select the minus sign or kappa.

This quadratic rule preserves the central action on the pair sector. A fixed
port still singles out a spin direction and does not commute with every binary
tetrahedral rotation. That failure is explicitly checked.

## 4. Introduce a relative coordinate, rather than rename existing information

The declared relative-coordinate carrier is

    l2({1,2,...}) tensor C²,

with Dirichlet origin and Hamiltonian

    H_rel=t(2I-S-S^dagger) tensor I2
          -u |1><1| tensor Q,
    t>0, u=kappa k>0.

Here S is the unilateral shift. This is a bounded self-adjoint lattice
Hamiltonian and hence admits norm-preserving unitary evolution. The free
continuum is [0,4t]. The site1 defect is short-range attraction, not Coulomb law.

The new coordinate n is neither the potential direction v, host depth h_T,
nor electron norm. No physical lattice spacing is supplied. A continuum
interpretation such as t=hbar²/(2 mu a²) would require independently supplied
mass and length, not derive them.

## 5. Exact binding theorem for the fixed port

In the bright channel the bound state exists **if and only if u>t**. Put

    q=t/u in (0,1),
    psi_n=sqrt(1-q²) q^(n-1),
    E=2t-u-t²/u=-t(1-q)²/q<0.

The first-site equation is

    (2t-u)psi_1-t psi_2=E psi_1,

and every bulk site obeys

    2t psi_n-t psi_(n-1)-t psi_(n+1)=E psi_n.

The geometric series gives norm one. Conversely, a decaying negative-energy
solution has 0<q<1 and its boundary equation requires u=t/q>t.

For u<=t, the quadratic form is

    <psi,H psi>=t sum_(n>=1)|psi_(n+1)-psi_n|²
               +(t-u)|psi_1|² >=0.

Thus there is no negative bound energy. The threshold q=1 solution is not
square summable. The dark spin channel has no attractive term and no bound
state in this model.

Three exact dimensionless fixtures verify the bulk/boundary equations,
Rayleigh energy and geometric normalization, including the exact infinite tail.
The no-binding quadratic-form identity is independently checked on finite
support controls. The theorem is the displayed infinite-domain argument,
not an extrapolation from a finite matrix diagonalization.

## 6. Optional isotropic extension: preserve the complete bound doublet

Average the fixed-port projector over the existing 24 binary tetrahedral spin
matrices:

    Q_bar=(1/24) sum_U U Q U^dagger=I2/2.

This exact equality is checked. The averaging is an **additional interaction
permission**, not something the original fixed arrow automatically performs.
It is not reported as 24 new ordinary transfer arrows.

At unchanged total trace strength u, both spin channels receive attraction
u/2. Therefore the isotropic model binds if and only if **u>2t**. Its bound
spin subspace has dimension two, with a common spatial profile and arbitrary
logical electron seed.

The fixture t=1, total u=4 gives q=1/2 and E=-1/2 in both spin channels.
The checker transports an explicit bound spinor witness in every one of the
24 original potential fold interiors. This preserves the entire potential
sphere as bound internal-state data, not merely as unused source provenance.

This is not a fitted hydrogen energy. The values are declared dimensionless
verification controls, and the physical strength remains uncalibrated.

## 7. Potential realization and invisible data remain correctly typed

The same spinor-to-potential bridge is used at every nonzero local spinor
amplitude. A geometric bound profile changes the local norm but not its ray.
Nodes need the separate zero stratum; no ray is assigned to zero amplitude.

For the fixed-port model:

- the bound bright ray is potential vertex D;
- the unbound dark ray is the ABC face centre;
- both have zero potential mode Gamma, but different port intensities.

The source potential mode alone is therefore not the interaction strength.
The isotropic extension permits every potential ray in its degenerate bound
subspace. The original one-arrow dark phase is still not a physical readable
coordinate merely because the complete realization retains it.

## Verification

    python research/voevodsky/checkers/check_single_port_binding_dynamics.py

Passed:

- source proton projector, port norm and electron tight-frame metric;
- directed-map non-Hermiticity and reciprocal weighted self-adjointness;
- nine exact reversible Cayley controls and energy conservation;
- central-symmetry obstruction for scalar direct-sum mixing;
- rank-one pair quadratic interaction and its fixed-port rotation failure;
- exact 24-action isotropic average;
- three infinite-profile binding fixtures and no-binding form controls;
- local potential reconstruction along a bound profile;
- bound spinor witnesses in all 24 folds for the isotropic fixture.

SCC freeze:
`a7a1b25979a0b21e4f734773937adcc91f9d0d6bdf18897909e4a70c26fc3dd2`.

- Contract: `inputs/single-port-binding-dynamics-v1.json`.
- Receipt: `results/single-port-binding-dynamics-v1.json`.
- Model: `scc-models/single-port-binding-dynamics-v1.json`.

All shared source stores remain unchanged. The next physical gate is a
source-selected relative kinetic and attractive interaction law, with allowed
orientation/measurement access and a physical scale. No masses, charge,
Coulomb field, reciprocal physical particle vertex or hydrogen spectrum follow
from this conditional model alone.
