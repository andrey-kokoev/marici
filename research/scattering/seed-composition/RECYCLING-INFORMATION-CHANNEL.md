# Unit eventual success is a lossy reduced channel, not reversible transfer

**Fourth batch, iteration 6 of 20.**

**Strength:** exact eventual-channel resolvent, direct operator-basis stationarity and entangled-reference witnesses. Not physical recovery or a source implementation.

[Previous error/recycling fixture](SELECTOR-PULSE-ERRORS.md) · [Checker](check_recycling_information_channel.py) · [Receipt](results/recycling-information-channel.v1.json)

## 1. Fresh eventual channel

Keep the declared coupling cos(epsilon)=99/101, sin(epsilon)=20/101, all corrected failure branches and their cross-sector coherence. Align the logical frames of plus and minus by the existing swap generator B.

For input blocks X_pp, X_mm, X_pm, X_mp in those logical frames, let

    Y=(X_pm-X_mp)/(2i),
    Z^0=Z-tr(Z)I2/2.

The eventual logical output is exactly

    (tr X_pp+tr X_mm)I2/2
      +eta_plus X_pp^0+eta_minus X_mm^0+eta_y Y^0.

The three coefficients lie in Q(sqrt(19)); their exact values are in the receipt. Illustratively,

    eta_plus ≈0.945527,
    eta_minus≈0.00766027,
    eta_y    ≈0.0316046.

The checker solves separate scalar and logical-traceless three-coordinate resolvents, then verifies the entire channel on sixteen matrix units:

    E(X)=immediate_success(X)+E(recycling_failure(X)).

Trace preservation and output support in plus are checked directly. The preceding uniform two-step contraction makes the success Kraus series converge and establishes uniqueness of this stationary solution. No sector dephasing or positive-square-root substitute is inserted.

## 2. Reduced irreversibility is explicit

Two orthogonal-sector inputs,

    rho_plus=P_plus/2,
    rho_minus=P_minus/2,

have the same reduced eventual output P_plus/2. Hence this rank-four-input reduced channel has no recovery map preserving arbitrary input information. Unit success probability does not make it an isometric transfer.

The success-time record already distinguishes these inputs to some extent: immediate success occurs with probability 9/25 for rho_plus and zero for rho_minus. This locates actual input information outside the reduced output without claiming that success time alone is a complete decoder.

## 3. Entangled-reference witness

On either doublet separately, the aligned logical channel is depolarizing with factor eta_plus or eta_minus. For a Bell-entangled input/reference its output Choi state is

    eta |Bell><Bell|+(1-eta)I4/4.

Its partial transpose has one eigenvalue (1-3eta)/4 and three eigenvalues (1+eta)/4. The checker verifies this matrix decomposition exactly, including radical-sign comparisons rather than floating-point thresholds.

For plus, eta_plus>1/3: reference entanglement survives but is degraded. For minus, 0<eta_minus<1/3: the two-qubit Choi state is PPT and separable, so the restricted reduced channel is entanglement breaking. The fixture's eventually successful minus preparation therefore does not preserve even an arbitrary encoded qubit's reference entanglement when histories are ignored.

This uses the two-qubit PPT/separability and Choi entanglement-breaking theorems, not a new machine-formal proof. The Bell matrices use logical output/reference coordinates, not all physical matter/field coordinates.

## 4. Where information remains

The complete coherent dilation has the form

    V_infinity=sum_{time,history} |time,history> tensor K_time,history.

Eventual Kraus completeness gives V_infinity* V_infinity=I. Thus orthogonal ground inputs have orthogonal joint output/history states. A maximally entangled four-level input/reference retains four equal Schmidt weights in that full dilation; the reduced two-level output alone cannot hold the full information.

The relevant information can reside in joint output/history correlations and the coherent measurement apparatus/environment, not necessarily in history alone. If branch records are physically measured and treated as classical, the full coherent dilation also includes the measurement environment. Its mathematical existence does not establish operational access to it, nor deterministic quantum recovery from classical labels.

## 5. Next history-assisted recovery gate

Test the exact successful Kraus branches on each doublet for deterministic history-conditioned unitary recovery. Determine whether their effects are scalar on the code or distinguish logical states. Separate classical record access from coherent apparatus access, and state any additional feedback requirements.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. No physical preparation, spin, annihilation or photon output is admitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_recycling_information_channel.py
python research/scattering/seed-composition/check_recycling_information_channel.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

Predecessor channels are freshly recomputed. Exact resolvent, stationarity, sign and partial-transpose checks verify the local receipt; isometric dilation and convergence statements remain explicitly scoped mathematical arguments.
