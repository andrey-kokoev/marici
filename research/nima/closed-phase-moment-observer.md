# A closed phase-sensitive observer for the returning barycenter

## Next operation, not a new dynamics

Freshly read the previous memory/first-moment packet. Keep its conditional conservative swap unchanged and ask what observer can predict the active and record centers without reconstructing all amplitudes.

The original observation profile contains eight real quadratic quantities: two budgets and the three first-moment components of each sector. Barycenters are their ratios when the relevant budget is nonzero. The profile deliberately does not include every possible joint coherent observable.

Let x be the twelve carrier coefficients, w the twelve record coefficients with Pw=0, P the uniform mean projector, and X_j the diagonal cone-centroid coordinate matrices. Their mean positions vanish, so P X_j P=0.

## Required additional records

Write

    A=||x||^2, B=||w||^2,
    a_j=x^dagger X_j x, b_j=w^dagger X_j w.

Add the coherent mean budget and two phase-sensitive three-vectors:

    h=||P x||^2,
    s_j=2 Re((P x)^dagger X_j x),
    r_j=2 Re((P x)^dagger X_j w).

These seven additional quantities close the observation exactly. Under the already chosen swap,

    A_next=h+B,       B_next=A-h,       h_next=h,
    a_next=b+r,       b_next=a-s,
    s_next=r,         r_next=s.

No new force or numerical response gain was fitted. These identities follow by substituting x_next=P x+w and w_next=(I-P)x, and using P X_j P=0.

The checker verifies all fifteen as exact quadratic-form identities on the zero-mean record subspace, so the statement is not limited to the two previously prepared contrast states. Real matrices define Hermitian identities as well; the direct trajectory controls use rational real coefficients.

## A precise minimality result

Represent the physical coefficient domain as twelve carrier coordinates plus eleven independent record contrasts. Restrict all quadratic-form matrices to that domain.

- The eight original forms are linearly independent.
- Their span together with the eight evolved forms has dimension fifteen.
- The fifteen displayed forms are independent and close under evolution.

Thus fifteen is the minimal dimension of a **linear space of quadratic readouts** containing the requested eight observations and closed under this update. This is not a lower bound on every imaginable nonlinear encoding, and not a count of independent particles or geometric dimensions.

This also does not mean that all phase information is recovered. The profile predicts the requested budgets and first moments; other probes may require more data. Complete amplitudes/history remain retained separately.

## What the earlier two runs teach in these coordinates

At the moment when the two preparations have identical carrier and record intensities, their r vectors have opposite transverse components. The next active first moment is b+r, so this is precisely the information needed to predict their different returning centers.

An intensity-only observer is therefore insufficient. The missing quantity is not another spatial point: it is a correlation between the readable carrier mean and the stored record.

The prior conserved first moment of the full coherent sum x+w included all carrier-record cross terms. The present r contains only the mean-record part. The omitted contrast-record cross term is invariant under this swap and is not needed to propagate this chosen eight-observation profile. The closed observer is not claimed to recover that additional joint readout for arbitrary initial states.

All equations use coefficient normalization. Multiplying all budgets, first moments and correlations by 20/3 restores the previous local-mode norm convention without changing barycenters.

## Physical boundary

The memory law is still the explicitly selected conservative projector lift; it has not become a uniquely selected physical law merely because its observer now closes. The positional weighting remains an intensity reader, not a derived matter-energy density. Opposite relative phase is not automatically opposite electric charge.

This step constructs a predictive reduced observer and identifies exactly which retained phase correlations it needs. It does not supply electron identity, a mass scale, physical time, force or recoil.

## Verification

`python research/nima/checkers/check_closed_phase_moment_observer.py` passes exact rank and operator identities, two three-advance histories and five general rational-state transition controls. Receipt: `results/closed-phase-moment-observer.json`. No old dynamics or source geometry was changed; no fresh Agda proof or ledger entry is claimed.
