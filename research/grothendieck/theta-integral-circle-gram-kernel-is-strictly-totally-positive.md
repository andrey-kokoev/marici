# The integral-circle Gram kernel is strictly totally positive

## Bounded question

Which aggregations preserve the all-order labelled sign regularity proved in
packet 112?

## Labelled kernel

Let

\[
 K(t,n)=b(t,n^2),
 \qquad t\ge1,
 \qquad n\in\mathbb Z_{>0}.
\]

For every order `r`, ordered scales `t_1<...<t_r`, and ordered labels
`n_1<...<n_r`, packet 112 proves

\[
 \operatorname{sgn}\det[K(t_i,n_j)]
 =\varepsilon_r,
\]

where `epsilon_r` depends only on the order and is never zero.

## Source-faithful quadratic aggregation

Define the two-copy Gram kernel

\[
 \mathcal G(t,s)
 =\sum_{n\ge1}K(t,n)K(s,n).
\]

The sum converges absolutely and locally uniformly on `t,s>=1` because of the
Gaussian decay in `n^2`.  For ordered tuples `t_1<...<t_r` and
`s_1<...<s_r`, Cauchy--Binet gives

\[
\begin{aligned}
 \det[\mathcal G(t_i,s_j)]
 =\sum_{1\le n_1<\cdots<n_r}
 &\det[K(t_i,n_k)]\\
 &\times\det[K(s_j,n_k)].
\end{aligned}
\]

Each factor has sign `epsilon_r`, so every product is strictly positive.
At least one label tuple exists, and convergence permits the finite-truncation
limit. Therefore

\[
 \boxed{
 \det[\mathcal G(t_i,s_j)]>0
 \quad\text{at every finite order}.}
\]

The Gram kernel is strictly totally positive of infinite order.

## Operator form

If `B` is the map from winding coefficients to scale profiles,

\[
 (Bc)(t)=\sum_{n\ge1}K(t,n)c_n,
\]

then

\[
 \mathcal G=BB^*.
\]

The theorem is not merely positivity of `BB*`; it states positivity of every
ordered minor.  Integral square separation supplies the coherent orientation
whose sign disappears only after the two determinant factors are multiplied.

This is the exact all-order version of

\[
 \text{two labelled copies}
 +\text{faithful contraction}
 \longrightarrow
 \text{positive coupled readout}.
\]

## Why linear theta aggregation is different

The Riemann Fourier kernel is the linear compression

\[
 \Phi(t)=\sum_{n\ge1}K(t,n),
\]

not the Gram kernel `G`.  Cauchy--Binet has no second oriented determinant in
this scalar contraction.  Consequently the theorem above cannot be shortened
to a claim that the translate kernel of `Phi` is totally positive.

Indeed, total positivity of the appropriate translation kernel of `Phi`,
combined with the standard analytic hypotheses, is essentially the missing
Pólya/Laguerre orientation and therefore cannot be inferred merely from the
labelled theorem without proving a new aggregation law.

## Explanation and scope

This precisely locates what scalar observation destroys:

\[
 \boxed{
 \text{labelled orientation survives quadratic comparison but is erased by
 one-sided summation}.}
\]

The result is a universal coupled positivity theorem for the completed
integral-circle source.  It is not RH because the physical Xi readout is
linear and oscillatory after Mellin/Fourier transformation.

The next admissible attack is to ask whether the modular seam or endpoint
differential supplies a canonical **second orientation factor** for the
linear readout.  A construction that merely squares `Phi` changes the physical
question.  The falsifier is any proposed linear aggregation identity whose
purported second factor cannot be derived before scalar compression.
