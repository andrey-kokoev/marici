# Burnol's prime-two boundary is pointwise indefinite but support-positive in the first Galerkin scout

Status: level-44 continuum positivity proved; full infinite-tower and RH
claims remain outside this theorem

## Exact boundary problem

At the support boundary \(c=\sqrt2\), Burnol's proof exposes the multiplier

\[
\alpha(\tau)=
\frac{8\sqrt2\cos(\tau\log2)}{1+4\tau^2}
-\log\pi
+\Re\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\]

A high-precision scout finds

\[
\min_{0\le\tau\le20}\alpha(\tau)
\approx-1.04068425705481
\]

at

\[
\tau\approx2.06499924367117.
\]

The positive-axis crossings are approximately \(0.89044917\) and
\(6.40634873\). Thus Burnol's argument cannot reach \(c=\sqrt2\) by asserting
pointwise nonnegativity of \(\alpha\).

## Support-constrained compression

The relevant test functions are not arbitrary Fourier densities. Their
logarithmic representatives are confined to an interval of length \(\log2\).
We therefore compressed the Fourier multiplier to that interval and computed
its lowest Galerkin eigenvalues using a unitary padded FFT.

Across spatial resolutions 128, 256, and 512 and padding factors through 128,
the lowest eigenvalue remained positive. The best frequency-resolution pair
at 256 support points gave

\[
\lambda_1\approx0.00132501183043,
\qquad
\lambda_2\approx0.0727802744605,
\qquad
\lambda_3\approx0.660360424836.
\]

The 512-point scout with padding 64 gives

\[
\lambda_1\approx0.00132758094046.
\]

## Shape of the nearly-null mode

The lowest mode is even to numerical precision and has no internal zero. Its
correlation with the first Dirichlet mode is

\[
\left|\left\langle v_1,
\cos\frac{\pi x}{\log2}\right\rangle\right|
\approx0.9992665277.
\]

It places about \(69.6\%\) of its Fourier mass inside the negative multiplier
band. The energy balance is nearly exact:

\[
E_-\approx-0.4663343600,
\qquad
E_+\approx0.4676619409.
\]

The bare cosine has Rayleigh quotient \(0.0026545988\), so it captures the
shape but not the sharp margin. Even Dirichlet subspaces of dimensions
\(1,2,4,8,16,32\) give lowest values

\[
0.00265460, 0.00159014, 0.00157656,
0.00150736, 0.00143449, 0.00138586.
\]

Their slow convergence reveals a boundary layer. The endpoint-to-peak sample
ratio decreases from \(0.0441\) to \(0.0382\) to \(0.0344\) under successive
spatial doubling, rather than behaving like a fixed smooth cosine profile.

## Interpretation

The boundary is pointwise indefinite but apparently positive after imposing
the source support constraint. The very small first eigenvalue makes this a
near-critical uncertainty-principle problem, not broad positivity.

This is evidence for the prime-two contraction, not a proof. A theorem now
needs a directed lower bound for the compressed operator, or an analytic
**logarithmic uncertainty inequality** showing that no \(\log2\)-supported
function can place enough Fourier mass in the negative band of \(\alpha\).

The slow boundary layer makes a small fixed polynomial basis unattractive.
Burnol's native conductor-operator language, \(\log|x|+\log|D|\), is better
matched to the asymptotic symbol and should be the next analytic comparison.

The next finite work is to compare the compressed boundary operator with the
known conductor operator or a Sonine-space restriction, isolate the compact
prime-two correction, and seek a certified lower bound on the resulting
ground-state energy.

## Exact finite-rank reduction

The rational prime-two/endpoint part of \(\alpha\) has an elementary inverse
Fourier transform. With the convention \(d\tau/(2\pi)\),

\[
\frac{8\sqrt2\cos(\tau\log2)}{1+4\tau^2}
\longleftrightarrow
\sqrt2\left(e^{-|r-\log2|/2}+e^{-|r+\log2|/2}\right).
\]

