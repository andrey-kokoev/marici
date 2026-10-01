# Equal mass gaps: symmetry audit and the missing protected kernel

## Forward-realization question

Can the existing rooted carrier symmetry force the energy choices in the
[charged-core dressing model](mass-comparison-charged-core-dressing.md)? The
source and dressing checkers are freshly rerun. This audit concerns a finite
Hamiltonian, not a theorem about all relativistic field theories.

## Exact orbit obstruction

The four labels have a distinguished shared reference. Their rooted permutation
group is S3. A rooted directed edge has three orbits: outward, inward, internal,
with sizes3,3,6. Neutral state alternatives form one orbit of size3.

Even if one allows INDEPENDENT rooted relabellings for the outer edge and the
two inner comparison roles, the1836 slots have30 orbits:

- 27 arrow-block orbits (three edge orbits in each of three roles);
- 3 state-block orbits (outer edge orbit times the transitive state-pair block).

This is a generous symmetry enlargement, not a derived incidence-preserving
source action. Tying all roles to the SAME relabelling yields311 orbits. The
source's exact incidence attachments would have to determine the admitted group.
Neither tested action makes all slots equivalent.

A diagonal one-body energy invariant under the generous action still has30
independent orbit coefficients. Doubling just one27-slot state orbit gives1863
rather than1836 while preserving every permutation in that action. This is an
explicit counterexample to symmetry-forced equal gaps.

Even imposing arbitrary permutations of ALL neutral slots would only fix their
common gap. It would not equate that gap to the separate elementary excitation
or remove the core energy. Such a much larger symmetry is not yet sourced.

## Charge-sector energy offset theorem

Let Q be the declared electric-charge analogue and U any fixed internal symmetry
with [U,Q]=0. A spectral projector P_q of Q commutes with every such U. Therefore
if [H,U]=0, so does

    H_lambda = H + lambda P_q.

The entire q sector moves in energy without changing its eigenvectors, internal
gaps or these symmetries. Choose q=+1; neither the vacuum nor the elementary
q=-1 energy changes. The proposed ratio changes.

Thus ordinary charge-preserving internal symmetries ALONE cannot fix relative
energies of these sectors. This does not exclude a further Hamiltonian algebra,
local field-theoretic law or a symmetry relating different charge sectors.
Global projectors need not be local operators in a field theory; this theorem
is about the finite model and the stated commutation constraints. In the present
binary model P_plus=c(1-e) is already a two-occupation operator.

A simple swap of the elementary charged occupation and a neutral comparison
occupation does not preserve Q. Equating their gaps by such an exchange would
require a new charge-changing structure, not the existing relabelling symmetry.

## A stronger candidate, and its own falsifier

A possible energy-protection law would be

    H = Delta K + sum_a A_a^dagger A_a,
    [K,A_a]=0.

If K is independently supplied and a state lies in the common kernel of the
A_a, then its energy is Delta times its K eigenvalue. To obtain the proposed
ratio one would need protected kernel states with K=1 and K=1836.

The dressing baseline can be REWRITTEN this way by CHOOSING

    K=e+sum_s n_s,
    A_s=sqrt(J)(n_s-c).

That rewriting is not a derivation of the law. Number conservation forbids the
previous transverse X perturbation, but does not protect a common kernel.
Replace the constraints by

    A_s(eta)=sqrt(J)[n_s-(1-eta)c].

This keeps Q, K, positivity and all neutral-slot permutations. At J=2 and
eta=1/10, every occupied slot costs1+2/100 while an empty core-associated slot
costs2*(9/10)^2. Complete occupation still minimizes the core-sector energy,
but its ratio is46818/25=1872.72. There is no common zero mode in that sector.
The vacuum and elementary sector retain their original energies.

Hence even the positive-square representation plus a counting charge is
insufficient. The actual next constructor is a SOURCE-DERIVED algebra or index
protecting nonempty kernels in the relevant sectors, together with the source
identification of K. Assigning K=1836 after counting desired slots would merely
move the assumption into the conserved charge.

## Verification

    python research/nima/checkers/check_mass_gap_symmetry.py
    python research/aspect/scc/scc.py check nima-mass-gap-symmetry

Orbit enumeration, invariant weights, small charge-preserving permutation tests
and the kernel-lift example are exact. The projector theorem is algebraic; the
finite permutation test is a regression illustration, not its proof for arbitrary
unitaries. Report: `results/mass-gap-symmetry.json`.

No measured mass or fractional correction is used as an input. Public constant
claims are unchanged: the mechanism remains conditional, not a mass derivation.
