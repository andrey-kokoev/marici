# Exact Hamiltonian observer through complete retained T9

## Result

The declared interface-preserving coefficient Hamiltonian now has an executable energy observer through the COMPLETE retained native T9 state.43 exact checks pass.

It reads38 active linear coordinates per matrix-response channel and retains all99 kernel directions. Its energy equals the original candidate Hamiltonian exactly. J4 and the existing branch-summary convention are not redefined.

This closes the mathematical observer gap for this candidate. It does NOT select the candidate physically, derive an energy unit, admit a detector, recover the old four-mode rotor or construct a Postnikov tower.

## Candidate and observer contract

Reuse the independently classified S4 source-action combination from `interface-preserving-carrier-hamiltonian.md`. Its native coefficient generator A is real skew, has rank38, and acts on137 matrix-valued slots. The source field F has four scalar response channels.

The declared Hamiltonian is

    H(F)=||A F||^2/4,
    Omega=A/2,
    K=A^T A/2.

The observer constructs a rational independent row basis C of A. Let

    E=C^T(CC^T)^-1,
    N=I-EC.

Then CE=I38, EC projects orthogonally onto the active space, and N retains the99-dimensional stationary kernel.

The existing Hamiltonian-compatible WG verifies this supplied interface, producing

    D_active=C A E,
    Omega_active=E^T Omega E,
    K_active=E^T K E,
    G_active=E^T E.

The active form is nondegenerate, the active metric and energy Hessian are positive definite, and exactly

    C A=D_active C,
    K=C^T K_active C.

For z=CF, the observer returns

    H(F)=trace(z^T K_active z)/2.

It ALSO retains NF and the complete source coefficient field with declared provenance. Reconstruction is F=Ez+NF. Equal z or equal energy does not identify the full retained state.

The rational row-basis choice is a software coordinate convention, not a normalized apparatus mode frame or calibrated reader gain.

## Through the actual retained T9 value chart

The predecessor constructs the consistent complete native value chart T and leaf decoder L, with LT=I. It includes137 leaf values,32 intermediate means and32 final means, while carrying original metadata separately.

The target reader is explicitly

    z=C L F_target.

For every tested consistent target F_target=TF, this returns exactly CF and reconstructs the entire source field including its kernel.

The executable reader checks the supplied chart's dimensions, left-inverse identity and consistency T L F_target=F_target. A changed family mean with unchanged leaves is refused; arbitrary independent family values are not treated as native T9 states.

This is an explicit OBSERVER EXTENSION on retained leaf data. It is not claimed to be the original J4 alone, a physical detector or a new admitted comparison context.

## What is minimal and what is retained

K has rank38. If a linear amplitude reader P with m rows permits exact quadratic factorization K=P^T QP on the full coefficient space, then

    38=rank(K)<=rank(P)<=m.

The constructed38-row reader attains that lower bound.

This is minimality for a LINEAR amplitude interface with exact quadratic-energy reconstruction on the full137-dimensional coefficient space. It is not a minimum number of nonlinear scalar measurements, physical detector ports, primitive preparations, or coordinates on the restricted factored-leg preparation manifold.

The final-family mean reader has rank32. Together with C it has rank70, leaving67 additional static directions. No reader silently discards those directions. The observer stores NF in its original137-row representation, redundantly retaining all99 independent kernel directions; complete T9/source records remain available.

The kernel has zero energy and stationary dynamics only under THIS fixed coefficient Hamiltonian. Another source operation, context or energy model can act on it. The earlier source-memory kernel warnings are not withdrawn.

## Exact spectral interpretation

For Z=-A^2, the exact squared-angular-frequency bands are:

| Squared frequency | Dimension per scalar response channel |
|---:|---:|
| 32 | 36 |
| 128 | 2 |
| 0 | 99 |

The rational orthogonal projectors are

    P_low=Z(128I-Z)/3072,
    P_high=Z(Z-32I)/12288,
    P_zero=I-P_low-P_high=N.

Consequently

    H(F)=8||P_low F||^2+32||P_high F||^2.

These are angular-frequency and coefficient-energy relations in the declared model. They are not particle masses, quantum excitation energies, physical time standards or Postnikov homotopy dimensions.

## The readout hostile is resolved explicitly

The previously checked invertible factored-leg perturbation preserves every family mean while changing the active leaf data. The new reader distinguishes their energies:

    supplied fixture:2288/225,
    same-family-mean rival:23416/225.

Both values use the SAME declared energy convention. No reference value is refitted. This confirms that the required information was in retained data, not in the outer means.

Exact Cayley evolution transports z through C U E, preserves H, and leaves NF stationary. The checker verifies the same-generator identity through the complete retained target generator as well.

A separate kernel perturbation leaves z and H unchanged but changes the full state. The observer reconstructs that different state rather than identifying or resetting it.

## Exact arithmetic implementation and regressions

Initial runs timed out in generic symbolic positive-definiteness/rank routines; no passing result was recorded for those attempts. The final implementation uses exact rational Schur pivots for positive-definiteness and rational-domain matrix ranks. It does not replace proofs with floating thresholds or weaken the metric conditions.

New controls reject indefinite matrices with positive diagonal, singular semidefinite metrics and nonsymmetric metrics, while accepting an exact positive rational metric.

After the shared WG validation optimization, both prior owner-local suites were freshly rerun:

- `check_hamiltonian_descent_wg.py`:45 checks;
- `check_source_arrow_hamiltonian_descent.py`:54 checks.

The new observer checker freshly reruns the65-check interface-preserving classification and its pinned-T9 numerical dependencies. Counts are suite-specific, not independent evidence to add.

## Remaining source and physical obligations

The mathematical chain now includes an explicitly declared source-action combination, closed native coefficient dynamics, complete retained T9 transport and an energy reader.

Still supplied or unestablished:

- admission/implementation of the source-action combination, rather than mere membership in a matrix span;
- physical meaning and units of the coefficient metric, Hamiltonian and angular clock;
- an instrument measuring the required amplitudes/energy, with back-action and uncertainty;
- primitive leg/joint preparation and retained-environment/reset resource accounting;
- operation-preserving identification with actual native source constructors beyond the coefficient model;
- an actual Postnikov source, attaching data and rung-stage identification.

No mathematics here manufactures those physical inputs. Repeating WG or reading J4 again cannot determine them.

## Controllability follow-up

`shared-leg-controllability-audit.md` now derives input variations from the actual30 shared legs and audits the prior common family-gain law.29 checks show conditional scalar-energy regulation, not full active controllability: the current gain/drift orbit has only two continuous parameters, and even the generic shared-leg active-image ceiling84 is below152 active scalar coordinates across four response channels. Independent actuator admission is still required; the observer does not supply it.

## Verification and artifacts

    uv run research/strominger/checkers/check_retained_hamiltonian_observer.py

43 exact checks pass. No new Agda/Rzk formal closure or empirical calibration is claimed.

- `research/strominger/checkers/retained_hamiltonian_observer.py`
- `research/strominger/checkers/check_retained_hamiltonian_observer.py`
- `research/strominger/results/retained-hamiltonian-observer.json`

The result includes the full38-row reader and its energy Hessian.

Graph report: `ev-000000015909-d8692a10-206f-4cc6-95b9-346806f12762` (proposal `ep_57c22cee-1305-4a81-bed1-be65b89ae16b`). Admission records scoped provenance, not truth certification. No Git commit or push was authorized or performed.