For \(|r|\le\log2\), which is exactly the difference range of the support
interval, this simplifies to

\[
2\cosh(r/2).
\]

Hence the compressed boundary operator is exactly rank two:

\[
B
=2|c\rangle\langle c|-2|s\rangle\langle s|,
\qquad
c(x)=\cosh(x/2),\quad s(x)=\sinh(x/2).
\]

The FFT action agrees with this real-space formula to about \(9\times10^{-10}\)
in the current padding census.

Let \(A_\infty\) be the compression of

\[
-\log\pi+\Re\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\]

Its first six sampled eigenvalues are

\[
-1.28588046, 0.08480089, 0.58205825,
0.92724298, 1.17515436, 1.37844630,
\]

with alternating even/odd parity. Thus the observed archimedean index is one,
carried by the even sector. Standard rank-one inertia reduces positivity to
two scalar resolvent gates:

\[
1+2\langle c,A_\infty^{-1}c\rangle\le0
\quad\text{(even)},
\]

\[
2\langle s,A_\infty^{-1}s\rangle\le1
\quad\text{(odd)}.
\]

At the finest current resolution these evaluate to approximately

\[
-0.00119900,\qquad 0.14115981.
\]

The odd gate has wide margin. The prime-two boundary theorem is therefore
concentrated almost entirely in the near-critical even secular inequality,
together with a proof that \(A_\infty\) has index one on the support interval.

## Exact real-space conductor form

The digamma identity gives

\[
h_\infty(\tau)
=h_\infty(0)
+\int_0^\infty
\frac{e^{r/2}}{\sinh r}
\bigl(1-\cos(\tau r)\bigr)\,dr,
\]

where

\[
h_\infty(0)
=-\log\pi+\psi(1/4)
=-\log\pi-\gamma-\frac\pi2-3\log2.
\]

For a zero-extended function supported on an interval \(I\) of length
\(L=\log2\), Parseval converts this into

\[
\begin{aligned}
\langle f,A_\infty f\rangle
={}&C_L\|f\|^2\\
&+\frac12\int_0^L
\frac{e^{r/2}}{\sinh r}
\int_{\mathbb R}|f(x+r)-f(x)|^2\,dx\,dr,
\end{aligned}
\]

with

\[
C_L=h_\infty(0)+
\int_L^\infty\frac{e^{r/2}}{\sinh r}\,dr
\approx-2.37847682784580.
\]

Thus the archimedean operator is an explicit positive logarithmic difference
energy minus a scalar mass. Its index-one theorem is a nonlocal Poincaré
theorem, not an opaque spectral assertion.

For the normalized trial function

\[
f_0(x)=\sqrt{2/L}\cos(\pi x/L),
\]

the autocorrelation for \(0\le r\le L\) is exactly

\[
R_0(r)=\left(1-\frac rL\right)\cos\frac{\pi r}{L}
+\frac1\pi\sin\frac{\pi r}{L}.
\]

Direct 80-digit quadrature gives

\[
\langle f_0,A_\infty f_0\rangle
\approx-1.12744036888818,
\]

and

\[
2|\langle\cosh(x/2),f_0\rangle|^2
\approx1.13009549396338.
\]

Their sum is

\[
\boxed{0.00265512507519669>0.}
\]

This independently confirms the FFT normalization. The remaining theorem is
a rank-one-strengthened logarithmic Poincaré inequality at the arithmetic
width \(L=\log2\), extending this balance from the cosine trial mode to every
supported function.

The universal lower comparison

\[
\frac{e^{r/2}}{\sinh r}\ge\frac1r
\]

is too coarse. On the same cosine it supplies difference energy only

\[
1.05878776646842,
\]

and would yield the negative total bound

\[
-0.189593567414004.
\]

Therefore the prospective theorem is not generic support uncertainty for the
logarithmic Laplacian. It must retain the finer completed archimedean weight;
that source coefficient carries essential positivity information.

