# 1739 — Higher-Rank Supported Readout Requires the Complete Principal-Angle Packet

## Higher-rank falsifier

Let \(P\) and \(Q\) be state and measurement projectors.  The nonzero spectrum
of

\[
PQP
\]

is

\[
\{\cos^2\theta_i\},
\]

where \(\theta_i\) are their principal angles.

## Total-overlap failure

The total Born overlap

\[
\operatorname{Tr}(PQ)=\sum_i\cos^2\theta_i
\]

does not determine the pair.  In rank two, the realizable spectra

\[
\{0,1\}
\qquad\text{and}\qquad
\left\{\frac9{25},\frac{16}{25}\right\}
\]

both have trace one, but their determinants are

\[
0
\qquad\text{and}\qquad
\frac{144}{625}.
\]

Thus a single summed probability loses invariant higher-rank information.

## Complete static packet

The characteristic polynomial

\[
\boxed{\chi_{PQP}(\lambda)}
\]

equivalently the complete squared principal-angle spectrum, determines all
unitary-invariant polynomial readouts of the static projector pair.  In rank
two, trace and determinant generate the power traces through the exact Newton
recurrence.

## Narrow result

The rank-one scalar of Entry 1738 generalizes to a finite principal-angle
packet, not to one scalar.  This is a higher-rank coefficient/readout object
over the same labelled state–measurement incidence.  No new Cut carrier
stratum is required.

This result is static.  It does not imply that endpoint principal angles
control nonabelian Berry transport along a loop.

## Durable artifacts

- `research/benincasa/checkers/higher_rank_principal_angle_packet.rs`
- `research/benincasa/results/higher-rank-principal-angle-packet.json`
- `research/benincasa/higher-rank-principal-angle-packet.md`

## Next falsifier

Construct two loops with identical endpoint principal-angle packets but
different Wilczek–Zee holonomy.  Determine whether the projector path recovers
the nonabelian transport and whether physical readout requires a matrix-valued
interference reference.
