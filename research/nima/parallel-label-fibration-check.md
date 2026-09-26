# Checking parallel endpoint fibrations followed by label fibrations

## Prior-work correction

The operator identified this as repeated work. The substantive recovery and
return-cycle results already appear in `table-fibration.md` / `TableFibrationCycle.agda`
(`marked-recovery`, `twice-correct`, `four-path`). The new nested-fiber module is a
specialized regression, not a new research frontier.

More importantly, `whole-package-generators.md`, `observer-higher-groupoid-fragment.md`
and `native-table-equivalence.md` already retain complete histories, both schedules,
comparison witnesses and comparisons of comparisons, and reify them as the next
source package. A zero reconstruction error for the row projection does not erase
that retained comparison data. The scalar orientation difference below is a separate
illustration, not the established meaning of the operator's higher residual.

Resume from the complete native package/history/comparison interface. The remaining
physical question is an action or generating-functional readout of that retained
structure, not reconstruction of basic fibers or invention of higher comparison types.

## Frozen interpretation and obligation

The operator asks to check the proposed C: form input and output fibrations in
parallel, then fiber each over the original labels, and reverse the construction.
The active SCC obligations are reconstruction/route compatibility first, then
readout compatibility. No addition of differently typed presentations is assumed.

For rows R with maps s:R->S, t:R->T, l:R->L, the retained views have row types

\[
A=\sum_{a:S}\sum_{k:L}\sum_{(r,p):\operatorname{fib}_s(a)}(l(r)=k),
\qquad
B=\sum_{b:T}\sum_{k:L}\sum_{(r,q):\operatorname{fib}_t(b)}(l(r)=k).
\]

This interpretation fibers each endpoint family internally over labels. Both views
retain the shared original row, not just lists of endpoint values for a label.
Changing which payload survives changes the mathematical operation.

## Formal result

`agda/ParallelLabelFibration.agda` uses the actual `TableFibrationCycle.fibrate`.
It proves, at arbitrary universe level, that each nested total is isomorphic to R:
forget the endpoint/label witnesses in one direction; insert the source endpoint,
label and reflexivity witnesses in the other. Both inverse laws are proved.
The two parallel views recover the same row and preserve every row-based readout.

Thus the lossless construction has an inverse. As stated it maps a table to a
pair of nested presentations; simply applying that grouping operation again is
not yet a typed endomorphism or a specified reconstruction algorithm.

There is an explicit way to realize the requested involution: on a tagged type of
raw and grouped presentations, define C to group raw data and ungroup grouped data.
The module proves C(C(x))=x for the individual nested view. The checker verifies
the corresponding paired-packet construction on all finite test cases.

This proves an involution can be *defined by supplying the reverse rule*. It does
not prove that applying the unchanged forward grouping rule twice reverses it.
This extension is available for any isomorphism and does not by itself supply an
interaction law. Its row-based observation is also proved invariant under C.

## Lossy counterexample and unique-label control

Take two inputs, two outputs, and one repeated label k:

```text
I1: a --k--> u       I2: a --k--> v
    b --k--> v           b --k--> u
```

After forgetting shared row identities and retaining only endpoint counts per
label, the two parallel packets agree. Their original incidence relations differ.
Joining solely on k creates all four possible links for either input. Repeating
that join keeps the four links: this support closure is idempotent, not involutive.
Both original examples have unique endpoint pairs, so that condition does not
repair the ambiguity.

If labels uniquely identify rows, labels already supply the missing join key.
The checker verifies exact support recovery on that subdomain. The collision
requires repeated labels with the pairing forgotten; it is not a counterexample
to full dependent fibers or unique-label reconstruction.

An incompatible pair consisting of one full input view and the other table's
full output view is rejected rather than silently treated as one coherent source.

## Which residual?

There are three distinct objects:

1. Lossless reconstruction error: zero after the specified inverse.
2. Lost-incidence data: needed to reconstruct a lossy packet; not generally an
   additive scalar and not selected by label marginals.
3. Orientation difference in a common additive representation: for a linear
   involution, define R=id-C. Then

\[
R(C(I))=-R(I),\qquad R^2=2R.
\]

The first expression is the residual on the reverse trip; the second applies the
residual operator twice. Over coefficients admitting division by two,
`(id-C)/2` is the projection onto the anti-invariant part. This is not a nonzero
residual obtained from the invariant row readout of bare grouping.

The checker tests the orientation identities for transpose on all 81 signed 2x2
matrices with entries -1,0,1. This is a separate common-space example, not a claim
that endpoint-label grouping is matrix transposition.

## Evidence and disposition

Fresh safe/cubical compilation passes. The executable check exhausts 4,681 ordered
tables with 0..4 rows over two labels, two inputs and two outputs, including empty
tables and repeated triples with distinct row identities. It checks both tagged
roundtrips, coherent parallel recovery, support-closure idempotence, the marginal
collision, unique-label recovery and orientation controls.

```text
pwsh -NoProfile -File research/nima/checkers/check_parallel_label_fibration.ps1 -Fresh
python research/nima/checkers/check_parallel_label_fibration.py
python research/aspect/scc/scc.py check nima-parallel-label-fibration
```

Receipts: `results/agda-ParallelLabelFibration.json` and
`results/parallel-label-fibration.json`. Formal closure hashes are checked.

Disposition: reversible double-fibration presentation is established; involution
requires the reverse branch to be part of C's definition. A nonzero physical
residual or generating function is not produced. Lossless invariance and loss of
incidence must not be combined into one claim. New files and evidence are
uncommitted; no existing researcher source was changed and no physical coupling,
independent review, commit or push is claimed.
The report event `ev-000000015609-7cd42cca-9968-4e30-b56c-f1670000d3ea`
at sequence 15609 is admitted but uncommitted; admission is not truth certification.
