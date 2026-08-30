# Theta Clark jet tower is source-closed but zero-loop supply is positive

## Functorial jet generation

Let

\[
 F(s)=\int_0^L f(q)e^{sq}\,dq
\]

with a theta-class source. Spectral differentiation is the source operation

\[
 F^{(k)}(s)=\int_0^L q^k f(q)e^{sq}\,dq.
\]

Multiplication by (q) preserves the finite-cutoff test space and the
superexponentially decaying completed theta space. Hence every finite Mellin
jet is generated inside the same source category.

For nonzero real (a), define the Clark operator

\[
 \mathcal C_a=1+ia\partial_s.
\]

Its iterates obey

\[
 \mathcal C_a^jF
 =\sum_{k=0}^j\binom jk(ia)^kF^{(k)}.
\]

This is triangular with nonzero diagonal coefficient ((ia)^j). Therefore
the first (m+1) Clark iterates span the first (m+1) Mellin jets. Higher
ports need not be adjoined after inspecting a zero multiplicity; they arise
by composition of one authorized constructor.

## Observability at arbitrary finite multiplicity

Suppose (s_0) is a zero of multiplicity (m). Then

\[
 F(s_0)=F'(s_0)=\cdots=F^{(m-1)}(s_0)=0,
 \qquad
 F^{(m)}(s_0)\ne0.
\]

It follows that

\[
 \mathcal C_a^jF(s_0)=0
\]

for (j<m), while

\[
 \mathcal C_a^mF(s_0)=(ia)^mF^{(m)}(s_0)\ne0.
\]

Use the ordinary endpoint row

\[
 O_0=\begin{pmatrix}1&F(s_0)\end{pmatrix}
\]

and the first nonzero Clark row

\[
 O_m=\begin{pmatrix}1&\mathcal C_a^mF(s_0)\end{pmatrix}.
\]

Their joint Gramian has determinant

\[
 |a|^{2m}|F^{(m)}(s_0)|^2>0.
\]

Thus the filtered Clark jet family is jointly faithful at every zero of finite
multiplicity. Since a nonzero entire function has only finite-order isolated
zeros, this covers every scalar zero without assuming simplicity.

## Why this is filtered rather than one Hilbert tower

The statement is pointwise finite: each zero is resolved at its first nonzero
jet. It does not assert that the infinite direct sum of all jet rows is a
bounded observation operator. Such a claim would require source-derived
weights and a separate completion theorem.

The natural object is therefore a filtered jet prolongation. Every finite
stage is authorized and exact; no single infinite norm is silently imposed.

## Identity-loop supply

At a transmission zero, the total endpoint shear is the identity. On an
identity loop with equal endpoint storage, Kitaev's storage-cocycle theorem
gives boundary supply equal to the path Gramian:

\[
 Q_{\mathrm{loop}}=W_{\mathrm{loop}}.
\]

For the Clark rows above, this Gramian is positive definite. Therefore a
faithful zero-state does not have vanishing loop supply. Scalar silence removes
the endpoint displacement, but the transverse jet channel carries a strictly
positive relationship current.

## Consequence for zero confinement

A Green identity cannot infer (\delta=0) by declaring all boundary supply
zero at a scalar zero. Once the source-authorized jet ports are retained, the
zero has positive boundary supply.

Any zero-confinement theorem must instead derive an additional signed current
whose contribution cancels this positive Clark supply for an admissible
zero-state. The primitive, prime-square, mixed-seam, and archimedean channels
are the remaining candidates. Their cancellation must be typed and
source-local, not imposed after scalar aggregation.

## Falsifier

Source closure fails if repeated Clark differentiation leaves the declared
theta test space or if its triangular jet coefficient vanishes. Finite
observability fails if the first nonzero derivative gives a singular two-row
Gramian. A zero-flux argument fails immediately if it omits the positive Clark
loop supply.

## Scope

This proves source closure and pointwise finite observability of the Clark jet
tower at every scalar zero. It also proves that a faithful zero carries
positive identity-loop supply. It does not construct its cancelling arithmetic
current, establish an infinite jet Hilbert completion, orient zeros, or prove
RH.
