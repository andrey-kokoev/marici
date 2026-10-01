# History equivalence under recursive comparison and active updates

## Precise equivalence being tested

Hold actual maps C, the reference d and return r fixed. Two valid records may
differ in unit witnesses, comparison witnesses and triangle fillers while all
specified actual-map and residual readouts agree. This is a history equivalence
at fixed map data, stronger than merely having the same scalar mean.

The question is whether the same future operation preserves that equivalence.
The answer depends on the operation set.

## Fixed-frame comparison descends

For the implemented weak-return constructor,

    C_new=C2*r*C1,
    h_new=h2*r*C1+d*r*h1+d*u.

Suppose h_i changes by a closed z_i and u changes by a closed a. The actual map
is unchanged, and the new witness changes by

    z2*r*C1+d*r*z1+d*a.

This is closed by Leibniz because C1,d,r are closed. Therefore the actual map,
its reference residual and the comparison-boundary readout remain equal.
Induction gives the result for every finite word of this fixed-frame comparison
operation. Any readout depending only on those actual maps has the same result.

Exact tests perturb each of the14 coherent-history tangent directions at two
amplitudes. All28 trials preserve observations across all five four-input
bracketings and a further comparison. Retained histories can still differ.

This theorem does not cover history-dependent scheduling, weighting, or the
still-unspecified family-promotion endpoint rule.

## A protected update distinguishes histories

Use two copies X,Y of a zero-differential complex with one coordinate in degree0
and one in degree1. Initially d=r=I. Compare two coherent unit histories:

    history0: u=v=0,
    history1: u=v=E10.

Both have the same actual/reference/return maps, zero round-trip residuals and
zero triangle discrepancy. Give both the same active request: install the new
agreement frame

    C'=d'=diag(1,2), r'=diag(1,1/2),

while keeping their unit histories locked. Both round-trip equations still
hold, and both requested actual comparison residuals are zero. The triangle
condition becomes

    d'*u-v*d'=0.

It holds for history0. For history1 its value is E10, which cannot be filled in
the zero-differential complex. The implemented protected-update policy therefore
accepts the first request and rejects the second.

This is a counterexample to quotienting the full partial update protocol by
present response equality: the operation's domain is not a union of those
equivalence classes. It does not require a new history-dependent force.

## Permission to edit exposes a different distinction

If both histories may change under equal coefficient weights, both requests
succeed. For history1, coherence requires v_new=2u_new. The least-change version is

    u_new=3/5, v_new=6/5, cost=1/5.

History0 remains unchanged at cost0. These are costs of the declared policy,
not derived physical energies. A physical measurement would need an independent
link to the admission event or resource accounting before this could affect a
measured normalization.

## Active edit versus passive basis change

A passive B-side basis change also transports v to g*v*g^-1. In the example it
maps v=E10 to2E10 while u remains E10. The triangle then holds exactly, and the
coherent transported version requires no history edit. This control separates
an active request with frozen history from a mere change of presentation.

## Structural synthesis

The response quotient is sound for fixed-frame recursive composition. Complete
operational state also includes the history constraints governing future
admission. Those cannot generally be discarded under the protected-update API.

For the zero-differential example, a retained history u=v permits active frame
changes g satisfying g*u=u*g. Thus history determines a stabilizer of admissible
reference changes, even when its present residual readout is zero.

The next carrier-level question is which active reference changes are actually
admitted and how acceptance, rejection or retry enters the process. Restricting
to fully transported frame changes preserves the tested equivalence; allowing
protected active edits requires retaining an admission-sensitive history summary.
The current tests establish operational distinguishability, not a numerical
physical coupling or a new history-dependent dynamics law.

## Verification

    python research/nima/checkers/check_history_observational_congruence.py

Exact hidden-direction tests, five bracketings plus continuation, a two-history
accept/reject counterexample, permitted-edit minima0 and1/5, and passive
basis-transport control. The observability, policy and shared-leg prerequisite
checks also run.
