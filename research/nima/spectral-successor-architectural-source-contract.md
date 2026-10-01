# Architectural source contract for spectral-record succession

## Primary-source result

The inspected architectural sources explicitly leave the fields we were searching for open. This is documented underspecification, not merely failure to locate an implementation.

### What the source fixes

`docs/system-characteristics.md`, lines 93–116, defines retained family promotion:

    groups = summarize(current_records, grouping_keys, retain_members=True)
    next_records = addcolumn(groups, "label", unique_index)

The interface is one fresh label per grouped record. All matching records and their many-to-many structure remain recoverable through members or links. The next level organizes these retained families.

Consequently the justified generic input/output contract is:

    Input: current complete records + supplied grouping keys
    Output: freshly labelled grouped records retaining every member/link

It is not a contract taking bare projectors and inferring their next endpoints.

### What the source explicitly leaves to the implementation

The same passage says: "Grouping keys, next-level endpoint fields, and label lifetime are part of the implementation contract."

`docs/theory-page.md`, "What promotion determines", lines 329–342, further says the intended horizontal generator and next-level endpoint maps "remain to be selected and connected" to the checked candidates. It explicitly calls independent all-pairs comparison a separate operation and leaves its identification with the tower successor open.

`docs/system-characteristics.md`, "Recursive comparison constructor", lines 621–640, documents an actual independent product constructor with members F_v x F_w. This specifies what that candidate does; it does not settle that candidate's application to the present spectral records. The source distinguishes retaining a family from adding an independently variable operand.

## Answers for the present spectral branch

| Question | Source-backed answer | Unfilled spectral binding |
|---|---|---|
|What are members?|The complete records selected by the supplied grouping keys, retained without destructive aggregation|No cited rule chooses primitive occurrences versus individual mode records versus complete three-mode packages as this successor's input domain|
|What are new endpoints?|Fields of an explicit implementation contract|No spectral-specific assignment recovered|
|Joint relation or independent pairs?|Promotion retains supplied member incidence; the separate all-pairs constructor explicitly creates a product|No source selection of that product as this spectral successor|

The two original triangle contexts and their modes remain valid retained data. A mode history window is provenance, not automatically the incoming fibre of a new endpoint map. Equal projectors or the seed-symmetry intertwiner do not determine those fields.

## Disposition

Do not implement another adapter under the claim that it follows from family promotion. Mark this particular spectral-successor binding as OPEN BY SOURCE SPECIFICATION. A future source extension must supply the spectral input domain, grouping keys, endpoint maps and intended operation. An explicit experimental policy could supply them, but would be a new hypothesis rather than recovery of the cited architecture.

No further reconstruction or covariance check can select those intentionally unspecified fields. The existing record retention, symmetry comparison and candidate successor results remain useful independently of that selection.

## Evidence scope

Directly inspected the cited passages in `docs/system-characteristics.md` and `docs/theory-page.md`, alongside the previously recovered recursive family-comparison contract. No source documentation was modified, no adapter was implemented, and no fresh computational verification was needed or claimed for this textual contract audit.
