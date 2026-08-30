# The one-sided theta transfer is outer but not bounded below

## Theorem

Let

\[
m_\Phi(z)
=
\int_0^\infty
\Phi(u)e^{-zu}\,du,
\qquad
\operatorname{Re}z>0,
\]

where \(\Phi\) is the completed Riemann theta kernel in the frozen normalization. Then \(m_\Phi\) is an outer function of the right-half-plane Hardy algebra, up to a positive constant normalization.

It is not invertible in \(H^\infty\), because its boundary modulus tends to zero at infinity.

## Hardy membership

Since \(\Phi\in L^1(0,\infty)\),

\[
|m_\Phi(z)|
\le
\|\Phi\|_1
\qquad
(\operatorname{Re}z>0).
\]

Thus

\[
m_\Phi\in H^\infty(\mathbb C_+).
\]

The completed theta series has superexponential half-line decay, so its Laplace transform continues analytically across every finite point of the imaginary axis.

## No Blaschke factor

Strict theta monotonicity proved earlier gives the Stieltjes representation

\[
m_\Phi(z)
=
\frac1z
\int_{(0,\infty)}
(1-e^{-zs})\,d\mu(s),
\qquad
\mu=-d\Phi>0.
\]

Hence

\[
\operatorname{Re}(z,m_\Phi(z))>0
\qquad
(\operatorname{Re}z>0).
\]

Therefore \(m_\Phi\) has no zeros in the open right half-plane. Its Blaschke factor is constant.

## No finite singular inner factor

For \(\omega\ne0\),

\[
\operatorname{Re}(i\omega m_\Phi(i\omega))
=
\int_{(0,\infty)}
(1-cos \omega s)\,d\mu(s).
\]

The measure \(\mu\) has a smooth strictly positive density on a nontrivial interval because \(-\Phi'(s)>0\) for \(s>0\). Thus the integral is strictly positive for every \(\omega\ne0\). At \(\omega=0\),

\[
m_\Phi(0)=\int_0^\infty\Phi(u)\,du>0.
\]

So \(m_\Phi\) is nonzero at every finite boundary point. Together with analytic continuation across finite boundary arcs, this excludes a singular inner measure supported on the imaginary axis.

## Boundary asymptotic

The completed kernel satisfies

\[
\Phi(0)>0,
\qquad
\Phi'\in L^1(0,\infty).
\]

Integration by parts gives

\[
m_\Phi(z)
=
\frac{\Phi(0)}z
+
\frac1z
\int_0^\infty
\Phi'(u)e^{-zu}\,du.
\]

Along the boundary, the Riemann--Lebesgue lemma yields

\[
i\omega m_\Phi(i\omega)
\longrightarrow
\Phi(0)
\qquad
(|\omega|\to\infty).
\]

Consequently,

\[
|m_\Phi(i\omega)|
\sim
\frac{\Phi(0)}{|\omega|}.
\]

This has two consequences.

First,

\[
\int_{\mathbb R}
\frac{|\log|m_\Phi(i\omega)||}{1+\omega^2}
\,d\omega
<\infty.
\]

Thus the canonical outer factor is well-defined in the ordinary right-half-plane Hardy class.

Second, the decay is polynomial, not exponential. Hence the inner factor cannot contain a delay term

\[
e^{-az},
\qquad a>0.
\]

## Canonical factorization

The canonical factorization of a nonzero right-half-plane \(H^\infty\) function consists of:

- a Blaschke factor;
- a singular boundary inner factor;
- a possible exponential delay;
- an outer factor.

All three nonconstant inner components have now been excluded. Therefore

\[
m_\Phi=c\,O_\Phi,
\qquad
|c|=1,
\]

with \(O_\Phi\) outer. Since \(m_\Phi(x)>0\) for \(x>0\), the phase can be fixed as \(c=1\) in the source frame.

## History consequence

Under the Hardy--Laplace representation,

\[
H^*\simeq M_{m_\Phi},
\qquad
H\simeq M_{m_\Phi}^*.
\]

Multiplication by a nonzero analytic function is injective, and outerness gives dense range. Hence

\[
\ker H^*=0,
\qquad
\ker H=0.
\]

Therefore

\[
\ker
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix}
=
0.
\]

The source-derived causal/anti-causal theta history has no exact dark state.

## Noncoercivity remains exact

Because

\[
|m_\Phi(i\omega)|\to0,
\]

one still has

\[
\inf_{\|f\|=1}
\|M_{m_\Phi}f\|
=
0.
\]

Thus zero belongs to the approximate spectrum even though it is not an eigenvalue. The history Dirac is injective but not bounded below.

This is the precise analytic type needed by the programme:

- exact state faithfulness;
- dense reciprocal range;
- no global theta-only Green margin.

## Separation from the completed zero divisor

The bilateral completed section uses reciprocal boundary combination:

\[
\Xi(\omega)
=
m_\Phi(i\omega)+m_\Phi(-i\omega)
=
2\operatorname{Re}m_\Phi(i\omega)
\]

in the corresponding normalization.

Both one-sided factors may be nonzero while their real parts cancel. Therefore outerness of \(m_\Phi\) does not imply RH. It proves instead that zeros are not created inside the causal propagation block.

The completed zero mechanism must enter through reciprocal sewing, the boundary relation, or the final determinant comparison.

## Architectural consequence

The zero-free bulk factor in the finite-rank sewing theorem is now source-authorized:

\[
\text{outer theta history propagation}
\times
\text{reciprocal arithmetic boundary defect}.
\]

The next RH-bearing construction is the filtered boundary return

\[
G(z)
=
V^*(I-S(z))^{-1}U
\]

or its boundary-triple equivalent, with \(U,V\), and the reciprocal constitutive law derived independently from the completed wall--jump incidence.

No further bulk zero-exclusion theorem is needed for the one-sided theta history.
