# Observation without a primitive execution direction

The operator proposed that evaluation/execution means the observer area is greater than zero. This experiment formalizes ONE precise interpretation, not a claim about geometric area or a proof that this definition uniquely captures execution.

## Objects

* X is an underlying mathematical structure, including its equality paths.
* F : X → Type is a family of possible witnessed contents.
* A probe p : O → X specifies observational support and access.
* Observe(p) = (o : O) → F(p(o)) is a coherent observation on that support.

The probe need not be an embedding; repeated access is allowed. No measure has been introduced. For this first model, positive support means an inhabitant of O. Nonempty support is not in general positive geometric measure.

Crucially, existence of the structure (X,F) does NOT mean that a global section of F has been chosen or even exists. Local observations can be available without a globally compatible choice.

## Checked laws and tests

`agda/ResolutionNetObservation.agda` passes a fresh safe Cubical Agda --ignore-interfaces check. Log: results/agda-observation.log. This also freshly checks the imported circle-cover regression. The whole-prototype audit receipt predates this addition.

1. Restriction along accessible support maps has identity and composition laws.
2. Restriction preserves equality: it cannot distinguish two already equal observations.
3. Empty support has an observation, but any two such observations are equal. It carries no distinguishable content in this model.
4. Witnessed comparisons of probes act by dependent transport. Their actions compose, and commute with restriction.
5. A point probe into the double cover has distinguishable true and false observations. Transport around a loop acts nontrivially despite unchanged support and endpoint map.
6. The same double cover has no global coherent observation over its entire base.
7. Positive support alone does not construct an observation: the constant empty fibre over Unit is a counterexample.

There is no time parameter, transition scheduler or reduction relation in this module. The witness action is a mathematical comparison, not a claim that an event occurred in time.

## Consequence for the proposal

A candidate definition is: execution is the manifestation of an existing witnessed structure through supported observation. This is a choice of foundational vocabulary, not a derived theorem identifying it with all conventional uses of execution.

If observer area means ACTUAL witnessed access rather than merely available support, the positivity condition should include a witnessed observation. Positivity of an unfilled interface alone does not suffice. Nor does positivity imply change, completion, or a unique answer.

What this model does establish is that meaningful observable distinctions and nontrivial comparison action need no primitive clock. What it does not establish is how physical time, causality, probability, geometric area, resource ownership or irreversible records arise.

The next structural question is compatibility of overlapping observations: which local witnesses can coexist or be glued, and which comparisons obstruct a global observation? A directed search for compatible observations can remain optional implementation machinery rather than the definition of computation.
