# Positive rest energy: completion and limits — iteration 3

## Established mathematical statement

For the explicitly completed internal/contact model of iteration 2, all retained states have internal energy bounded below by a strictly positive constant. Its lowest localized energy is enclosed exactly by

    13019412352006053/70368744177664000
      < E0 <
    52077649408024711/281474976710656000,

or approximately 0.185016977411665 model units.

A relativistic center-of-mass completion now makes this a genuine **conditional invariant rest energy**, rather than merely an internal eigenvalue:

    H_CM = sqrt(c² |P|² + epsilon² H_internal²),
    E_rest = epsilon E0 > 0,
    m_model = epsilon E0/c² > 0.

Here epsilon is a positive physical energy unit and c>0. The center-of-mass coordinate is new and independent of the original relative encounter coordinate. This is an explicitly added spectral kinetic law, not a substitution in the local contact boundary equations.

## Why the rest statement follows

H_internal is the self-adjoint positive continuum/contact operator already certified, not just its finite core matrix. It commutes with the independent center-of-mass momentum. Functional calculus therefore gives

    H_CM²-c² |P|² = epsilon² H_internal².

Restricting to the lowest internal bound-state branch yields the positive mass shell

    E(P)²-c² |P|² = (epsilon E0)².

At P=0, its energy is exactly epsilon E0. Adjoining a separate empty sector with Hamiltonian zero supplies a common vacuum reference without adding a scalar shift to the occupied Hamiltonian.

In one translation dimension the formal boost on a suitable smooth momentum-space core is

    B = i hbar/c² [H d/dp + H'/2],
    H'=c²p/H.

It satisfies [B,P]=i hbar H/c² and [B,H]=i hbar P. Twenty exact rational mass-shell examples check these coefficient identities. The algebraic argument, not that finite sample, supplies the general identity. A physical three-dimensional neutron spin representation has not been derived by this exercise.

## Which assumptions create the positive gap

1. A stationary source action beta*(sum of actual source projectors)/3 is added to the old core. This is a new law, not the unchanged ordered pulse programme. The fixture sets beta=1.
2. The continuum threshold is the supplied positive Delta=1/2. Contact and kinetic parameters remain eta=2, ell=kappa=1.
3. The relativistic center-of-mass law above is an additional kinematic completion.
4. Identifying the lowest resulting branch with a physical isolated neutron remains a separate physical assertion. The current mathematics describes the entire coupled bound system.

No physical energy unit, MeV number or mass measurement was used to fit E0. A positive conversion factor would preserve the sign; calibration is needed for a numerical physical mass, whereas justification of the action and particle sector is needed for the physical identification itself.

## Executable tests against an unjustified universal rest claim

### Remove stationary bank action

At beta=0 the original six bank zero modes return. For beta>0, bank trial vectors give an upper bound proportional to beta. Hence the full gap can approach zero with unchanged carrier and pulse matrices.

### Remove the external threshold

Choose a normalized sine packet supported on [a,a+L] with a>0, and set every core/memory component to zero. It vanishes at the contact, so the source action and contact form contribute nothing. Its Rayleigh energy is

    Delta + kappa pi²/L².

For Delta=0 these energies tend to zero. Rational bounds using pi<22/7 verify the approach explicitly. No local core charging term can eliminate that zero infimum of the full open-channel sector.

Thus positivity of the whole completed model is not a consequence of the carrier or source records alone. The positive-threshold and stationary-action assumptions are indispensable. Re-labelling the lowest coupled level as an isolated neutron mass would not supply them.

## Final disposition

**Completed:** a fully retained, conservative model with certified positive internal energy and a consistent positive invariant rest-energy extension, under explicit new assumptions.

**Not established:** a source-selected physical neutron rest law or a predicted physical neutron mass. Both zero-gap and positive-gap Hamiltonians remain compatible with the retained algebraic carrier and operation records. More computation of those same records cannot select between those physical laws without additional input.

Further source-supported progress requires justification or admission of the stationary action and particle-sector identification, followed by a physical energy/time calibration if a mass value is sought. Generating another arbitrary offset, threshold or charging strength would not resolve that obligation.

## Reproduction

```sh
python research/strominger/checkers/check_neutron_rest_energy_completion.py
```

Six checks passed. The checker freshly validates source hashes, rechecks the rational positive-gap certificates, reconstructs the proposed source action, tests the exact mass-shell algebra and records the zero-gap counterexamples.

Receipt: `research/strominger/results/neutron-rest-energy-completion.json`.
