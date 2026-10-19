# Constructed spinor–potential–single-link bridge

## Result

The previously missing coordinate bridge is implemented and checked.
It uses the **existing electron doublet, potential tetrahedron, potential
projector and declared single proton-facing arrow**. No transfer arrow was added.

- All 24 original potential fold interiors are reached by explicit spinors.
- Potential mode + known electron norm + complex link reading reconstruct the
  electron generically, and recover the potential witness in this alignment.
- On the dark electron line, those same data still hide phase. The complete
  retained realization therefore includes an internal phase witness there.
- All 24 existing binary tetrahedral actions transport to the same potential
  tetrahedron; their central minus-one fixes the potential ray but changes phase.

This is a declared information-space bridge, **not a physical interaction or
proof that potential-mode or phase-witness coordinates are measurable**.

## Source-bound alignment

Use Pauli coordinates for the nonzero logical electron seed z=(z0,z1), with
n=||z||², and its unit Bloch vector

    r=(2 Re(conj(z0)z1), 2 Im(conj(z0)z1), |z0|²-|z1|²)/n.

The source potential tetrahedron has vertices

    A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1).

Its barycentric radial lift is

    alpha=-1/min_i(POINTS[i] dot r),
    v_i=(1+alpha POINTS[i] dot r)/4.

Then v is on the actual source boundary B, with nonnegative coordinates and at
least one zero. The construction is a radial homeomorphism between the Bloch
sphere and this potential boundary. Conversely

    d(v)=sum_i v_i POINTS[i]=alpha r,
    r=d(v)/||d(v)||.

The checker records a positive algebraic certificate alpha with
alpha²=||d(v)||²; it is determined by v, not another independent state variable.
The potential mode is the existing Gamma(v)=L_AB d(v), extended to real
Q(sqrt3) inputs, not a newly chosen projector.

The actual electron face projector eigenlines land at potential vertices
**D,C,B,A** for electron faces 0,1,2,3. This permutation is checked from the
stored projectors. The alignment is an explicit coordinate declaration, not
a derived physical spatial orientation.

## Attach to the repaired host interface

For any host position x in T, retain

    ((x,Gamma(v)), (h_T(x),v))

in the already constructed free-mode pullback R ~= T x B. Host position does
not determine v or Gamma(v). Every potential point is available at every x,
including the resolved host barycentre with h_T(x)=0.

The refined retained realization records the logical norm and phase as well as
this potential ray. As a state space it is T x (C² minus {0}), projecting onto
T x B. It has six real information coordinates before fixing norm, not six
physical spatial dimensions. Zero spinor is excluded and requires a separate
vacuum stratum; assigning it a ray would be an error.

## The single-arrow interface

As in the preceding construction, let E be the stack of the four electron
face projectors and ell its face0 spin0 row. E^dagger E=2I; the normalized
encoder is J=E/sqrt2. In the exact E-coordinate convention the declared raw
arrow reads

    a=ell z,
    target=proton raw AB:x,
    projected receiver=N_proton e_(AB,x) a.

The checker binds that actual source proton column and checks forward transfer
and algebraic scalar readback at a nonzero column entry for every test input.
Conversion to the J convention introduces the stated factor 1/sqrt2, not a
physical coupling-strength derivation.

The potential mode Gamma(v) and coefficient amplitude a are **different
functions of the same retained state**, not equal complex values by fiat.
The bare arrow still has logical rank one.

## Full reconstruction with a potential witness

Let R_z=zz^dagger/n be the projector obtained from r, and b=ell^dagger.
For a!=0,

    z=n R_z b/conjugate(a).

Thus the potential ray, norm and complex amplitude determine the entire seed
on the bright chart. The preceding same-link/same-norm pair b+d,b-d, where
d=(-ell1,ell0), now has different potential witnesses. Both round-trip exactly.

For a=0, retain the internal witness c=d^dagger z. Then

    z=n R_z d/conjugate(c).

It is nonzero for every nonzero dark state. Removing this witness is rejected
by the decoder. It is retained electron information, **not a second proton
arrow or an extra physical measurement**.

