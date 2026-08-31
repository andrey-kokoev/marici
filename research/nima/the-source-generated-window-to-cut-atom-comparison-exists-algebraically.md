# The source-generated window-to-cut-atom comparison exists algebraically

## Common finite source

Let \(\mathcal A_{\mathrm{fin}}\) be the finite linear span of labelled
prime-power scale atoms \(e_{p,k}\), with

\[
a_{p,k}=k\log p.
\]

There are two source-derived maps:

\[
F:=D\mathcal K,
\qquad
Fe_{p,k}=q_{a_{p,k}},
\]

and

\[
I:=\mathcal I,
\qquad
Ie_{p,k}=u_{p,k}=(g_{a_{p,k}},h_{a_{p,k}}),
\]

with Euler weights retained as separate diagonal coefficients when required.

## Injectivity of the front realization

Suppose a finite packet satisfies

\[
\sum_jc_jq_{a_j}=0,
\qquad
a_j>0
\]

with distinct \(a_j\).  Fourier transformation gives

\[
\widehat f_0(\xi)
\sum_jc_j\left(e^{-2\pi ia_j\xi}-e^{2\pi ia_j\xi}\right)=0.
\]

The Gaussian transform never vanishes.  Distinct exponentials are linearly
independent, so every \(c_j=0\).  Hence \(F\) is injective on the finite
labelled source.

Prime-power locations are distinct across different labels: if

\[
k\log p=\ell\log q,
\]

then \(p^k=q^\ell\), which for primes forces \(p=q\) and \(k=\ell\).
Thus no hidden cross-prime collision occurs.

## Canonical algebraic comparison

Because \(F\) is injective, define

\[
\boxed{
J_0:F(\mathcal A_{\mathrm{fin}})
\longrightarrow I(\mathcal A_{\mathrm{fin}}),
\qquad
J_0(Fc)=Ic.
}
\]

This map is well defined and unique.  Labelwise,

\[
J_0(q_{a_{p,k}})=u_{p,k}.
\]

It is not fitted from endpoint scalar ratios; it is induced by the common
source parameterization.  It preserves prime and grade labels, reciprocal
orientation, and every finite cutoff.

For the strict first-Adams packet, applying the frozen orientation matrix
\(S_{12}=\operatorname{diag}(-1,+1)\) on the source gives

\[
J_0(-q_L+q_{2L})=-u_{p,1}+u_{p,2}.
\]

Thus the grade-one sign twist is transported before any trace readout.

## Literal arithmetic readout

On the cut-atom side,

\[
N_0(g_{a_{p,k}})=\Phi'(a_{p,k}).
\]

After the logarithmic Euler boundary coefficient,

\[
2kL\,\frac1k p^{-k/2}N_0(g_{kL})
=\kappa_p^{(k)}.
\]

Therefore the composite

\[
F(\mathcal A_{\mathrm{fin}})
\xrightarrow{J_0}
I(\mathcal A_{\mathrm{fin}})
\xrightarrow{N_0}
\mathbb C^{(\mathbb P\times\mathbb N)}
\]

has exactly the frozen Euler-to-theta sampling values.  The Gaussian-smoothed
ordinary transpose of \(F\) is bypassed rather than inverted: the comparison
passes through the common source graph.

## What this closes

On every finite labelled packet, including the primitive/square first-Adams
cell:

- the endpoint--archimedean comparison exists algebraically;
- it is unique on the source-generated front range;
- it preserves prime, grade, and reciprocal signs;
- its cut-side normal trace is literal theta sampling;
- no inverse heat operator or fitted scalar is used.

Hence local common-carrier **existence** is closed at the algebraic level.

## Completion gate

Nothing above proves that \(J_0\) is bounded, closable, or Green-isometric in
the declared completed topologies.  The front family can become poorly
conditioned under infinite synthesis even though every finite packet is
independent.  The cut-atom norm is constant before Euler loading, whereas the
window/front norms and mutual Grams have different scale behavior.

The earliest remaining theorem is therefore:

> Prove that the graph of \(J_0\) is closed, or identify its closure, in the
> source-authorized joint Green topology; then show that the resolved and
> cut-atom radicals agree on that graph.

The connected tail is included algebraically but requires its nuclear
completion to be compared with the front synthesis completion.  Global closed
range and radical descent remain open.  No RH conclusion is authorized.
