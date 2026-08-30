# Fifth rung: govern ontology extension

## Question

Rung four requires an extensible hostile language. What prevents that rule from
admitting arbitrary names, sterile recursive terms, aliases, or preferred
conclusions?

## Admission object

An ontology extension is admitted only when it carries all six fields:

1. source provenance;
2. a well-typed term;
3. a pair or family it would distinguish;
4. an operational witness connecting it to a possible readout or constructor;
5. proof that it is not an alias of an existing coordinate;
6. a bounded decisive test.

If provenance, typing, target, or nonredundancy fails, reject it. If those
structural gates pass but the operational witness or bounded test is missing,
defer it. Admit only when all six pass. Speaker identity, popularity, current
vocabulary membership, and desired verdict are never substitutes.

## Exact attack

The checker exhausts all 64 Boolean evidence profiles. Exactly one is admitted,
three are deferred, and sixty are rejected. Six mutant policies, each omitting
one evidence gate, receive an explicit counterexample. Always-admit,
always-reject, name-whitelist, popularity, and sterile fresh-chain policies are
also rejected. Decisions are invariant under renaming and monotone under added
evidence.

Grothendieck's theta chain is the positive witness: it has source-labelled
two-port provenance, a separating relative readout, an exact ternary
obstruction, and a finite binary-repair no-go. The possible arity-four lift
under variable source amplitude is deferred because the required operational
witness or authorized multiplication has not yet been supplied.

A later four-atom hostile sharpens the deferred branch. Reflection-balanced
pairs at scales one and two can still have reciprocal off-seam zeros, so
pairwise reciprocal balance is not sufficient. The missing term must constrain
cross-scale interference among several reflected pairs; it remains deferred
until a source-derived multiscale invariant and operational constructor exist.

## Disposition

Rung five converts open-ended ontology growth into three typed outcomes:

`admit | defer with exact missing constructor | reject with exact failed gate`.

This policy is itself only relatively closed. A genuinely new kind of evidence
may force a later enlargement of the governance language.

Rung six now allocates finite experimental capacity among the admitted and
deferred obligations. See `sixth-rung-experimental-portfolio-controller.md`.

## Verification

Run `python research/aspect/checkers/check_five_rung_tower.py`.