## The infinite gamma tower admits a finite positive truncation

The exact source weight decomposes into half-integer gamma channels:

\[
\frac{e^{r/2}}{\sinh r}
=2\sum_{n\ge0}e^{-a_nr},
\qquad
a_n=2n+\frac12.
\]

Equivalently, the \(n\)-th Fourier multiplier is

\[
g_n(\tau)=
\frac{2\tau^2}{a_n(a_n^2+\tau^2)}\ge0.
\]

Every omitted gamma level is therefore positive semidefinite. Let \(T_N\)
denote the endpoint-completed operator using only the first \(N\) levels.
The 1024-point scout gives

\[
\lambda_{\min}(T_{43})
\approx-5.85936\times10^{-5},
\]

\[
\lambda_{\min}(T_{44})
\approx2.65189\times10^{-6},
\]

and

\[
\lambda_{\min}(T_{45})
\approx5.98926\times10^{-5}.
\]

Thus level 44 is the first positive truncation in every sufficiently refined
current scout. If \(T_{44}\ge0\) is certified, then

\[
T_\infty=T_{44}+\sum_{n\ge44}g_n(D)\ge0
\]

follows immediately. This is a source-derived finite certificate contract,
not a fitted cutoff: the remainder has a fixed positive sign.

## Exponential-kernel boundary-value realization

Each gamma channel has the exact physical-space form

\[
g_n(D)=\frac2{a_n}I-K_{a_n},
\qquad
K_a(x,y)=e^{-a|x-y|}.
\]

The first channel and endpoint term simplify further:

\[
-e^{-|x-y|/2}+2\cosh\frac{x-y}{2}
=e^{|x-y|/2}.
\]

Consequently

\[
T_{44}
=d_{44}I
+e^{|x-y|/2}
-\sum_{n=1}^{43}e^{-a_n|x-y|},
\]

where

\[
d_{44}=h_\infty(0)+\sum_{n=0}^{43}\frac2{a_n}
\approx2.63378349367197.
\]

Every exponential kernel is the Green kernel of a second-order
constant-coefficient equation. The continuum certification problem can
therefore be converted into a finite auxiliary-channel boundary-value system
with 44 rates and parity-separated boundary conditions. A directed
Evans/Sturm or interval transfer-matrix count can certify that this system has
no eigenvalue below zero. That is now the preferred proof implementation.

## Stable boundary-value determinant scout

Writing \(y_0\) for the growing kernel channel and \(y_n\) for the 43
decaying channels gives

\[
y_0''-\frac14y_0=f,
\qquad
y_n''-a_n^2y_n=-2a_nf,
\]

with

\[
f=\frac{\sum_{n=1}^{43}y_n-y_0}{d_{44}-\lambda}.
\]

At the right endpoint, the growing channel has slope \(+a_0\), while every
decaying channel has slope \(-a_n\). At the interval center, even modes have
zero derivative and odd modes have zero value. These conditions define two
\(44\times44\) Evans determinants.

Naive shooting is numerically invalid: its log-determinants at zero are about
797 and 654, and double precision produces many false sign changes. The
authorized stable realization propagates the endpoint boundary plane
backward while QR-renormalizing it after short steps. Its even root is

\[
\lambda_{44}^{\rm BVP}
\approx2.71879497\times10^{-6},
\]

with no odd root in \([-10^{-4},10^{-4}]\). Using 8, 16, 32, and 64 QR steps
gives respectively

\[
2.7187949667,
2.7187949636,
2.7187949671,
2.7187949691
\quad\times10^{-6}.
\]

The agreement across step counts and with the independent FFT value
\(2.65188806\times10^{-6}\) validates the BVP typing. It does not certify the
sign. The remaining implementation is directed ball-arithmetic propagation,
together with an Evans/Sturm zero count excluding all \(\lambda\le0\), not
merely evaluation near the observed root.

## First directed-ball gate

