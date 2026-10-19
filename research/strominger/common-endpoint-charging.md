# Common signed endpoint-rotor charging on the three source graphs

## Construction

One constructor now accepts the actual internal graph, exterior leads, charge and shared field coefficients. It preserves the supplied source kinetic operator K, including the elementary spinor's complex hopping phases.

Let L be the unweighted internal electric graph Laplacian, R=L^+ its inverse on zero-sum charges, and S the map from lead fluxes to their attached vertices. For charge q, site occupation N_i and integer endpoint/lead momenta n, ell, impose

    G_i=n_i+(S ell)_i-q N_i=0,
    sum ell=q, sum n=0.

The physical basis over matter position i has n=q e_i-S ell. A hop i to j shifts endpoint momentum by q(e_j-e_i), preserving every G_i. Products of relative endpoint factors telescope on loops; the intrinsic K phases remain untouched.

The common Hamiltonian is assisted source hopping plus

    (beta/2) n^T R n + (beta/2)||ell||² + (eta/2)q².

Therefore the exact matter block at fixed lead flux is

    H_ell = K + diag_i[(beta/2)(q e_i-S ell)^T R(q e_i-S ell)]
                 + [(beta/2)||ell||²+(eta/2)q²]I.

This is one rule, with no particle-dependent offsets. It generalizes the existing elementary endpoint parent by deriving the internal charging matrix from each graph rather than copying its K4 coefficient beta/8 to arbitrary graphs.

The retained field convention is unit electric cost per source link/lead. The matter hopping strengths still come from the native coefficient operator and need not equal the field weights. Charges are the prior assigned +1, 0, -1. Beta=3/5 and eta=1/5 are the prior common fixture.

The no-matter sector has q=n=ell=0 and energy zero, with the same field variables. This supplies the common empty reference.

## Source and metric retention

Proton and belt K are reconstructed from the actual weighted matter/link adapter. Their metric is M=diag(source mode norms), and M K is symmetric; connected positive graph weights establish K>=0 and its simple constant kernel. The adapter's underlying native-energy-store hash is checked.

Electron K=I-Q is exactly the conference-matrix operator of the prior endpoint parent. Q*=Q and Q²=I are checked. All four triangular source Wilson phases remain +/-i. No link minimization cancels them.

For K4, R=(I-ones/4)/4. The new constructor consequently recovers the prior electron formula exactly:

    H_ell=K+(beta/4)diag(ell)
             +[5 beta||ell||²/8+beta/8+eta/2]I,
    sum ell=-1.

The inherited adapters describe invariant selected source sectors: 12 proton modes, 18 belt modes and four elementary face-line modes. The remaining native carrier directions are recorded; a field interaction on those complements is not supplied here. The ground comparisons below concern these selected-sector parent models.

## Fresh energy results

All values use the same empty reference and fixture units.

| Sector | Signed charge | Ground energy |
|---|---:|---:|
| Proton | +1 | 0.5491721529617364… |
| Neutron belt | 0 | **0** |
| Electron | -1 | (59-sqrt(1609))/40 = 0.4721914439934211… |

The proton result is enclosed by rational weighted-LDL bounds in all twelve unit-lead blocks. Every other integer flux with sum one has squared norm at least three. Positive source K and internal field energy therefore give the global outside-block bound 3 beta/2+eta/2=1, above the computed ground. This is not a finite-flux cutoff estimate.

The electron block characteristic polynomial is checked exactly for each of its four unit-lead fluxes. The same outside-flux positivity bound certifies its analytic ground globally. Its ground multiplicity is four, as in the prior quantum parent.

For the neutral belt, ell=0 gives exactly K and its rank-one zero mode. Any nonzero integer flux with sum zero has squared norm at least two and energy at least beta. Therefore its zero ground is exact.

Consequently

    E_p/E_e = 1.1630285977172172…,
    (E_b-E_p)/E_e = -1.1630285977172172….

Both fail the retained mass comparison. In particular, the neutral result holds for all beta>0, eta>=0 under this purely external-charge law: rescaling its clock cannot create belt rest energy.

## Meaning of the result

The desired common typed parent is now executable, and it reproduces the strongest prior elementary construction rather than a flat substitute. The result also pinpoints its missing energy-bearing content: a neutral interaction or internal charge sector. A neutral belt does not acquire energy merely by inserting its positive norm into an external electromagnetic Gauss source.

The prior neutral-mediator and seam-occupation models are possible named input branches for that content. Their energies must be added through actual compatible operators and a common vacuum, not pasted in as fitted sector constants. The failed common-gap and reduced-electrostatic branches remain controls.

## Verification

```sh
python research/strominger/checkers/check_common_endpoint_charging.py
```

Nine reported checks passed, plus internal assertions covering every physical-basis Gauss solution, electric norm identity, hopping charge shift and elementary characteristic polynomial. Charge reversal with reversed lead flux preserves the proton block energies. Invalid total lead charge is rejected. The benchmark is opened only after energy bounds are constructed.

Files:

- Core: `checkers/assemble_endpoint_charging.py`.
- Frozen model: `contracts/common-endpoint-charging.json`.
- Exact operators, resistance matrices, energy intervals and source hashes: `results/common-endpoint-charging.json`.

No shared source or result store was modified.
