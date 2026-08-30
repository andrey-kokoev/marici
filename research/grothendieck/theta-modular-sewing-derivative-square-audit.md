# Theta modular sewing has a graded derivative square, not an odd-data kernel

## Audit target

Nima proposed the cross-sector test

\[
\partial S=S\partial,
\qquad
\nabla S-S\nabla=\text{external-boundary evaluation},
\]

and asked whether theta's cancellation of labelled odd boundary jets is
precisely internal-boundary cancellation.

The answer is positive after one necessary typing correction:

\[
\boxed{
\text{ordinary differentiation does not commute with even folding;
it switches sewing parity.}
}
\]

Moreover, the cancelled odd seam traces are not the kernel of the sewing map.
They are the kernel condition for smooth descent through the seam.

## Label summation and parity-sensitive sewing

Let

\[
\Sigma(f_1,f_2,\ldots)=h=\sum_{n\ge1}f_n
\]

on the positive half-line. On suitable rapidly convergent theta-source
families, differentiation commutes with label summation:

\[
D\Sigma=\Sigma D.
\]

Introduce the two extensions

\[
(E_+h)(u)=h(|u|),
\qquad
(E_-h)(u)=\operatorname{sgn}(u)h(|u|).
\]

Away from the seam \(u=0\),

\[
DE_+=E_-D,
\qquad
DE_-=E_+D.
\]

Distributionally, the second identity carries the seam defect

\[
\boxed{
DE_-h=E_+Dh+2h(0)\delta_0.
}
\]

The correctly typed sewing operator is therefore the graded pair

\[
S_+=E_+\Sigma,
\qquad
S_-=E_-\Sigma,
\]

with

\[
DS_+=S_-D
\]

for continuous half-line totals and

\[
\boxed{
DS_-=S_+D+2\,\operatorname{ev}_0\Sigma\,\delta_0.
}
\]

This is the exact sewing/derivative square. The commutator is not an
unspecified anomaly: it is boundary evaluation at the seam.

## Higher derivatives and the odd-jet defect

Repeated differentiation gives

\[
D^{2m}E_+h
=E_+D^{2m}h
+2\sum_{j=0}^{m-1}
h^{(2j+1)}(0)\,
\delta_0^{(2m-2j-2)}.
\]

Thus \(E_+h\) is smooth across the seam exactly when

\[
h^{(2j+1)}(0)=0
\qquad(j\ge0).
\]

For the labelled theta source, individual \(f_n\) have nonzero odd one-sided
jets, while modular completion proves

\[
\sum_{n\ge1}f_n^{(2j+1)}(0)=0.
\]

Consequently the distributional internal-boundary current cancels only after
full label summation. This verifies Nima's proposed interpretation:
the previously observed odd-jet cancellation is exactly the folded-label
presentation of internal seam-current cancellation.

## Why “odd jets equal the kernel of sewing” is false

Let

\[
J_{\rm odd}(h)=
\bigl(h'(0),h'''(0),h^{(5)}(0),\ldots\bigr).
\]

The modular identity says

\[
J_{\rm odd}\Sigma(f_n)=0.
\]

It does not say

\[
S_+(f_n)=0.
\]

Indeed the completed theta source is a nonzero smooth even function. Therefore

\[
\ker S_+
\subsetneq
\ker(J_{\rm odd}\Sigma)
\]

on any domain containing the theta family. The right-hand side is the
smooth-sewing locus, not the zero object.

Equivalently, sewing forgets the decomposition-dependent internal boundary
currents while retaining the completed bulk source. Confusing these two
kernels would identify descent with annihilation.

## Surviving completed odd data

The strongest possible “all odd data are killed” claim has an immediate exact
falsifier. If \(\Phi(u)\) is the nonconstant completed even theta source, then

\[
\Phi'(-u)=-\Phi'(u),
\qquad
\Phi'(0)=0,
\]