On overlapping phase charts, c/a and a/c are the reciprocal ray coordinates.
The normalized state space is the Hopf phase bundle over B, not a globally
trivial sphere times a selected phase. The compact receipt stores c only on
the exact dark stratum; this is an exact stratified representation, not a
numerically well-conditioned global chart. Near darkness one should use the
second phase chart before the division by a becomes unstable.

## Stronger result: mode and link intensity recover the fold witness

The source alignment has a useful exact compatibility:

    normal k=(1,1,-1),
    bright unit Bloch direction=-k/sqrt3,
    delta=||b||²=||d||².

Consequently the normal Bloch coordinate is

    beta=k dot r=sqrt3(1-2|a|²/(delta n)).

The existing source real recovery matrix turns Gamma(v) into the transverse
vector w, with k dot w=0. Because d(v)=alpha r,

    r=w/alpha + k beta/3,
    alpha²=||w||²/(1-beta²/3).

For w!=0 the positive square root determines alpha and therefore r and v.
For w=0, beta=+sqrt3 or -sqrt3 determines the normal pole. This reconstructs
the potential witness from **mode, norm and link intensity**, without using
stored v or its radial certificate. The complex link additionally supplies
phase on the bright chart.

In particular, the old two zero-mode witnesses are distinguished by the
link intensity: the bright ray is vertex D; the dark ray is the centre of
face ABC. Their potential modes both vanish, but their link amplitudes do not
agree. The decoder is checked on all 2,184 exact test inputs. Its positive-root
routine operates in Q(sqrt3) for these source-derived inputs; arbitrary real
inputs use the corresponding real positive root, not an assumed closed
quadratic field.

This recovery uses the norm and retained potential mode as well as the arrow.
It does not mean the single arrow itself transmits all these records.

## The irreducible invisible direction at darkness

For z=d and z'=i d:

    n(z)=n(z'), v(z)=v(z'), Gamma(v(z))=Gamma(v(z')),
    a(z)=a(z')=0,
    c(z')=i c(z).

Thus even the potential mode, full potential witness, norm and one-arrow
reading do not give global full-spinor recovery. The dark phase circle remains
invisible unless its internal witness or an additional permitted comparison
is accessed. A mathematical complete realization is not a measurement claim.

Similarly, z and -z have the same potential ray but opposite retained phase.
This carries the electron's binary spinorial central action; it is not the
potential atlas deck involution. That deck generally changes the ray while
preserving Gamma. The two constructions' uses of 'two sheets' are not conflated.

## Verification and artifacts

    python research/voevodsky/checkers/check_spinor_potential_link_bridge.py

Passed:

- native electron L,G,N encoder intertwiners and unchanged logical dimension;
- 2,184 exact spinor round trips, including serialized receipts;
- independent mode-based reconstruction without stored v or alpha;
- actual proton forward column and algebraic link readback;
- retained-frame norm identity |a|²+|c|²=delta ||z||²;
- explicit interior witness in every one of the original 24 folds;
- all 24 binary tetrahedral actions and central-minus-one phase;
- rejection of zero input, missing dark phase, wrong radial certificate and
  incompatible norm.

Early serialization exposed Fraction/D representation defects, which were
fixed without modifying source arithmetic. The first coarse ray grid reached
20 folds; a finer grid supplied the four missing interior witnesses. The
24-fold acceptance condition was retained, not weakened. Full radial
surjectivity also follows from the displayed homeomorphism.

SCC freeze:
`fd6da072bfc1920878305d502b81d8f0aae13cf72d68e4da7f02896ed8f6d1d8`.

- Contract: `inputs/spinor-potential-link-bridge-v1.json`.
- Receipt: `results/spinor-potential-link-bridge-v1.json`.
- Model: `scc-models/spinor-potential-link-bridge-v1.json`.

No shared source/store was modified. Remaining physical work is to specify
which records a permitted interface can actually read, and to supply an
interaction law if binding or dynamics is claimed. This bridge supplies
neither a reciprocal Hamiltonian nor mass, energy or binding predictions.
