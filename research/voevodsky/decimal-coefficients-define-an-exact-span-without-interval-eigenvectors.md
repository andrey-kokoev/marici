# Decimal coefficients define an exact span without interval eigenvectors

## Question

How can exported floating Ritz and tail coefficients become an exact finite certificate object without asserting that interval boxes contain a distinguished orthonormal eigenbasis?

## Claim boundary

Treat each emitted decimal as an exact rational number and define the selected subspace by its column span. Orthogonal projection, tail orthogonalization, captured trace, and the final quadratic form are then finite rational-plus-integral constructions. No interval eigenvector theorem or choice of an exact point inside independent coefficient balls is required.

## Exact selected span

Let

\[
C:\mathbb R^{25}\longrightarrow H_{160}
\]

be the exported \(160\times25\) coefficient matrix, padded from its first 80 rows, with decimal strings interpreted as rationals. Define

\[
G=C^*C.
\]

It suffices to certify \(G>0\). The orthogonal projection onto the exact decimal span is

\[
P=C G^{-1}C^*.
\]

This construction is invariant under every invertible change of the 25 column coordinates. Near-orthonormality of \(G\) is useful conditioning evidence but is not part of the definition.

## Exact tail map

Let \(D:\mathbb R^{25}\to H_{160}\) be the exported decimal tail matrix. Its exact orthogonalized version is

\[
D_Q=(I-P)D
=D-CG^{-1}C^*D.
\]

Therefore

\[
C^*D_Q=0
\]

holds algebraically. The certificate need not prove that independently rounded columns happened to remain exactly orthogonal.

## Captured concentration trace

Let \(K=C^*TC\). The concentration trace captured by the exact selected span is

\[
\operatorname{Tr}(PTP)
=
\operatorname{Tr}(G^{-1}K).
\]

Thus the complement trace residual is

\[
\rho=rac{70}{\pi}-\operatorname{Tr}(G^{-1}K).
\]

An interval upper bound \(\rho<1/130\) proves the complement concentration bound directly.

## Coordinate form of the Schur certificate

Set

\[
Z=C-D_Q.
\]

For coefficient vectors \(x\in\mathbb R^{25}\), the trial vector is \(Zx\). Every candidate and residual Gram matrix is a quadratic form in these fixed coordinates. Positivity of the resulting \(25\times25\) matrix proves positivity for all nonzero \(x\); normalization by \(G\) is needed only to quote a Hilbert-space spectral margin, not to prove positivity.

If an explicit normalized margin is desired and

\[
L\geq\mu G,
\]

then the induced form has lower bound \(\mu\) on the selected span.

## Interval implementation

A rigorous checker should:

1. parse coefficient strings as exact rationals or zero-radius Arb values;
2. prove \(G>0\) by interval \(LDL^*\);
3. enclose \(G^{-1}\) or solve interval systems with residual verification;
4. construct \(D_Q\) through the displayed formula;
5. enclose \(K\), \(\rho\), the tail floor, and the final lower form;
6. prove the lower form positive by interval \(LDL^*\).

Independent entry radii may be added later to absorb source-rounding uncertainty, but they are not needed to define an exact candidate from emitted decimals.

## Disposition

The coefficient gate is reduced from interval certification of eigenvectors to certification of an exact decimal span and finite matrix inverses. The current coefficient checker, which only asks whether interval Gram entries contain identity and zero cross-Gram entries, is diagnostic and must be superseded by this exact-span construction before continuum certification. No continuum positivity or RH implication is asserted.
