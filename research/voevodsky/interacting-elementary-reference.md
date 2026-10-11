# The actual electron spinor under the same neutral field

## Result

The all-face field contact of the existing four-face spinor is exactly its collective rank-two return. Both logical spins couple equally. The same neutral mediator lowers its occupation-sector rest energy from one clock unit to three quarters of a unit.

Normalizing the proton–belt splitting by THIS interacting elementary state gives

    0.18619762532247 < (E_belt-E_proton)/E_e < 0.18619762534688.

The corresponding held-out readout is 95.146791 keV, versus the retained reference 1293.332721 keV. Electron dressing changes the earlier 71.360093 keV readout but does not close the numerical comparison.

## 1. Source-addressed contact, without selecting a spin

Read the actual face projectors P_i from `electron_tetrahedral_spinor_store.json`. They obey

    sum_i P_i=2I_2,
    Jz=(P_0z,P_1z,P_2z,P_3z)/sqrt(2),
    J^dagger J=I_2,
    N_e=J J^dagger.

All six unordered pairs of tetrahedral faces are geometrically shared edges. Apply the same equal-phase edge-sum rule used for the other carriers, with local negative-polarization projection on each incident face.

Each face occurs in three edges. Writing Bz=(P_i z)_i, the raw edge-sum map is (3/sqrt(2))*B. Its Gram is 9I_2. Normalizing gives exactly J, so

    field contact P_e=N_e.

This is a rank-two projector, not a chosen coherent spinor vector. Source rotations preserve J and N_e; the full-rotation central sign remains -I on the logical doublet. No spin component is deleted to obtain a scalar energy.

## 2. Kinetic control and occupation offset

The supplied spinor stages are L,N_e,N_e. Their uniform projector-defect control is

    K_e=(I-L)+2(I-N_e).

Its spectrum is 0 with multiplicity two, 2 with multiplicity two and 3 with multiplicity four. It annihilates N_e and commutes with it. Any positive weights on these same defects leave the following ground-energy result unchanged.

This is a carrier defect-energy control, not a derivation of the elementary rest offset. For that offset we retain the preceding occupation-sector constructor: one occupied elementary core costs E_star, with an empty core costing zero. The one-particle sector has baseline mu_e=1 in elementary-gap units and contains the actual eight-coordinate spinor. The zero-particle vacuum is separate, not a duplicated spinor.

## 3. Same mediator, same empty reference

Use exactly the preceding scalar-field law with Delta=1 and g=1/2:

    H_e = 1 + K_e + a^dagger a + (1/2)N_e(a+a^dagger).

In the finite-record realization replace the oscillator terms by the same neutral pool and signed controlled gates. Its scalar g*sqrt(M) contribution is subtracted against the SAME empty pool reference used for proton and belt. No elementary-specific vertex, record scale or field baseline is introduced.

On the coherent doublet N_e=I and K_e=0. The mediator displacement therefore gives

    E_e = 1-g^2/Delta = 3/4.

The logical doublet is retained while the neutral field is displaced. On the remaining carrier modes P_e=0; their undriven ground energies are at least three units including the occupation offset, so they cannot undercut this state. Carrier charge and number are unchanged.

For M neutral bits the exact result is

    E_e(M) = 1 + M*(1-sqrt(1+1/M))/2.

The same displacement shift occurs for the coherent proton profile. It is their different sector baselines, not a different field treatment, that distinguish their total energies.

## 4. Compare using the dressed elementary denominator

The earlier bare-gap comparison used E_e=1. The common-field comparison instead divides by the actual E_e(M), or 3/4 in the oscillator limit.

| Neutral records | (belt-minus-proton)/interacting elementary rest energy |
|---|---:|
| 16 | 0.18192512942623 to 0.18192512942766 |
| 64 | 0.18509892377706 to 0.18509892378986 |
| 256 | 0.18592095903704 to 0.18592095905788 |
| Oscillator | 0.18619762532247 to 0.18619762534688 |

The finite-pool numerator bounds include omitted occupations and non-symmetric record sectors. The elementary denominator has an exact algebraic expression, enclosed rationally.

Only after this calculation, use the retained reference electron rest energy 510998.95 eV to compare dimensionless predictions:

    predicted increment: 95146.7910323 to 95146.7910447 eV,
    reference increment: 1293332.72146155 eV.

The intervals are disjoint. Dressing the actual spinor under the same field does not generate the missing mass ratio. No fitted offset is returned to the Hamiltonian.

## What is now localized

The neutral vertex, finite-record realization, common empty reference and full-spin elementary field contact have explicit constructions. For this profile, changing positive spinor defect weights cannot change its rest gap: the entire coherent doublet is dark to those defects.

The remaining elementary input is its occupation-sector charging/rest-offset law. Choosing baseline one was an executable reference construction, not a value derived by the spinor return. A source-derived correction must change a real sector energy or interaction, not merely rename the defect gap. The proton common baseline and complete absolute mass readout also remain to be selected.

The present construction uses the checked four-face spinor; it does not import the distinct proposed five-cell geometry as an already equivalent dynamical carrier. Nuclear binding remains a separate composite-sector calculation.

## Verification

    python research/voevodsky/checkers/check_interacting_elementary_reference.py

Results: `results/interacting_elementary_reference.json`. Exact checks reconstruct the stored face projectors, all-face contact Gram and rank-two return, kinetic eigenspaces and finite-pool dressed ratios. The source store, field results and held-out reference are separately hashed. No empirical input selects the field or occupation rule.
