# Actual seed under the existing section-field promotion rule

## Correction to the preceding audit

`section-field-promotion-cycle.md` already specifies the section-to-field successor E+=sum_(sigma:S) X with evaluation (sigma,x)->sigma(x). The earlier statement that no explicit endpoint promotion rule had been found was incomplete. What remains unestablished is the selection of this candidate as the intended physical transport and its connection to the confirmed transport-role diagram.

This experiment applies that existing rule, without silently replacing it by reindexing or line-graph promotion, to AB, BC, CA, AD, DB, BA.

## Executed rung trace

Use unique edge labels and fixed column names (label,from,to), selecting label first. Sections retain their actual row witnesses, not just endpoint values.

| Rung | Promoted field | Label values | Source values | Target values | Rows | Status |
|---:|---|---:|---:|---:|---:|---|
|12|Initial|6|4|4|6|Explicit|
|11|Label|1|4|4|6|Explicit|
|10|Source|1|4|4|16|Explicit|
|9|Target|1|4|144|576|Explicit|
|8|Label|576|4|144|576|Explicit|
|7|Source|576|382205952|144|1528823808|Exact count only|

At the first label step all six fibers are singleton: the new label is the unique full label section, with the old label retained as provenance. Source fibers then have sizes (2,2,1,1), giving four sections and sixteen evaluation rows. Incoming fibers now have sizes (6,6,2,2), not the original seed's (2,2,1,1): the source-section contexts distinguish rows. Target promotion therefore creates 144 sections and 576 rows.

After the next label promotion, source fiber sizes are (144,96,192,144) in checker order. Their product gives 382205952 sections. The checker counts this next step without allocating its 1528823808 rows. No rung6-to-rung4 realization is claimed by this experiment.

All original seed edges remain recoverable by evaluation through the explicitly built steps. Evaluation need not be injective: several promoted contexts can evaluate to the same old row. This is retained provenance, not a two-sided inverse of all new context information.

## Unique routing survives as a coherent section

At rung9, inspect target sections whose selected rows all have the SAME source-section value. Exactly one exists. Its evaluated original edges are

    AD, DB, BC, CA.

Thus the unique seed cycle cover found in `seed-endpoint-sections-and-unique-return-cycle.md` lifts through the actual section-field constructor. It gives four evaluation rows under one target section and one source-section value, retaining the original target keys as provenance.

This is a useful canonical subconfiguration under the stated constant-source condition. It is not a derivation that all other rows should be pruned. Such pruning would discard original AB/BA responsibilities and many new section contexts. Nor are the four evaluation rows automatically four distinct physical endpoints: their promoted field values coincide and their provenance differs.

## Result

A concrete endpoint constructor was already available. Applied literally, it creates rapid context growth, not automatic minimal compaction. Within it, the unique simultaneous seed routing survives as a distinguished coherent section. The next structural question is whether the intended cycle selects such coherent subconfigurations, retains the full context space, or identifies contexts by an explicitly recoverable quotient. Those objectives differ and cannot be chosen just to obtain a desired count.

## Verification

    python research/nima/checkers/check_seed_section_promotion_trace.py

Passes, including the imported 441 finite promotion cases, actual seed field/provenance checks, unique coherent routing, and exact next-step counts. No physical readout, particle identity or primitive execution-cost claim follows from these counts.
