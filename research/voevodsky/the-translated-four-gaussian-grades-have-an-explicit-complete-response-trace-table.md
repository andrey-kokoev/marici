# The translated four Gaussian grades have an explicit complete-response trace table

## Question

Can the wall, causal-history, and principal-value entries of the translated fourth-grade Gaussian packet be evaluated before the missing theta-history Green metric is declared?

## Claim boundary

Yes. For every translated grade \(U_af_j\), \(0\le j\le3\), origin value, total mass, half-line history, and principal-value response are explicit in elementary Gaussian functions and Dawson's integral. These are the source response coordinates needed to assemble a target Gram, but they do not choose the coefficients of the relative Green form.

## Definitions

Let

$$
f_j(x)=x^je^{-\pi x^2},
\qquad
(U_af_j)(x)=f_j(x+a).
$$

For \(g\), retain

$$
B(g)=g(0),
\quad
Q(g)=\int_{\mathbb R}g(x)\,dx,
$$

$$
A(g)=\int_{-\infty}^0g(x)\,dx,
\quad
C(g)=\operatorname{pv}\int_{\mathbb R}\frac{g(x)}x\,dx.
$$

Write

$$
E_a=e^{-\pi a^2},
\qquad
H_a=\frac12\left(1+\operatorname{erf}(\sqrt\pi a)\right),
$$

and let \(D(y)=e^{-y^2}\int_0^ye^{r^2}\,dr\) denote Dawson's integral.

## Value and mass

Directly,

$$
B(U_af_j)=a^jE_a.
$$

Translation invariance of total mass gives

$$
(Q_0,Q_1,Q_2,Q_3)
=
\left(1,0,\frac1{2\pi},0\right).
$$

## Half-line history

After \(y=x+a\),

$$
A(U_af_j)=\int_{-\infty}^ay^je^{-\pi y^2}\,dy.
$$

Integration by parts yields

$$
A_0(a)=H_a,
$$

$$
A_1(a)=-\frac{E_a}{2\pi},
$$

$$
A_2(a)=\frac{H_a-aE_a}{2\pi},
$$

$$
A_3(a)
=-E_a\left(\frac{a^2}{2\pi}+\frac1{2\pi^2}\right).
$$

These formulas include the translated fourth-grade causal trace exactly.

## Principal-value response

The base Hilbert integral is

$$
C_0(a)
=
\operatorname{pv}\int_{\mathbb R}
\frac{e^{-\pi(x+a)^2}}x\,dx
=-2\sqrt\pi\,D(\sqrt\pi a).
$$

Using \(y=x+a\) and polynomial division by \(y-a\), one obtains

$$
C_1(a)=1+aC_0(a),
$$

$$
C_2(a)=a+a^2C_0(a),
$$

$$
C_3(a)=\frac1{2\pi}+a^2+a^3C_0(a).
$$

Thus the previously unlisted fourth-grade principal-value entry is explicit.

## Reflection checks

Dawson's function is odd. Therefore the formulas obey the parity/reflection laws forced by Fourier square. At \(a=0\),

$$
C_0=C_2=0,
\qquad
C_1=1,
\qquad
C_3=\frac1{2\pi},
$$

matching principal-value cancellation for even grades and division of odd grades by \(x\).

## Two-ray assembly

For

$$
E=-2\pi L^2f_0+4\pi^2L^2f_2,
$$

$$
O=8\pi Lf_1-8\pi^2Lf_3,
$$

and

$$
g_+=U_L(E+O),
\qquad
g_-=U_{-L}(E-O),
$$

every response coordinate is obtained by the displayed linear combinations at \(a=\pm L\). Together with the already computed translated \(L^2\) Gram, this supplies the complete scalar value/history/PV table before Green weighting.

## Remaining metric gate

A relative theta-history Green form may weight and polarize:

- the ordinary \(L^2\) block;
- endpoint values;
- causal-history graph energies;
- principal-value tails;
- Wronskian boundary terms.

The response table computes the vectors entering those terms, but the repository still must declare their joint sesquilinear coefficients and radical quotient. Assigning coefficients to force agreement with the Stieltjes metric would remain circular.

## Disposition

All translated four-grade scalar response coordinates, including the formerly missing \(f_3\) causal and principal-value entries, are now explicit. The first-Adams matrix-unit test is reduced from missing response evaluations to one genuinely missing object: the independently sourced relative theta-history Green polarization.