but \(\Phi'\) is not identically zero. It is a canonical completed odd
section. Likewise, odd Mellin/tangent responses can survive away from the
seam.

Therefore modular sewing annihilates precisely the local odd seam traces that
obstruct smooth even descent. It does not annihilate global odd sections,
odd parameter responses, or every datum of odd parity.

## Corrected cross-sector conjecture

A source-sewing operator \(S\) on a labelled relative object carries a
boundary-defect map \(B_{\rm int}\) such that:

1. internal presentation boundaries occur in \(B_{\rm int}\);
2. source completion makes their signed sum vanish;
3. differentiation is natural in a graded sewing complex;
4. the failure of the derivative square is supported only on genuine
   external-boundary evaluation; and
5. global odd sections may survive after their seam traces vanish.

For theta, the external endpoint defect vanishes because the completed source
has the required endpoint decay and the modular seam has zero odd trace. For
cosmology, nonzero finite endpoint primitives can instead require an explicit
relative extension.

This is a statement about descent of boundary role, not disappearance of all
odd data.

## Scope boundary

The displayed identities prove the local folded-source square for
\(D=\partial_u\). They do not by themselves prove the full
Gauss--Manin/thimble identity for a parameter connection \(\nabla\).
That stronger statement requires transporting the relative integration cycle
and applying the relative Stokes formula; its remaining defect should then be
checked against the actual external endpoints. The present theorem supplies
the seam term and its exact cancellation, not the unavailable physical
relative-chain pushforward in another sector.

## Exact fixed-cycle Mellin sewing theorem

There is nevertheless an exact relative-chain theorem on theta's fixed real
cycle. Put

\[
\Gamma_+=[0,\infty),
\qquad
\Gamma_-=(-\infty,0],
\qquad
\Gamma=\Gamma_-+\Gamma_+,
\]

with their standard orientations. Their internal boundaries at zero cancel:

\[
\partial\Gamma_+=[\infty]-[0],
\qquad
\partial\Gamma_-=[0]-[-\infty].
\]

For the completed half-line source \(h=\Sigma(f_n)\), define

\[
Z(z)
=\int_\Gamma e^{zu}E_+h(u)\,du
=\int_0^\infty
\bigl(e^{zu}+e^{-zu}\bigr)h(u)\,du.
\]

Theta-source decay is superexponential at both external ends after modular
completion. Hence parameter differentiation is exact:

\[
\boxed{
\partial_z^k Z(z)
=\int_\Gamma u^k e^{zu}E_+h(u)\,du.
}
\]

In particular, label summation, oriented chain sewing, and the parameter
connection commute on every compact \(z\)-set on which the dominated
convergence estimate is taken:

\[
\boxed{
\partial_z\,\mathcal I_\Gamma S_+
=\mathcal I_\Gamma S_+\,\partial_z.
}
\]

Here \(\partial_z\) acts on the exponential coefficient rather than on the
source label, so the notation means naturality of the integrated family, not
an identification of two unrelated derivatives.

For source differentiation, let \(D_{\rm half}^k\) mean classical
differentiation on each open half-line, excluding delta distributions inserted
at the seam. Relative Stokes gives

\[
\int_\Gamma e^{zu}D_{\rm half}^k(E_+h)\,du
=(-z)^kZ(z)
+\text{internal seam current}
+\text{external endpoint current}.
\]

The external current is zero by theta decay. The internal current is exactly
the finite distributional combination of odd jets displayed above. Therefore
modular completion yields

\[
\boxed{
\int_\Gamma e^{zu}D_{\rm half}^k(E_+h)\,du
=(-z)^kZ(z)
}
\]

for every \(k\), because all completed odd seam jets vanish.

This is the fixed-cycle realization of

\[
\partial S=S\partial,
\qquad
\nabla S-S\nabla=\text{external-boundary evaluation}:
\]

the first identity must be parity-graded before integration, and the second
has zero right-hand side for the completed real theta cycle.

## What remains beyond the fixed real cycle

The theorem above uses a nonmoving real chain and entire coefficient
\(e^{zu}\). A genuine complex-thimble Gauss--Manin theorem additionally
requires:

1. a transported relative thimble local system;
2. covariance across Stokes mutation;
3. control of complex endpoints at infinity; and
4. proof that no wall-crossing term survives in the total sewn cycle.

Our earlier mutation-invariance result strongly suggests item 2 for the total
denominator-free current, but it does not supply the full relative-chain
transport. Thus the real Mellin square is proved while the complex-thimble
extension remains an explicit separate gate.

## Complex relative-period theorem

The completed theta integrand has an additional source property that removes
the finite-endpoint part of that gate. In logarithmic coordinate, put

\[
\omega_z(u)=e^{zu}\Phi(u)\,du,
\qquad
\partial_z^k\omega_z=u^ke^{zu}\Phi(u)\,du.
\]

Let \(D_{\rm fin}\) be the zero divisor of the analytically continued source
\(\Phi\). Every derivative in the parameter \(z\) vanishes on that divisor:

\[
\left.\partial_z^k\omega_z\right|_{D_{\rm fin}}=0
\qquad(k\ge0).
\]

Fix one theta analyticity strip

\[
\mathcal U_k
=\left\{u:\left|\Im u-k\pi\right|<\frac\pi4\right\}.
\]

Consider a differentiable family of relative paths
\(\gamma_z:[0,1]\to\mathcal U_k\) whose finite endpoints lie in
\(D_{\rm fin}\), while any infinite endpoints remain in uniformly decaying
theta sectors. Differentiating a moving-path integral gives

\[
\frac d{dz}\int_{\gamma_z}\omega_z
=\int_{\gamma_z}\partial_z\omega_z
+\omega_z(\gamma_z(1))\gamma_z'(1)
-\omega_z(\gamma_z(0))\gamma_z'(0).
\]

The finite endpoint terms vanish because \(\Phi=0\); the infinite terms
vanish by the stated uniform decay. Therefore

\[
\boxed{
\nabla_z\int_{\gamma_z}\omega_z
=\int_{\gamma_z}u\,\omega_z
}
\]

for Gauss--Manin transport of the relative class. Iteration gives all
\(z\)-jets.

For an incidence chain

\[
\Gamma_z=\sum_j n_j\gamma_{j,z},
\]

any shared internal endpoint cancels a second time by oriented incidence.
Thus the derivative square is insensitive to how the total path is subdivided
among zero-to-zero and zero-to-infinity edges.

## Stokes mutation contributes no derivative defect

Suppose a wall changes a thimble basis by

\[
\gamma'=A\gamma,
\qquad
n'=A^{-T}n,
\qquad
A\in GL_r(\mathbb Z),
\]

while preserving the total relative class. The period vector and every
parameter-derivative vector transform by the same \(A\). Hence

\[
n'^T\partial_z^kp'
=n^T\partial_z^kp
\]

for all \(k\). Stokes mutation then contributes neither a jump in the total
period nor an extra connection term. It only reallocates the same relative
period among basis edges.

This upgrades the earlier mutation-invariance theorem from the quadratic cone
readout to the full period jet:

\[
\boxed{
\text{the total completed Mellin jet is covariant under integral
Picard--Lefschetz mutation.}
}
\]

No common thimble phase or componentwise positivity is needed.

## Narrowed remaining gate

The complex theorem is exact under two hypotheses that are not yet global
theorems for the full outer parameter domain:

1. the incidence chain after each wall is the Gauss--Manin continuation of
   the original real relative class; and
2. every infinite end remains in a decay sector uniformly enough to discard
   the endpoint arc.

For \(u=x+iy\) and \(x\to+\infty\), each theta label contains the decisive
factor

\[
\exp\!\bigl(-\pi n^2e^{2x}e^{2iy}\bigr),
\]

whose modulus decays superexponentially exactly inside the open sectors

\[
\cos(2y)>0,
\qquad
\left|y-k\pi\right|<\frac\pi4
\quad(k\in\mathbb Z).
\]

The negative end has the reflected condition by modular evenness. Hence the
arc-at-infinity falsifier is geometrically explicit: a transported endpoint
leaving every closed subsector
\(\left|y-k\pi\right|\le\pi/4-\varepsilon\) loses the uniform decay estimate.

The first three-edge reconstruction supplies numerical evidence for the first
hypothesis at the first two mutations, not a global proof. The sharp
falsifiers are now correspondingly narrow:

- a wall at which the incidence mutation changes the relative class; or
- an endpoint ray crossing a theta anti-decay boundary, producing a nonzero
  arc-at-infinity term.

Finite source-zero endpoints themselves cannot generate the missing defect.

## Asymptotic classification of infinite thimble ends

The infinity hypothesis can also be reduced sharply. In any closed subsector
of a positive theta-decay wedge, the \(n=1\) label dominates and

\[
\Phi(u)
=4\pi^2
\exp\!\left(\frac92u-\pi e^{2u}\right)
\left(1+O(e^{-2\Re u})+O(e^{-3\pi e^{2\Re u}\cos(2\Im u)})\right).
\]

The precise lower-order expression is unimportant here; the decisive action
for the completed Mellin integrand is

\[
\mathcal A_z(u)
=\pi e^{2u}-\left(z+\frac92\right)u+O(e^{-2u}),
\qquad
e^{zu}\Phi(u)\asymp e^{-\mathcal A_z(u)}.
\]

Let \(u=x+iy\) tend to \(+\infty\) along a constant-phase steepest-descent
end. The exponentially large part of the phase is

\[
\Im\mathcal A_z(u)
=\pi e^{2x}\sin(2y)+O(x+|z|\,|u|).
\]

For this phase to remain constant modulo lower-order variation,

\[
\sin(2y)\longrightarrow0,
\]

so every asymptotic end must approach

\[
y\longrightarrow\frac{k\pi}{2}.
\]

There are two alternating types:

\[
\begin{array}{c|c|c}
y\to k\pi & \cos(2y)\to+1
& \Re\mathcal A_z\to+\infty\quad\text{(decay)}\\
y\to\pi/2+k\pi & \cos(2y)\to-1
& \Re\mathcal A_z\to-\infty\quad\text{(anti-decay)}.
\end{array}
\]

The boundary directions \(y\to\pi/4+k\pi/2\) are also inadmissible: the
superexponential damping disappears while the algebraic exponential
prefactor grows.

Consequently every convergent downward theta thimble ending at
\(+\infty\) must approach \(y=k\pi\). More precisely its phase equation gives

\[
y-k\pi=O\!\left((1+x)e^{-2x}\right),
\]

with a constant depending locally on \(z\). It therefore eventually lies
inside every fixed decay wedge

\[
|y-k\pi|\le\frac\pi4-\varepsilon
\]

for some \(\varepsilon>0\). Modular evenness gives the corresponding statement
at \(-\infty\).

Thus an already convergent canonical thimble cannot silently acquire a
nonzero arc-at-infinity term while remaining in the same endpoint class.
Escape to an anti-decay sector is a loss of admissibility, not an ordinary
Stokes basis mutation.

## Single remaining global topological gate

Combining the seam theorem, finite-zero endpoint theorem, mutation covariance,
and asymptotic end classification leaves one substantive global condition:

\[
\boxed{
\text{the incidence chain in every chamber must be the Gauss--Manin
continuation of the original real relative class.}
}
\]

If that holds, the complete Mellin period and all its \(z\)-jets sew across
every Stokes wall without boundary defects. The remaining RH difficulty is
then analytic positivity of the resulting basis-free quadratic current, not
connection compatibility.

## Endpoint-incidence uniqueness theorem

For the completed Mellin period, the remaining topological condition is
automatic inside one theta analyticity strip once its endpoint statement is
typed correctly. Fix

\[
\mathcal U_k
=\left\{u:\left|\Im u-k\pi\right|<\frac\pi4\right\}.
\]

The coefficient

\[
e^{zu}\Phi(u)
\]

is holomorphic on \(\mathcal U_k\). Source zeros are endpoints for a
convenient thimble incidence presentation, but they are not punctures or
singularities of the integrand. The strip boundary is different: the defining
theta series loses its decay domain there and may not be crossed by this
argument.

First ignore infinity and let \(D\subset\mathcal U_k\) be any finite set of
allowed relative endpoints. The long exact sequence of the pair gives

\[
0=H_1(\mathcal U_k)
\longrightarrow H_1(\mathcal U_k,D)
\mathop{\longrightarrow}^{\partial}
H_0(D)
\longrightarrow H_0(\mathcal U_k)
\longrightarrow0.
\]

Consequently

\[
\boxed{
H_1(\mathcal U_k,D)\cong\widetilde H_0(D),
}
\]

and the boundary map is injective. Two relative one-chains with the same
oriented endpoint zero-chain are therefore the same relative class.

Analytically, the same conclusion is even more direct. Every one-form

\[
\partial_z^k\omega_z
=u^ke^{zu}\Phi(u)\,du
\]

is holomorphic on the simply connected strip \(\mathcal U_k\) and therefore
has a global primitive there. Its integral over every finite closed
difference cycle in that strip is exactly zero by Cauchy's theorem. The
endpoint-incidence result consequently holds simultaneously for the full
Mellin jet, not only for the base period.

For theta chains with infinite ends, truncate at \(\Re u=\pm R\). Two
admissible representatives approaching the same decay ends can be joined
there by arcs contained in a common closed decay wedge. The asymptotic theorem
above makes the integrals over those joining arcs tend to zero
superexponentially as \(R\to\infty\). The finite truncated difference is a
closed cycle in \(\mathcal U_k\), hence bounds because
\(H_1(\mathcal U_k)=0\).

It follows that an oriented incidence chain satisfying

1. every internal source-zero endpoint occurs with total coefficient zero;
2. its external boundary is
   \([+\infty_{\rm dec}]-[-\infty_{\rm dec}]\); and
3. all infinite edges are admissible,

is automatically the same completed relative class as the real Mellin
contour.

Thus

\[
\boxed{
\text{endpoint incidence, not saddle count or wall history, determines the
completed theta relative class.}
}
\]

An integral Picard--Lefschetz mutation is one mechanism that preserves this
incidence, but it is not additional authority once the total boundary has
been checked.

## Consequence: the connection problem is closed

Combining:

- modular cancellation of internal seam jets;
- exact fixed-cycle Stokes;
- vanishing of all finite source-zero endpoint evaluations;
- covariance of every Mellin jet under basis mutation;
- asymptotic classification of admissible infinity ends; and
- endpoint-incidence uniqueness,

proves that every admissible sewn incidence presentation with the physical
external boundary carries the same completed Mellin period and all of its
parameter jets.

There is no remaining connection or wall-crossing obstruction for an
incidence chain that stays within one theta analyticity strip. Globally, one
must still prove that the physical incidence continuation never leaves that
strip (or separately construct an authorized analytic continuation across its
boundary). Subject to that domain gate, the hard unsolved statement is
cleanly analytic:

\[
\boxed{
Q_z(\Gamma)>0
}
\]

throughout the required parameter domain. This positivity would exclude
zeros, so it cannot be inferred from the topological theorem.

## New sharp falsifier

A proposed thimble reconstruction is rejected if:

- its internal endpoint incidence does not cancel;
- it changes either physical decay end;
- an end is anti-decaying; or
- an edge crosses a theta analyticity-strip boundary; or
- it introduces an actual singularity of the coefficient, rather than a
  harmless source zero.

If none occurs, disagreement with the real-contour period is numerical
quadrature or path-truncation error, not a distinct relative class.

## The strip-domain gate is optional

The physical completed Mellin period does not require any complex-thimble
continuation. Its source contour is the fixed real line

\[
\Gamma_{\mathbb R}=\mathbb R\subset\mathcal U_0.
\]

The completed theta source decays superexponentially as
\(|u|\to\infty\). Consequently, for every compact \(K\subset\mathbb C_z\) and
every \(m\ge0\), there is an integrable real majorant for

\[
\sup_{z\in K}
\left|u^m e^{zu}\Phi(u)\right|.
\]

It follows that

\[
Z(z)=\int_{\mathbb R}e^{zu}\Phi(u)\,du
\]

is entire in the parameter \(z\), with all derivatives obtained on the same
fixed real contour:

\[
Z^{(m)}(z)
=\int_{\mathbb R}u^me^{zu}\Phi(u)\,du.
\]

Thus the physical relative class never approaches an analyticity-strip
boundary. Complex thimbles are optional coordinate systems for asymptotic or
numerical analysis; their global continuation is not part of the existence,
analyticity, or connection proof for the completed period.

If a chosen thimble presentation crosses
\(|\Im u|=\pi/4\), that presentation ceases to be authorized by the current
theta-series chart. It does not obstruct the fixed real source integral.

## Final reduction of the thimble programme

All topological and connection gates can therefore be removed from the
minimal RH proof contract. The intrinsic object is

\[
Z(z)=\int_{\mathbb R}e^{zu}\Phi(u)\,du,
\]

or equivalently its quarter-centered squared-coordinate transform. The sole
remaining theorem sought in this lane is a real-source proof of the
basis-independent positivity current

\[
Q_z
=\Re\!\left(
(\beta-i\alpha)Z'(z)\overline{Z(z)}
\right)>0
\]

on the target outer domain.

Thimble calculations remain useful hostile diagnostics: a reconstructed chain
must agree with the real contour, and component signs expose why
componentwise positivity fails. But they carry no independent proof
obligation once the undecomposed real-source representation is retained.

This is another surprise-propagation correction:

\[
\boxed{
\text{the apparent global thimble-transport problem was created by replacing
a fixed entire-parameter source integral with moving coordinates.}
}
\]
