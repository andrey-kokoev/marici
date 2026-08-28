# The Mixed Cauchy Defect Is a Dirichlet Green Kernel

## Result

Let

\[
\phi(u)=e^{-|u|/2},
\qquad
\delta(u,v)=\phi(u+v)-\phi(u)\phi(v).
\]

The previous mixed-sector calculation showed that \(\delta(u,v)\) vanishes
when \(u,v\) have the same sign and is positive when their signs are
opposite.  On the positive-frequency chart put

\[
K(x,y)=\delta(x,-y),\qquad x,y>0.
\]

Then

\[
K(x,y)
=e^{-|x-y|/2}-e^{-(x+y)/2}
=2\sinh\!\left(\frac{\min(x,y)}2\right)
 e^{-\max(x,y)/2}.
\]

This is exactly the Dirichlet Green kernel on the half-line for

\[
L=-\frac{d^2}{dx^2}+\frac14.
\]

Thus the failure of the Cauchy observer to be multiplicative across the two
Fourier--Tate sectors is not merely entrywise positive.  It is a positive
definite source kernel.

## Direct Gram factorization

For prime frequencies \(x=\log p\), \(y=\log q\),

\[
K(\log p,\log q)
=\sqrt{\frac{\min(p,q)}{\max(p,q)}}-\frac1{\sqrt{pq}}
=\frac{\min(p,q)-1}{\sqrt{pq}}.
\]

Define

\[
f_p(r)=\frac{\mathbf 1_{[1,p]}(r)}{\sqrt p}
\quad\in L^2([1,\infty),dr).
\]

Then

\[
K(\log p,\log q)=\langle f_p,f_q\rangle.
\]

Consequently, for every finite complex packet \((c_p)\),

\[
\sum_{p,q}\overline{c_p}K(\log p,\log q)c_q
=\int_1^\infty
\left|\sum_{p\ge r}\frac{c_p}{\sqrt p}\right|^2dr
\ge0.
\]

The nested indicator functions for distinct primes are linearly independent,
so every finite prime Gram matrix is strictly positive definite.

The same statement holds for arbitrary distinct positive frequencies.  The
Green-kernel identification gives the canonical continuum completion and
shows that this positivity is imposed by the Cauchy scale, not by prime
arithmetic.

## Meaning

The relationship energy between the two one-sided Mellin sectors is the
Dirichlet energy seen through the resolvent \(L^{-1}\).  The boundary at
\(x=0\) is the sewing seam.  Within either sector the observer is a character;
after opposite-sector composition, the lost multiplicativity reappears as a
positive Green energy.

This is the first universal coupled positivity theorem in the present Euler
completion lane: opposite-sector composition produces positive half-line
Green energy.

It also explains why the half-offset is rigid.  The decay exponent \(1/2\)
becomes the mass term \(1/4\) in \(L\).

## Scope correction: the raw energy is not the BSY entropy

The positivity is too strong to identify its raw quadratic form directly
with the Balazard--Saias--Yor entropy.  Under RH that entropy vanishes.  But a
strictly positive finite Gram form vanishes only when its mixed coefficient
packet vanishes.  Reciprocal theta--Tate sewing is nontrivial, so an equality

\[
\mathcal D_{\mathrm{BSY}}=\langle c,Kc\rangle
\]

would incorrectly force the mixed sewing state itself to disappear under RH.

Therefore the physical quantity must be relative.  The viable architecture
expresses \(\mathcal D_{\mathrm{BSY}}\) as the mixed Green bulk minus a
source-derived modular boundary repair.

The Green bulk is now canonical and positive.  All remaining RH content lies
in deriving the boundary repair from the primitive, prime-square,
archimedean, and seam channels, then proving that the resulting relative form
is the BSY divisor entropy.

## Next theorem and falsifier

Derive the actual mixed-word coefficient packet before scalar aggregation and
compute its Green current.  The target identity is a source-typed Schur or
Green formula

\[
\mathcal D_{\mathrm{BSY}}(c)
=\langle c,Kc\rangle-B_{\mathrm{mod}}(c),
\]

where \(B_{\mathrm{mod}}\) is fixed independently by theta--Tate boundary data.

The smallest falsifier uses one forward and one backward prime-frequency
word.  If the declared modular current fails to reproduce the exact boundary
term of the Dirichlet Green identity, or if it is chosen only after evaluating
the BSY scalar, the proposed completion square does not close.
