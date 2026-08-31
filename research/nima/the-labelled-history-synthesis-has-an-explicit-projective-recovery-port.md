# The labelled history synthesis has an explicit projective recovery port

> **Status update.** The successor packet
> `the-full-fourier-observer-is-jointly-faithful-on-the-codiagonalized-translated-theta-source.md`
> proves that the complete Fourier family is algebraically faithful after the
> common-history codiagonal. The fibrewise recovery below remains the explicit
> continuous inverse before codiagonalization; quantitative continuity after
> codiagonalization remains open.

## Question

Can the source label coefficients be recovered continuously from the completed labelled theta-history range without claiming a Hilbert lower bound?

## Claim boundary

Yes. Fiberwise coefficient extraction followed by inversion of the exact Euler half-density coefficient gives a left inverse on the source-generated labelled range. It is continuous in the projective exponential topology with a shift of slightly more than one half exponential order. It is not bounded on the unweighted Hilbert direct sum and does not survive an undeclared codiagonal that erases label projections.

## Normalized fibre extraction

For \(\lambda=(p,k)\), let

\[
L_\lambda=k\log p,
\qquad
a_\lambda=\frac1k e^{-L_\lambda/2}.
\]

Write the two translated source atoms as

\[
\theta_\lambda^+=\tau_{L_\lambda}\Phi,
\qquad
\theta_\lambda^-=\tau_{-L_\lambda}\Phi.
\]

Translation is isometric, so both have the same nonzero graph norm \(\|\Phi\|_{\mathcal E_w}\). On the one-dimensional source-generated fibre define

\[
\eta_\lambda^\pm(h)
=\frac{\langle\theta_\lambda^\pm,h\rangle}
{\|\Phi\|_{\mathcal E_w}^2}.
\]

Then

\[
\eta_\lambda^\pm(c\theta_\lambda^\pm)=c,
\qquad
|\eta_\lambda^\pm(h)|
\le\frac{\|h\|}{\|\Phi\|_{\mathcal E_w}}.
\]

## Recovery map

The labelled synthesis is

\[
(\mathcal Ic)_\lambda
=a_\lambda
\bigl(c_\lambda^+\theta_\lambda^+,
      c_\lambda^-\theta_\lambda^-\bigr).
\]

Define

\[
(\mathcal Rh)_\lambda^\pm
=a_\lambda^{-1}\eta_\lambda^\pm(h_\lambda^\pm).
\]

Directly,

\[
\mathcal R\mathcal I=I
\]

on finite packets and therefore on the projective completion by continuity. This is a genuine source-recovery port, not a fitted pseudoinverse.

## Projective continuity

For target seminorms

\[
Q_\delta(h)
=\sum_\lambda e^{\delta L_\lambda}
\left(\|h_\lambda^+\|+\|h_\lambda^-\|\right),
\]

one has

\[
|a_\lambda^{-1}|=k e^{L_\lambda/2}.
\]

For every \(\varepsilon>0\),

\[
k\le C_\varepsilon e^{\varepsilon L_\lambda}.
\]

Consequently

\[
q_\delta(\mathcal Rh)
\le
\frac{C_\varepsilon}{\|\Phi\|_{\mathcal E_w}}
Q_{\delta+1/2+\varepsilon}(h).
\]

Thus \(\mathcal R\) is continuous on the projective source-generated history range. Prime and grade cutoffs commute with both \(\mathcal I\) and \(\mathcal R\).

## Graph projection

The composite

\[
\mathcal P_{\rm src}=\mathcal I\mathcal R
\]

is the identity on the labelled source-generated range and is label diagonal. On any ambient fibre larger than the source line, the same formula gives the orthogonal projection onto the translated theta atom before multiplication and cancellation of \(a_\lambda\). It therefore separates source-bearing history from unrelated analytic directions without quotienting the arithmetic carrier.

## Hilbert limitation

The operator norm of the finite-cutoff recovery satisfies

\[
\|\mathcal R_X\|\ge
\max_{\lambda\le X}|a_\lambda^{-1}|,
\]

which diverges with the cutoff. Hence no bounded recovery map exists on the unweighted labelled Hilbert completion. The projective estimate is not a Hilbert coercivity theorem.

## Codiagonal limitation

The construction uses every label projection and its translated atom. If a map

\[
C:H^{\rm lab}\to H^{\rm common}
\]

sums the fibres first, \(\mathcal R\) does not factor continuously through \(C\) without a quantitative label observer. The complete Fourier family is now proved jointly faithful, but one scalar sum or one Laplace response cannot reconstruct the labelled packet.

## Direction rescore

- Label-retaining projective recovery port: completed.
- Hilbert-bounded recovery from the same incidence: 0/10.
- Recovery after common-history codiagonalization: 9/10, requiring a jointly faithful observer.
- G4 recovery-port comparison: 10/10, interface-blocked.
- Projective trace surjectivity onto source labels: completed on the source-generated range.

## Disposition

The source graph now has an explicit continuous recovery port and projection in its authoritative projective topology. The remaining G4 closed-range question is whether G4 retains this labelled graph before codiagonalization or supplies another faithful observer. No RH conclusion is authorized.
