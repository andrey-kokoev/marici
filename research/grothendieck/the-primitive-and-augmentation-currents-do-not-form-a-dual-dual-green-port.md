# The primitive and augmentation currents do not form a dual--dual Green port

## The typing problem

Let

\[
\mathcal S_P\subset \ell^2(P)\subset \mathcal S_P'
\]

be the rapid-decay prime rigging.  The primitive current

\[
b_p=\frac{\log p}{\sqrt p}
\]

is a continuous covector in \(\mathcal S_P'\), but not a vector in the
middle Hilbert space.  Aspect's cutoff calculation gives the same type to
the completed augmentation comb: its finite normalized representatives do
not converge as Hilbert states; the completed object is the augmentation
row in \(\mathcal S_P'\).

Consequently these two boundary objects cannot be inserted into the Green
form as though one were automatically a state and the other its response.
They have the same variance.  The canonical pairing is defined on

\[
\mathcal S_P'\times\mathcal S_P,
\]

not on \(\mathcal S_P'\times\mathcal S_P'\).

## No continuous dual--dual extension

There is no jointly continuous bilinear form

\[
B:\mathcal S_P'\times\mathcal S_P'\longrightarrow\mathbb C
\]

whose restriction to \(\mathcal S_P'\times\mathcal S_P\) is the canonical
test--distribution pairing.

Indeed, such a form would curry to a continuous map

\[
J:\mathcal S_P'\longrightarrow(\mathcal S_P')'\cong\mathcal S_P.
\]

Agreement with the canonical pairing would make \(J\) the identity on
\(\mathcal S_P\).  Finite-support packets are dense in the strong sequence
dual \(\mathcal S_P'\), so continuity would force \(J\) to be the identity
on all of \(\mathcal S_P'\).  This is impossible because, for example, the
primitive current belongs to \(\mathcal S_P'\setminus\mathcal S_P\).

Thus a formula that directly contracts the completed primitive current with
the completed augmentation current necessarily introduces extra structure:
a pivot, a regularization, a graph domain, or a separately sourced
comparison channel.

## Consequence for the neutral-relation programme

The local oriented form

\[
\Omega_p=\epsilon_p\wedge\mu_p
\]

is canonical on algebraic finite packets.  Its graph is neutral there.  The
obstruction is not its local sign and not finite maximality.  The obstruction
appears when both distinguished boundary sections complete into the dual
grade.  There is then no inherited Green contraction with which to state
maximal neutrality.

Choosing a weighted Hilbert pivot \(Z_\delta\) repairs the contraction for
each \(\delta>0\), but the choice of \(\delta\) is not selected by Fourier or
Mellin covariance and the primitive norm diverges as \(\delta\downarrow0\).
The pivot therefore cannot be silently treated as source data.

The correctly typed alternatives are now exhaustive:

1. derive a source map sending one completed current back into a test-grade
   mate;
2. derive a canonical renormalized pairing on the particular source orbit;
3. retain the two currents as parallel covectors and introduce an independent
   state-valued control port against which both are evaluated.

Adding further covector-valued coherence rungs cannot solve the variance
defect.  At least one constructor must change variance.

## Hostile test

For any proposed completed Green current, inspect every contraction.  If it
contains a term of the form

\[
\langle b,a\rangle,
\qquad b,a\in\mathcal S_P',
\]

the proposal must name the source-derived pivot or regularization that makes
the expression meaningful.  Agreement of its finite-cutoff values is not
sufficient: different pivots agree on finite packets while defining
different completed boundary relations.

This is the present real obstacle.  The missing RH constructor is not another
finite coherence cell.  It is a variance-changing boundary comparison that
turns the two completed covectors into an admissible Green pair without being
chosen from the desired zero confinement.

