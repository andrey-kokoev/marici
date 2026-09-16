# Harmonic-oscillator regularization proves the comb-orbit Gram identity at every positive scale

## Question

Can the source-derived shifted-comb intertwiner satisfy the required Hilbert orbit-Gram test despite raw combs being non-Hilbert distributions?

## Claim boundary

Yes at every positive Fourier-equivariant oscillator scale. Harmonic-oscillator smoothing turns the complete comb orbit into Schwartz vectors, commutes with Fourier, and the oriented radial-log Mellin transform is unitary. Hence the orbit Gram matrices agree exactly. The zero-scale comb limit remains distributional and need not converge in Hilbert norm.

## Fourier-equivariant regulator

Use the Fourier-balanced harmonic oscillator

$$
\mathsf H
=-\frac{d^2}{dx^2}+4\pi^2x^2.
$$

For the convention

$$
\mathcal Ff(y)=\int f(x)e^{-2\pi ixy}\,dx,
$$

one has

$$
\mathcal F\mathsf H=\mathsf H\mathcal F.
$$

For \(\tau>0\), let

$$
R_\tau=e^{-\tau\mathsf H}.
$$

The Mehler kernel implies

$$
R_\tau:\mathcal S'(\mathbb R)\longrightarrow\mathcal S(\mathbb R)
$$

continuously, and

$$
R_\tau\mathcal F=\mathcal F R_\tau.
$$

## Regulated comb orbit

For the shifted comb \(P_a\), define

$$
p_{a,\tau}=R_\tau P_a\in\mathcal S(\mathbb R).
$$

Its full orbit is

$$
p_{a,\tau},
\quad
\mathcal Fp_{a,\tau},
\quad
\mathcal F^2p_{a,\tau},
\quad
\mathcal F^3p_{a,\tau}.
$$

Equivariance gives

$$
\mathcal F^j p_{a,\tau}
=R_\tau\mathcal F^jP_a,
$$

so smoothing does not alter the sewing law or introduce fitted phases.

## Unitary oriented radial Mellin map

Define the oriented log-radial half-density map

$$
(Uf)_\epsilon(u)
=e^{u/2}f(\epsilon e^u),
\qquad \epsilon\in\{+1,-1\}.
$$

A change of variables gives

$$
\|Uf\|_{L^2(du)\otimes\mathbb C^2}
=\|f\|_{L^2(dx)}.
$$

Applying the unitary Fourier transform in \(u\), denoted \(\mathcal M_{\log}\), gives a unitary map

$$
C=\mathcal M_{\log}U:
L^2(\mathbb R)
\longrightarrow
L^2(\mathbb R_t)\otimes\mathbb C^2.
$$

The previously derived gamma-matrix identity says

$$
C\mathcal F=G(t)\mathcal R_t C
$$

on the Schwartz core and therefore on \(L^2\).

## Orbit-Gram identity

For every \(\tau>0\) and \(0\le j,k<4\), unitarity gives

$$
\left\langle
\mathcal F^jp_{a,\tau},
\mathcal F^kp_{a,\tau}
\right\rangle_{L^2(dx)}
=
\left\langle
C\mathcal F^jp_{a,\tau},
C\mathcal F^kp_{a,\tau}
\right\rangle_{L^2(dt)\otimes\mathbb C^2}.
$$

Using the intertwining identity, the right-hand side is the Gram matrix of the gamma-sewn radial orbit. Thus the complete four-character norm test passes exactly at every positive scale.

## Zero atom and endpoint

The oscillator regulator includes the character-comb zero atom as an ordinary Schwartz contribution. If one passes instead to the punctured Mellin Dirichlet section, that atom must be projected to its separately declared endpoint channel before comparison. These are two different regulated interfaces and must not be mixed.

## Limit boundary

As \(\tau\downarrow0\),

$$
p_{a,\tau}\to P_a
$$

in \(\mathcal S'\), not generally in \(L^2\). Therefore the regulated Gram matrices may diverge and no unrenormalized Hilbert Gram is assigned to the raw comb. The distributional Hurwitz--polylogarithm sewing remains the valid zero-scale limit.

## Disposition

The source-derived comb-to-oriented-radial intertwiner passes the exact Hilbert orbit-Gram acceptance test for every positive Fourier-equivariant oscillator scale. The remaining analytic issue is not Gram matching but whether the external G4 contract admits this canonical regulated family or specifies a compatible renormalized zero-scale limit.