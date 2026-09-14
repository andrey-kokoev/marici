# Actual consecutive-prime fixed-ratio grade and reflection

## Question

How does the explicit product grade restrict to the actual consecutive-prime shell catalogue, and what does reciprocal reflection act on?

## Claim boundary

The actual catalogue resolves the fixed-ratio multiplicity: for reduced positive integers \(a,b\) with \(D=\log(a/b)\), every ordered theta-label pair at ratio \(m/n=a/b\) is uniquely

\[
(n,m)=(kb,ka),\qquad k\geq1.
\]

A source edge is therefore indexed by \((j,k)\), where \((p_j,p_{j+1})\) is a consecutive increasing prime pair. The grade

\[
W_D(j,k)=\log(kb p_jp_{j+1})
\]

and product sublevels give an explicit source-instantiated finite exhaustion.

## Consecutive-prime cutoff

Set

\[
E_{D,N}=\{(j,k):kb p_jp_{j+1}\leq N\}.
\]

Each set is finite, nested in \(N\), and exhaustive. Its interval is

\[
[\log(kbp_j),\log(kbp_{j+1})],
\]

with length \(\log(p_{j+1}/p_j)\). Consequently

\[
\log(p_{j+1}/p_j)
\leq W_D(j,k)
\leq \delta^{-1}e^{\delta W_D(j,k)}.
\]

The continuity constant remains independent of the cutoff.

## Correction to reciprocal closure

The actual shell catalogue requires \(p_j<p_{j+1}\). It does not contain the reversed tuple \((p_{j+1},p_j)\) as another source shell. Hence the earlier product-cutoff candidate's closure under \(p\leftrightarrow q\) is a property of its enlarged oriented-edge census, not of the actual consecutive-prime source.

Source reciprocal reflection instead exchanges the ordered theta labels:

\[
(n,m)=(kb,ka)
\longmapsto
(m,n)=(ka,kb),
\]

and therefore sends the ratio block \(D\) to \(-D\). It preserves the increasing shell pair. The reflected grade is

\[
W_{-D}(j,k)=\log(ka p_jp_{j+1})=W_D(j,k)+D.
\]

Thus it is not generally grade invariant, but differs by one blockwise additive constant. The projective seminorms transform exactly by

\[
q_\delta^{-D}(Rc)=e^{\delta D}q_\delta^D(c).
\]

Using the inverse block gives the reciprocal scaling back. Therefore reflection is a continuous projective-space isomorphism between the \(D\) and \(-D\) blocks. At \(D=0\) it is grade preserving.

## Disposition

The actual shell catalogue supplies the previously missing fixed-ratio multiplicity and validates product-sublevel continuity after restriction to consecutive primes. Withdraw within-block \(p\leftrightarrow q\) closure as a source claim. Retain it only for a deliberately enlarged oriented interval graph. Reciprocal source coherence belongs between the \(D\) and \(-D\) blocks and is controlled by an additive grade shift.
