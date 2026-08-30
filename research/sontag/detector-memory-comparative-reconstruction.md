# Detector-memory comparative reconstruction

Owner: `marici.Sontag`

Source owner: `marici.Aspect`

## Why this is the first example

This packet starts from the source-typed finite instrument in
`research/aspect/finite-dead-time-photodetection-memory-instrument.md`. The
Aspect checker is reproduced 10/10 without modifying its optical basis,
efficiency, recovery amplitudes, outcome maps, or preparation order.

The question is not whether a two-state detector can be rewritten in control
notation. It is whether the mature control neighborhood of a hidden-memory
instrument predicts additional Marici objects that the isolated click record
does not contain.

## Move 1: compress the quantum instrument to its memory behavior

After each optical input is destroyed, the predictive memory state is a
probability column on ready/dead states \((R,D)\). For a photon probe, the
click and no-click substochastic maps are

\[
M_c=\begin{pmatrix}0&0\\9/25&0\end{pmatrix},\qquad
M_n=\begin{pmatrix}16/25&9/25\\0&16/25\end{pmatrix}.
\]

Their sum is the memory transition for a photon bin. An empty recovery bin
has the single no-click transition

\[
M_e=\begin{pmatrix}1&9/25\\0&16/25\end{pmatrix}.
\]

This compression is authorized only because Aspect's separate Kraus labels
destroy the relevant optical coherences. It is a derived behavioral view of
the source instrument, not a replacement for the four-state quantum source.

## Move 2: the record process forces hidden memory

Starting ready, the probabilities of one click and two immediate clicks are

\[
p(c)=9/25,\qquad p(cc)=0.
\]

The predictive Hankel minor indexed by prefixes and suffixes
\(\{\epsilon,c\}\) is

\[
H=\begin{pmatrix}1&9/25\\9/25&0\end{pmatrix},
\qquad \det H=-81/625.
\]

Its rank is two. The iid reset model instead sets
\(p(cc)=p(c)^2=81/625\), giving determinant zero and predictive rank one.
Thus the observed word law itself demands at least two predictive states.

Control theory has now predicted a missing Marici object: a **history
behavior**, consisting of outcome words with their source-ordered
probabilities. One-time effect values cannot represent this distinction.

## Move 3: physical state and predictive belief are different

The detector memory is physically either ready or dead. An observer who sees
only records carries a belief \(r=\Pr(R)\). A photon-bin click has probability

\[
q_c(r)=\frac9{25}r.
\]

After a no-click record the normalized belief becomes

\[
r^+=\frac{9+7r}{25-9r}.
\]

For the exact prior \(r=1/2\), the same no-click record produces
\(r^+=25/41\), neither physical pure state. The belief simplex is therefore
an epistemic prediction object derived from the instrument and record; it is
not the detector's physical memory carrier.

This predicts a second missing Marici object: a **filter state** with a
normalization/update law. Conflating it with the source state would turn
observer information into physical ontology.

## Move 4: observability requires intervention authority

An empty bin always records no-click from both \(R\) and \(D\), so passive
one-bin observation cannot distinguish them. A photon probe produces click
probabilities \(9/25\) and zero respectively, so their output laws are
different. The controlled word `empty, photon, click` has probability
\(9/25\) from \(R\) and \(81/625\) from \(D\).

The distinction is not supplied by a richer readout alone. It uses Aspect's
separate source-preparation constructor. Hence the Marici observability object
must include a declared family of admissible interventions, not merely a
detector effect family. Algebraic probe capability does not authorize physical
preparation.

## Move 5: recovery is an exact storage semigroup

Starting dead, after \(k\) empty bins the dead mass is

\[
d_k=(16/25)^k.
\]

The next photon clicks with conditional probability

\[
q_k=\frac9{25}\left(1-(16/25)^k\right).
\]

Thus dead-state mass is a source-derived storage variable satisfying

\[
d_{k+1}-d_k=-\frac9{25}d_k.
\]

This is not energy storage; it is unavailable detector capability. The
control comparison predicts that Marici needs resource types richer than one
undifferentiated energy notion. Here the relevant resource is readiness.

## Move 6: the next missing-state test

The two-state model predicts the geometric recovery deficit

\[
9/25-q_k=(9/25)(16/25)^k.
\]

If a calibrated apparatus violates this recurrence, the discrepancy is not a
parameter adjustment inside the ready/dead model. It predicts additional
state: recovery age, afterpulse memory, or another hidden mode. Predictive
Hankel rank across controlled histories supplies the finite discriminator.

This completes one comparative loop:

`source instrument -> control behavior -> missing-object prediction -> exact source test -> refined Marici type`.

## Disposition

The example constructs four Marici candidates from one source-typed optical
fragment:

1. an outcome-history behavior;
2. a filter/belief state distinct from physical memory;
3. an intervention-indexed observability object;
4. a readiness storage and dissipation law.

These are source-typed sector objects because their maps are derived from
Aspect's instrument. They are not yet operations of the common scalar
Carrier. The next cross-sector question is whether an established Carrier
history, incidence, or instrument operation realizes the same four-object
pattern without erasing occurrence provenance.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 9/10. The strongest gain is the separation of physical memory, belief,
record history, and probe authority. The unusually small two-state model is
the main confound.

Raw delta: iid sufficiency is eliminated; the hidden-memory and history-rank
branches survive; a single realized no-click remains nonfaithful, while
controlled output laws distinguish the pure memory states. Four candidate
Marici objects and one exact enlargement falsifier are constructed. The
checker passes 16 of 16 exact tests. Continuous time, afterpulsing, graded
recovery, and common-carrier realization remain open.
