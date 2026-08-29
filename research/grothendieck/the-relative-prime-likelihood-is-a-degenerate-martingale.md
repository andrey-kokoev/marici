# The Relative Prime Likelihood Is a Degenerate Martingale

## Finite-cutoff interface

Let the reference state be the product of Haar measures on the prime circles.
For a finite prime cutoff, the arithmetic state has density

$$
L_X(\theta)=\prod_{p\le X}P_{r_p}(\theta_p),
\qquad
r_p=p^{-1/2},
$$

where

$$
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
$$

Since every Poisson kernel has Haar integral one, the family $L_X$ is a
nonnegative martingale under the reference product state and

$$
\mathbb E_0 L_X=1.
$$

Thus every finite cutoff admits an ordinary density and an ordinary relative
modular operator.

## Logarithmic drift and fluctuation

The exact Fourier expansion is

$$
\log P_r(\theta)
=\log(1-r^2)
+2\sum_{k\ge1}\frac{r^k}{k}\cos(k\theta).
$$

Under Haar measure,

$$
\mathbb E_0\log P_r=\log(1-r^2)
$$

and orthogonality of the circle characters gives

$$
\operatorname{Var}_0(\log P_r)
=2\sum_{k\ge1}\frac{r^{2k}}{k^2}.
$$

For $r_p=p^{-1/2}$ this becomes

$$
\mathbb E_0\log P_{r_p}
=-\frac1p+O(p^{-2}),
$$

$$
\operatorname{Var}_0(\log P_{r_p})
=\frac2p+O(p^{-2}).
$$

Writing

$$
B_X=\sum_{p\le X}\frac1p,
$$

the independent bounded prime increments obey the normalized strong law

$$
\frac{\log L_X}{B_X}\longrightarrow-1
$$

almost surely under the Haar product state. Consequently

$$
L_X\longrightarrow0
$$

almost surely, even though every finite-cutoff expectation remains one.
Therefore the martingale is not uniformly integrable and has no nonzero
$L^1$ density limit.

## The primitive-square pair is one stochastic object

The divergent random part is already the primitive character:

$$
2r_p\cos\theta_p.
$$

Its accumulated quadratic variation is

$$
2\sum_{p\le X}r_p^2
=2B_X.
$$

The square current supplies the matching deterministic drift through

$$
\log(1-r_p^2)=-r_p^2+O(r_p^4).
$$

All fluctuating grades $k\ge2$ have summable total variance, because their
leading contributions are $O(p^{-2})$. Hence the nonsummable interface is
not the square current alone. It is the coupled pair

$$
\text{primitive fluctuation}
\quad+\quad
\text{square compensator}.
$$

This is the probabilistic form of the earlier three-grade boundary typing:

- grade one carries the divisor and the divergent interface noise;
- grade two is its required compensator and representation anomaly;
- grades three and higher form the determinant-class remainder.

## Consequence for relative modular reconstruction

The finite relative modular densities do not converge to an ordinary spatial
density in the Haar representation. Subtracting only the deterministic square
current cannot repair this: the centered primitive sum still has variance
$2B_X\to\infty$. Conversely, keeping the exponential compensator produces
the original martingale, which degenerates to zero.

Therefore the infinite interface cannot be any of the following:

- an ordinary Radon--Nikodym derivative in the Haar product representation;
- a scalar $L^1$ limit of finite relative modular operators;
- a deterministic square-current renormalization of the primitive sum;
- a bounded change of vacuum.

The surviving object must retain the primitive fluctuation and square
compensator as independent but coherent boundary coordinates. Candidate
homes include a correspondence between the disjoint GNS representations, a
distributional logarithmic cocycle, or a Fock-type noise extension. Any such
construction must recover each finite $L_X$ without claiming that the
infinite product is a density.

## Sharp next gate

Construct the centered logarithmic interface

$$
M_X
=\sum_{p\le X}
\left(
\log P_{r_p}(\theta_p)
-\log(1-r_p^2)
\right)
$$

together with its source-fixed quadratic compensator $B_X$. Determine
whether reciprocal and archimedean sewing produce a canonical distributional
limit of the pair $(M_X,B_X)$ before exponentiation. The hostile test is
mandatory: any proposed scalar limit must confront

$$
\operatorname{Var}_0(M_X)=2B_X+O(1)\longrightarrow\infty.
$$

The durable conclusion is that the square-grade anomaly does not merely
measure disjointness after the fact. It is the compensator required by the
primitive-current stochastic interface, and the two cannot be separated in
the completed theory.
