# Mirror completion preserves the source gates but reverses the sign readout: WP786

## Question

Can anomaly cancellation, RG attraction, threshold survival, and a
parity-sensitive instrument together select the absolute sign left open by
WP785?

## Exact chiral hostile pair

Use the genuinely chiral charge packet

\[
Q=(-9,-5,-1,7,8)
\]

and its charge-conjugate mirror \(-Q\). Neither packet contains a vectorlike
pair. Both satisfy

\[
\sum_i q_i=0,\qquad \sum_iq_i^3=0.
\]

Their ordinary quadratic RG weight is the same:

\[
\sum_iq_i^2=220.
\]

Every even charge moment is mirror invariant, while every odd moment reverses
sign. Vanishing odd anomaly coefficients therefore remain zero. Local anomaly
consistency does not choose between the chiral source and its mirror.

## RG and threshold equivariance

For an exchange-odd portal contrast \(\Delta\), a mirror-equivariant
autonomous flow has

\[
\beta(-\Delta)=-\beta(\Delta).
\]

The exact normal form

\[
\beta(\Delta)=\Delta(\Delta^2-v^2)
\]

has paired fixed points \(\Delta=\pm v\) with the same critical exponent
\(2v^2\). RG attraction can select the nonzero orbit \(\lvert\Delta\rvert=v\)
without selecting its sign.

A mirror-equivariant finite matching map

\[
\Delta_{\mathrm{low}}=Z\Delta
\]

likewise transports both branches. Threshold survival is not branch
selection.

## Readout is not retrocausal authority

An inclusive width proportional to

\[
\Delta_{\mathrm{low}}^2
\]

identifies the two branches. A parity-sensitive labelled response

\[
A_P=L\Delta_{\mathrm{low}}
\]

reverses sign and separates them whenever \(LZ\ne0\). The exact two-response
Gram value is \(2(LZ)^2\).

This supplies a possible instrument for determining which branch was
realized. It does not make that branch unavoidable at the source. Using the
measured parity sign to delete the mirror constructor would invert the
source-to-readout arrow.

## Classification

The complete tested pipeline factors as

\[
\{Q,-Q\}
\longrightarrow
\{\lvert\Delta\rvert\}
\longrightarrow
\{R_{\mathrm{incl}}\},
\]

unless a parity-labelled instrument retains the final sign. The first
nonfaithful arrow is already at the mirror-equivariant source laws: anomaly
cancellation and even RG data admit both constructors.

The next source must therefore be non-mirror-completable. An oriented boundary,
incidence object, or asymmetric initial state must be part of the admitted
source definition, with its mirror excluded by an independently stated
consistency condition rather than by the desired observation. The same object
must also fix the continuous portal normalization and threshold clock;
otherwise it selects only sign.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp786_mirror_completion_sign_selection_no_go.py

Generated result:
research/flavor/results/wp786_mirror_completion_sign_selection_no_go.json
