# The Stieltjes incidence closes the cyclic prime lift but not its enlarged Green extension

## Rehydrated source result

The arithmetic-to-endpoint incidence already exists. For \(L=\log p\),

\[
J_pe_1=W_L,
\qquad
J_pe_2=W_{2L}
\]

in the reduced Stieltjes space \(L^2(\nu)\).

Its Gram matrix is

\[
A_p=J_p^*J_p
=
\begin{pmatrix}
a_p&z_p\\
\bar z_p&b_p
\end{pmatrix},
\]

with the source bounds

\[
m_\nu^2
\le a_p\le b_p\le1.
\]

Thus neither endpoint is in the cyclic Green radical.

## Pauli-frame lower bound

Let

\[
X=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
Y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
\]

The two-port observer

\[
\mathcal O_pv
=
\begin{pmatrix}
J_pXv\\
J_pYv
\end{pmatrix}
\]

satisfies the exact twirl identity

\[
\mathcal O_p^*\mathcal O_p
=
XA_pX+YA_pY
=
2
\begin{pmatrix}
b_p&0\\
0&a_p
\end{pmatrix}.
\]

Hence

\[
2m_\nu^2I
\le
\mathcal O_p^*\mathcal O_p
\le
2I
\]

uniformly over primes.

The endpoint cross-correlation \(z_p\) cancels. Therefore no endpoint-angle
estimate is needed to preserve the primitive and square arithmetic
coordinates on the cyclic cell.

## What is actually missing

Let \(\mathcal G_p^{\mathrm{cyc}}\) be the cyclic Stieltjes Green space and let

\[
\mathcal G_p^{\mathrm{full}}
=
\mathcal G_p^{\mathrm{cyc}}
\oplus
\mathcal G_p^{\mathrm{aux}}
\]

denote the full wall--history--tail/PV--reciprocal cell before radical
reduction.

The unresolved map is an extension

\[
\iota_p:
\mathcal G_p^{\mathrm{cyc}}
\longrightarrow
\mathcal G_p^{\mathrm{full}}
\]

such that:

1. \(\iota_p\) preserves the polarized Stieltjes Green form;
2. the full trace restricts to the established endpoint trace;
3. the full radical has trivial intersection with
   \(\iota_p\mathcal G_p^{\mathrm{cyc}}\);
4. the \(X\) and \(Y\) outputs retain their types until the global evaluator;
5. the complete source sewing commutes with \(\iota_p\).

This is an extension/intertwining theorem, not an incidence-construction
theorem.

## Block criterion

Write the full Green form on reduced coordinates as

\[
G_p^{\mathrm{full}}
=
\begin{pmatrix}
A_p&C_p\\
C_p^*&D_p
\end{pmatrix}.
\]

If \(D_p\) is positive on its reduced support and

\[
\ker D_p\subseteq\ker C_p,
\]

then eliminating the auxiliary sector gives the effective cyclic form

\[
A_p^{\mathrm{eff}}
=
A_p-C_pD_p^\dagger C_p^*.
\]

The Stieltjes incidence survives faithfully exactly when

\[
\mathcal O_p^*
\begin{pmatrix}
A_p^{\mathrm{eff}}&0\\
0&A_p^{\mathrm{eff}}
\end{pmatrix}
\mathcal O_p
\]

has a prime-uniform positive lower bound in the typed two-port frame.

A sufficient normalized condition is

\[
\left\|
A_p^{-1/2}
C_pD_p^\dagger C_p^*
A_p^{-1/2}
\right\|
\le1-\delta_{\mathrm{ext}}.
\]

Then

\[
A_p^{\mathrm{eff}}
\ge
\delta_{\mathrm{ext}}A_p,
\]

and the established cyclic Pauli bound yields a full-cell lower bound
proportional to \(2\delta_{\mathrm{ext}}m_\nu^2\).

## Exact restriction alternative

The strongest desired result is not merely a contraction estimate but exact
restriction:

\[
C_pD_p^\dagger C_p^*=0
\]

on the cyclic endpoint incidence range.

That would mean the auxiliary sector supplies orientation and completion
without loading the already established primitive--square energy.

This is unlikely if the odd Schur return is genuinely generated through the
tail/PV history. In that case the correct target is strict loading, not
decoupling.

## Relation to the overlap matrix

The finite wall--endpoint comparison and the Stieltjes incidence are both
known. The first unresolved overlap entry is now the complete return

\[
K_p^{\mathrm{return}}
=
A_p^{-1/2}
C_pD_p^\dagger C_p^*
A_p^{-1/2}.
\]

The extension passes if \(1\) is uniformly excluded from its spectrum. In the
positive case, strict contraction is a clean sufficient certificate.

Thus the finite wall--endpoint--prime packet has reduced to one local
Birman--Schwinger operator.

## Completion

Twisted Mellin equivariance should make the return prime diagonal. If so,

\[
K^{\mathrm{return}}
=
\bigoplus_pK_p^{\mathrm{return}},
\]

and completion requires

\[
\sup_p\|K_p^{\mathrm{return}}\|<1.
\]

The \(O(\sqrt{\log p})\) history-lift growth is harmless under the frozen
primitive-square coefficient product. The live completion risk is saturation
of the normalized return, not summability.

## Hostiles

1. Preserve \(J_p\) but let the enlarged radical intersect its range.
2. Keep both endpoint norms positive while the Schur return kills one Pauli
   output.
3. Prove strict loading for every prime with norms tending to one.
4. Preserve the scalar Euler readout while losing the \(Y\)-oriented port.
5. Use a fitted auxiliary inverse before proving
   \(\ker D_p\subseteq\ker C_p\).
6. Control diagonal prime returns but permit cross-prime coherent loading.

## Verdict

The source Stieltjes incidence \(J_p\) and its uniform cyclic arithmetic margin
are already complete.

The next executable local theorem is the enlarged-cell extension estimate

\[
\sup_p
\left\|
A_p^{-1/2}
C_pD_p^\dagger C_p^*
A_p^{-1/2}
\right\|
<1.
\]

This is the exact point where the cyclic endpoint realization either survives
the complete causal-history Green constructor or is lost to an auxiliary
Schur return.
