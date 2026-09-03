# Higher-dimensional faithful-face no-go

## Question

Can a higher-dimensional SNC geometry add the missing face while retaining a faithful comparison to the original nonzero triangle class?

## Claim boundary

Three boundary divisors can meet transversely in a smooth threefold, producing a 2-simplex in the dual complex. Its oriented boundary is the primitive three-edge cycle, so the filled dual complex has first homology zero rather than rank one.

This face cannot transport to a filler of the original triangle under a chain map that preserves its primitive class. Chain maps send boundaries to boundaries. Hence the image of the filled face boundary cannot be the verified nonboundary `sigma123` in the original complex. Equivalently, a retraction from the filled simplex to its boundary inducing the identity on the cycle would force zero first homology to surject onto rank-one first homology.

The obstruction also applies to the regulator comparison: a map carrying the higher-dimensional nullhomotopy to the original pair would kill `Xi_log`, contradicting its verified nonzero de Rham class.

## Disposition

Higher dimension supplies a geometric face only by losing faithfulness on the target primitive class. It cannot fill the fixed-source horn. The remaining branch is to classify whether a deliberately nonfaithful correspondence has an independently sourced physical readout; absent that extra map, it is only a class-killing change of presentation.

## Verification

- `research/voevodsky/check_cosmology_higher_dimensional_faithful_face_no_go.py`
- Execution pending: structured-command MCP is unavailable in this turn, so no results JSON is claimed.
