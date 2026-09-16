# The positive Witt obstruction is an explicit principal-angle multiplier

## Generic Halmos block

Let \(P\) and \(Q\) be two orthogonal projections. On a two-dimensional generic Halmos block, choose coordinates such that

\[
P=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]

Write the principal angle as \(\theta\in(0,\pi/2)\). Then

\[
Q=
\begin{pmatrix}
\cos^2\theta&\cos\theta\sin\theta\\
\cos\theta\sin\theta&\sin^2\theta
\end{pmatrix}.
\]

Set

\[
c=\cos\theta,
\qquad
s=\sin\theta.
\]

## Signed and absolute operators

The signed difference is

\[
D=P-Q.
\]

Its eigenvalues are \(-s\) and \(s\). Therefore

\[
|D|=sI.
\]

The common remainder that would be required to reduce the positive pair \((P,Q)\) to the Jordan pair of \(D\) is

\[
K_\theta
=\frac{P+Q-|P-Q|}{2}.
\]

Since the eigenvalues of \(P+Q\) are \(1-c\) and \(1+c\), the eigenvalues of \(K_\theta\) are

\[
\kappa_-(\theta)
=\frac{1-c-s}{2},
\]

\[
\kappa_+(\theta)
=\frac{1+c-s}{2}.
\]

For every strict generic angle,

\[
c+s>1.
\]

Hence

\[
\kappa_-(\theta)<0.
\]

Positive common-face Jordan reduction fails on every nontrivial generic Halmos block.

## Exact obstruction size

The negative-part magnitude is

\[
\eta(\theta)
=\frac{c+s-1}{2}.
\]

It vanishes at the two boundary geometries:

\[
\eta(0)=0,
\qquad
\eta(\pi/2)=0.
\]

It is maximal at \(\theta=\pi/4\):

\[
\max\eta
=\frac{\sqrt2-1}{2}.
\]

Thus the obstruction is concentrated in the genuine generic-angle or plunge sector. It disappears on exact common and exact orthogonal atoms.

## Contraction coordinate

Let

\[
\lambda=\cos^2\theta
\]

be the eigenvalue of the inside compression \(PQP\). Then

\[
c=\sqrt\lambda,
\qquad
s=\sqrt{1-\lambda}.
\]

The obstruction multiplier becomes

\[
\eta(\lambda)
=
\frac{
\sqrt\lambda+
\sqrt{1-\lambda}-1
}{2}.
\]

It is positive precisely for

\[
0<\lambda<1.
\]

It vanishes at \(\lambda=0,1\) and reaches its maximum at \(\lambda=1/2\).

## Functional calculus

Let \(B=PQP|_{\operatorname{ran}P}\) be the generic compression. The negative obstruction of the forced common remainder is unitarily represented by

\[
\eta(B)
\]

on the generic principal-angle carrier, with the corresponding outside copy supplied by the Halmos polar unitary.

Therefore asymptotic positive minimalization is equivalent to control of one explicit functional-calculus multiplier rather than an unnamed negative remainder.

## Correct asymptotic condition

Let \(M_\alpha\) denote the observer/source map into the generic contraction carrier. A graph-form version of the required estimate is

\[
\|\eta(B_\alpha)^{1/2}M_\alpha g\|^2
\longrightarrow0
\]

for every vector in a common phase-energy core, together with a regulator-uniform graph bound sufficient for lower semicontinuity and recovery.

For operator-norm reduction one would require

\[
\|\eta(B_\alpha)\|\longrightarrow0.
\]

That condition is generally too strong whenever genuine plunge eigenvalues remain near \(1/2\).

The form-level condition can still hold if observer mass in the middle-angle sector vanishes in the completion topology.

## Bulk and boundary interpretation

Near \(\lambda=1\), the two projection ranges are nearly common. The negative obstruction tends to zero, while the positive eigenvalue of \(K_\theta\) retains the common bulk.

Near \(\lambda=0\), the ranges are nearly orthogonal. Both common-remainder eigenvalues tend to zero, and the absolute fold is already close to minimal.

Near \(\lambda=1/2\), neither interpretation dominates. This is the maximal positive-Witt obstruction and the precise sector requiring analytic control.

## Relation to dyadic refinement

Dyadic Halmos refinement does not reduce total Gram by itself. It resolves the spectrum of \(B\) into progressively finer angle bands.

Its useful role here is diagnostic. It isolates the middle-angle bands on which \(\eta(B)\) is large and the endpoint bands on which positive reduction is asymptotically harmless.

Any proof of minimalization must show that the observer-weighted contribution of the middle bands has the required limit. Merely increasing dyadic depth cannot create additional positive capacity.

## Consequence for the completion gate

The first quantitative input for the reduced absolute form is now

\[
q_\alpha^{obs}(g)
=
\langle M_\alpha g,
\eta(B_\alpha)M_\alpha g\rangle.
\]

The relevant question is whether this obstruction form vanishes, remains finite as a nonzero boundary correction, or must be incorporated into the limiting positive form.

The answer cannot be obtained from signed convergence because \(\eta(B)\) is invisible to \(P-Q\) as a signed common-face test.

## Disposition

For projection-pair polarities, failure of positive Witt reduction is measured exactly by

\[
\eta(\lambda)
=
\frac{
\sqrt\lambda+
\sqrt{1-\lambda}-1
}{2}.
\]

The open minimalization theorem is therefore an observer-weighted spectral estimate for this explicit principal-angle multiplier on the generic Halmos sector.
