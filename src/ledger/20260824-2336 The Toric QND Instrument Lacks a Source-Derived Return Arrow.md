# Entry 2336: The toric QND instrument lacks a source-derived return arrow

The prediction was frozen before inspecting the toric instrument and fault
packets.  Four faces of the proposed constructor diagram are exact:

\[
\text{parity interaction},\quad
\text{classical record},\quad
\text{Lueders successor},\quad
\text{repeatability/coarse-graining}.
\]

The fifth face is absent.  The pointer is assumed prepared in \(|0\rangle\),
but no admitted source operation resets the used pointer or derives a fresh
replacement.  Thus

\[
\text{source-derived repeatable QND instrument}
\not\Rightarrow
\text{source-closed reusable constructor}.
\]

This falsifies the frozen positive prediction at its predeclared
`missing_reset_authority` gate.  The existing single-fault theorem cannot
repair the gap because it explicitly excludes preparation faults, general
gate faults, multiple faults, and verified cat preparation.

The corrected criterion is:

> A repeatable instrument becomes a constructor only when apparatus
> return/replacement belongs to the same source-authority closure as the
> task, interaction, record, and successor maps.

The stronger fault-tolerant recovery constructor remains unproved and also
requires a noise model, decoder/cost functional, conditional recovery, and
degradation theorem.

Evidence:

- `research/nima/toric-constructor-sufficiency-prediction.md`
- `research/nima/toric-source-closed-constructor-sufficiency.md`
- `research/nima/checkers/check_toric_source_closed_constructor.py`
- `research/nima/results/toric_source_closed_constructor.json`
- sequence claim `seqclaim-200195998d42c84e31fda461`