The 44-channel flow is now also propagated in Sage/Arb at 256-bit precision.
The step exponential uses scaling and squaring with an explicit matrix-norm
Taylor remainder. Sage has no QR decomposition over `RealBallField`, so the
implementation uses midpoint QR only to choose an invertible point-valued
right preconditioner. Multiplying the full ball matrix by that preconditioner
does not alter its enclosed column space and contributes no floating-point
claim to the certificate.

For 32 steps and Taylor order 24, the even center determinant at
\(\lambda=0\) is enclosed strictly on the negative side:

\[
D_+(0)\in[-1.276,-0.724]\times10^{-6}.
\]

Thus zero is rigorously excluded as an even eigenvalue of \(T_{44}\). The odd
determinant is not yet certified: its current interval contains zero because
the normalized determinant is extremely small. Most importantly, a pointwise
sign at zero does not exclude negative eigenvalues. The remaining proof gate
is therefore a parity-separated Evans/Sturm zero count on \(\lambda\le0\),
with a coarse operator lower bound supplying the finite left endpoint.

## One-fold and local Bernstein structure

Writing \(t=|x-y|\), the continuous kernel has the exact form

\[
K_{44}(t)=e^{t/2}
\left(1-\sum_{n=1}^{43}e^{-(2n+1)t}\right).
\]

The parenthesized polynomial is strictly increasing as a function of \(t\).
It has one zero,

\[
t_*=0.28119957431739495\ldots
=0.4056852313\ldots\log2.
\]

There is a stronger exact property on \(0\le t\le\log2\):

\[
K_{44}'(t)>0,
\qquad
K_{44}^{(2m)}(t)<0,
\qquad
K_{44}^{(2m+1)}(t)>0.
\]

Odd derivatives are manifestly positive. For every even order \(2m\ge2\),
the first decaying channel already dominates the growing channel, since

\[
\frac{(5/2)^{2m}e^{-5t/2}}{(1/2)^{2m}e^{t/2}}
=5^{2m}e^{-3t}
\ge \frac{5^{2m}}8>1.
\]

