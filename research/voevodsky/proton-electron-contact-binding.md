# A retained proton–electron interaction: 1D binding and a 3D nonbinding control

Date: 2026-10-10

## Result

A constituent-preserving singlet interaction now connects the actual retained
proton mode to either of the new five-cell electron doublet extensions. The
vertex is implemented by the previously constructed signed neutral-record gates,
not by appending a negative binding constant.

With one fixed mediator, one fixed reference and a declared relative-motion
Hamiltonian:

- the 1D model has exactly one singlet bound level below breakup;
- the triplet channels remain unbound;
- at the same frozen t=Delta=1, g=1/2, the 3D onsite model has **no** level below
  breakup, by an analytic upper bound on its bound-state criterion;
- no measured energy, particle mass or length was fitted.

This supplies a conditional interaction witness, not hydrogen binding. The
spatial kinetic law, contact range, proton spin extension, opposite phase
weights and physical implementation of the collective pair control remain
explicit inputs. The 3D result is a failure of this particular onsite fixture,
not a no-go for finite-range, stronger, or otherwise different interactions.

## 1. Prior constructions reused

`electron-pairing-coupling.md` already supplies the normalized logical singlet

    |s>=(|0,1>-|1,0>)/sqrt(2),  Pi=|s><s|.

It also makes explicit that the original rank-one, central-even proton must be
enlarged by a spinor factor before this vertex is well typed. That enlargement
is retained here; it is not presented as a discovery of proton spin from the
original vector protocol. The vertex is invariant under a common spin rotation
and under opposite supplied phase weights. Neither property derives electric
charge normalization or exchange statistics.

`finite-record-mediator-constructor.md` supplies the signed record gates and
uniform positive-generator identity used below. We reuse its finite apparatus
rather than introducing an unaccounted field self-energy.

`pentachoron-cycle-spin-energy-transport.md` supplies both conditional electron
doublets. Its checker now exports the actual normalized cell and face embeddings
for both chiralities and both lift choices, rather than asking the new test to
reconstruct a doublet by its desired rank.

## 2. Bind the interaction to retained raw records

The checker reconstructs the original twelve proton triangle modes from the
Merkle source's ordered corners. Their concatenated norm squared is 80. The
normalized 36-coordinate vector v is checked against the stored native
Hamiltonian and return:

    H_p v=0, N_p v=v.

The declared spin extension W_p maps a logical doublet to 72 raw coordinates.
Each electron embedding W_e maps its logical doublet to 40 face coordinates:
five cells, four face ports per cell, two spin components per port. All four
chirality/lift variants are checked. Both embeddings are isometries.

At the ABCD attachment, rescaling by sqrt(5) recovers exactly the old eight-row
tetrahedral encoding P_i/sqrt(2), including the stored projector coefficients.
The factor is the already declared normalization for distributing a state over
five cells, not a new interaction strength.

Define the raw pair vector and projector by

    |s_raw>=(W_p tensor W_e)|s>,
    Pi_raw=|s_raw><s_raw|.

The checker retains all 2880 nonzero raw pair coefficients, verifies unit norm,
and recovers the original logical singlet from them. The projector is represented
by its rank-one factor, without allocating a 2880-square dense matrix. These are
pair coefficients, not ordinary arrow counts or an energy count.

The effect annihilates vacuum and single-species sectors and commutes with both
species-number operators. It scatters a pair without converting or destroying
its constituents. No deterministic antilinear spin flip is used.

The coupling is evaluated in the admitted source-selected carrier sectors. Its
projector preserves them; it does not approximate an uncontrolled leakage into
other carrier modes. No physical locality across the many raw ports is inferred
from the logical rank-one description.

## 3. Relative coordinate and the same mediator at every separation

Introduce the **additional** relative-coordinate space l2(Z^d), with

    (K_d psi)(x)=t sum_j [2psi(x)-psi(x+e_j)-psi(x-e_j)],
    C=|x=0><x=0|, A=C tensor Pi.

The zero site denotes coincidence of the chosen attachment. The lattice,
nearest-neighbour kinetic law, point-contact range and t are supplied modeling
inputs. They are not derived from the simplex metric, and an integer site is
not a calibrated physical distance. Center-of-mass motion can be factored out;
"bound" here concerns the relative coordinate.

One neutral two-state mediator has occupation n=(I-Z)/2 and flip X. It is the
**same two-state system** at contact and at breakup. Since A is a projector,
reuse the two self-adjoint involutions

    R_plus =(I-A) tensor I + A tensor X,
    R_minus=-(I-A) tensor I + A tensor X.

Their positive generators obey exactly

    (I-R_plus)/2+(I-R_minus)/2=I-A tensor X.

The complete pair-sector Hamiltonian is

    H_full=E_carriers+K_d+Delta n+g[I-A tensor X],
    Delta>0, t>0, g>0.

E_carriers is the sum of the same admitted carrier ground energies on both
sides of the comparison. It need not be identified with physical rest masses.
The displayed model uses one energy unit and freezes t=Delta=1, g=1/2; the
mediator gap and half-gap coupling reuse the prior fixture. The kinetic
coefficient remains an additional declared choice.

At separation C=0, the ready mediator has energy g, NOT zero. The breakup
threshold with this same apparatus is

    E_breakup=E_carriers+g.

Consequently the relative operator is

    H_rel=H_full-E_breakup=K_d+Delta n-g C Pi X.

The scalar g is identical at contact and separation. There is no subtraction
of two independent mediator vacua, change in reservoir count, or varying
contact-dependent energy offset. The full unshifted gate energy is positive;
H_rel>=-g. A negative relative level can therefore coexist with positive full
energy.

Had we varied the strength g with separation while dropping its scalar gate
term separately at each location, we would have changed the reference. That
is deliberately not the construction tested here.

