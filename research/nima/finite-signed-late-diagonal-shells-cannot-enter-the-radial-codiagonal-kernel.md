# Finite signed late diagonal shells cannot enter the radial codiagonal kernel

## Question

Can cancellation between finitely many signed diagonal prime shells produce a nonzero packet in the balanced radial codiagonal kernel?

## Claim boundary

Not for finitely many sufficiently late shells with distinct lower endpoints. Their diagonal autocorrelations have strictly ordered double-exponential separation tails. The shell with smallest lower endpoint decays slowest and cannot be cancelled by later shells; induction removes every coefficient. Infinite projective loadings and shells crossing a theta transition require separate estimates.

## Finite signed packet

Let

\[
a_1<a_2<\cdots<a_N
\]

be lower endpoints beyond the finite transition region of the first completed-theta label. Let \(\rho_j(t)\) denote the corresponding real diagonal shell autocorrelation and take complex coefficients \(c_j\). Suppose the loaded packet lies in the radial codiagonal kernel. Then its derivative source vanishes, rapid decay removes the integration constant, and

\[
\sum_{j=1}^N c_j\rho_j(t)=0
\]

for every sufficiently large positive \(t\).

## Ordered separation tails

For late shells, the first completed-theta label controls the autocorrelation. The shifted factor has leading exponential

\[
\exp\left[-\pi e^{2(u+t)}\right].
\]

Endpoint localization at the lower shell boundary gives each nondegenerate shell a nonzero leading factor of the form

\[
\rho_j(t)
=B_j(t)
\exp\left[-\pi e^{2a_j}e^{2t}\right]
\left(1+o(1)\right),
\]

where \(B_j(t)\) contains only exponential and polynomial factors of lower order than the displayed double exponential. Higher theta-label pairs are superexponentially smaller and do not change this ordering.

For \(j>1\),

\[
\frac{\rho_j(t)}{\rho_1(t)}
=
\frac{B_j(t)}{B_1(t)}
\exp\left[
-\pi\left(e^{2a_j}-e^{2a_1}\right)e^{2t}
\right]
\left(1+o(1)\right)
\longrightarrow0.
\]

The nonzero first-shell leading factor makes division legitimate away from at most isolated large parameters.

## Inductive coefficient extraction

Divide the vanishing combination by \(\rho_1(t)\) and let \(t\to+\infty\). Every later-shell ratio vanishes, so

\[
c_1=0.
\]

Remove that term and repeat with \(a_2\), then successively with every lower endpoint. This yields

\[
c_1=c_2=\cdots=c_N=0.
\]

Therefore no nonzero finite signed or complex combination of distinct late diagonal shells lies in the codiagonal kernel.

## Strength boundary

The proof uses separation coordinate asymptotics, not wall positivity. It therefore permits arbitrary finite signs and phases. It does not yet cover:

- infinitely many shells, where the smallest active endpoint may be absent or tail interchange may fail;
- repeated lower endpoints with different internal labels;
- shells meeting a zero or transition of the leading completed-theta atom;
- ordered off-diagonal label pairs.

Those cases require a uniform asymptotic basis or the retained label recovery observer.

## G4 consequence

For every finite late cutoff, the diagonal signed source survives the radial codiagonal faithfully. Any finite-cutoff G4 radical that removes such a packet must therefore come from a later metric, gauge relation, or non-source compression, not from endpoint–Wronskian balancing.

This supplies a cutoff-level hostile: a proposed G4 quotient fails if it declares a nonzero finite late diagonal packet null while preserving the source radial codiagonal.

## Direction rescore

- Finite signed late diagonal loading: excluded from the codiagonal kernel.
- Infinite projective signed loading: 8/10; requires uniform tail interchange.
- Repeated-endpoint internal labels: 7/10.
- Ordered off-diagonal packets: 7/10.
- G4 radical identification: interface-blocked.

## Disposition

The codiagonal is faithful on every finite signed family of distinct sufficiently late diagonal shells. The next depth-first extension is the infinite projective loading, where one must control tail limits uniformly rather than appeal to finite induction. No RH conclusion is authorized.
