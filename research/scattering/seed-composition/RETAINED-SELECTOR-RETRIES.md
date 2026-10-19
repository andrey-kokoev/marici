# Retained selector retries: initial-sector selection, not deterministic logical preparation

**Fourth batch, iteration 2 of 20.**

**Strength:** exact eighteen-component failure channel, all-depth retry effects by induction, and reduced-state/readout disturbance. Not physical feedback implementation.

[Previous control construction](RETAINED-SELECTOR-CONTROLS.md) · [Checker](check_retained_selector_retries.py) · [Receipt](results/retained-selector-retries.v1.json)

## 1. Actual retained failure channel

The success operator is B=(3/5)P_plus. Failure is the retained controller map with components R_g from the previous turn, not a single positive square root of its effect.

The reduced channel, after ignoring that controller for statistics, is

    Phi(X)=sum_g R_g X R_g*.

Exact operator-basis checks give, on either diagonal sector block,

    Phi(X_plus)=(-4/25)X_plus+(2/5)tr(X_plus)P_plus,
    Phi(X_minus)=(1/5)X_minus+(2/5)tr(X_minus)P_minus.

Each R_g preserves both sectors. The channel is not equal to applying sqrt(P_minus+(16/25)P_plus) as a single failure operator. That substitution gets the failure probability right but the logical-state transformation wrong.

## 2. Complete retry tree and limiting effects

Every failure appends a fresh controller slot; old slots and first-success time remain records. A length-n history carries R_last...R_first. Summing their squared amplitudes gives the exact all-failure effect

    F_n=P_minus+(16/25)^n P_plus.

The cumulative success effect and the first-success effect at attempt k are

    S_n=[1-(16/25)^n]P_plus,
    S_first(k)=(9/25)(16/25)^(k-1)P_plus.

The checker verifies depths zero through eight without enumerating exponentially many histories, using the actual channel dual. The all-depth result follows from Phi*(P_plus)=(16/25)P_plus and Phi*(P_minus)=P_minus. At every depth S_n+F_n=I.

Thus eventual success probability is tr(P_plus rho), while the limiting all-failure effect is P_minus. Retries do not convert the minus sector. A conditional plus preparation is not deterministic preparation from arbitrary input.

## 3. Logical state depends on retained history

For plus input, the normalized reduced state after n failures has Bloch vector scaled by (-1/4)^n. Pure input has purity [1+(1/16)^n]/2. Ignoring the failure history therefore depolarizes the logical state even though its sector remains plus.

Pooling all success times in infinite retries gives Bloch factor 9/29. A pure plus witness then has purity 461/841. Immediate success preserves its plus logical state; delayed success need not give the same reduced state.

This is a statement about ignoring records, not intrinsic destruction in the joint system/controller map. In fact every plus failure branch satisfies

    P_plus R_g*R_g P_plus=kappa_g P_plus,

with kappa_g=2/125 for the two central branches and 19/500 for the sixteen half-quaternion branches. Hence each normalized plus branch is a unitary. The actual history may permit feedback correction, but implementing that correction is another control question. A measured branch label is an additional readout after failure, not a label read before the selector's coherent recombination.

## 4. Fixed-lead readout is a separate operation

A retained lead measurement reduces to Delta(X)=diag(X) when its record is ignored. On any ground input its sector weights become equal:

    tr(P_plus Delta(X))=tr(P_minus Delta(X))=tr(X)/2.

For plus input specifically,

    P_plus Delta(X_plus) P_plus=(X_plus+tr(X_plus)P_plus)/6.

Conditional plus survival has probability one half and Bloch factor one third. A lead readout can populate plus from minus but disturbs the original coherent sector and state. It is not included in the retry formulas above. The measurement record must remain accounted for; its reduction for statistics is not silent physical erasure.

## 5. Next feedback gate

Construct the history-conditioned polar correction of R_g on plus and a gauge-compatible extension on minus. Test whether it belongs to the native finite control library or needs a genuinely new rotation/controller. Account for feedback, intermediate work and all failure histories rather than calling retries lossless because their effects converge.

Root outcome remains null. Shared sources, historical receipts, atlas and formal contracts are unchanged. Physical spin selection, charge conjugation, annihilation and photon output remain unadmitted.

## Reproduce

```sh
python research/scattering/seed-composition/check_retained_selector_retries.py
python research/scattering/seed-composition/check_retained_selector_retries.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

All predecessor maps are freshly recomputed; exact arithmetic tests the actual reduced channel on an operator basis. History-tree induction and limiting geometric sums are explicitly stated mathematical arguments, not new machine-formal or physical admission.
