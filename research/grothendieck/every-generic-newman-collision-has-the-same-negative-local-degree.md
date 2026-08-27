# Every Generic Newman Collision Has the Same Negative Local Degree

## Collision map

On the real spectral axis define the coupled map

\[
\mathcal F(\lambda,x)
=
\left(H_\lambda(x),\partial_xH_\lambda(x)\right).
\]

Its zeros are exactly the real multiple zeros of the Newman family. This is
the coupled value--tangent system that survived every scalar source-shape
falsifier.

At a generic collision write

\[
A=H_{xx}(\lambda_0,x_0)\neq0,
\qquad
B=H_{xxx}(\lambda_0,x_0).
\]

Using \(H_\lambda=-H_{xx}\), the Jacobian with variables ordered as
\((\lambda,x)\) is

\[
D\mathcal F
=
\begin{pmatrix}
-A&0\\
-B&A
\end{pmatrix}.
\]

Therefore

\[
\det D\mathcal F=-A^2<0.
\]

Every generic collision has Brouwer local degree \(-1\), independent of the
theta source, collision height, third derivative, or label presentation.

## Global counting consequence

Let \(\Omega\) be a bounded rectangle in the \((\lambda,x)\)-plane whose
boundary contains no zero of \(\mathcal F\), and assume every collision inside
is generic. Brouwer degree gives

\[
\deg(\mathcal F,\Omega,0)
=-#\{\text{collisions in }\Omega\}.
\]

Collisions cannot cancel one another in the boundary winding because all have
the same sign. This is stronger than merely saying that collisions are
isolated.

The finite-height reachability problem therefore reduces to one boundary
observable:

\[
\operatorname{wind}_{\partial\Omega}
\left(H_\lambda(x)+iH_x(\lambda,x)ight).
\]

If that winding is zero, the rectangle contains no generic collision. If it
is negative, its magnitude counts them exactly. Higher collisions can be
handled by perturbation or local multiplicity, but their sign must be audited
separately.

## Why this is a genuine compression

The earlier labelled-current target attempted to show directly that the
value and tangent coordinates never vanish together at any interior point.
The degree theorem replaces that two-dimensional search by a one-dimensional
boundary calculation. It also prevents scalar cancellation among multiple
bad events.

This does not make the problem finite automatically. Taking spectral height
to infinity requires the all-scale carrier from the preceding packets. But at
every fixed height, collision reachability is completely measured by one
source-derived boundary winding.

## Aspect-style apparatus

The boundary of \(\Omega=[\lambda_-,\lambda_+]\times[-T,T]\) has four typed
ports:

1. the physical-time edge \(\lambda=\lambda_-\);
2. the de Bruijn real-phase edge \(\lambda=\lambda_+\);
3. the positive-height wall \(x=T\);
4. the negative-height wall \(x=-T\).

The complete winding is the mate of those four ports. Computing only the two
heat-time edges is a destructive completion because collisions can enter
through the height walls. Reciprocal symmetry relates the height walls but
does not erase their oriented contribution.

This is precisely Aspect's architecture: retain every boundary port until the
native two-dimensional degree has been formed, then compress.

## Remaining theta theorem

The next finite calculation should derive the four edge phases directly from
the theta integral and ask whether their combined winding vanishes for
\(0\leq\lambda\leq\lambda_+\). The infinity programme must then prove that the
height-wall contribution has a controlled all-scale limit.

The two outstanding gates are now sharply separated:

1. finite rectangles: compute or constrain one coupled boundary degree;
2. infinite height: prove compatibility of those degrees under exhaustion.

## Scope

Uniform negative local degree is exact and universal. A vanishing global
boundary degree for the theta family has not been proved. No RH conclusion is
claimed.

