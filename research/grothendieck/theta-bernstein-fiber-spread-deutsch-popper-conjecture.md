# Theta Bernstein fiber-spread conjecture

## Deutsch--Popper formulation

Let

\[
H(x)=\frac{s(s-1)}{2s-1}\frac{\xi'(s)}{\xi(s)},
\qquad s=\frac12+\sqrt x,
\qquad x>\frac14,
\]

and put \(f=H'\).  The conjecture has two irreducible clauses.

### Clause A: positive scale transport

The function \(f\) is completely monotone:

\[
(-1)^k f^{(k)}(x)\ge0
\qquad(k\ge0,\ x>1/4).
\]

Equivalently, there is a unique positive Bernstein measure \(\mu\) such that

\[
f(x)=\int_0^\infty e^{-(x-1/4)t}\,d\mu(t).
\]

The measure must be derived from the fixed completed theta/arithmetic source;
a fitted exponential mixture does not satisfy this clause.

### Clause B: convolution fibers cannot collapse onto balance

For two independent \(\mu\)-scales \(t,u\), disintegrate
\(\mu\otimes\mu\) over the faithful sum coordinate \(v=t+u\).  Then

\[
\boxed{
\operatorname{Var}(t\mid t+u=v)\ge\frac{v^2}{20}
}
\]

for almost every nonzero convolution fiber.

Equivalently, the pushforward under \(v=t+u\) of

\[
\left(t^2+u^2-3tu\right)d\mu(t)d\mu(u)
\]

is a positive measure \(\sigma\).

## What it explains

The exact identity

\[
\begin{aligned}
\mathcal N(H)
&=2H'H'''-3(H'')^2\\
&=\iint e^{-(x-1/4)(t+u)}
\left(t^2+u^2-3tu\right)d\mu(t)d\mu(u)
\end{aligned}
\]

then gives

\[
\mathcal N(H)(x)=\int_0^\infty e^{-(x-1/4)v}\,d\sigma(v).
\]

Thus the conjecture explains simultaneously:

1. rank-two Schwarzian positivity;
2. the observed alternating derivative hierarchy of \(\mathcal N\);
3. why generic positive, log-concave, and increasing-curvature sources fail;
4. why the mechanism is intrinsically two-copy and fiberwise; and
5. why a faithful transport coordinate is essential.

The hard-to-vary causal chain is

\[
\boxed{
\text{completed labelled source}
\longrightarrow \mu\ge0
\longrightarrow \text{noncollapsed sum fibers}
\longrightarrow \sigma\ge0
\longrightarrow \mathcal N(H)\ge0.
}
\]

Removing either middle clause admits explicit counterexamples.  A positive
source need not produce a completely monotone \(H'\), and a positive
Bernstein measure can concentrate on one scale, giving zero conditional
variance and a negative Schwarzian numerator.

## Popperian falsifiers

Clause A is falsified by any \(x>1/4\) and \(k\ge0\) with

\[
(-1)^kH^{(k+1)}(x)<0,
\]

or by any negative ordinary or shifted Hankel minor of that derivative
sequence.

Clause B is falsified by one positive-mass convolution fiber with

\[
\operatorname{Var}(t\mid t+u=v)<\frac{v^2}{20}.
\]

The weaker global condition \(\mathcal N(H)<0\) also falsifies Clause B but
does not localize the failed fiber.

## Current evidence and status

Fixed-contour theta reconnaissance at
\(x=0.251,1,10,100,400\) finds alternating derivatives of \(H'\) through the
available order and positive ordinary and shifted Hankel minors through order
three.  It also finds alternating derivatives of \(\mathcal N\) through order
six and positive initial Stieltjes Hankel minors.

These are hostile finite tests, not a proof.  Neither clause is established,
RH is not proved, and rank-two positivity alone would still be weaker than
the all-rank Loewner positivity needed by the larger program.

The first immediate attack pushes both derivative sequences through order
ten at \(x=0.251,10,400\).  Every tested sign survives.  All available
ordinary and shifted Hankel determinants through size five are positive for
both \(H'\) and \(\mathcal N\).  Doubling fixed-contour quadrature resolution
changes the moment candidates by at most approximately
\(2.2\times10^{-9}\) relatively.  This materially strengthens the finite
evidence but remains non-certified reconnaissance.

The arithmetic attack also rules out a tempting proof shortcut.  With

\[
A(r)=\frac r2-\frac1{8r},
\qquad s=r+\frac12,
\]

one prime-power exponential contributes \(-A(r)e^{-\lambda s}\) to \(H\),
up to its positive von Mangoldt coefficient.  Its contribution to \(H'\) is

\[
\frac{\lambda A(r)-A_r(r)}{2r}e^{-\lambda s}.
\]

At the outer boundary \(r=1/2\), \(A=0\) and \(A_r>0\), so this quantity is
negative.  Therefore the prime sector does not possess a separately positive
Bernstein measure on the whole outer ray.  Completion, gamma, and
prime-power terms must be transformed as one coupled object.  Any proof that
assigns an independent positive measure to every arithmetic sector is
falsified already at \(s=1\).

## Conditional spectral theorem and the origin of \(1/20\)

Assume RH only for this section.  Writing the critical-line zeros as
\(1/2\pm i\gamma\), the completed product in the \(x\)-coordinate gives

\[
(\log C)'(x)=\sum_\gamma\frac1{x+\gamma^2}.
\]

Since \(H=(x-1/4)(\log C)'\), exact differentiation yields

\[
\boxed{
H'(x)=\sum_\gamma
\frac{\gamma^2+1/4}{(x+\gamma^2)^2}.
}
\]

Put \(a_\gamma=\gamma^2+1/4\).  The elementary Laplace identity for a
double pole gives the explicit Bernstein density, based at \(x=1/4\),

\[
\boxed{
d\mu(t)=\sum_\gamma a_\gamma t e^{-a_\gamma t}\,dt.
}
\]

Thus each zero contributes a shape-two gamma component.  The constant
\(1/20\) is forced by this shape.  For two equal-rate components,
conditioning on \(t+u=v\) leaves density proportional to \(t(v-t)\), so
\(t/v\) has the \(\operatorname{Beta}(2,2)\) law and

\[
\operatorname{Var}(t\mid v)=\frac{v^2}{20}.
\]

Unequal rates only increase the spread after exchange pairing.  Pair the
ordered rate choices \((a,b)\) and \((b,a)\), and set \(t=v/2+z\).  Their
combined conditional density is proportional to

\[
\left(\frac{v^2}{4}-z^2\right)
\cosh((a-b)z),
\qquad |z|<v/2.
\]

The first factor is the centered \(\operatorname{Beta}(2,2)\) density, while
\(\cosh((a-b)z)\) increases with \(|z|\).  Chebyshev's covariance inequality
applied to \(z^2\) and this cosh factor gives

\[
\mathbb E[z^2]_{a,b}\ge\mathbb E[z^2]_{a,a}=\frac{v^2}{20}.
\]

Every exchange-paired component has mean \(v/2\), so mixing over zero pairs
preserves the bound.  Hence

\[
\boxed{
\text{RH implies Clauses A and B, and complete monotonicity of }\mathcal N.
}
\]

This explains the constant and the alternating hierarchy, but it does not
prove RH: the measure was obtained from a critical-line zero product.  The
noncircular breakthrough would be to derive the same positive shape-two
gamma mixture—or an equivalent measure with the same fiber law—from the
fixed theta/arithmetic source without first locating the zeros.

## Sharpening: the order-two Stieltjes conjecture

For a general nontrivial zero \(\rho\), put

\[
w_\rho=(\rho-1/2)^2,
\qquad
a_\rho=\frac14-w_\rho.
\]

Without assuming RH, logarithmic differentiation of the paired completed
product gives the contribution

\[
\boxed{
\frac{a_\rho}{(x-1/4+a_\rho)^2}
}
\]

to \(H'\).  Its inverse Laplace term is
\(a_\rho t e^{-a_\rho t}\).  An off-line zero therefore appears as a complex
rate; the shape-two kernel itself does not change.

This sharpens Clause A.  Mere complete monotonicity of \(H'\) asks only for
\(\mu\ge0\) and may allow cancellations among complex spectral rates.  The
hard-to-vary source statement is the generalized Stieltjes representation of
order two

\[
\boxed{
H'(x)=\int_0^\infty
\frac{d\nu(a)}{(x-1/4+a)^2},
\qquad d\nu(a)\ge0,
\qquad \operatorname{supp}\nu\subseteq[1/4,\infty).
}
\]

Equivalently,

\[
d\mu(t)=t\left(\int_0^\infty e^{-at}\,d\nu(a)\right)dt,
\]

so \(\mu(t)/t\) is completely monotone.  This one statement supplies both
original clauses because the exchange-paired shape-two components obey the
fiber variance theorem proved above.

Subject to a complete audit of convergence, analytic continuation,
multiplicities, polynomial terms, and possible boundary contributions, this
sharpened conjecture is expected to be equivalent to RH.  The forward
implication is clean: an
order-two Stieltjes function is holomorphic away from the real cut
\(( -\infty,0]\) when the rate support begins at \(1/4\), whereas each
zero-coordinate \(w_\rho\) produces a double pole of \(H'\).  Hence every
\(w_\rho\) must be real and nonpositive, and

\[
(\rho-1/2)^2<0
\quad\Longrightarrow\quad
\Re\rho=1/2.
\]

Conversely RH supplies

\[
d\nu(a)=\sum_\gamma a_\gamma\,\delta_{a_\gamma}(da),
\qquad a_\gamma=\gamma^2+1/4.
\]

The noncircular target is now precise:

\[
\boxed{
\text{derive the order-two Stieltjes representation of }H'
\text{ from the fixed completed theta source.}
}
\]

Equivalently, construct directly from the completed theta Carrier a Hilbert
space, a cyclic vector \(\Omega\), and an operator

\[
\boxed{
H'(x)=
\left\langle\Omega,
\left(x-\frac14+A\right)^{-2}\Omega
\right\rangle,
\qquad
A=A^*,\quad A\ge\frac14.
}
\]

The involutions alone do not select this operator.  They explain the fold
coordinate \(x=(s-1/2)^2\); the source-derived positive resolvent kernel must
select the physical critical-line sector and prove the lower spectral bound.
Symmetry organizes the candidates, while the source kernel supplies the
comparison and positivity.

### Free-Carrier realization no-go

The lower bound suggests the existing source operator

\[
L_0=\frac14-\partial_u^2,
\qquad L_0K=\Phi.
\]

However, the desired \(A\) cannot be the unrestricted free operator on
\(L^2(\mathbb R)\), nor a cyclic compression selected only by an ordinary
Hilbert vector.  Fourier transformation gives, for every
\(\Omega\in L^2(\mathbb R)\),

\[
\boxed{
\left\langle\Omega,
\left(x-\frac14+L_0\right)^{-2}\Omega
\right\rangle
=\frac1{2\pi}\int_{\mathbb R}
\frac{|\widehat\Omega(k)|^2}{(x+k^2)^2}\,dk.
}
\]

The associated spectral measure is absolutely continuous with respect to
Lebesgue measure in \(k\), and its pushforward under
\(a=1/4+k^2\) remains absolutely continuous away from the threshold.  Passing
to the cyclic reducing subspace generated by \(\Omega\) does not change this
measure class.

By contrast, if the matrix coefficient equals \(H'\) and the product and
continuation audit closes, its meromorphic double poles force the unique
order-two Stieltjes measure to be discrete at the spectral rates.  An
ordinary \(L^2\) vector cannot have Fourier mass supported on those discrete
frequencies.  Candidates such as \(K\), \(\Phi\), \(\sqrt\Phi\), or
\(L_0^{1/2}K\) therefore cannot repair the spectral-type mismatch while the
operator realization remains free.

There is also no whole-line boundary-condition escape: the minimal
whole-line Laplacian is essentially self-adjoint.  A half-line boundary
extension retains continuous positive spectrum and cannot generate the
required infinite discrete sequence above the threshold without an
additional source-derived confining or canonical-system structure.

Thus \(L_0\) remains the correct free ancestor—it supplies the exact
eigenvalue dictionary

\[
L_0e^{zu}=(1/4-z^2)e^{zu}
\]

and the lower edge \(1/4\)—but the theta sewing must genuinely change the
realization, not merely choose a cyclic vector.  The surviving candidates are
a theta-weighted/confining Sturm--Liouville operator or a canonical system
whose free limit is \(L_0\).

The most canonical one-density confining realization is also falsified.  Set

\[
Q_\Phi=\partial_u-\frac12(\log\Phi)',
\qquad
A_\Phi=\frac14+Q_\Phi^*Q_\Phi.
\]

This operator has all the formal virtues: it is source-derived from the
positive completed density, bounded below by \(1/4\), has ground state
\(\sqrt\Phi\), and is confining because \(\Phi\) decays superexponentially.
Dependency-free finite-difference/Sturm reconnaissance, stable under halving
the grid spacing, gives its low spectrum as approximately

\[
0.25, 21.8086, 48.0850, 77.8479, 110.6251, 146.1057,
184.0730, 224.3626,\ldots
\]

The first required reconstructed rate is \(200.04046\), strictly between the
last two displayed eigenvalues.  Neither parity subsequence contains it.
Hence the ground-state transform has the correct positivity and spectral
type but the wrong spectral locations.

The failure localizes the missing information.  A construction using only
the scalar density \(\Phi\) forgets the labelled modular sewing and transport
data.  The surviving operator must retain that richer Carrier structure,
most plausibly as a matrix/canonical system rather than a scalar
ground-state Schrödinger operator.

Artifacts:

- checkers/theta_ground_state_operator_spectrum.py
- results/theta-ground-state-operator-spectrum.json

The sharp falsifier is a necessary order-two Stieltjes inequality that fails,
or a source-derived inverse density \(\mu(t)/t\) that becomes negative.

### First order-two hostile test

The correct local moment candidates for this stronger conjecture are not the
raw alternating derivatives.  They are

\[
q_k(x)=\frac{(-1)^kH^{(k+1)}(x)}{(k+1)!},
\]

because an order-two Stieltjes representation makes \(q_k\) the moments of
\(z=(x-1/4+a)^{-1}\).  Therefore both ordinary and shifted Hankel matrices of
\((q_k)\) must be positive.  Nonnegative rates alone give
\(q_{k+1}\le q_k/(x-1/4)\), but the RH-sufficient support
\(a\ge1/4\) gives the sharper condition

\[
\boxed{q_{k+1}\le\frac{q_k}{x}.}
\]

At \(x=0.251,10,400\), all available derivative signs, the sharper
\(a\ge1/4\) support bounds,
ordinary Hankel determinants through size seven, and shifted determinants
through size six survive.  After diagonal normalization, doubling the
fixed-contour quadrature resolution preserves every tested positive sign;
even the smallest ordinary determinant has relative cross-resolution
disagreement at most about \(2.1\times10^{-3}\).  This is strong hostile
reconnaissance but remains a floating, finite test rather than an interval
certificate.

### Gaussian reconstruction from theta jets

The factorially normalized moments also permit a dependency-free Gaussian
quadrature reconstruction of the finite candidate measure.  Orthonormal
polynomials are built directly from the theta-derived moment functional, and
their Jacobi matrix supplies nodes

\[
z=(x-1/4+a)^{-1}
\]

and positive quadrature weights.  Five-node reconstructions at
\(x=0.251,10,400\) have only positive nodes and weights, and every recovered
rate satisfies the required \(a\ge1/4\) support condition.

At \(x=0.251\), the reconstructed rates begin

\[
a\approx
200.04062, 445.7184, 733.0595, 1872.68, 20451.2.
\]

The smallest rate is stable under moving the observation point to \(x=10\),
where it becomes \(200.04071\).  Its implied critical-line ordinate is

\[
\sqrt{a-1/4}\approx14.13473.
\]

No zero ordinate is supplied to the reconstruction: this value is recovered
from fixed-contour theta jets alone.  The associated quadrature weight near
the boundary is approximately \(0.004999\), consistent with the predicted
transformed atom weight \(a/(x-1/4+a)^2\).

This is a substantive reconstruction test, not a proof.  Positivity of a
finite Hankel truncation guarantees a finite quadrature model, and higher
spectral nodes are strongly compressed and observation-point dependent at
this order.  The hard theorem remains positivity and consistency of the
entire moment tower.

Two additional theta jets permit a seven-node reconstruction.  Near the
outer boundary, at \(x=0.251\), its first four implied ordinates are

\[
14.13472514189,quad
21.022189813,quad
25.03356576,\quad
31.49845.
\]

Repeating at \(x=10\) changes the first three by only approximately

\[
1.35\times10^{-10},qquad
3.96\times10^{-5},qquad
3.13\times10^{-3}.
\]

Increasing the quadrature size from six to seven moves the second and third
ordinates sharply toward the known low Riemann spectrum.  This
observation-point consistency is stronger than positivity of one finite
Hankel matrix: the same candidate rate measure is viewed through two
different resolvent coordinates.

The hostile large-\(x\) case also exposes the numerical limit.  At \(x=400\),
the seven-node reconstruction develops a spurious low node even though all
finite nodes and weights remain positive.  High-order moment conditioning,
not positivity, is the limiting factor there.  Low-order reconstruction near
the source boundary is therefore evidential; unrestricted atom claims from
ill-conditioned far-ray moments are not.

### Source-moment Jacobi operator

The Gaussian reconstruction is already a finite canonical operator model.
Fix a base point \(x_0>1/4\) and let

\[
q_k(x_0)=\frac{(-1)^kH^{(k+1)}(x_0)}{(k+1)!}.
\]

If the full ordinary and shifted Hankel forms are positive, they define a GNS
Hilbert completion of polynomials with

\[
\langle z^i,z^j\rangle=q_{i+j}(x_0).
\]

Multiplication by \(z\) is then a positive self-adjoint Jacobi operator
\(Z_{x_0}\).  The sharp support inequalities

\[
q_{k+1}\le q_k/x_0
\]

encode \(0<Z_{x_0}\le x_0^{-1}\).  Functional calculus consequently defines

\[
\boxed{
A=Z_{x_0}^{-1}-(x_0-1/4)I\ge1/4.
}
\]

The finite Gaussian rules are precisely the finite Jacobi truncations of
this construction.  In their diagonal spectral presentation,

\[
A_n=\operatorname{diag}(a_1,\ldots,a_n),
\qquad
\Omega_n=(\sqrt{\nu_1},\ldots,\sqrt{\nu_n}),
\]

and they reproduce the available theta moments of
\(\langle\Omega_n,(x-1/4+A_n)^{-2}\Omega_n\rangle\).

Undoing the resolvent tilt gives

\[
\nu_j=\frac{w_j}{z_j^2}.
\]

For the seven-node reconstructions at \(x_0=0.251\) and \(x_0=10\), the
first rate and cyclic mass are

\[
a_1\approx200.04045484,
\qquad
\nu_1\approx200.0404549,
\]

stable across the two base points at roughly the \(10^{-7}\) scale.  The
relation \(\nu_1\approx a_1\) is exactly the spectral prediction
\(d\nu=\sum a_\gamma\delta_{a_\gamma}\).  The second mass is already close to
its rate, while higher atoms remain truncation-sensitive.

This provides a canonical operator construction conditional on the infinite
moment inequalities; it does not prove those inequalities.  Its advantage is
conceptual economy: the missing source theorem is exactly what is required
to make the GNS form positive, bounded, and base-point consistent.  Once that
is proved, self-adjointness and \(A\ge1/4\) follow from standard moment and
functional calculus rather than being separately guessed.

Two refinements make this criterion exact.

First, base-point consistency is automatic from the derivative definition:

\[
\boxed{
\partial_xq_k(x)=-(k+2)q_{k+1}(x).
}
\]

This is the moment form of the resolvent identity.  The observed covariance
of finite reconstructed atoms is its truncated numerical shadow.

Second, the scalar bounds \(q_{k+1}\le q_k/x\) are necessary but not
sufficient for support in \([0,1/x]\).  The complete Hausdorff support test
requires positivity of three Hankel families:

\[
(q_{i+j})_{i,j\ge0}\succeq0,
\qquad
(q_{i+j+1})_{i,j\ge0}\succeq0,
\]

and the upper-support localizing family

\[
\boxed{
\left(\frac{q_{i+j}}x-q_{i+j+1}\right)_{i,j\ge0}\succeq0.
}
\]

The localized family survives every available finite test through size seven
at \(x=0.251,10,400\).  This corrects the earlier weaker scalar support test;
it remains finite reconnaissance.

Finally, the moment tower is generated by one familiar divided difference.
Taylor expansion and integration of the derivative series give

\[
\boxed{
\sum_{k\ge0}q_k(x)t^k
=\frac{H(x)-H(x-t)}{t}.
}
\]

Thus the Jacobi/GNS construction is the canonical operator realization of
the separated Loewner kernel already derived from the completed source.  The
“entire Hankel tower” is not new bookkeeping: it is the coefficient shadow of
one two-point kernel.  The source-side theorem can therefore be attacked as a
single positive-kernel factorization, with the shifted and localized forms
encoding respectively positivity of \(Z\) and the sharp bound
\(Z\le x^{-1}\).

### Out-of-sample finite Gram factor

The seven-node operator reconstructed solely from theta jets at
\(x_0=0.251\) was tested away from its construction point.  Its squared
resolvent predicts direct fixed-contour values of \(H'\) with relative errors
of approximately

\[
4.5\times10^{-16},quad
3.1\times10^{-16},quad
3.8\times10^{-16},quad
2.2\times10^{-10}
\]

at \(x=1,10,100,400\), respectively.  Integrating the same finite resolvent
from the base point reproduces \(H\) with relative error at most about
\(1.7\times10^{-11}\) on those anchors.

More strongly, define the explicit seven-dimensional feature map

\[
R_7(x)_j=
\frac{\sqrt{\nu_j}}{x-1/4+a_j}.
\]

Then

\[
K_7(x,y)=\langle R_7(x),R_7(y)\rangle
\]

matches the direct theta divided difference
\((H(x)-H(y))/(x-y)\) with relative errors approximately

\[
4.6\times10^{-16},quad
3.4\times10^{-16},quad
2.4\times10^{-11},quad
1.6\times10^{-11}
\]

on the pairs \((1,10),(10,100),(100,400),(1,400)\).  Thus a positive Gram
factor has been explicitly constructed to high accuracy over the full outer
scale from seven source-moment atoms.

This is still not an exact factorization: the finite Gaussian model is built
from a positive truncation of the same theta moment functional, and its
excellent out-of-sample accuracy does not prove positivity of every
truncation or convergence of the Jacobi operators.  It does identify the
missing theorem sharply:

\[
\boxed{
\text{prove the source-moment Jacobi approximants are positive,
support-localized, and converge to a base-point-independent operator.}
}
\]

No further guess about the feature map is required; its finite form is
already \(\sqrt{\nu_j}/(x-1/4+a_j)\).

The dimension scan confirms systematic Gaussian convergence.  For operators
of dimensions two through seven reconstructed at \(x_0=0.251\), the maximum
relative error in \(H'\) over \(x=1,10,100,400\) decreases as

\[
3.72\times10^{-2},\quad
1.77\times10^{-3},\quad
5.72\times10^{-5},\quad
1.53\times10^{-6},\quad
2.28\times10^{-8},\quad
2.16\times10^{-10}.
\]

Once the full three-family Hausdorff positivity theorem is established, this
convergence is not an additional conjecture.  Compact support makes the
moment problem determinate; Gaussian/Jacobi truncations converge to the
unique multiplication operator, and the exact differential transport of the
moments gives base-point independence.

The logical first gate must nevertheless remain visible.  The smallest
nontrivial ordinary Hankel determinant is

\[
q_0q_2-q_1^2
=\frac{2H'H'''-3(H'')^2}{12}
=\frac{\mathcal N(H)}{12}.
\]

Thus the infinite operator theorem already contains the rank-two Schwarzian
theorem as its first coupled condition.  That condition is now directedly
certified on \(1/4\le x\le400\) and proved analytically for \(x\ge400\), hence
holds universally on the outer ray.  Higher positive reconstructions cannot
substitute for the remaining higher-rank gates.

Nor can universal rank two be promoted formally to rank three.  The exact
factorially normalized jet

\[
(q_0,q_1,q_2,q_3,q_4)=(1,1,2,5,51/4)
\]

has all three adjacent rank-two Hankel minors positive,

\[
q_0q_2-q_1^2=1,
\quad q_1q_3-q_2^2=1,
\quad q_2q_4-q_3^2=1/2,
\]

while

\[
\det(q_{i+j})_{0\le i,j\le2}=-1/4.
\]

This is an exact logical falsifier of a rank-two-to-operator leap.  The next
irreducible theorem is positivity for three separated heights; the already
proved confluent rank-three theorem controls only its diagonal limit.

Artifacts:

- checkers/theta_order_two_stieltjes_gaussian_reconstruction.py
- checkers/rank_two_not_rank_three_hankel_falsifier.py
- results/theta-order-two-stieltjes-gaussian-reconstruction.json
- results/rank-two-not-rank-three-hankel-falsifier.json

## Immediate attack

1. Push Clause A to higher derivative and Hankel orders using analytic kernel
   differentiation on the fixed real contour.
2. In parallel, derive the arithmetic candidate for \(\mu\) on \(s>1\) using
   the subordination identity for \(e^{-a\sqrt x}\), retaining completion,
   gamma, and prime-power terms together.
3. If a positive \(\mu\) is obtained, disintegrate its self-convolution over
   \(v=t+u\) and test the variance threshold before attempting a global
   transport proof.