## 4. Exact 1D binding mechanism

In the singlet sector, write a(x),b(x) for mediator occupations 0 and 1. For a
candidate E=-q<0,

    (K_1+q)a=g delta_0 b(0),
    (K_1+Delta+q)b=g delta_0 a(0).

For z>0 the diagonal free resolvent is

    G_1(z)=<0|(K_1+z)^(-1)|0>=1/sqrt(z(z+4t)).

Its kernel decays as r(z)^|x|, where

    r(z)=[2t+z-sqrt(z(z+4t))]/(2t),  0<r(z)<1.

The central recurrence and normalization verify this formula; the checker also
exercises exact rational decay fixtures. Eliminating the two contact amplitudes
gives the necessary and sufficient condition

    g^2 G_1(q) G_1(q+Delta)=1,

or

    q(q+4t)(q+Delta)(q+Delta+4t)=g^4.

The left side increases strictly from zero to infinity for q>0. Hence exactly
one negative level exists for every g>0 in this 1D model. The exponentially
summable resolvent kernels construct its eigenvector. An eigenvector with both
contact amplitudes zero would have to be a negative-energy free state, which
is impossible, so no negative levels are omitted by this elimination.

For t=Delta=1, g=1/2 the polynomial is

    q^4+10q^3+29q^2+20q-1/16=0.

Exact rational bisection gives

    0.003110951810693763 < q < 0.003110951810695539.

Those decimals display certified rational endpoints in the receipt. They are
model-unit binding energies, not electronvolts or a hydrogen prediction.

On triplets Pi=0; the operator is K_1+Delta n and has no negative level. Thus
this particular pair vertex is spin-selective. The selection came from the
admitted neutral singlet operation, not from geometry alone.

### Finite-box failure control

Exact Schur recursions for Dirichlet intervals with radii 4,8,16 detect no level
below the infinite-volume threshold. Radii 32 and 64 do detect binding and
bound it less strongly than the full line. A small-box diagonalization would
therefore have missed this weak bound state. The infinite-lattice conclusion
comes from the resolvent proof, not an extrapolated numerical cutoff.

## 5. Same coupling in three dimensions: no binding at the frozen fixture

Do not promote the 1D result to a spatial particle. On Z^3 the exact criterion
for a negative level is still

    g^2 G_3(q) G_3(q+Delta)=1, q>0,

but the threshold Green function is finite. Using k in [-pi,pi]^3,

    G_3(0)=(2pi)^(-3) integral dk / [2t sum_j(1-cos(k_j))].

The inequality 1-cos u>=2u^2/pi^2 on that interval gives a denominator lower
bound 4t|k|^2/pi^2. Enlarge the integration cube to the ball of radius sqrt(3)pi:

    G_3(0)<=sqrt(3)pi/(8t).

Also G_3(Delta)<=1/Delta, since K_3>=0. Both resolvents decrease with q, so for
all q>0,

    g^2 G_3(q) G_3(q+Delta)
       <= g^2 sqrt(3)pi/(8t Delta).

At the unchanged t=Delta=1, g=1/2, use sqrt(3)<7/4 and pi<22/7 to obtain the
strict rational certificate

    g^2 G_3(q) G_3(q+Delta) < 11/64 < 1.

The bound-state equation cannot hold. The singlet and triplet sectors therefore
have no level below breakup in this **3D onsite fixture**. This is an analytic
nonbinding result, not failure to find a numerical eigenvalue. No coupling was
increased afterward to force a desired hydrogen-like answer.

## 6. What this unlocks, and what it does not

The previous cross-carrier gap now has an explicit conditional witness:
source-bound pair typing, both constituent numbers, a neutral mediator,
relative motion, bounded total energy, and a common breakup reference all appear
in the same construction. Reversibility follows from its bounded self-adjoint
lattice/finite-record Hamiltonian; switching and preparing the controls is not
thereby free or autonomous.

All four electron embedding variants have the same logical spectrum here,
because the same singlet interaction is transported through their isometries.
This test does not select chirality or spin lift. A fixed microscopic contact
operator, rather than transported logical copies, would be needed to distinguish
them physically.

The next useful source input is a justified spatial kinetic coefficient and
interaction range/profile in three dimensions, or a genuinely different
admitted mediator. These cannot be supplied by counting the raw pair terms or
by changing the breakup energy reference. A stronger 3D coupling would be a
new fixture, not evidence explaining why nature has that coupling.

The 1D existence witness remains valid. The 3D control prevents mistaking it
for completed hydrogen binding. No isotope, mass, charge or stability claim is
upgraded.

Constructive successor: `gauss-derived-spatial-binding.md` replaces the gapped
onsite record with the previously supplied local Gauss-field energy on a
spatial lattice. It derives a Green-kernel interaction with both self-energies
retained and certifies conditional 3D binding at fixed coefficients. This is a
changed field architecture, not a repair of the onsite fixture under unchanged
assumptions.

## Verification

Freshly executed:

```sh
python research/voevodsky/checkers/check_pentachoron_cycle_transport.py
python research/voevodsky/checkers/check_proton_electron_contact_binding.py
```

The new checker verifies the proton Merkle source, native zero mode and return,
all four exported electron embeddings and old attachment coefficients, raw
singlet encoding/decoding, 24 common binary-tetrahedral rotations, supplied
opposite-phase controls, species-number preservation, signed-gate identities,
rational root isolation, finite-box controls and the rational 3D upper bound.
The analytic proofs above supply the infinite-volume and all-q conclusions.

Receipt: `results/proton_electron_contact_binding.json`, with source and
implementation hashes. Prior pairing and finite-record construction code is
referenced; their entire historical checker chains were not rerun here.
