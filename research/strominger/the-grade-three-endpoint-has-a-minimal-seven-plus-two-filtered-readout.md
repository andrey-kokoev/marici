# The Grade-Three Endpoint Has a Minimal Seven-Plus-Two Filtered Readout

## Result

The seven-port grade-changing readout reaches the weights

\[
m=-3,-2,\ldots,3
\]

inside the nine-dimensional grade-three endpoint (mathcal H_4^{(4)}). Its quotient consists of the two extremal weights (m=\pm4).

Those two missing directions are already present among the nine executable (l=4), spin-2 low-mode ports. Applying two spin raises gives

\[
\eth^2:\mathcal H_4^{(2)}\longrightarrow\mathcal H_4^{(4)}.
\]

The squared coefficient is

\[
((4-2)(4+3))((4-3)(4+4))=14\cdot8=112.
\]

It is nonzero for every weight. Retaining only its two extremal source ports supplies exactly the complement of the transported seven-dimensional image.

Hence there is an executable filtered readout

\[
\mathcal H_3^{(2)}
\oplus
\operatorname{span}\{{}_2Y_{4,-4},{}_2Y_{4,4}\}
\longrightarrow
\mathcal H_4^{(4)}
\]

of rank nine.

## Minimality

The transported image has codimension two. Any readout preserving that seven-dimensional image requires at least two additional independent scalar ports to cover the target. The two extremal ports do so with disjoint weight support. Deleting any one of the resulting nine ports lowers the rank to eight.

Thus the filtered completion law is

\[
7+2=9.
\]

This is not numerology: the two is the exact dimension of the quotient between consecutive spherical endpoint representations.

## Atlas rather than unique presentation

The same target can also be observed directly by raising all nine (l=4), spin-2 ports twice. That gives an alternative nine-port chart.

The two presentations serve different contracts:

- the direct (l=4) chart observes the target without retaining its relation to grade two;
- the (7+2) chart retains the seven transported grade-two directions and records only the two genuinely new grade-three directions separately.

The second chart is therefore minimal relative to the grade filtration, not uniquely minimal among all target observations.

## Relation to the 21-port packet

The source packet has multiplicities

\[
5+7+9=21.
\]

The filtered grade-three chart uses seven (l=3) ports and two extremal (l=4) ports. The remaining twelve ports comprise five (l=2) ports and seven nonextremal (l=4) ports. They are not discarded globally: they support the lower endpoint and the alternative direct target chart.

## Authority

The 21 ports are source-authorized executable finite integrals, and their finite linear aggregation is independently authorized. Aspect therefore admits the (7+2) construction as a `derived_filtered_readout`.

It remains an observation compiler. It does not create a physical spin-4 target field or authorize higher-spin dynamics.

## Evidence replay

The checker derives all nine coefficients, verifies the disjoint (7+2) support decomposition, proves deletion minimality, retains the alternative nine-port chart, and invokes Aspect's current decision function.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/seven_plus_two_filtered_endpoint_completion_checks.py
```

Machine-readable results are written to `research/strominger/results/seven_plus_two_filtered_endpoint_completion_checks.json`.
