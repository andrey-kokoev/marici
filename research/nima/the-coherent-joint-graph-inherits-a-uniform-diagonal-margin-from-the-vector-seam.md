# The coherent joint graph inherits a uniform diagonal margin from the vector seam

## Coherent sector

For the full labelled boundary seam, let

\[
J:\mathcal H_F^{\rm res}\to\mathcal H_I^G
\]

be the bi-bounded front-to-cut comparison.  The coherent pullback is its graph:

\[
H_{\rm coh}
=
\{(x,Jx):x\in\mathcal H_F^{\rm res}\}.
\]

Use the joint norm

\[
\|(x,Jx)\|_{\rm coh}^2
=\|x\|_F^2+\|Jx\|_I^2.
\]

There is a uniform lower comparison constant \(m_J>0\):

\[
\|Jx\|_I\ge m_J\|x\|_F.
\]

## Analytic observation of coherent states

Let \(\mathcal A\) be the doubled analytic observer on the cut/history
realization.  Its graph-norm margin is \(c_A>0\); in the normalized doubled
quarter-turn construction, \(c_A=1\):

\[
\|\mathcal A y\|^2\ge c_A\|y\|_I^2.
\]

Restrict the complete Green observer to the coherent graph and retain this
analytic component:

\[
J_{\rm Green}(x,Jx)
\supseteq\mathcal A(Jx).
\]

Then

\[
\|J_{\rm Green}(x,Jx)\|^2
\ge c_A\|Jx\|_I^2.
\]

The comparison lower bound gives

\[
\|x\|_F^2
\le m_J^{-2}\|Jx\|_I^2,
\]

so

\[
\|(x,Jx)\|_{\rm coh}^2
\le(1+m_J^{-2})\|Jx\|_I^2.
\]

Consequently

\[
\|J_{\rm Green}(x,Jx)\|^2
\ge
c_A\frac{m_J^2}{1+m_J^2}
\|(x,Jx)\|_{\rm coh}^2.
\]

Thus the coherent-diagonal margin satisfies

\[
\delta_{\rm diag}^2
\ge
c_A\frac{m_J^2}{1+m_J^2}>0.
\]

## Arithmetic reinforcement

On primitive-square coordinates, the retained Pauli observer additionally
gives

\[
\|\mathcal O x\|^2\ge2m_\nu^2\|x\|^2.
\]

Therefore the low-grade coherent margin can be sharpened by adding the
arithmetic and analytic lower bounds.  The connected grades need no arithmetic
coercivity: the bi-bounded vector seam and analytic observer already control
them through \(Jx\).

## Gauge and radical qualification

The estimate is on the reduced coherent graph after the compatible zero-trace
radical quotient.  If an authorized gauge remains, apply it on both source and
cut sides before using the bi-bounded comparison.  No nonzero coherent class
can be killed by the analytic observer because both \(J\) and \(\mathcal A\)
are bounded below.

The retained provenance identity is not used in the observer norm.  It appears
only in the construction of the closed graph.  Coherent observability comes
from the full analytic vector output.

## Cutoff uniformity

The constants \(m_J\) and \(c_A\) are independent of prime and grade.  All
maps commute with prime cutoffs and obey typed grade-cutoff naturality.
Therefore the same diagonal margin holds at every finite cutoff and on the
completed labelled graph.

## Scalar hostile

If the analytic vector \(Jx\) is first projected to the scalar Wronskian row,
the comparison lower bound disappears because the scalar coefficient tends to
zero.  The coherent margin then collapses along prime basis vectors.  Hence the
margin belongs before terminal scalarization.

## G3 consequence

The full labelled vector seam and doubled analytic observer close the coherent
common-mode margin:

\[
\delta_{\rm diag}
\ge
\sqrt{c_A}\frac{m_J}{\sqrt{1+m_J^2}}>0.
\]

The remaining independent G3 gate is the normalized mixed coupling between
coherent and disagreement sectors after all retained observer blocks are
assembled.  No RH conclusion is authorized.
