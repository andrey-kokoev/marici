# The front Stieltjes state gives a canonical bounded pairing for window multipliers

## Result

The comoving kernel lands naturally in a multiplier algebra, but a multiplier algebra has no canonical Hilbert inner product.

The source front \(H\) supplies the missing state: its Stieltjes measure

\[
d\nu=-dH.
\]

Using the cyclic vector \(1\in L^2(\nu)\), every endpoint multiplier becomes a Hilbert vector, and the adjacent-window mixed pairing is bounded, nonzero, and has a fixed sign.

This constructs a canonical relative-pairing candidate. It does not yet prove that this state is the complete source Green energy.

## Source measure

Assume \(H\) is continuous, strictly decreasing, with the source boundary normalization

\[
H(-\infty)=1,
\qquad
H(+\infty)=0.
\]

Then

\[
\nu((a,b])=H(a)-H(b)
\]

defines a probability measure on the \(q\)-line.

If \(H\) is differentiable,

\[
d\nu(q)=-H'(q)\,dq.
\]

The measure is source-derived from the same front that defines the windows. No external Gaussian or Lebesgue state is inserted.

## Cyclic multiplier representation

Let

\[
\mathcal H_\nu=L^2(\mathbb R,d\nu).
\]

Every bounded window \(W_t\) acts by multiplication on \(\mathcal H_\nu\). The constant function \(1\) belongs to \(\mathcal H_\nu\) and has norm one.

Define the source-state embedding

\[
\iota_\nu:
L^\infty(\nu)\to\mathcal H_\nu,
\qquad
\iota_\nu(f)=f\cdot1.
\]

Then

\[
\|\iota_\nu(f)\|_{L^2(\nu)}
\le
\|f\|_\infty.
\]

Composing with the comoving kernel gives

\[
\mathcal M_{\mathrm{fin}}(\mathbb R_t)
\xrightarrow{\mathcal K}
L^\infty(\nu)
\xrightarrow{\iota_\nu}
L^2(\nu).
\]

Thus arithmetic delta incidences now have concrete Hilbert endpoint images

\[
\delta_t\longmapsto W_t\in L^2(\nu).
\]

## Canonical polarized pairing

Define

\[
\langle f,g\rangle_\nu
=
\int_{\mathbb R}
\overline{f(q)}g(q)\,d\nu(q).
\]

For source measures \(\mu,\lambda\),

\[
G_\nu(\mu,\lambda)
=
\left\langle
\mathcal K\mu,\mathcal K\lambda
\right\rangle_\nu.
\]

This form is positive and bounded:

\[
|G_\nu(\mu,\lambda)|
\le
\|\mu\|_{\mathrm{TV}}
\|\lambda\|_{\mathrm{TV}}.
\]

It is automatically Hermitian and descends through exactly the kernel of the represented comoving transform in \(L^2(\nu)\).

## Endpoint energies

For \(t>0\),

\[
W_t(q)<0
\]

on the strict-front support. Hence

\[
\|W_t\|_{L^2(\nu)}^2
=
\int|W_t|^2\,d\nu
>0.
\]

At prime endpoints,

\[
a_p^\nu
=
\|W_{\log p}\|_{L^2(\nu)}^2,
\]

\[
b_p^\nu
=
\|W_{2\log p}\|_{L^2(\nu)}^2.
\]

Since \(t\mapsto|W_t(q)|\) is increasing and \(\log p\ge\log2\),

\[
a_p^\nu,b_p^\nu
\ge
m_\nu^2,
\]

where

\[
m_\nu^2
=
\int
|W_{\log2}(q)|^2\,d\nu(q)>0.
\]

Also

\[
a_p^\nu,b_p^\nu\le1.
\]

Therefore the endpoint Green candidate has a prime-uniform absolute scale in the source Stieltjes state.

## Adjacent mixed pairing

Let

\[
L=\log p,
\qquad
D_L=W_{2L}-W_L.
\]

The order relations are

\[
-1\le W_{2L}\le W_L\le0,
\qquad
D_L\le0.
\]

Define the oriented multiplier pairing

\[
\beta_p^\nu
=
\left\langle
W_{2L},
D_LW_L
\right\rangle_\nu
=
\int
W_{2L}(q)D_L(q)W_L(q)\,d\nu(q).
\]

Every factor is real. Where the adjacent annulus has positive front mass,

\[
W_{2L}<0,
\qquad
D_L<0,
\qquad
W_L<0,
\]

so the product is negative. Strictness gives

\[
\beta_p^\nu<0.
\]

The magnitude obeys

\[
|\beta_p^\nu|
\le1.
\]

Thus the local mixed scalar is bounded and has the reciprocal endpoint orientation fixed by the order \(L\to2L\).

Reversing the endpoint order replaces \(D_L\) by \(-D_L\) and reverses the sign.

## Pauli frame in the Stieltjes metric

Let \(J_p:\mathbb C^2\to L^2(\nu)\) send

\[
e_1\mapsto W_L,
\qquad
e_2\mapsto W_{2L}.
\]

Its diagonal Gram entries are \(a_p^\nu,b_p^\nu\). The Pauli-twirl identity yields

\[
\|J_pXv\|_\nu^2+\|J_pYv\|_\nu^2
\ge
2m_\nu^2\|v\|^2.
\]

Thus the arithmetic two-port frame survives this source-state realization uniformly over primes. Endpoint correlation cancels exactly.

## Authority boundary

The Stieltjes state is canonical relative to the front \(H\), but it is not automatically the complete Green state required by the RH constructor.

The source must still prove one of:

- the relative Green boundary form is exactly \(G_\nu\);
- it is uniformly equivalent to \(G_\nu\);
- or a comparison cell transports \(G_\nu\) into the declared Green form.

Set membership and positivity alone do not establish that identity.

In particular, the scalar \(\beta_p^\nu\) must not be identified with the desired Adams mixed block merely because both are bounded and oriented.

## Remaining theorem

The frontier is now an exact metric-authority comparison:

> Prove that the source Green/Stokes form pulled back through the comoving kernel equals, or is uniformly equivalent to, the front Stieltjes pairing on the endpoint and adjacent-window incidence range.

If this holds, the first strict Adams edge has explicit lifts, positive endpoint scales, a bounded oriented mixed pairing, prime diagonality, and harmless completion growth.
