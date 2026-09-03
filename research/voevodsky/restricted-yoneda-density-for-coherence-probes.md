# Restricted Yoneda density for coherence probes

## Question

Can the probe-faithfulness gate be converted into a constructive criterion for selecting enough coherence observables?

## Claim boundary

This packet gives a categorical criterion and a finite linear rank test. It does not establish that Kitaev's currently available physical probes satisfy the criterion.

## Full representable probes

For a locally small category, the Yoneda embedding sends an object \(X\) to all representable probes

\[
\operatorname{Hom}(-,X).
\]

Yoneda is fully faithful: all typed representable probes jointly determine arrows. Thus there is no abstract impossibility of detecting coherence maps when every mathematical probe is available.

The physical problem is restricted Yoneda. Let \(\mathcal P\) be the admitted probe subcategory. Restriction gives

\[
Y_{\mathcal P}(X)=\operatorname{Hom}(-,X)|_{\mathcal P}.
\]

This restricted embedding is faithful only when \(\mathcal P\) is separating for the relevant arrows; stronger reconstruction statements require an appropriate density theorem. Operational availability, gauge descent, and fault independence can make \(\mathcal P\) much smaller than the full representable family.

## Finite linear criterion

If candidate coherence residuals lie in a finite-dimensional vector space \(V\), scalar probes \(q_1,\ldots,q_m\in V^*\) are jointly faithful exactly when

\[
\bigcap_i\ker q_i=\{0\}.
\]

Equivalently, the probe matrix has rank \(\dim V\). When the rank is \(r<\dim V\), the unresolved fiber has dimension at least \(\dim V-r\). This supplies an executable acceptance test rather than a qualitative request for more probes.

After quotienting gauge directions \(G\subseteq V\), the correct target is \(V/G\). Probes must vanish on \(G\), descend to the quotient, and have full rank there. Full rank in presentation coordinates is irrelevant if the probes do not descend.

## Probe design

A minimal finite probe design proceeds as follows:

1. type the residual space or tangent/linearized quotient actually claimed;
2. identify and quotient certified gauge directions;
3. express every admitted observable as a functional on that quotient;
4. compute exact probe rank and common kernel;
5. add probes whose functionals reduce the common kernel;
6. separately certify composition preservation, coverage, and fault independence.

Rank closure addresses faithfulness only. It does not establish physical construction or higher-simplex coverage.

## Kitaev placement

The four-copy Bargmann trace contributes one complex coordinate, equivalently at most two real scalar functionals when both quadratures are independently accessible. The reported frozen fixture has only a real value, but this does not determine the rank of the probe family on the relevant fusion-channel coherence quotient.

The next exact test is therefore not repetition of the same loop. It is:

- define the finite residual space for the electric associator loop modulo gauge;
- derive the linear or nonlinear observable map of every admitted preparation/permutation/readout setting;
- compute whether the resulting family separates quotient points;
- exhibit the unresolved fiber when it does not.

## Disposition

The required notion is restricted-Yoneda separation. In finite linear sectors it becomes an exact rank test. This converts probe sufficiency into a typed, falsifiable constructor while preserving the distinction between mathematical representables and physically admitted probes.

## Verification

- `research/voevodsky/checkers/check_restricted_yoneda_probe_density.py`
- `research/voevodsky/results/restricted_yoneda_probe_density.json`
