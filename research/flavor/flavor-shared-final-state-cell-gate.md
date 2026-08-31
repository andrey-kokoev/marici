# Shared final-state cell gate: WP1050

## Question

Does a null-complete overlap monitor prove that the Flavor and reference
amplitudes share one `physical16` final-state cell?

## Same-cell coordinate

Add a same-cell certificate \(\sigma\), where \(\sigma=1\) means the
Flavor/reference cross amplitude is a cofinal final-state amplitude and
\(\sigma=0\) means it is a split-cell or reference-only proxy. The monitor
record remains

\[
M=\eta c,
\]

while the science interference row is

\[
D=4\nu dc\sigma\mathcal L g.
\]

Use coordinates

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma).
\]

WP1044--WP1049 rows have rank seven on eight coordinates. A same-cell
certificate raises the rank to eight.

## Split-cell hostile

The same-cell partial-overlap packet

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma)=(0,4,1,1,1,1/2,1/2,1)
\]

and the split-cell proxy

\[
(B,\mathcal L,g,\nu,d,c,\eta,\sigma)=(0,4,1,1,1,1/2,1/2,0)
\]

share

\[
B=0,
\qquad
S=4,
\qquad
V_{\rm ref}=1,
\qquad
\text{epoch}=1,
\qquad
M=1/4,
\qquad
\eta=1/2.
\]

But their science interference rows differ:

\[
D_{\rm same}=8,
\qquad
D_{\rm split}=0.
\]

Thus the split-cell proxy can present an overlap-monitor record yet cannot
support the same-cell gain reconstruction. Decoding it as a same-cell overlap
would divide by zero when used in the gain formula.

## Classification

This is a conditional shared-cell gate. Null accounting separates monitor
efficiency from overlap, but it does not prove the overlap occurs in one
physical `physical16` final-state cell.

## Disposition

Productive. WP1049's null-complete monitor alternative now has an explicit
same-cell separation gate. The next required object is the actual
`physical16` shared final-state event cell with typed Flavor, reference,
cross-amplitude, and null outcomes; split-cell cross-amplitude proxies must be
rejected.

Checker: `research/flavor/checkers/wp1050_shared_final_state_cell_gate.py`

Result: `results/wp1050_shared_final_state_cell_gate.json`
