# The doubled quarter-turn history observer closes the full analytic margin

## Analytic observer

On the common closed history domain, define

\[
Q_\pm x=\frac1{\sqrt2}(x\pm iHx)
\]

and retain both reciprocal outputs:

\[
\mathcal A_{\rm hist}x=(Q_+x,Q_-x).
\]

This observer does not use the retained source identity coordinate.  Its two
components are the causal and anti-causal quarter-turn outputs themselves.

## Exact norm identity

The parallelogram identity gives

\[
\begin{aligned}
\|\mathcal A_{\rm hist}x\|^2
&=\frac12\|x+iHx\|^2+rac12\|x-iHx\|^2\\
&=\|x\|^2+\|Hx\|^2.
\end{aligned}
\]

Thus the doubled observer is an isometry from the history graph norm into the
reciprocal two-channel output:

\[
\|\mathcal A_{\rm hist}x\|=\|x\|_{\operatorname{graph}(H)}.
\]

In particular,

\[
\|\mathcal A_{\rm hist}x\|^2\ge\|x\|^2.
\]

No spectral estimate is needed for the doubled bound; the mixed terms cancel
exactly.

## Relation to the one-sheet estimates

The theta-mass theorem separately gives

\[
Q_\pm^*Q_\pm\ge\frac18I.
\]

Those estimates prove that each reciprocal sheet is individually bounded
below.  The doubled identity is stronger as a graph-norm statement and shows
that the pair observes every history direction, including any zero-trace bulk
direction.

Hence the earlier concern that endpoint traces might miss the even zero-trace
bulk does not apply to the complete doubled history observer.  It applies only
if one projects to endpoint traces before forming \(\mathcal A_{\rm hist}\).

## Radical descent

If an even bulk radical \(N_0\) is removed before completion, \(H\) descends on
the declared quotient and the same identity holds there.  Conversely, if

\[
\mathcal A_{\rm hist}x=0,
\]

then adding and subtracting the two equations gives

\[
x=0,
\qquad
Hx=0.
\]

Therefore the doubled analytic observer has zero radical on its graph domain.

## Prime and grade completion

The history operator is label diagonal:

\[
H=\bigoplus_{p,k}H_{p,k}.
\]

Consequently

\[
\mathcal A_{\rm hist}
=\bigoplus_{p,k}(Q_{p,k,+},Q_{p,k,-}),
\]

and the norm identity holds after summing any finite cutoff.  Projective-rung
convergence extends it to the completed labelled carrier.  The lower constant
is independent of prime, grade, and cutoff.

## Endpoint and wall coordinates

The half-density endpoint traces and explicit wall coordinate are continuous
on the history graph.  Adding them to the doubled observer can only increase
its positive norm.  They supply boundary orientation and linking data but are
not needed for analytic coercivity.

A terminal projection that keeps only endpoint traces would discard the bulk
and lose this theorem.  Such a projection is a later readout, not the complete
analytic G3 observer.

## G3 consequence

For the complete reciprocal history output, the analytic margin is explicit:

\[
\delta_A=1
\]

when measured against the history graph norm.  If G3 normalizes against the
underlying Hilbert norm instead, the same construction gives a lower bound at
least one.

This closes the full doubled-history contribution to \(\delta_A\), including
the zero-trace bulk.  Any additional analytic summand not contained in the
closed history graph must be audited separately, but endpoint, wall, and
Wronskian additions do not reduce the margin.

G3 remains open at the glue, coherent-diagonal, and global mixed margins, and
at preservation of the arithmetic frame by the terminal observer.  No RH
conclusion is authorized.
