# Eighth completion axis: final retained-graph status

## Theorem in the declared scope

On the projective exponential/Laurent source, with forward retained-graph realization, admitted Mellin/Laurent graph multipliers, transverse marked physical cuts, and retained source-pulled `QDLO` completion, regulator passage defines a lax cubical natural transformation

\[
R:\mathcal Q_X(H,V,D,q,L,C,O)
\Longrightarrow
\widehat{\mathcal Q}(H,V,D,q,L,C,O).
\]

It has 128 components and 448 naturality cells. Six generic face families are strict:

\[
R\times H,
R\times V,
R\times D,
R\times L,
R\times C,
R\times O.
\]

The chart family is coherently lax:

\[
R\times q,
\qquad
A_X=P_X\mathcal F(I-P_X),
\]

with shell modification

\[
A_X=P_X\mathcal F(P_Y-P_X)+P_X\mathcal F(I-P_Y).
\]

The leakage cell is nonzero, so no strict finite-cutoff 8-cube is claimed.

## Closed gates

1. Rooted substitution extends through projective exponential completion.
2. Physical cut extends through the minimal projective Laurent localization.
3. Forward realization extends to retained graph completion; no inverse is asserted.
4. Convolution successor and retained observation have a faithful common joint graph.
5. Pulling that graph back along arithmetic synthesis gives the minimal faithful source completion. Joint closability follows by dependency induction from continuity of `U_4` and closability of the admitted multiplier and retained observation.
6. Rooted convolution preserves the pulled-back graph for admitted multipliers.
7. Marked transverse cuts preserve it for admitted Laurent multipliers.
8. Fourier leakage is continuous on the `QDLO` graph and its shell cocycle survives all admitted transports.
9. These data assemble into the lax eighth coherencer in the declared retained-graph scope.

## Nonclaims

The theorem does not include arbitrary completed observers, nontransverse loaded-current divisors, reverse realization equivalence, bare-`L2` endpoint evaluation, or strict finite-cutoff Fourier naturality.

## Verification

The aggregate certificate is

- `research/nima/results/lax-eighth-completion-coherencer.json`.

Its generator is

- `research/nima/check_lax_eighth_completion_coherencer.py`.

The complete local suite, plus the inherited Fourier leakage, Mellin/de Rham domination, and exact physical cut-coaction regressions, passes.
