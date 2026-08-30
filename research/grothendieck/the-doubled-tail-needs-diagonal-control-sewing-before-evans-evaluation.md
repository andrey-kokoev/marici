# The doubled tail needs diagonal control sewing before Evans evaluation

## One sheet after the infinity condition

For a fixed source `f`, consider the homogeneous rank-two tail system

\[
G'(q)+sG(q)+c f(q)=0,
\qquad
c'(q)=0.
\]

Impose `G(infinity)=0`. Whenever the tail integral exists, every solution is

\[
G(q)=c\int_q^\infty f(v)e^{s(v-q)}\,dv.
\]

Thus the pre-Evans solution module of one sheet has complex rank one. Its sole
free coordinate is the constant-channel amplitude `c`. Evaluation at zero is

\[
G(0)=cF(s),
\qquad
F(s)=\int_0^\infty f(v)e^{sv}\,dv.
\]

This is a genuine source-derived zero-to-boundary-state bridge, but it does not
orient the coefficient `F(s)`.

## Naive doubling is rank two

Before reciprocal sewing, the plus and minus sheets have independent constant
amplitudes `(c_+,c_-)`. Their decaying solution module is therefore
`C^2`. Any single complex Evans row on this module has a nonzero kernel by the
constructible-rank obstruction.

Consequently the doubled system cannot be treated as two independent decaying
tails followed by one scalar comparison. A coherence law must act on the
control channels before the Evans projection.

## Diagonal control sewing

The minimal source-compatible sewing identifies the amplitudes,

\[
c_+=c_-=:c.
\]

This is the pullback of the two sheet-control maps over one common source
amplitude. The sewn pre-Evans module is again a line. A terminal sum readout
then becomes

\[
E_s(c)=c\bigl(F_+(s)+F_-(s)\bigr).
\]

The exact checker verifies the rank transition

\[
2\longrightarrow1
\]

and exhibits a nonzero scalar-null vector before sewing.

## What the sewing proves and does not prove

Diagonal control sewing resolves a typing defect. It makes the two-sheet
comparison a single source preparation rather than an arbitrary pair of
preparations. This is the control-tower coherence required by the multi-tower
picture.

It does not prove zero exclusion. On the sewn line, the Evans map is injective
exactly when its coefficient is nonzero:

\[
F_+(s)+F_-(s)\neq0.
\]

For the completed theta source that coefficient is the scalar function whose
zeros are under investigation. Therefore the diagonal pullback cannot itself
explain RH; it reconstructs the correctly typed spectral problem.

Nor may the equality `c_+=c_-` be imposed merely to obtain rank one. It must be
derived from the fact that both sheets are localizations of one labelled
source amplitude. Alternative source-authorized incidence could select a
different line and a different Evans coefficient.

## Multi-tower meaning

The input and output towers are insufficient without a control tower:

- the input tower supplies the source amplitude;
- the two transport towers produce the decaying plus and minus tails;
- the control coherence says both transports act on the same preparation;
- the Evans map reads the sewn terminal pair.

The cross-tower coherence cell is therefore not decorative. Without it the
constructible image has rank two and scalar exclusion is algebraically
impossible. With it, the rank defect is repaired but the analytic nonvanishing
problem remains intact.

## Next gate

Derive the sheet-control incidence from the labelled theta/Tate source and
then ask whether the complete boundary currents impose a second relation on
the rank-one coefficient before scalar evaluation. If every current merely
reconstructs `F_++F_-`, the construction is exact but non-explanatory. A real
advance requires an independently derived off-seam constraint on that
coefficient.
