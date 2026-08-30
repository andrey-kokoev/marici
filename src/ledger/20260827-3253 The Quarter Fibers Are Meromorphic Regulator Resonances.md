# 3253 — The Quarter Fibers Are Meromorphic Regulator Resonances

Date: 2026-08-27

Status: exact source-typing result with replicated finite-field ranks; the
resonant support remains a finite-field theorem.

## Question

Entry 3250 showed that integral pole-depth transport does not connect the
physical exponent to the quarter fibers. Does the frozen source contain a
different parameter that types them?

## Source regulator

The homogeneous three-site source uses

\[
\gamma=\epsilon-\frac12.
\]

Thus the physical point is

\[
\epsilon=0,qquad \gamma=-\frac12,
\]

whereas the two quarter fibers occur at

\[
\begin{array}{c|c}
\gamma&\epsilon\\
\hline
-5/4&-3/4\\
-7/4&-5/4.
\end{array}
\]

The dimension-preserving syzygy primitive has boundary order

\[
K^{\gamma+1}=K^{\epsilon+1/2}.
\]

Literal relative-boundary vanishing therefore holds in the chamber

\[
\operatorname{Re}\epsilon>-\frac12.
\]

Both quarter fibers lie outside that chamber.

## Ordered rank audit

The full sparse pencil gives the following rank triples at both primes
(32003) and (32009):

\[
\begin{array}{c|c|c}
\gamma&\epsilon&
(\operatorname{rank}M,\operatorname{rank}[M;L],r_{\rm rel})\\
\hline
-1/2&0&(479,505,26)\\
-5/4&-3/4&(479,500,21)\\
-3/2&-1&(479,498,19)\\
-7/4&-5/4&(479,498,19)\\
-2&-3/2&(477,503,26).
\end{array}
\]

The first quarter defect is encountered only after leaving the literal
boundary-vanishing chamber. The second is reached only beyond the established
half-integer relative-rank defect at \(\gamma=-3/2\). At \(\gamma=-2\), the
source module itself changes rank.

## Narrow conclusion

The dimensional regulator supplies a source-derived coordinate containing the
quarter fibers. It does not make them physical at \(\epsilon=0\). Their correct
type is:

\[
\text{meromorphic regulator-plane resonance of the exponent adapter}.
\]

They are not new Carrier strata and not singular support of the physical
three-site coefficient object. Any use of these fibers in a physical theorem
must derive a meromorphic continuation or dimensional recurrence together with
its relative-boundary correction; simple substitution into the physical
residue complex is invalid.

## Next falsifier

Construct the source dimensional recurrence across

\[
\epsilon=-\frac12, -\frac34, -1, -\frac54
\]

as a morphism of relative complexes. Determine whether the quarter cokernels
appear as canonical residues of that recurrence or disappear after including
the boundary term lost outside the literal chamber. This is now a
regulator-transport question, not a search for cosmological support.

## Artifacts

- `research/benincasa/checkers/exponent_adapter_regulator_path.py`
- `research/benincasa/results/exponent_adapter_regulator_path.json`
- sequence claim `seqclaim-d0fd49ecdd5c5873cc27524c`
