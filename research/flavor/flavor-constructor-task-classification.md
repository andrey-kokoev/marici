# Six constructor task classes are not interchangeable (WP73, move 2/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Classification

On the admitted substrate `X16`, the six task types have distinct signatures:

| task | substrate output | record | proper image required | repeatability target |
|---|---|---|---|---|
| preparation | chosen `a in A` from a blank/resource state | optional | yes | repeated preparations remain in `A` |
| discrimination | input `x` preserved | label appended | no | same label on repeated trials |
| filtering | accepted `x` preserved, otherwise failure flag | flag appended | conditional only | stable acceptance predicate |
| stabilization | arbitrary `x` driven toward `A` | optional | yes | `A` is invariant/attracting |
| copying | `(x,blank)->(x,x)` for declared distinguishable attributes | optional | no | copies preserve the attribute |
| readout | input `x` preserved | value appended | no | calibrated repeatable record |

Preparation and stabilization can be selectors. Filtering is only a selector
when the success probability, rejected branch, apparatus reset, and source of
postselection are physically typed; the predicate alone is not one.
Discrimination and readout can be faithful without reducing the state family.
Copying applies to an information-variable attribute, not arbitrary continuous
unknown Yukawa states.

## Composition rules

Appending a record after reversible RG remains readout.  Conditioning a
readout on a desired answer does not manufacture preparation.  A proper-image
mathematical channel becomes a candidate constructor only after its apparatus,
resource return, and repeated-use error are supplied.  Reference-assisted
tasks compose only inside the enlarged relational experiment.

## Smallest exact falsifier

Let `x+ != x-` be a physical16 pair with `pi10(x+)=pi10(x-)`.  A measured-ten
readout gives the same record and preserves both inputs.  It therefore neither
discriminates this pair nor selects one member, even if its fiber is finite.

Verification:
`python research/flavor/checkers/wp73_constructor_task_classification.py`.
