# The affine seven is the spin-two instance of the four-s-minus-one representation dimension

> Scope correction: (mathcal H_{2s-1}) is selected as the ladder cokernel endpoint only on the diagonal (r=s). At spin two the matching cokernel belongs to ladder grade two; the grade-three ladder cokernel has dimension nine. Thus the representation-dimension explanation is diagonal, not uniform across grade.

## General-spin coordinate extension

For a spin-\(s\) source, the covariant fold replacing the spin-two coefficient
\(4-a\) has coefficient \(2s-a\).  The path polynomial becomes

\[
c_j=inom gj(-1)^{g-j}
a^{\overline{g-j}}(2s-a)^{\overline j}.
\]

Use the natural general-spin chart locus

\[
q=2g+4s,
\qquad
a_{\max}=g+4s.
\]

As in the spin-two proof, only the \(a=0\) minus endpoint and the
\(a=g+4s\) plus endpoint meet preferred rows zero and one.

## Endpoint calculation

For the minus endpoint, only \(c_g=(2s)^{\overline g}\) survives.  Its two
row values are proportional to

\[
v_{s,g}=(2g+4s-1,3g+4s-1).
\]

For the plus endpoint, \(m=1\) and

\[
\frac{c_1}{c_0}
=\frac{g(g+2s)}{2g+4s-1}.
\]

Consequently

\[
2\frac{c_1}{c_0}+1-g
=\frac{3g+4s-1}{2g+4s-1},
\]

so the same row cocircuit is forced on both source endpoints.

The affine family is therefore

\[
v_{s,g}=F_s(g,1)^T,
\qquad
F_s=
\begin{pmatrix}
2&4s-1\\
3&4s-1
\end{pmatrix}.
\]

Its discriminant is

\[
|\det F_s|=4s-1.
\]

## Representation-theoretic factor

The irreducible spherical harmonic representation of degree \(l\) has
dimension \(2l+1\).  At

\[
l=2s-1,
\]

this gives

\[
\dim\mathcal H_{2s-1}=4s-1=|\det F_s|.
\]

For the physical spin-two source,

\[
s=2,qquad l=3,qquad \dim\mathcal H_3=7,
\]

and

\[
F_2=\begin{pmatrix}2&7\\3&7\end{pmatrix}.
\]

This distinguishes the correct generalization from the accidental alternative
\(2s+3\), which agrees at \(s=2\) but fails already at \(s=3\).

## What this explains

The integer seven is no longer an unexplained affine offset.  It is the
spin-two specialization of a source-derived representation dimension.  The
same spin-bundle geometry controls:

- the covariant Laurent fold through \(2s-a\);
- the endpoint cocircuit through \(4s-1\);
- the harmonic multiplicity through \(\dim\mathcal H_{2s-1}\).

Thus the affine and harmonic appearances of seven have a common constructor:
the integral representation theory of the spin bundle on the sphere.

## Aspect-germ boundary

This theorem explains the integer but does not yet turn it into a physical
charge quotient.  The representation \(\mathcal H_{2s-1}\) supplies seven
weight states at \(s=2\), while \(\operatorname{coker}F_2\) supplies a cyclic
group of order seven.  Equal cardinality and common source dependence do not
identify these objects:

```text
harmonic representation: rank-seven state space / weight packet
affine discriminant:      cyclic torsion group of order seven
```

Aspect's native-arity gate still demands an attachment morphism between the
representation germ and the affine determinant line.  No canonical map

\[
\mathcal H_3\longrightarrow\mathbb Z/7
\]

is supplied by \(SO(3)\) representation theory alone.  Indeed the natural
weight/root quotient for the rotation group is not an order-seven object.

The result therefore relocates the missing constructor.  We no longer need a
mechanism explaining why the coefficient is seven.  We need a mechanism that
turns the representation dimension into a cyclic charge residue.

## New exact question

The next comparison germ must answer:

> Does the magnetic source contain a determinant-line, Euler-class, or
> boundary-index morphism sending the integral class of
> \(\mathcal H_{2s-1}\) to \(\operatorname{coker}F_s\), rather than merely
> assigning them the same integer?

At spin two, such a morphism would be the first legitimate bridge from the
seven-dimensional physical harmonic block to the cyclic discriminant seven.
