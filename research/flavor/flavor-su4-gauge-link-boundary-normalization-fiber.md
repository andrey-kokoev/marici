# An SU(4) gauge link fixes the spectral sign but leaves a boundary normalization: WP772

## Question

Can one simple five-dimensional parent simultaneously derive the link
representation, its coupling normalization, and the positive spectral lift
required by WP771?

## Gauge-Higgs source

Take a five-dimensional \(SU(4)\) vector multiplet and the parity

\[
P=\operatorname{diag}(1,1,-1,-1).
\]

Conjugation by \(P\) splits the adjoint into seven even and eight odd real
generators:

\[
15=7+8.
\]

The even algebra has dimensions

\[
7=3+3+1
\]

and is \(SU(2)_A\times SU(2)_B\times U(1)\). The odd sector is a complex
\((2,2)\) bifundamental. With opposite orbifold parity for \(A_5\), this sector
supplies the link as a gauge component rather than an independently normalized
hypermultiplet.

For the pure bulk vector packet,

\[
N_V=15,
\qquad
N_H=0,
\qquad
\kappa=2+N_V-N_H=17>0.
\]

The same simple parent therefore supplies the bifundamental representation,
one bulk gauge coupling, and the positive spectral sign needed for the
half-twist basin. This is the first tested object to join those formerly
separate frames.

## Complete boundary kinetic ring

The orbifold boundary preserves only the subgroup. Its local action therefore
admits independent inverse kinetic coefficients. Writing

\[
g_A^2=\frac{1}{C+\tau_A},
\qquad
g_B^2=\frac{1}{C+\tau_B},
\qquad
C=\frac{\ell}{g_5^2},
\]

shows that generic boundary terms split the two couplings.

Even an exact exchange symmetry only imposes

\[
\tau_A=\tau_B=\tau.
\]

It preserves equality but not the common magnitude. On the WP771 portal
normalization with \(C=1\),

\[
\tau=0\;\Longrightarrow\;\Delta=\frac{1}{10},
\]

whereas

\[
\tau=1\;\Longrightarrow\;\Delta=\frac{1}{20}.
\]

Both packets have the same simple bulk group, parity, gauge-link
representation, positive spectral index, and exchange symmetry.

## Classification

\(SU(4)\) gauge-Higgs unification is a progressive joint source principle: it
makes the link and positive spectral sign unavoidable inside the admitted
bulk packet. It does not fix the physical gauge normalization because the
complete residual-symmetry boundary operator ring contains an exchange-even
kinetic modulus.

The next constructor must fix or eliminate that common boundary coefficient
without borrowing the desired low-energy normalization. Only then can an
isolated RG trajectory fix \(g_*^2\). The WP770 two-port map still requires an
actual realization in `physical16` production and decay channels.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp772_su4_gauge_link_boundary_normalization_fiber.py

Generated result:
research/flavor/results/wp772_su4_gauge_link_boundary_normalization_fiber.json
