# Finite retained records construct the neutral mediator vertex

## Result

A source-addressed signed-gate construction produces the complete neutral displacement vertex, including its diagonal terms. A pool of finite neutral records has the oscillator ladder as its fixed-occupation limit. The heavier-belt ordering survives at finite pool sizes.

The direct elementary-rest-energy test also has a definite result: this rule gives approximately 71.3601 keV splitting when its clock unit is the electron rest energy, against the retained reference 1293.3327 keV. The ordering is explained; that direct scale identification fails.

## 1. Two source-controlled signed record gates

Use the existing all-face projector P_s=|W_s><W_s|, a neutral record flip X and its two signed controlled extensions:

    R_plus  = (I-P) tensor I + P tensor X,
    R_minus = -(I-P) tensor I + P tensor X.

Each is a self-adjoint involution in the inherited metric. Both retain the carrier and record and are undone by a second application. The spectator sign matters even when it looks like an inactive endpoint phase: after source control it is relative phase information.

Apply the existing uniform generator Q_R=(I-R)/2 separately to both:

    Q_plus + Q_minus = I-P tensor X.

This identity gives the required flip vertex with a SCALAR diagonal term, not a species-dependent P term. There is no discarded contact self-energy. This differs from the failed single exchange-projector construction.

The source inputs are the actual normalized all-face projector and the signed record maps. Tensor copies and controlled signed extensions are the construction operations in standard matrix semantics; this is not a claim that these new gates were already words of the original three-stage circuit. As in the prior uniform-local-core construction, the claim is explicit uniform realization, not uniqueness.

## 2. Pool normalization and common empty reference

For M neutral records set lambda_M=g/sqrt(M), with the same g=1/2 for both carriers. The complete finite law is

    H_full = K + sum_j n_j + lambda_M sum_j(Q_plus,j+Q_minus,j).

With no occupied carrier P=0, its ready-record vacuum energy is

    E_empty = M*lambda_M = g*sqrt(M).

The identical scalar appears in every occupied sector. Subtracting THIS SAME reference gives

    H_full-E_empty = K + sum_j n_j
                    - (g/sqrt(M))*P sum_j X_j.

The sign of the displacement is equivalent to the previous oscillator vertex by record-parity reversal. This subtraction changes neither species ordering nor a breakup comparison using the same pool. The preparation of the ready record pool is retained input, not an erased resource.

The collective 1/sqrt(M) coefficient is the declared equal-strength normalized-pool rule. It is not inferred from the number of seams or chosen from the neutron mass. It gives a finite limiting vertex rather than divergent coherent strength as the pool grows. Every occupation generator uses the same elementary gap unit.

## 3. Derive the oscillator ladder

In the permutation-symmetric record sector, let |n> be the normalized sum of all record strings with n occupied bits. Then

    <n+1|sum_j X_j/sqrt(M)|n>
      = sqrt((n+1)*(1-n/M)).

On each fixed occupation range this tends to sqrt(n+1), the oscillator raising coefficient. sum n_j reads n exactly. Thus the earlier neutral oscillator and its displacement vertex have an explicit finite-record realization.

In the unnormalized basis D_n=(n!/M^(n/2))*sum_(|string|=n)|string>, the metric is

    <D_n,D_n> = n! product_(k=0,...,n-1)(1-k/M).

The raising coefficient is 1 and lowering coefficient n*(1-(n-1)/M). All reduced energy arithmetic is rational. Individual records and histories remain in the full tensor construction; the symmetric subspace is the field-state sector, not deletion of record distinctions.

Other permutation irreducibles have effective pool M'=M-2k and occupation offset k>=1. Their ground energy is bounded below by

    k-g^2*M'/M > 0.

Hence they cannot undercut the negative symmetric-sector energies. The calculated minima are full-pool ground energies, not only symmetry-restricted candidates.

## 4. Finite-pool energy controls

For the proton, P projects onto its coherent return. The record ground state factorizes and has exact energy

    E_p(M) = M*(1-sqrt(1+1/M))/2.

For the belt, the inherited two-mode carrier does not commute with P. Exact Schur-tail bounds retain that interaction and all omitted finite-pool occupations.

| Neutral records M | Certified belt-minus-proton interval |
|---|---:|
| 16 | 0.13713311567905 to 0.13713311568013 |
| 64 | 0.13900355494968 to 0.13900355495930 |
| 256 | 0.13948602169875 to 0.13948602171438 |
| Oscillator | 0.13964821899185 to 0.13964821901016 |

These controls preserve the same carrier contacts, spin action and species labels. They change only the size of the neutral field apparatus. No assertion of a unique physical M is made.

## 5. Elementary gap versus rest energy: construct and test the reference

The same occupation generator (I-Z)/2 has ready energy 0 and occupied energy E_star. Restrict a charged reference to one empty vacuum and an occupied logical spin doublet:

    H_e = 0 direct_sum E_star*I_2,
    Q_e = 0 direct_sum -I_2.

Its sector excitation energy above the common ready reference IS its gap. This removes the arbitrary coherent-sector offset in this particular occupation-sector constructor; it does not extract a physical electron Hamiltonian from a return projector. The neutral pool has P=0 in this reference and the same empty energy as elsewhere.

Now test the direct physical identification E_star=m_e*c^2 without changing g, the contact profiles or either species offset. Using the existing retained rounded mass receipt only AFTER the law is frozen:

| Increment | Electron rest-energy units | keV |
|---|---:|---:|
| Constructed oscillator-limit splitting | 0.139648219 | 71.3600933 |
| Retained neutron-minus-proton reference | 2.530989 | 1293.3327215 |

The intervals are disjoint. A common bare offset cannot repair this difference. We do not feed the missing factor back into the vertex.

## Next constructor

The neutral field is no longer merely an independently postulated infinite oscillator: its vertex and ladder have explicit finite signed-record constructions. Remaining source input is the physical admission of the controlled signed extensions and normalized record pool, together with the actual elementary charged sector. The direct common-gap electron identification has failed its quantitative test.

The next productive comparison is an interacting elementary carrier under the SAME source-addressed field action, rather than scaling this splitting to fit the reference. Its rest gap, polarization and record preparation must be compared in one common empty sector. No nuclear cross-carrier binding is inferred from these single-particle energies.

## Reproduce

    python research/voevodsky/checkers/check_neutral_mediator_mass_bridge.py
    python research/voevodsky/checkers/check_finite_record_mediator_constructor.py

Results: `results/finite_record_mediator_constructor.json`. Exact tests cover the signed-gate identities, weighted Hermiticity, occupation reference, rational finite-pool ground brackets, non-symmetric-sector bounds and disjoint held-out mass intervals. Source and reference receipts are separately hashed. The infinite-field checker retains its previous result when the pool parameter is absent.