Thus \(K_{44}'\) is completely monotone on the full prime-two interval: the
kernel is a local Bernstein function of separation. This rules out hidden
oscillatory sign bands and supplies the correct shape constraint for a direct
quadratic-form proof. It does not alone imply positivity of
\(d_{44}I+K_{44}\); the next step is to turn this shape theorem into a sharp
bound on the negative short-range interaction.

The shape theorem also exposes the earlier rank-one gate directly. Put

\[
B(t)=K_{44}(\log2)-K_{44}(t).
\]

Then \(B\ge0\), it is decreasing with alternating derivatives, and

\[
T_{44}
=d_{44}I-B_{\rm op}
+K_{44}(\log2)|1\rangle\langle1|.
\]

Thus prime-two completion subtracts one positive decreasing distance
interaction from the local counterterm and restores its sole unstable mode
through a constant-mode rank-one channel. A 1200-point Nyström scout gives

\[
\lambda(B)=3.3654,\ 2.5704,\ 2.0513,\ldots,
\qquad d_{44}=2.63378\ldots.
\]

Consequently \(d_{44}I-B_{\rm op}\) has one observed negative direction, with
a robust gap above the second eigenvalue, while the rank-one term acts on that
direction. This is discovery evidence, not yet the continuum theorem. It
suggests a sharper two-part certificate: prove
\(\lambda_2(B)<d_{44}<\lambda_1(B)\), then prove the associated rank-one
secular inequality. Only the second part is near saturation.

The odd sector admits a particularly small certificate candidate. On the
half-interval \([0,L/2]\), its positive kernel is

\[
B_-(x,y)=B(|x-y|)-B(x+y)\ge0.
\]

With the elementary positive weight

\[
\phi(x)=x\exp(-7x^2-32x^4),
\]

a high-order quadrature scout gives

\[
\sup_{0<x\le L/2}
\frac{\int_0^{L/2}B_-(x,y)\phi(y)\,dy}{\phi(x)}
\approx2.594996
<d_{44},
\]

leaving margin about \(0.0388\). A directed interval quadrature of this one
scalar ratio would certify the weighted Schur bound and remove the complete
odd sector. No fitted eigenvector is needed: the integer coefficients
\((-7,-32)\) retain essentially the full margin of the optimized scout.

## Exact even secular gate

Let

\[
A=d_{44}I-B_{\rm op},
\qquad
c=K_{44}(\log2).
\]

Once \(A\) is known to have exactly one negative direction and the constant
vector couples to it, the rank-one inertia formula says that

\[
A+c|1\rangle\langle1|\ge0
\quad\Longleftrightarrow\quad
1+c\langle1,A^{-1}1\rangle\le0.
\]

The coefficient is source-fixed and has the exact prime-two form

\[
c
=\sqrt2-\sum_{n=1}^{43}2^{-(2n+1/2)}
=\frac{5+4^{-43}}{3\sqrt2}.
\]

Likewise

\[
d_{44}
=-\log\pi-\gamma-\frac\pi2-3\log2
+4\sum_{n=0}^{43}\frac1{4n+1}.
\]

Thus the secular test contains no fitted coefficient. Gauss--Legendre
Nyström values converge slowly because of the diagonal cusp, but extrapolation
in the observed \(N^{-2}\) error gives

\[
1+c\langle1,A^{-1}1\rangle
\approx-4.15\times10^{-6}.
\]

Its sign and scale agree with the positive BVP eigenvalue
\(2.7188\times10^{-6}\). This is the genuinely near-saturated theorem: the
odd-sector inequality has percent-scale reserve, whereas the even completion
crosses its scalar repair threshold by only a few parts in a million.

## Total-positivity shortcut is closed

The alternating derivative signs on \([0,\log2]\) do **not** license a
Pólya-frequency or total-positivity theorem. The distance kernel already has
a certified negative ordered \(2\times2\) minor. At

\[
x=(0.11832377,0.15811552),
\qquad
y=(0.07854827,0.11835137),
\]

256-bit Arb evaluation gives

\[
\det\bigl(B(|x_i-y_j|)\bigr)
=-111.1054748937158591990\ldots<0.
\]

A broader deterministic random scout also finds negative minors frequently at
orders two through four. Hence \(B(|x-y|)\) is not totally nonnegative, and
variation-diminishing machinery cannot be used to infer that its second
eigenvalue is the top odd eigenvalue. The required inertia statement must be
certified directly, for example by the already typed parity-separated
Evans/Sturm system. This is also a scope correction: local complete
monotonicity of \(K'\) is a shape theorem, not a global spectral-ordering
theorem.

## Secular threshold census

Applying the same Gauss--Legendre Nyström convention and quadratic
\(N^{-2}\) extrapolation at adjacent truncation levels gives

\[
\begin{array}{c|c|c}
\text{level}&S_N=1+c_N\langle1,A_N^{-1}1\rangle
&\lambda_{\min}(T_N)\\
\hline
41&+2.9986\times10^{-4}&-1.9467\times10^{-4}\\
42&+1.9135\times10^{-4}&-1.2422\times10^{-4}\\
43&+9.0255\times10^{-5}&-5.8590\times10^{-5}\\
44&-4.0864\times10^{-6}&+2.6532\times10^{-6}\\
45&-9.2263\times10^{-5}&+5.9892\times10^{-5}.
\end{array}
\]

Thus level 44 is the first observed crossing in the scalar secular gate as
well as in the independent lowest-eigenvalue census. The sign convention is
the rank-one inertia convention: \(S_N<0\) is the repaired side. These are
extrapolated discovery values, not directed certificates. The sharp finite
target is now the pair

\[
S_{43}>0,
\qquad
S_{44}<0.
\]

The first directed half of this threshold statement is now available from
the boundary system itself. In one consistently oriented 256-bit Arb
determinant line,

\[
D_{43,+}(-10^{-4})
\in[1.6942,1.6958]\times10^{-5},
\]

while

\[
D_{43,+}(0)
\in[-2.415,-2.365]\times10^{-5}.
\]

The midpoint QR factors enter only as point-valued right preconditioners and
are normalized to positive determinant, so they cannot create this sign
change. Continuity therefore gives an even eigenvalue in
\((-10^{-4},0)\): level 43 rigorously fails positivity. This proves the
failure side without assuming the unproved one-defect inertia statement. The
level-44 success side still requires exclusion of every nonpositive root.

## Directed odd-sector closure

The weighted Schur inequality is now certified by FLINT/Arb analytic
integration. The implementation uses the exact two-chart split at \(y=x\),
adaptive interval subdivision in the outer parameter \(x\), and a separately
desingularized fixed-cube formula on
\([0,\log(2)/4096]\). With 192-bit balls, 64 initial boxes, and maximum
subdivision depth 12, the run reports

- 1830 certified adaptive boxes;
- no failed integrations;
- no unresolved boxes;
- a certified endpoint enclosure;
- strict upper bound below \(d_{44}\) on every box.

The tightest accepted adaptive enclosure retains positive reserve

\[
d_{44}-\sup_{\rm boxes}\frac{B_-\phi}{\phi}
>8.55\times10^{-6}.
\]

This small *certification* reserve reflects interval overestimation; the
midpoint inequality has reserve about \(0.039\). Since \(B_-\) is a positive
kernel and \(\phi>0\) in the open half-interval, the weighted Schur theorem
gives

\[
\|B_-\|<d_{44}.
\]

The level-44 odd sector is therefore rigorously positive. All remaining
near-critical work is even.

## Temple shortcut audit

A direct Rayleigh--residual proof was also tested after the odd closure. Two
natural trial spaces expose complementary conditioning defects:

- Product Gauss quadrature in polynomial bases samples the derivative cusp
  on \(x=y\) incorrectly. Its apparent lowest value converges from the
  negative side at order \(N^{-2}\), reproducing the already diagnosed
  Nyström bias rather than the continuum form.
- Endpoint-vanishing odd-cosine trial spaces avoid that cusp in multiplier
  coordinates and give positive Ritz values. A 96-mode scout initially gives
  a positive truncated Temple bound, but the unresolved high cosine tail is
  too large. The eigenfunction does not satisfy the artificial endpoint
  condition strongly enough for this basis to yield a short residual proof.

The full-space multiplier residual is not a valid replacement: most of it is
the action outside the compressed support interval and must be removed before
Temple's inequality is applied. Therefore no Temple certificate is claimed.
The viable even route remains the finite-channel boundary response with a
validated root/inertia count, or a support-adapted trial basis whose tail is
proved rather than truncated.

## Symmetric Riccati reduction of the even sector

The auxiliary coupling matrix is not symmetric in its original labelled
coordinates, but it has the exact positive symmetrizer

\[
H=\operatorname{diag}
\left(1,\frac1{2a_1},\ldots,\frac1{2a_{43}}\right).
\]

After \(z=H^{1/2}y\), the second-order system becomes

\[
z''=\widetilde M(\lambda)z,
\qquad
\widetilde M(\lambda)
=\operatorname{diag}(a_n^2)
-\frac{qq^T}{d_{44}-\lambda},
\]

where

\[
q=(-1,\sqrt{2a_1},\ldots,\sqrt{2a_{43}})^T.
\]

This is a self-adjoint matrix Sturm system with the original diagonal Robin
boundary slopes. Wherever its center Dirichlet-to-Neumann matrix \(P(\lambda)\)
has no Riccati pole, Green's identity gives

\[
v^TP'(\lambda)v
=\int_0^{L/2}
\frac{|q^Tz_v(x)|^2}{(d_{44}-\lambda)^2}\,dx
\ge0.
\]

A double-precision scout on \([-0.2311,0]\) finds no sampled position-block
singularity and constant center-response inertia \((43-,1+)\). At zero the
largest negative response eigenvalue is

\[
-5.67877\times10^{-6},
\]

while at the left endpoint the sole positive response eigenvalue remains
\(8.0765\ldots\). The proof contract is now finite and directed: certify the
two endpoint inertias and exclude position-block singularities on the
rectangle

\[
(x,\lambda)\in[0,L/2]\times[-0.2311,0].
\]

Monotonicity then excludes every even root at \(\lambda\le0\). Combined with
the directed odd Schur theorem, this would prove \(T_{44}>0\).

The fixed \(\lambda=0\) inertia is now directed. The stabilized 256-bit ball
plane was transformed by the exact symmetrizer, converted to the center
response, and subjected to a midpoint orthogonal congruence. Interval
Gershgorin discs certify

\[
\operatorname{inertia}P(0)=(43-,1+)
\]

with no unresolved disc. In particular, the near-zero negative response
direction is separated from zero despite its scale.

At \(\lambda\to-\infty\), the rank-one coupling vanishes and the response is
exactly diagonal: the growing \(a_0\) channel is positive and the 43 decaying
channels are negative. Hence the limiting inertia is also \((43-,1+)\).
Since \(P'(\lambda)\succeq0\), equality of these endpoint inertias would rule
out every zero crossing. The only remaining logical gate is global existence
of this Riccati chart: the position block must have no zero on

\[
(x,\lambda)\in[0,L/2]\times(-\infty,0].
\]

Thus the even positivity problem has reduced from an 88-dimensional spectral
claim to one matrix disconjugacy/pole-exclusion theorem.

## Closure of the level-44 continuum theorem

The pole-exclusion theorem is already contained in the directed odd result.
Suppose the position block had a zero at \(x_0\), and put
\(\ell=L/2-x_0\). Solving the individual channel equations with a Dirichlet
condition at \(x_0\) and the source Robin condition at \(L/2\) reduces the
common forcing \(F=q^Tz\) to

\[
F=\frac1{d_{44}-\lambda}C_\ell F.
\]

The channel Green functions give exactly

\[
C_\ell(s,t)
=K_{44}(s+t)-K_{44}(|s-t|),
\qquad 0\le s,t\le\ell.
\]

For a decaying channel, its contribution is

\[
e^{-a|s-t|}-e^{-a(s+t)},
\]

while the growing \(a_0=1/2\) channel contributes

\[
e^{a_0(s+t)}-e^{a_0|s-t|}.
\]

Their sum is precisely the positive folded odd kernel already certified.
Restricting the same positive Schur integrand and weight to a shorter interval
cannot increase its bound. Therefore

\[
\|C_\ell\|
\le\|C_{L/2}\|
<d_{44}
\le d_{44}-\lambda
\qquad(\lambda\le0).
\]

The pole equation is impossible. Thus the Riccati chart exists for every
\(\lambda\le0\). Its Loewner monotonicity, its exact limiting inertia
\((43-,1+)\), and its directed zero-endpoint inertia \((43-,1+)\) exclude
every even zero. The directed weighted-Schur theorem excludes every odd zero.
Since the essential diagonal is positive,

\[
\boxed{T_{44}>0.}
\]

Level 43 has a directed even eigenvalue in \((-10^{-4},0)\), so 44 is the
first rigorously separated crossing of the pair.

Finally, the secular sign follows without resolving its few-parts-per-million
value directly. Directed Arb integration gives

\[
\frac{\langle1,B1\rangle}{\|1\|^2}
=3.2837698479145955\ldots
>d_{44}
\]

with margin \(0.6499863542\ldots\). Hence
\(A=d_{44}I-B\) has a negative direction. Because
\(T_{44}=A+c|1\rangle\langle1|>0\), the rank-one downdate has exactly one
negative direction. The rank-one inertia formula then yields the strict
source-normalized secular sign

\[
\boxed{
S_{44}=1+c\langle1,A^{-1}1\rangle<0.
}
\]
