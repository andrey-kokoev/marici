# Character-probe kernels are shell-polynomial interpolation kernels

## Question

What known equality controls the observed rule that completion of an arithmetic Boolean \(n\)-cube requires \(n-1\) modulated settings beyond the coarse incidence readout?

## Claim boundary

There is an exact linear-algebra factorization of every probe kernel through evaluation of shell-index Laurent polynomials. It explains the setting count whenever the relevant residue uses \(n\) distinct shells and the corresponding evaluation matrix is monic on that residue subspace. The factorization alone does not prove that every canonical cube creates such a residue, that it is the first one globally, or that the modular rank statements lift to characteristic zero.

## Shell decomposition

Let \(E=\bigoplus_{j\in J}E_j\) be the edge space decomposed by adjacent-prime shell index, let \(V\) be the vertex space, and let

\[
B_j:E_j\longrightarrow V
\]

be ordinary signed incidence restricted to shell \(j\). For

\[
x=\sum_jx_j
\]

define its shell-residue polynomial

\[
R_x(z)=\sum_j B_j(x_j)z^j\in V\otimes k[z,z^{-1}].
\]

The checker’s modulated incidence operator is exactly

\[
B_z(x)=R_x(z).
\]

Consequently, for a finite set of settings \(T=\{t_0,\ldots,t_{m-1}\}\),

\[
\ker(B_{t_0},\ldots,B_{t_{m-1}})
=
\{x\in E:R_x(t_r)=0\;\forall r\}.
\]

This is the controlling equality. A blind route is an edge assignment whose vertex-valued shell polynomial vanishes at every selected character.

## Categorical factorization

Define the shell-divergence map

\[
\Phi:E\longrightarrow V\otimes k^J,
\qquad
\Phi(x)=(B_jx_j)_{j\in J}.
\]

Let

\[
\operatorname{ev}_T:k^J\longrightarrow k^T,
\qquad
(a_j)_j\longmapsto\left(\sum_j a_jt^j\right)_{t\in T}.
\]

Then the complete probe factors as

\[
E\xrightarrow{\Phi}V\otimes k^J
\xrightarrow{1_V\otimes\operatorname{ev}_T}V\otimes k^T.
\]

Probe faithfulness on a subspace \(Q\subseteq E\) is precisely monicity of the composite restricted to \(Q\). Thus the setting problem is an interpolation problem on the image \(\Phi(Q)\), rather than a property of graph size alone.

## Vandermonde mechanism

Suppose the residue is supported on distinct shell indices

\[
j_1<\cdots<j_n.
\]

Evaluation at \(n\) settings has matrix

\[
M_{ri}=t_r^{j_i}.
\]

For consecutive exponents this is an ordinary Vandermonde matrix up to a nonzero monomial factor. For arbitrary increasing exponents over positive ordered settings it is a generalized Vandermonde matrix. Monicity of \(M\) forces every shell divergence \(B_{j_i}x_{j_i}\) to vanish separately.

With only \(n-1\) independent evaluations, \(M\) has a kernel of dimension at least one. A completed cube can turn that interpolation kernel into an actual edge-cycle residue. This gives the observed count:

The coarse setting \(z=1\), together with \(n-1\) modulated settings, supplies \(n\) evaluations.

## Derivative form

The Euler operator converts character derivatives into shell moments:

\[
\left.\left(z\frac{d}{dz}\right)^kR_x(z)\right|_{z=1}
=
\sum_j j^kB_j(x_j).
\]

Hence separated settings and a confluent jet at \(z=1\) are two bases for the same finite interpolation problem. The phrase “prime-index derivative” is accurate for this dual character coordinate: it means moments of the adjacent-prime shell index, not differentiation of the prime values \(p_j\).

## Relation to augmentation ideals

The standard cubical expression

\[
(g_1-1)\cdots(g_n-1)
\]

belongs to the \(n\)-th power of an augmentation ideal, and a one-parameter character sends it to

\[
\prod_i(z^{j_i}-1).
\]

That identity has an \(n\)-fold zero at \(z=1\). It is structurally adjacent to the present mechanism, but it is not yet an identification of the computed blind route with an augmentation-graded class. The checker acts on shell-weighted edge incidence; the exact established object is \(R_x(z)\). A comparison with an augmentation quotient requires an explicit map carrying the cubical boundary class to the shell-residue polynomial.

## Strongest falsification attempt

The interpolation explanation would fail if the declared settings were linearly dependent on the first five shell characters. Exact rational elimination of

\[
M_{ri}=t_r^i,
\qquad
1\leq i\leq n,
\]

for \(2\leq n\leq5\), using

\[
1,\frac56,\frac34,\frac7{10},\frac23,
\]

must give rank \(m\) for every prefix of \(m\leq n\) settings and rank \(n\) at \(m=n\). Repeating a setting must instead produce a nonzero determinant obstruction and rank loss.

## Disposition

The known equality behind the phenomenon is vector-valued polynomial evaluation, with its Vandermonde and confluent-derivative forms. The arithmetic novelty is localized: canonical consecutive-prime cubes repeatedly materialize the next interpolation-kernel direction at their final-edge grades. Establishing a functorial augmentation-filtration interpretation remains open.
