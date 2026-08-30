# Theta Evans forcing residual is the oscillatory separation transform

## Bounded question

What is the exact mixed-sheet forcing difference left by the source-derived
boundary-control Evans system?

## Tail pairings

Assume the completed logarithmic source (f) is real and put

\[
z=a+it.
\]

For the direct tail

\[
G_z(q)=\int_q^\infty f(v)e^{z(v-q)}\,dv,
\]

the forcing pairing is

\[
I_+(z)=\langle f,G_z\rangle
=\int_{q<v}f(q)f(v)e^{\overline z(v-q)}\,dq\,dv.
\]

For the reciprocal tail at \(-\overline z\),

\[
I_-(z)
=\int_{q<v}f(q)f(v)e^{-z(v-q)}\,dq\,dv.
\]

## Exact residual

With equal scalar controls, the doubled forcing residual from packet 230 is

\[
R_f(z)=2\Re\left(I_-(z)-I_+(z)\right).
\]

Writing (d=v-q>0) gives

\[
R_f(a+it)
=-4\int_{q<v}
f(q)f(v)\sinh(ad)\cos(td)\,dq\,dv.
\]

Define the positive separation measure in the variable (r>0):

\[
d\mu_f(r)
=\left(
\int_0^\infty f(q)f(q+r)\,dq
\right)dr
\]

when (f\ge0). Then

\[
R_f(a+it)
=-4\int_0^\infty\sinh(ar)\cos(tr)\,d\mu_f(r).
\]

## Orientation and oscillation

The hyperbolic factor has the sign of (a), but the cosine factor changes
sign with spectral height. Positivity of the source and of its separation
measure therefore does not orient the residual.

At (t=0), the sign is automatic:

\[
\operatorname{sgn}R_f(a)=-\operatorname{sgn}a
\]

for a nontrivial positive source. At general (t), no such conclusion follows.
A positive two-atom separation measure already produces cosine sign changes.

## Identification with the earlier curvature obstruction

The residual depends only on pairwise source separation and an oscillatory
character. This is the same invariant that appeared in the order-two theta
curvature factorization and in the mixed-sheet Green calculation. The Evans,
curvature, and reciprocal-separation lanes have not produced independent RH
conditions. They are three presentations of one source transform.

This compression matters epistemically: agreement among the three lanes is one
piece of evidence, not three.

## Exact remaining modular theorem

The source-current problem is now equivalent to orienting

\[
\int_0^\infty\sinh(ar)\cos(tr)\,d\mu_f(r)
\]

after the complete primitive, prime-square, seam, and archimedean sewing is
retained. A formal antiderivative or scalar regrouping does not solve it.

The required theorem must provide a source-local decomposition in which the
negative cosine bands are paired or transported into positive contributions,
or else show that the completed current cancels the oscillatory residual
exactly.

## Hostile falsifier

Replace \(\mu_f\) by two positive atoms. The cosine transform changes sign at
explicit heights even though the measure, reciprocal symmetry, Evans bridge,
and hyperbolic orientation all survive. Any proposed theorem using only these
features is therefore insufficient. It must invoke additional modular
structure of the theta separation measure.

## Scope

This packet computes the exact doubled Evans forcing residual and identifies it
with the oscillatory positive-separation transform. It proves that source
positivity and reciprocal hyperbolic orientation do not control its sign. It
does not derive the missing modular current identity or prove RH.
