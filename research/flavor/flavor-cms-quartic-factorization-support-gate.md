# CMS quartic factorization and support gate

Work package: WP589  
Owner: marici.Figueiredo

## Two independent gates

WP588 establishes the detector-factorization gate: a completed detector row is
independent of unknown portal-tangent lifts when it factors through the known
coupling projection \((\kappa_t^2,\kappa_4)\).

That condition is not sufficient by itself. The calibrated detector row must
also be defined on a domain overlapping the source-sensitive portal family.
WP589 applies both gates to the released CMS HHH quartic scan.

## Factorization passes

An idealized pure quartic response row is

\[
D_q=\begin{pmatrix}0&1&0\end{pmatrix}.
\]

It annihilates the representative lift-kernel coordinate and factors through
the known coupling pair. Thus the obstruction identified here is not an
algebraic failure of the quartic coordinate.

## Support fails

The released CMS scan fixes \(\kappa_t=1\). On the universal portal domain,

\[
\kappa_t^2=1-z,
\qquad
\kappa_4=1+{\lambda_s z^2\over\lambda_H}.
\]

Therefore

\[
\kappa_t=1
\quad\Longrightarrow\quad
z=0
\quad\Longrightarrow\quad
{\partial\kappa_4\over\partial\lambda_s}=0.
\]

The source-sensitive domain requires \(z>0\), so its intersection with the
released CMS slice is empty. If the boundary point is retained formally, the
combined source Jacobian has rank one: inclusive mixing sees the transverse
\(z\)-direction, while the quartic \(\lambda_s\)-column is zero.

## Consequence

Detector factorization and source-domain support are logically independent.
The CMS quartic coordinate passes the former as an algebraic row and fails the
latter as a released physical experiment. It therefore cannot supply WP588's
rank-two completion.

The operation remains a real physical quartic readout on its own kappa
framework slice. On the portal domain it is neither a selector nor a
rigidifier, and it does not refine the positive \(\lambda_s\)-fiber. No
reference port is involved.

The smallest repair is publication of the calibrated factorized quartic
response on a nonzero-mixing domain. If the response depends on additional
generator coordinates, the alternative repair is the complete source-derived
tangent and detector transport for those coordinates on that same domain.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp589_cms_quartic_factorization_support_gate.py

The generated result is
research/flavor/results/wp589_cms_quartic_factorization_support_gate.json.
