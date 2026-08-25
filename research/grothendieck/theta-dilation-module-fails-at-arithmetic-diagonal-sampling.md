# The dilation module fails at arithmetic diagonal sampling

## Bounded question

Can the hyperbolically centered two-copy fibers be placed in one fixed
Hilbert module whose scale translation produces the Laguerre density as a
positive matrix coefficient?

## Continuous dilation carrier

For a label pair `(n,m)`, packet 118 reduces the centered bulk to functions of

\[
 q=nm\,e^S
\]

and the centered difference `delta`, together with the fixed ratio label
`c_nm=log(m/n)`.  On the continuous radial space

\[
 L^2(\mathbb R_+,dq/q),
\]

the shift `S -> S+tau` is the unitary dilation

\[
 (T_\tau F)(q)=F(e^\tau q).
\]

Thus a fixed continuous Hilbert module exists after adjoining the label and
`delta` fibers.

## Physical readout is sampling, not an overlap

The theta density at scale `S` does not integrate the radial variable `q` with
Haar measure. It evaluates each label-pair section on the arithmetic diagonal

\[
 q=nm\,e^S
\]

and then sums over `(n,m)`.  Schematically,

\[
 g_n(S)
 =\sum_{m,n}\int
 \left|F_{m,n}(nm\,e^S,\delta)\right|^2d\delta
 +\text{seam terms}.
\]

By contrast, a unitary coefficient has the form

\[
 \langle H,T_SH\rangle
 =\int_0^\infty
 \overline{H(q)}H(e^Sq)\,\frac{dq}{q}.
\]

Evaluation on moving arithmetic points and Haar overlap of two transported
sections are different operations. Therefore continuous dilation does not
provide the spectral factor conjectured in packet 126.

## Exact location of the missing structure

\[
 \boxed{
 \text{dilation module exists;
 matrix-coefficient factorization fails at arithmetic diagonal sampling}.}
\]

The failure is not caused by the moving hyperbolic center, which is fixed by
the ratio label. It occurs when the continuous radial carrier is compressed to
the multiplicative semigroup of integer products `nm`.

This is the same structural boundary seen earlier in the adelic bridge:
finite-place integrality selects a discrete sector, but continuous
archimedean transport does not automatically become a faithful overlap on
that sector.

## Correspondence target

The next object must be a source-derived sampling correspondence

\[
 \mathbb R_+
 \xleftarrow{\;p\;}
 \mathcal Z
 \xrightarrow{\;q\;}
 \mathbb N\times\mathbb N
\]

whose pull--push converts radial dilation into labelled arithmetic sampling.
Any norm factor from this operation must retain multiplicities of the product
map `(n,m)->nm`; finite-to-one is not one-to-one.

The likely algebra is Mackey-like: pull along the continuous scale map, apply
the label transport, and push along the product fibers with their exact
cardinalities or weights.  Only such a correspondence could turn the sampled
readout into a genuine positive coefficient without erasing arithmetic
provenance.

## Falsifier

The smallest hostile test is a product value with two distinct factorizations,
for example `6=1*6=2*3=3*2=6*1`.  Construct the corresponding finite sampling
fiber and test whether the proposed pull--push inner product is independent of
factorization order and carries the required positive norm.

Failure of that Mackey square would disprove the spectral-factor programme at
the arithmetic sampling step, before any Fourier or zero computation.
