# The Prime-Square Current Is the Rank-One Seam Image

## Method-of-images factorization

Let

\[
L=-\frac{d^2}{dx^2}+\frac14.
\]

The inverse of \(L\) on the full line has kernel

\[
G_{\mathbb R}(x,y)=e^{-|x-y|/2}.
\]

For \(x,y>0\), imposing the Dirichlet condition at the sewing seam \(x=0\)
gives the method-of-images kernel

\[
G_D(x,y)
=G_{\mathbb R}(x,y)-G_{\mathbb R}(x,-y)
=e^{-|x-y|/2}-e^{-(x+y)/2}.
\]

This is exactly the mixed Cauchy defect found in Entry 3929.  Its second term
is not an arbitrary counterterm.  It is the unique reflected image that makes

\[
G_D(0,y)=0.
\]

Moreover, the reflected kernel has rank one:

\[
G_{\mathbb R}(x,-y)=b(x)b(y),
\qquad
b(x)=e^{-x/2}.
\]

Thus for a finite mixed packet \(c=(c_j)\) supported at positive frequencies
\(x_j\),

\[
Q_D(c)
=Q_{\mathbb R}(c)
-\left|\sum_j c_j e^{-x_j/2}\right|^2.
\]

The universal seam repair is therefore a source-fixed rank-one boundary
channel.

## Energy identity

For the point source

\[
\mu=\sum_jc_j\delta_{x_j},
\]

put \(u=G_D\mu\).  Then \(Lu=\mu\), \(u(0)=0\), and

\[
Q_D(c)
=\langle\mu,L_D^{-1}\mu\rangle
=\int_0^\infty
\left(
|u'(x)|^2+\frac14|u(x)|^2
\right)dx.
\]

Hence the earlier Gram positivity and the Green-current description are the
same theorem.  The mixed relationship weight is the energy of the unique
field whose seam value has been cancelled by its reflected image.

## Arithmetic specialization

At \(x_p=\log p\),

\[
b(x_p)=p^{-1/2}.
\]

The boundary repair becomes

\[
B_{\mathrm{seam}}(c)
=\left|\sum_pc_pp^{-1/2}\right|^2
=\sum_p\frac{|c_p|^2}{p}
+\sum_{p\ne q}\frac{\overline{c_p}c_q}{\sqrt{pq}}.
\]

Its diagonal is exactly the observed prime-square grade.  Thus the \(k=2\)
current is not merely another scalar subtraction: it is the diagonal shadow
of a coherent rank-one seam state.  The off-diagonal terms are the
cross-label data erased by scalar prime-square aggregation.

For the smallest forward--backward word at one prime,

\[
G_D(\log p,\log p)=1-\frac1p.
\]

The free mixed loop has weight \(1\), while sewing removes exactly \(1/p\).
This derives the prime-square correction without fitting it from the Euler
constant decomposition.

## Consequences for the completion square

There are now two distinct boundary operations:

1. The universal Dirichlet image repair converts the full-line Cauchy
   propagator into the positive mixed-sector kernel.
2. The still-missing theta--Tate modular repair must convert that positive
   mixed Green energy into the relative BSY entropy.

Conflating them would double-count the square channel.  Any proposed modular
current must state whether its \(k=2\) term is the rank-one image above or an
additional arithmetic boundary contribution.

The next finite audit is therefore forced.  Retain two distinct primes and
compare the typed coefficient of \(1/\sqrt{pq}\) in the completed
theta--Tate boundary current with the rank-one image coefficient.  If the
modular construction reproduces only the diagonal \(1/p\) terms, it has lost
the seam coherence and cannot descend to the positive Green state.
