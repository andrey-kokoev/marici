# Uniform Seam Transversality Is a Stable Decoder Theorem

Let (K=\ker Q), with residual (R:K\to Z) and seam observation
(H:K\to Y). The following finite-dimensional statements are equivalent:

\[
R^*R\le C^2H^*H;
\]

\[
\|Rx\|\le C\|Hx\|\quad(x\in K);
\]

and existence of a linear decoder (S:\operatorname{ran}H\to Z) such that

\[
R=SH,
\qquad
\|S\|\le C.
\]

Indeed, kernel inclusion makes (S(Hx)=Rx) well defined, and the domination
inequality makes it bounded. Conversely a bounded factorization gives the
inequality. The smallest possible decoder norm is

\[
\inf_{R=SH}\|S\|=\beta(H,R)^{-1}.
\]

Thus uniform seam transversality is exactly a stable mathematical decoder
theorem. Full finite rank supplies a decoder at each cutoff; it does not bound
the decoder norms.

For

\[
H_N=\operatorname{diag}(1,N^{-1}),
\qquad R_N=I,
\]

the unique decoder is

\[
S_N=\operatorname{diag}(1,N),
\]

so every cutoff is faithfully decoded while (\|S_N\|=N\). Noise of size
(N^{-1}) in the weak seam coordinate produces order-one residual error.
This is finite faithfulness without completion-stable inference.

## Decoder versus repair constructor

The factor (S) is a mathematical reconstruction map. Its existence does not
show that the source dynamics can implement a correction, feed it back into
the boundary state, preserve the real frame, or pay the interface cost. This
is the same distinction as toric-code syndrome data versus a preferred
physical decoder.

Three claims must remain separate:

1. seam data determine the residual algebraically;
2. the determination is uniformly stable through completion;
3. an authorized physical or arithmetic constructor executes the repair.

Only the first two follow from domination. The third requires an independently
typed source arrow and coherence laws.

## Falsifiers

- A decoder exists cutoffwise but its norm diverges.
- Exact noiseless reconstruction is reported as stable observability.
- A pseudoinverse is treated as a source-authorized constructor.
- The decoder repairs the scalar readout but not the typed seam or real-frame
  residual.
- Different bounded decoders agree on current data but differ on future
  authorized successors.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Decoder existence, sharp norm, cutoff uniformity, and constructor
authority were frozen.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The generalized lower-frame bound acquired its exact operational
meaning as the inverse norm of the best residual decoder. The theorem closes
mathematical inference but deliberately leaves executable repair unproved.
