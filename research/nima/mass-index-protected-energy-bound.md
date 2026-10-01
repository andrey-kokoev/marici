# Index protection fixes a declared energy bound, not its numerical value

## Fresh obligation

The prior Gauss/locality model protects transitions but permits local energy
shifts. This trial supplies a stronger spectral protection mechanism and audits
which additional assumptions it introduces. The preceding rotor, charge and
locality checks are freshly rerun. No measured mass or tail is used.

## Explicit protected bound

Take an auxiliary graded space with three even and two odd states, and define

    A = [[1,0,t],[0,1,u]],
    Q = [[0,0],[A,0]],
    H0 = Q^dagger Q + Q Q^dagger,
    H = |Z| I + H0.

The blocks of Q refer to the3+2 grading. Q^2=0 and H0>=0. A has rank2 for every
real t,u. There is one even zero mode proportional to(-t,-u,1), and no odd zero
mode because det(A A^dagger)=1+t^2+u^2>0. The index is therefore+1.

The lowest energy is EXACTLY |Z| and cannot shift under these A deformations.
More generally a fixed finite3-to2 graded complex retains index+1, though rank
drops may add paired zero modes. This is an explicit supersymmetric-quantum-
mechanics bound analogous to BPS saturation, not a relativistic supersymmetric
particle theory. The grading is auxiliary, not a derived assignment of fermionic
particle statistics. The3-to2 imbalance is a new input.

Unlike the earlier unprotected square constraints, this trial really does
protect saturation while its algebra and central shift are fixed. Adding a
constant energy correction without changing Q or Z violates that algebra.

## What chooses Z?

For the physical rotor labels k,n_e and external charge Q_ext=k-n_e, consider

    Z = sum_s r_s*n_s + n_e
      = (sum_s r_s)*k+n_e.

With r_s=1 this gives Z=1836*k+n_e, so the collective and elementary sectors
have protected energy ratio1836. With r_s=1 on arrow slots and2 on state slots,
it gives Z=1944*k+n_e and equally protected ratio1944. Both assignments are
integer, invariant under typed relabellings and compatible with the Gauss law.

These are different candidate central-charge assignments, not a deformation
permitted while fixing Z. The distinction is the point: an index can protect a
value once its central-charge law is supplied, but cannot select which law the
carrier realizes. Universal coefficients have not been derived by introducing
supersymmetry.

## Unwanted sectors in the naive completion

If the same index+1 auxiliary system is provided in EVERY integer charge sector,
then k=1,n_e=-1836 has Z=0 but external charge1837. It has an exactly zero-energy
state in this trial. Multiples give a whole charged zero-bound lattice.

This is an unwanted extra spectrum if the trial is supposed to describe massive
particle sectors. It is not a theorem ruling out supersymmetric matter. Actual
BPS spectra depend on sector and stability conditions; some sectors have no
saturating state. A complex or multi-component central charge can also avoid this
particular kernel but introduces additional pairing data. Neither repair may be
assumed merely to remove a failed prediction. Electromagnetic field energy and
relativistic dynamics have not been supplied here.

## The source graph's actual graded complex

The connected comparison incidence graph already gives a two-term cochain
complex C0 -> C1 with1836 vertices and15174 edges. Its incidence rank is1835.
Thus its genuine graph cohomology is

    dim H0 = 1,
    dim H1 = 13339,
    index = 1836-15174 = -13338.

Its Hodge Hamiltonian has both the constant degree-zero mode and the many cycle
modes. It does NOT supply the auxiliary3-to2 index+1 spectrum above. Choosing a
spanning tree would remove the cycles, but would discard existing operations;
filling them with higher cells would require actual coherence relations. Graph
connectivity alone does not authorize either deletion or filling.

This is a more precise source frontier than asking vaguely for supersymmetry:
the existing graph complex is available, while its admissible higher cells,
sector interpretation and central-charge pairing are not yet constructed.

## Verification and outcome

    python research/nima/checkers/check_mass_index_protected_bound.py
    python research/aspect/scc/scc.py check nima-mass-index-protected-bound

Four rational A deformations check nilpotency, surviving zero vectors, positive
odd block determinant, paired supertraces and bound saturation exactly. Source
graph Betti numbers use its checked connectivity and edge count. Charge and
energy counterexamples are exact. Report: `results/mass-index-protected-bound.json`.

We have a model of genuine energy protection, but neither1836 selection nor an
acceptable all-sector spectrum follows. The next upstream construction must
supply admissible higher coherence cells and the sector-dependent central pairing
from the carrier, not assign them from the desired mass ratio.
