# Flux-sector preparation audit (WP141)

Owner: `marici.Figueiredo`.

## Bounded question

Does an independently normalized thermal/nucleation law select the flux sector
left free by WP140, and does its threshold readout distinguish flux
orientation?

Pre-objective process report: excitement `9/10`, confidence `9/10` that a
normalized ensemble exists but retains multiple sectors, expected information
gain `8/10`. Confounds are the bounded four-sector census and schematic
Euclidean weights. These reports are non-evidential.

Freeze the source-admitted sector set

\[
\mathcal N=\{-4,-1,1,4\}
\]

before detector readout. For WP140, `V_min(n)=2|n|` at `a=1`. A finite
temperature or nucleation preparation therefore has weights

\[
w_n=q^{|n|},\qquad q=e^{-2\beta},\qquad q=\frac12.
\]

The exact normalization is

\[
Z=2(q+q^4)=\frac98.
\]

Consequently

\[
P(\pm1)=\frac49,
\qquad P(\pm4)=\frac1{18}.
\]

This is a genuine source-generated sector ensemble, frozen independently of
flavor and detector targets. It does not select one sector: every admitted
sector has positive probability.

With WP140's reach `3/4`, the `|n|=4` sectors are accessible and `|n|=1`
sectors inaccessible. Thus

\[
P_{\rm accessible}=\frac19,
\qquad P_{\rm inaccessible}=\frac89.
\]

The mean oriented flux is zero while `E|n|=4/3`. Threshold masses see only
`|n|` and partition the source into the sign pairs `{−1,1}` and `{−4,4}`.
An orientation-sensitive topological probe `O=n` separates all four sectors
algebraically, but no executable flavor/collider instrument for it is given.

The zero-temperature limit does not fully repair selection. It concentrates
on the lowest-energy pair `n=±1` but leaves their orientation degenerate. A
CP-odd bias or oriented boundary could choose a sign, yet that creates a new
relational source and must be fixed before the desired answer is inspected.

Classification: **normalized flux-sector ensemble; no sector-orientation
selector**. WP141 improves WP140 by replacing an unweighted discrete fiber
with exact probabilities, but the preparation remains non-singleton and is
mostly outside the declared detector domain.

The smallest point-selection falsifier is the positive probability of both
`n=1` and `n=4`; the smallest orientation falsifier is the equal pair
`P(n)=P(-n)`. The remaining gate is a source-derived oriented boundary or an
executable topological probe, followed by open-rival detector faithfulness.

Post-objective process report: excitement `9/10`, confidence `10/10`, realized
information gain `9/10`. Raw delta: one normalized four-sector law is
constructed; accessibility probabilities become `1/9` and `8/9`; two sign
classes remain; twelve of twelve checks pass; no orientation selector or
instrument is added. These reports are non-evidential.
