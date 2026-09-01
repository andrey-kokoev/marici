# History-plus-pairing gain no-go: WP1105

## Question

Does conditional history dilation combined with the bifundamental pairing
supply event reweighting or the gain law?

## Dimension and norm gate

History dilation supplies three slots; the bifundamental pairing has rank
three. Their internal composite has

\[
3\times3=9
\]

components, not six event rows. The history dilation is an isometry with gain
\(1\), and the pairing trace/rank is \(3\), not \(3/2\). Any rank-over-two
normalization would be additional source data.

## Production gate

The six soft branches retain

\[
q=\frac1{23}(6,8,1,4,2,2),
\]

not \((1/4)^6\). The composite supplies zero physical16 rows and no source
normalization.

## Classification

Negative gate. Three history slots times rank three, isometry, or \(I_3\)
trace cannot be promoted to six event weights or gain \(3/2\).

Checker: `research/flavor/checkers/wp1105_history_pairing_gain_no_go.py`

Result: `results/wp1105_history_pairing_gain_no_go.json`
