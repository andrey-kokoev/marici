# Charged-core dressing of the comparison programme

## Obligation and source

Forward realization: turn the existing shared-reference comparison domain into
stored excitation energy, then test whether its numerical ratio is forced.
The prior exact slot checker is freshly executed. The source supplies 1728
arrow-comparison slots and 108 state-comparison slots, not a Hamiltonian.
Neither the public constants table nor the measured mass ratio fixes parameters
in the following trial.

## Finite Hamiltonian

Introduce two binary occupations c,e and a neutral occupation n_s for every
comparison slot. The Hilbert space is a tensor product of 1838 two-level systems.
The core c controls dressing; e is a reference elementary excitation. Define

    Q = c-e,
    H = Delta_e e + mu c
        + sum_s [Delta_s n_s + J_s(n_s-c)^2].

Here symbols denote commuting number operators; gaps and stiffnesses are
positive and mu>=0. This Hamiltonian is new input, not derived carrier dynamics.
Q is a declared conserved quantity. Units use Delta_e=1 in the baseline.

In Q=-1, c=0,e=1 and every neutral channel is empty in the sector ground state.
Its energy above the vacuum is Delta_e.

In Q=+1, c=1,e=0. Each slot independently chooses between the empty penalty J_s
and occupied energy Delta_s. Therefore

    E_plus = mu + sum_s min(J_s,Delta_s).

If every J_s>Delta_s, the unique sector ground state fills every slot, with
neutral excitation gap min_s(J_s-Delta_s). This gives an obligatory complete
programme as simultaneous stored energy, rather than time-integrated work.
For uniform J=2, Delta_s=Delta_e=1 and mu=0, the energy ratio is exactly1836
and the fixed-charge neutral gap is1. Those parameter choices are explicit.

This is energetic stability within a restricted finite charge sector, not a
proof of proton stability or a lifetime against general interactions. The model
has no spacetime dynamics, fermionic statistics, antiparticles or baryon number;
its assigned charges do not identify actual protons and electrons. In particular,
charge alone in the real particle spectrum cannot distinguish a proton from a
positron. The carrier does not yet provide the extra particle-sector structure.

## Tests that preserve the declared lower structure

The Hamiltonian treats arrow and state slots as different types. Relabelling
carrier states preserves those types and therefore permits different gaps.
Changing the state-slot gap from1 to2, with stiffness3, leaves full dressing
stable but changes the ratio to1728+216=1944.

Other allowed scalar changes give:

| Change from baseline | Ratio | Result |
|---|---:|---|
| Bare core energy mu=1 |1837| Full dressing remains |
| Elementary gap Delta_e=2 |918| Full dressing remains |
| Stiffness J=1/2 |918| Empty slots preferred in positive sector |
| Stiffness J=1 |1836| All filling patterns degenerate; completion not forced |

The same construction on ANY finite slot set produces its cardinality at unit
gaps. Thus this Hamiltonian realizes the proposed count but does not select the
comparison domain from more general possibilities.

A charge-preserving neutral transverse term -g sum_s X_s is also allowed by
carrier relabellings. Subtracting the dressed c=0 vacuum, its energy per slot is

    sqrt((Delta+J)^2/4+g^2) - sqrt((Delta-J)^2/4+g^2).

For Delta=1,J=2,g=2 this equals (5-sqrt(17))/2, giving total804.98903568 rather
than1836; the elementary gap is still1. Even arbitrarily small nonzero g changes
the ratio. Q conservation does not protect the integer energy against quantum
dressing. The finite diagonal baseline is a mechanism trial, not a robust mass
prediction disguised as a count.

## Verification and remaining constructor

    python research/nima/checkers/check_mass_comparison_dressing.py

The count and diagonal minima use exact arithmetic. Independent enumeration of
all binary states for one through six slots checks the factorized spectrum.
The transverse example uses the explicit two-by-two eigenvalues and floating
arithmetic only for its reported decimal. Report:
`results/mass-comparison-dressing.json`.

The next upstream obligation is a source symmetry/constraint linking both slot
gaps to the elementary gap, fixing the bare core contribution and controlling
neutral quantum corrections. Without it, the mechanism is conditional and the
observed fractional tail must not be used to tune those free quantities.
