# Seed -> existing probes -> overlap kernel -> conditional exchange

## Existing geometry reused

`check_seed_probe_exchange_bridge.py` imports the existing `check_carrier_probe_adapter.py` rather than inventing feature entries. It restricts its two previously studied S4 function families to the actual six labelled seed occurrences. The ambient carrier is the 24 permutations of four vertices, not an identification with physical space.

The first family is the existing restriction of S12 fixed-label probes:

    f_(s,t)(g)=1[g(s)=s and g(t)=t].

The second is the prior direction-sensitive alternative:

    t_(s,t)(g)=1[g(s)=t].

Uniform counting and unit feature normalization are explicit representation choices, not derived physical calibration. They do not preserve the source S12 metric by a common rescaling, as the imported prior checker establishes.

## Computed kernels on the actual seed

| Probe family | Six-feature rank | AB/BA normalized overlap | What is forgotten? |
|---|---:|---:|---|
|Endpoint-fixing|5|1|The AB-minus-BA coefficient direction|
|Directed transition|6|1/3|No coefficient kernel on these six slots|

For endpoint-fixing probes, any two different unordered edge supports have normalized overlap 1/2. The shared reciprocal support has overlap one. Thus this Gram alone does not distinguish sharing one vertex from disjoint supports; original endpoint data must remain retained.

For directed-transition probes, contradictory assignments at a common source or a common target have overlap zero. Other distinct compatible assignments have overlap 1/3. This feature family therefore captures a different aspect of the port structure.

Both constructions use labelled endpoint data and have the existing carrier-relabelling covariance. They are different observations, not equivalent normalizations of one selected physical probe.

## Orientation and occurrence retention

The endpoint-fixing feature projection merges AB and BA. Retaining their coefficient difference alongside the visible sum recovers both exactly; other four seed coefficients remain independent. The checker verifies this recovery on a test vector, with the algebraic inverse (sum +/- difference)/2.

Exchange still uses six DISTINCT record slots. Equal carrier features do not identify records or executions: swapping the carrier's projection with record AB differs from swapping it with record BA. The full carrier-plus-record state retains the difference the carrier-probe view alone forgets.

## Existing exchange law, no fitted kernel

The checker uses raw indicator features with counting pairing divided by their common norm squared (2 for endpoint-fixing, 6 for transition probes). This is algebraically equivalent to unit-normalized features, with rational arithmetic throughout.

It then applies the SAME prior exchange operation to the actual four seam words, using a common test preparation q=0, w_AB=1 and other records zero. In both probe realizations:

- every executed corner preserves the declared quadratic budget;
- reversing the event word reconstructs the input exactly;
- the four-corner mixed output vector is nonzero.

The preparation and exchange interpretation are supplied test assumptions. No numerical feature was chosen to force that outcome, and no scalar physical measurement or energy was fitted. This establishes applicability of the algebra with computed kernels, not authorization of the dynamics.

## What is now settled and what is not

There is a concrete, tested seed-to-probe-to-kernel chain. We no longer need an arbitrary overlap parameter merely to study the conditional exchange candidate. The original occurrence information is retained, including the endpoint-fixing kernel.

But the source has not selected which probe describes the physical comparison, why counting is the physical pairing, or why a primitive traversal executes an exchange with a corresponding record. A derived Gram matrix licenses a mathematical unit-feature exchange construction; it does not establish that nature performs it. Physical preparation, event freshness/history and calibrated rung4 interrogation remain separate requirements.

## Discriminating predictions with identical named record readers

The checker now uses the same initial preparation (q=0, w_AB=1, all other w=0) and directly reads the same record coordinate in both models. No post hoc rescaling of those coordinates or change of observer is permitted.

| Protocol / reading | Endpoint-fixing probes | Directed-transition probes |
|---|---:|---:|
|AB then BA: final w_BA|1|1/3|
|AB then BA: w_BA squared|1|1/9|
|AB then BA: residual carrier budget|0|8/9|
|ABC: final w_BC|1/2|1/3|
|ABC: final w_CA|1/4|2/9|
|Mixed rectangle: BA record channel|1|1/3|
|Mixed rectangle: BC record channel|-1/2|-1/3|
|Mixed rectangle: CA record channel|-1/4|-2/9|

The mixed rows are signed differences of four separate outputs prepared identically. They are not a single fifth execution or physical interference amplitude. Squared record magnitude is a diagnostic, not a derived energy or probability.

The two-step protocol is already enough: exchange into u_AB, then into record BA, transfers exactly the normalized overlap <u_BA,u_AB>. Endpoint-fixing probes coincide, giving complete transfer; transition probes give overlap 1/3 and leave carrier budget 8/9. Both have the same total budget one, but different carrier/record allocations. The raw carrier coordinate pairing differs between models; the named record readings compared here use identical units and definitions.

This also holds on every one of the ten endpoint-composable primitive pairs: initializing record i and executing i then j gives w_j=Gram_ji. The checker tests all ten in both models. Hence the discrimination is not obtained by selecting a special numerical reader after seeing the answer.

### Shared predictions and source-selection boundary

Both models preserve the same primitive word history, give reversible events, conserve the declared total budget, respect the source relabelling with all marks transported, and exhibit nonzero mixed response for the stated preparation. None of these shared properties selects one kernel.

The prior probe construction selects endpoint-fixing features IF one requires literal restriction of the S12 fixed-label indicators. Requiring a carrier-feature readout that distinguishes all six directed seed coefficients without an additional orientation record would instead exclude that rank-five restriction. But the architecture only requires full retained records to remain recoverable; it does not require the carrier-probe projection alone to be injective. We cannot use that stronger condition to select transition probes without adding it explicitly.

Thus there is a small, concrete pair of differing conditional predictions, but no inspected physical source requirement selecting the model. The next justified decision would concern the actual preparation/measurement task that defines a primitive probe—not another recovery test or an adjustment of the output normalization.

## Verification

    python research/nima/checkers/check_seed_probe_exchange_bridge.py

Fresh exact checks pass, including the imported carrier-probe ranks, covariance and metric-mismatch controls, the six-row restrictions, four-corner execution, budget and inverse controls. No new formal Agda proof or physical prediction is claimed.
