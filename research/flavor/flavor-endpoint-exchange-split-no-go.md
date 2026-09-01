# Endpoint-exchange split no-go: WP1112

## Question

Does existing fused-defect interval geometry supply an endpoint exchange law
selecting the WP1111 Green–Schwarz split?

## Reflection obstruction

Endpoint exchange acts on the split parameter as \(t\mapsto -t\), so a
reflection-symmetric packet would force \(t=0\). But the selected quartet and
its reflected cell have different WP1070 cosets:

\[
s_{\rm quartet}=\Bigl(\frac12,\frac14,0,0,0,\frac34,0\Bigr),
\qquad
s_{\rm reflected}=\Bigl(\frac12,\frac34,0,0,0,\frac14,0\Bigr).
\]

Thus reflection maps the selected packet to a different packet. It is not a
symmetry fixing the quartet branch, and it cannot select \(t=0\) while that
branch is preserved.

## Classification

Negative gate. Interval reflection or endpoint exchange cannot be used to
force the local split. The remaining route is an independent orientation-odd
UV boundary datum.

Checker: `research/flavor/checkers/wp1112_endpoint_exchange_split_no_go.py`

Result: `results/wp1112_endpoint_exchange_split_no_go.json`
