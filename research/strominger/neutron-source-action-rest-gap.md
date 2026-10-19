# Positive full-sector energy from retained source actions — iteration 2

## Result and status of the new law

A **conditional full-sector positive-energy model** is now established, retaining all 24 neutron/bank coordinates. Its lowest stationary energy is approximately

    E0 = 0.185016977411665 model units.

Unlike the preceding rim-accessible result, this lower bound includes the formerly zero-energy bank states. No scalar rest offset was added.

The new dynamical assumption is explicit:

    H_core = K + beta A_source,
    A_source = (1/3) sum_{six labels, three frames} P_source(label,frame).

Every P_source is an actual previously retained canonical pulse generator. The factor 1/3 averages the three native frames, preserving the source C3 covariance. A_source is positive in the inherited metric.

**Making this source action stationary is a new Hamiltonian law.** It is not the old ordered-pulse programme, not a consequence of an isolated pulse receipt, and not a source-selected physical neutron rest law. The demonstration uses beta=1; strict positivity holds for every beta>0 under the other stated assumptions.

## Why the full gap is positive

All ingredients are positive forms. Exact ranks on the full 24-coordinate core are

    rank(K)=17,
    rank(K+A_source)=23,
    rank(K+A_source+W T)=24.

Thus there is no common zero vector of the native/seam energy, the source action and the rim contact. The coherent matched native-plus-bank direction left by the first two terms is observed by the last term.

With the existing strictly positive lead threshold Delta=1/2, the exterior continuum can be eliminated below threshold. At E=0 its contribution is a positive multiple of W T. The resulting finite Schur form is strictly positive; continuity gives a strictly positive lower spectral bound for the whole operator.

The proof works for every beta>0 because changing a strictly positive coefficient does not change the common kernel. It does not provide a beta-independent positive numerical lower bound.

## Exact numerical enclosure, not just an eigensolver estimate

For beta=1, kappa=ell=1, eta=2, Delta=1/2:

    13019412352006053/70368744177664000
      < E0 <
    52077649408024711/281474976710656000.

The interval width is less than 10^-14. The certificate uses exact rational square-root enclosures and LDL inertia for the continuum Schur form.

The low-energy reduction has 12 core dimensions, containing all six bank directions. The other 12 native directions remain explicitly accounted for and have energy at least 3/4, above the 1/2 continuum threshold. They cannot invalidate the ground-state bound.

## Energy ledger of the normalized lowest state

| Contribution | Model energy |
|---|---:|
| Previous native and seam energy | 0.020579273261555 |
| New stationary source action | 0.019303561616726 |
| Positive contact mismatch | 0.043912314586322 |
| Exterior kinetic energy | 0.039121253369700 |
| Exterior threshold energy | 0.062100574577362 |
| **Total** | **0.185016977411665** |

Both decaying exterior tails and the full core enter normalization. The energy is not obtained by counting memory slots or charging an unoccupied bank an arbitrary constant.

## Dependence on the supplied source-action strength

| beta | Lowest energy |
|---:|---:|
| 0.01 | 0.004370868579 |
| 0.1 | 0.043266168757 |
| 0.5 | 0.162054408685 |
| 1 | 0.185016977412 |
| 2 | 0.193676917188 |
| 10 | 0.199275270631 |

Bank trial vectors give E0(beta)<=beta times a finite source-dependent coefficient. Therefore E0 tends to zero as beta tends to zero. Selecting the stationary source action and its strength is a physical obligation, not something geometry or positivity alone resolves.

The positive external threshold is another essential input. If the asymptotic lead threshold is zero, arbitrarily broad wave packets far from the contact have energy tending to zero. One cannot claim a positive full-sector gap independently of that threshold either.

## Meaning for neutron rest energy

This construction closes the purely mathematical bank-zero-mode obstruction **under the stated new action**. It provides a positive candidate internal stationary energy for a retained neutron-labelled model.

It does not yet establish that this candidate is the physical neutron rest energy: the stationary law, physical sector identification, external threshold, and energy/time conversion are not source-selected. A center-of-mass dispersion identifying this internal energy with invariant mass has also not been derived here.

Accordingly, “positive full model energy proved” and “physical neutron rest mass established” remain different claims.

## Reproduction

```sh
uv run --offline --with numpy --with scipy python research/strominger/checkers/check_neutron_source_action_rest_gap.py
```

Six checks passed: exact source action, common-kernel removal, retained complementary sector, rational gap enclosure, normalized full energy accounting and conservative scattering after completion.

Outputs:

- `research/strominger/results/neutron-source-action-rest-gap.json`
- `research/strominger/results/neutron-source-action-rest-gap.npz`

The prior zero-bank model and its receipts were not overwritten.
