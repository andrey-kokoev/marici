# Terminal source signs are not single-crossing in Gale order

## Question

Does the fixed-eight terminal sign partition form a monotone boundary compatible with the log-supermodular absolute weights?

## Claim boundary

No. The first terminal case already contains the saturated Gale chain

\[
\{0\}<\{1\}<\{2\}
\]

with exact nonzero sign pattern

\[
+,-,+.
\]

Thus signs change twice in two cover moves. Positive labels are neither a Gale ideal nor a filter, and magnitude log-supermodularity cannot be combined with a single monotone sign cut to prove the transport.

The obstruction is exact and occurs for empty base with exchanged labels \((i,j)=(0,1)\). It refutes single-crossing, not structured alternation.

## Disposition

The immediate alternating pattern suggests a parity character rather than irregular interlacing. Test whether every nonzero source sign equals a case-dependent constant times \((-1)^{\sum K}\). If so, the sign complexity can be untwisted into a deterministic checkerboard grading while retaining log-supermodular magnitudes; if not, record the first residual sign defect.
