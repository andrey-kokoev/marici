# Port access as a physical boundary of task-relative sufficiency

Status: exact ideal-network bridge and proposed scientific target. Not an assembled apparatus or a completed native-query realization.

## Result

A physical input-port restriction can induce exactly the previously computed coordinate quotient, without a software rule forbidding arbitrary queries. The appropriate carrier is a persistent routing configuration, not merely the instantaneous RF field.

Let g be an even permutation of four port labels and let P_g be its ideal four-input/four-output transfer matrix. For a unit excitation at input s,

    P_g e_s = e_{g(s)}.

Access to one source input exposes one column: four possible responses, with three of the twelve A4 configurations in each class. This is the quotient g -> g(s).

An output-side permutation h gives

    P_h P_g e_s = e_{h(g(s))}.

Thus ALL output-side A4 transports preserve this quotient. Reading the destination, or testing one destination after selectable output transports, requires no knowledge of the other columns. With an independently supplied Boolean pointer this is the eight-state quotient (g(s),b); routing alone supplies the four-state carrier quotient, not the XOR pointer.

The endpoint restriction is now physical: which input may be energized and on which side controls act. Four output positions can be measured together or resolved through a common calibrated probe plus output routing. Neither a fixed source nor a fixed probe alone automatically selects a geometric face.

## Exact enlargement and predicted failure

Keep the network configuration fixed and permit excitation at a second input r != s. Two column responses determine an A4 permutation completely: two image assignments leave two S4 completions, exactly one even. Consequently the sufficient carrier description grows from four classes to twelve, or from eight to twenty-four states if the Boolean pointer is included.

Concrete pair, using image-list notation:

- G0 = ABCD (identity).
- G1 = ACDB (A fixed, B->C, C->D, D->B).

Input A exits at A for both. Every output-side transport preserves their equality at that input. Input B exits at B for G0 and at C for G1.

Any deterministic predictor whose retained network state is only the first column must predict the same second-column response for both and therefore fail on at least one. A randomized predictor conditioned only on that column must likewise give the same response distribution for both. Supplying the original configuration label to that predictor would change its available state and evade rather than pass the test.

## A sharper side-of-access theorem

Input-side permutations act as P_g P_k e_s = e_{g(k(s))}. This descends through the first-column quotient for all g if and only if k fixes s. There are three such input-side A4 permutations, compared with all twelve output-side permutations.

Thus the experiment has an asymmetric intervention prediction:

- Arbitrary output-side transports preserve the sufficiency of one column.
- Input-side transports that fix the accessible input preserve it.
- Input-side transports that move that input can expose distinctions erased by the reduction.

This gives a precise physical intervention boundary, stronger than a generic hidden-state reveal. It also states exactly why adding arbitrary controls would invalidate a claimed reduced model.

## What is retained, and what is measured?

The persistent network configuration contains all twelve possibilities. A first-column response is an observation of that configuration. It is not itself a complete physical copy of it.

A single one-hot field e_g(s) has only four possibilities. No later output-only operation can recover which of the three indistinguishable networks generated it. Opening a second source input interrogates the retained network with a new preparation; it does not reveal information magically retained in the first field.

This distinction determines the experimental ontology:

1. **Network identification version:** the physical state is the persistent configuration; source access is the task. Most direct match to the quotient theorem.
2. **Reduced-apparatus version:** replace the network by a device retaining only its first-column equivalence class. It reproduces the first-input task, but cannot uniformly reproduce second-input responses without additional retained state.
3. **Native controlled-pointer realization:** additionally implement the declared query XORs and successor retention. Neither of the preceding versions supplies this automatically.

The first is the best next candidate. The second tests reduction physically rather than solely as a predictive model. The third remains a larger engineering project.

## Medium-level experiment design

Compare two descriptions of the same held-out physical network settings:

- Full model: independently calibrated port transfer and transport composition.
- Reduced model: retains only the response class for one accessible input; no hidden setting labels.

Evaluate a restricted task with output-side interventions, then enlarge access to a second input or a specified input-side transport. Predict in advance the collision pair, equality domain, separating intervention, output channels and response margins. Include multiple pairs and independently calibrated transports, not one manually selected successful contrast.

For a stronger realization comparison, construct an actual reduced device with the same task interface and declared limited retained state. Do not equate a reduced software predictor with physically erasing the full device. Performance under task enlargement is a comparison of two architectures, not just two displays of one signal.

## Nonideal RF is part of the hypothesis

Real cable routes can expose configuration-dependent loss, phase, delay, reflections and crosstalk even at the first input. The ideal permutation quotient survives only when those differences are absent or bounded within a predeclared task tolerance across its frequency/time domain. Equality at one carrier does not establish broadband or transient equivalence.

This is a primary experimental issue, not a detail to normalize away. Establish common-path/fixture behavior and matching; retain complex response and power; test that the supposedly hidden configuration does not leak through unused-port loading or controller state. If first-input responses distinguish the pair, the intended equivalence claim fails on that domain. A nuisance-aware alternative quotient requires a separate model and fresh predictions.

An RF routing network is generally a multiport object (four inputs and four outputs here), not an arbitrary four-by-four matrix magically supplied by four receiver channels. Present KrakenSDR infrastructure provides a possible coherent receiver; the historical plan supplies no verified permutation router. No specific topology is selected here.

## Scientific positioning and decisive question

This mechanism follows ordinary linear network theory. The potential Marici contribution is the task-relative reduction and the exact intervention boundary, not unexpected RF behavior. A hand-wired pair alone would be a pedagogical example.

To merit the scientific target, demonstrate independent composition prediction, robust restricted-task equivalence, predicted failure under task enlargement, and preferably portability of the same quotient rule across distinct physical realizations. Compare with standard observability/minimal-realization methods directly. The finite ideal theorem itself should not be presented as new RF physics.

We now have a concrete positive answer to the earlier question: port access CAN induce the coordinate restriction naturally within a routing architecture. We have not established that the existing kit has this architecture, or that an arbitrary network exhibits it without being engineered to do so.

## Verification

    python research/strominger/checkers/check_endpoint_continuation_cells.py
    python research/strominger/checkers/check_port_access_sufficiency.py

The second checker verifies all four input choices, all twelve permutations, the three-element fibers, all two-column identifications, both intervention sides, and the explicit collision/separation pair. It checks source digests from the first receipt. Both are finite ideal-model checks, not physical measurements.

Related analysis: `research/strominger/endpoint-continuation-cells-v1.md`.
Receipt: `research/strominger/results/port-access-sufficiency/verification.json`.
