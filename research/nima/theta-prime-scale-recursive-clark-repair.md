# Prime-scale recursion supplies a source-specific Clark repair term

Status: exact modular-source identity and candidate mechanism; no Schur or RH
claim

## Arithmetic translate structure of the theta source

On the positive logarithmic chamber, write the completed theta density as

\[
\Phi(u)=\sum_{n\ge1}\phi_n(u),
\]

with

\[
\phi_n(u)=
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
e^{-\pi n^2e^{2u}}.
\]

If

\[
\phi(t)=
\left(4\pi^2e^{9t/2}-6\pi e^{5t/2}\right)e^{-\pi e^{2t}},
\]

then direct substitution gives the exact translate law

\[
\boxed{
\phi_n(u)=n^{-1/2}\phi(u+\log n).
}
\]

For (u\ge0), every summand is positive because
(2\pi n^2e^{2u}>3). This is stronger than positivity and evenness: the
source is an arithmetic superposition of one profile transported by the
multiplicative monoid of positive integers.

## Exact prime recursion

For a prime (p), split the source into indices divisible and not divisible
by (p). The divisible sector is

\[
\sum_{m\ge1}\phi_{pm}(u)
=p^{-1/2}\sum_{m\ge1}\phi_m(u+\log p)
=p^{-1/2}\Phi(u+\log p).
\]

Consequently

\[
\boxed{
\Phi(u)=\Phi_{p\nmid}(u)+p^{-1/2}\Phi(u+\log p),
\qquad
\Phi_{p\nmid}(u)=\sum_{p\nmid n}\phi_n(u)>0.
}
\]

This identity holds simultaneously for every prime and is compatible with
iterating prime powers. A generic positive even source—and in particular the
hostile two-atom source—does not carry this labelled all-prime recursion.

## The signed Clark fold acquires a positive repair

For the normalized Clark denominator put

\[
h_a(u)=(1-au)\Phi(u),\qquad a>0,
\]

and let (ell=\log p). Multiplying the prime recursion by (1-au), while
comparing with the translated signed density, gives

\[
\boxed{
h_a(u)-p^{-1/2}h_a(u+\ell)
=(1-au)\Phi_{p\nmid}(u)
+a\ell\,p^{-1/2}\Phi(u+\ell).
}
\]

The last term is strictly positive on the positive chamber. It is not fitted:
its coefficient is forced by the displacement of the fold under the prime
translation. Thus modular scale recursion produces exactly the architecture
missing from the generic one-fold argument:

\[
\text{translated signed fold}
+\text{primitive-prime signed remainder}
+\text{positive displacement repair}.
\]

The repair does not yet prove that the Fourier--Laplace transform of (h_a)
is upper-half-plane stable. The primitive-prime remainder still changes sign
at (u=1/a), and the faithful bilateral source requires the modular sewing at
(u=0). But the identity is the first candidate mechanism that is both
source-specific and capable of distinguishing the theta density from the
two-atom counterexample.

## The repair is not pointwise dominant

The positive displacement term cannot repair the signed density by a local
inequality. As (u\to+\infty), the primitive sector is dominated by (n=1):

\[
\Phi_{p\nmid}(u)\sim\phi_1(u).
\]

The shifted term is the sector of labels divisible by (p), whose first
contribution is (phi_p(u)). Their ratio contains

\[
\exp\!\left[-\pi(p^2-1)e^{2u}\right]
\]

times only an elementary exponential factor. Hence

\[
\frac{a\log(p)\,p^{-1/2}\Phi(u+\log p)}
{(au-1)\Phi_{p\nmid}(u)}\longrightarrow0.
\]

In the negative side of the fold, the source-forced positive repair is
asymptotically much smaller than the negative primitive remainder. Therefore
the prime recursion does **not** imply pointwise positivity of the Clark
density or of a local energy integrand. Any successful repair must occur only
after transform and sewing.

## Transform recursion and the arithmetic half-line

Let

\[
F_a(z)=\int_0^\infty h_a(u)e^{izu}\,du,
\qquad
B_{a,p}(z)=\int_0^{\log p}h_a(u)e^{izu}\,du,
\]

and denote the transform of the right-hand side of the prime recursion by
(R_{a,p}(z)). Changing variables in the shifted integral gives

\[
\int_0^\infty h_a(u+\log p)e^{izu}\,du
=p^{-iz}\bigl(F_a(z)-B_{a,p}(z)\bigr).
\]

Therefore

\[
\boxed{
\left(1-p^{-1/2-iz}\right)F_a(z)
=R_{a,p}(z)-p^{-1/2-iz}B_{a,p}(z).
}
\]

The prime multiplier vanishes exactly at

\[
\boxed{
z=\frac{2\pi k}{\log p}+\frac i2,
\qquad k\in\mathbb Z.
}
\]

The height (1/2) is forced by the translate weight (n^{-1/2}). It is not
inserted from a zero list. In the centered variable
(s=1/2+iz), this upper (z)-line maps to the outer boundary
(\operatorname{Re}s=0) of the critical strip, not to the RH line itself.

Since (F_a) is entire under the superexponential source decay, every
apparent prime-multiplier pole is cancelled by the finite chamber term and
the primitive-sector transform:

\[
R_{a,p}(z)=p^{-1/2-iz}B_{a,p}(z)
\quad\text{when}\quad p^{-1/2-iz}=1.
\]

This cancellation is an exact finite sewing constraint. Dropping
(B_{a,p}) would manufacture false arithmetic singularities. The promising
object is therefore not the Euler-like multiplier alone, but the triple

\[
\boxed{
\text{prime multiplier}
+\text{primitive-label transform}
+\text{finite modular sewing current}.
}
\]

The next question is whether these cancellation identities for all primes
assemble into a positive Hardy-space boundary form. A single-prime recursion
cannot suffice: its multiplier has zeros inside the upper (z)-half-plane
and is rescued only by the source-defined finite current.

## The bare arithmetic character is not the Hilbert feature

The semigroup character

\[
\chi_z(n)=n^{-1/2-iz}
\]

has modulus (n^{y-1/2}) for (z=x+iy). Although each nontrivial label is a
strict contraction when (y<1/2), the full character vector is not square
summable in the relevant upper half-plane:

\[
\sum_{n\ge1}|\chi_z(n)|^2
=\sum_{n\ge1}n^{2y-1}=\infty
\qquad(y>0).
\]

Therefore a polarization that treats the label characters themselves as
Hilbert-space features is mistyped. The logarithmic commutator is exact, but
its putative positive contraction loss cannot be summed before the finite
chamber/tail data are restored.

## The source-normalized tail feature

For the primitive profile (phi), define

\[
T(q,z)=\int_q^\infty\phi(v)e^{izv}\,dv,
\qquad q\ge0,
\]

and

\[
\boxed{
G(q,z)=e^{-(1/2+iz)q}T(q,z).
}
\]

At the arithmetic scales (q=\log n), this is exactly the half-line transform
of the transported source label:

\[
G(\log n,z)
=\int_0^\infty(S_n\phi)(u)e^{izu}\,du.
\]

The superexponential tail of (phi) makes the labelled family summable even
when the naked characters are not. Thus (G(\log n,z)), not
(chi_z(n)), is the faithful candidate feature.

Differentiating in the continuous scale variable gives the exact forced flow

\[
\boxed{
\partial_qG(q,z)
=-(1/2+iz)G(q,z)-e^{-q/2}\phi(q).
}
\]

The oscillatory phase cancels completely from the boundary forcing. The
coefficient (1/2+iz) is the centered Mellin variable, while the forcing is
real and source-positive on the modular chamber. This is a more faithful
transport law than the bare identity
(partial_y\chi_z(n)=\log(n)\chi_z(n)): differentiating the complete feature
also differentiates its moving tail.

For the signed primitive fold define

\[
T_a(q,z)=\int_q^\infty(1-av)\phi(v)e^{izv}\,dv.
\]

Then the transform of the (n)-labelled Clark contribution is

\[
e^{-(1/2+iz)q}
\left[T_a(q,z)+aq\,T(q,z)\right]_{q=\log n}.
\]

The positive commutator repair (aqT) and the signed primitive tail (T_a)
are therefore two components of one source-normalized tail feature. They may
not be polarized independently.

## Revised positivity target

The next legitimate Gram construction must use the tail-weighted arithmetic
features and prove convergence before taking cross-label sums. Its prospective
energy has three typed pieces:

\[
\boxed{
\text{Mellin scale flow of }G
+\text{positive boundary forcing }e^{-q/2}\phi(q)
+\text{discrete sampling at }q=\log n.
}
\]

The sharp test is whether Green's identity for the forced scale flow, summed
over the multiplicative labels with the modular sewing relation retained,
reproduces the de Branges Bezoutian. If it leaves a boundary term of
indefinite sign, the positive-commutator explanation is insufficient in its
current form.

## Exact Green identity: positive bulk with two rank-one defects

Put

\[
s_z=\frac12+iz,
\qquad
f(q)=e^{-q/2}\phi(q),
\]

so that

\[
\partial_qG(q,z)=-s_zG(q,z)-f(q).
\]

For two spectral parameters (z,w), let

\[
P(q;z,w)=G(q,z)\overline{G(q,w)}.
\]

Since

\[
s_z+\overline{s_w}=1-i(\bar w-z),
\]

direct differentiation gives

\[
i(\bar w-z)P
=\partial_qP+P+f(q)
\left(G(q,z)+\overline{G(q,w)}\right).
\]

The source tail makes (G(q,z)\to0) as (q\to\infty). Integrating and
completing the square therefore yields

\[
\boxed{
\begin{aligned}
i(\bar w-z)\int_0^\infty
G(q,z)\overline{G(q,w)}\,dq
={}&\int_0^\infty
\bigl(G(q,z)+f(q)\bigr)
\overline{\bigl(G(q,w)+f(q)\bigr)}\,dq\\
&-\int_0^\infty f(q)^2\,dq
-G(0,z)\overline{G(0,w)}.
\end{aligned}
}
\]

The first term is a positive Gram kernel. The remaining obstruction has rank
at most two on every finite spectral packet:

1. the constant kernel (int f^2), representing the primitive source norm;
2. the boundary kernel (G(0,z)\overline{G(0,w)}), representing the primitive
   Fourier tail at the modular seam.

On the diagonal (w=z=x+iy), the identity becomes

\[
2y\int_0^\infty|G(q,z)|^2\,dq
=\int_0^\infty|G(q,z)+f(q)|^2\,dq
-\int_0^\infty f(q)^2\,dq
-|G(0,z)|^2.
\]

This identity is source-faithful and denominator-free. It also holds for a
generic sufficiently decaying primitive profile, so it cannot by itself imply
RH. Its importance is architectural: the continuous Mellin-scale flow has a
positive bulk and a finite, explicitly typed defect rather than uncontrolled
indefinite curvature.

The modular/arithmetic theorem is now sharply localized. After discrete
sampling at (q=\log n), summing labels, applying the Clark differential
(1+ia\partial_z), and sewing the reflected chamber, the source must repair
exactly these primitive norm and seam-boundary channels. If additional
indefinite cross-label terms remain, the present positive-commutator mechanism
does not close.

## The Clark differential creates one Jordan cross-channel

The complete one-label Clark feature is

\[
H(q,z)=(1+ia\partial_z)G(q,z).
\]

Differentiating the forced scale equation with respect to (z) gives the
closed triangular pair

\[
\boxed{
\begin{aligned}
\partial_qG&=-s_zG-f,\\
\partial_qH&=-s_zH+aG-f.
\end{aligned}
}
\]

Thus the Clark differential does not commute with scale transport. It creates
a rank-one nilpotent/Jordan coupling (G\mapsto aG) inside the continuous
state.

Repeating the Green calculation directly for (H) yields

\[
\boxed{
\begin{aligned}
i(\bar w-z)\int_0^\infty
H(q,z)\overline{H(q,w)}\,dq
={}&\int_0^\infty
\bigl(H(q,z)+f(q)\bigr)
\overline{\bigl(H(q,w)+f(q)\bigr)}\,dq\\
&-\int_0^\infty f(q)^2\,dq
-H(0,z)\overline{H(0,w)}\\
&-a\int_0^\infty
\left[
G(q,z)\overline{H(q,w)}
+H(q,z)\overline{G(q,w)}
\right]dq.
\end{aligned}
}
\]

The last line is the new obstruction. On the diagonal, introduce

\[
U_\pm=\frac{H\pm G}{\sqrt2}.
\]

Then

\[
G\overline H+H\overline G
=|U_+|^2-|U_-|^2.
\]

The Clark differential therefore produces exactly one positive and one
negative continuous bulk channel. It is a typed defect of the Jordan scale
flow, not one of the two rank-one boundary defects found before applying the
differential.

A nonzero nilpotent operator cannot be skew-adjoint in a positive-definite
finite-dimensional metric. Consequently no constant positive symmetrizer of
the local ((G,H)) state can simply erase this cross-channel. Its control must
come from the arithmetic sampling, reflected modular sewing, or an enlarged
boundary complex.

This is the precise remaining gate for the positive-commutator proposal:

\[
\boxed{
\text{prove that the all-prime sewn source controls the negative }U_+
\text{ channel without fitting a projector.}
}
\]

If the sampled/sewn Green identity retains this indefinite norm difference
with no source-derived comparison between (U_+) and (U_-), the mechanism
does not prove the Schur property.

## Scope correction: the sheared norm line is sheet-dependent

The scale-dependent shear

\[
K_a=H_a-aqG
\]

does remove the Jordan coupling. It gives

\[
\partial_qK_a=-s_zK_a+g_a(q),
\qquad
g_a(q)=(aq-1)f(q),
\]

and therefore a positive-bulk Green identity with defects

\[
-\int_0^\infty g_a(q)^2\,dq
-K_a(0,z)\overline{K_a(0,w)}.
\]

However, the spectral-independent norm line does not cancel merely because
it is independent of (z,w). Clark reflection exchanges

\[
E_a=X+iaX'
\quad\longleftrightarrow\quad
E_a^*=E_{-a}=X-iaX'.
\]

The reflected forcing is

\[
g_{-a}(q)=(-aq-1)f(q),
\]

so on the positive tail chart

\[
\boxed{
\int_0^\infty
\left(g_a(q)^2-g_{-a}(q)^2\right)dq
=-4a\int_0^\infty qf(q)^2\,dq\ne0.
}
\]

Thus sheet antisymmetrization leaves a source-fixed first-moment line. It
would cancel only if the genuine reflected sewing simultaneously reverses
the oriented scale coordinate (q\mapsto-q), with the measure and source
orientation transported accordingly. That operation is not contained in the
one-sided tail flow and must be derived from the bilateral modular source.

The corrected sheared architecture on the positive chart is therefore

\[
\boxed{
\text{positive sheared bulk}
+\text{sampled arithmetic repair}
-\text{primitive seam form}
-\text{sheet-odd source-moment line}.
}
\]

This does not falsify the shear mechanism. It identifies its exact remaining
Beck--Chevalley/sewing test: construct the reflected tail chart and determine
whether orientation reversal kills the moment line or transports it into a
nonnegative boundary current. Treating spectral independence as cancellation
would skip that required map.

## Completed bilateral sewing does cancel the sheet-odd moment

After aggregating the arithmetic labels into the completed modular-even
source, the two scale charts may be placed on one oriented coordinate
(q\in\mathbb R), with

\[
f_{\rm bil}(q)=e^{-|q|/2}\Phi(|q|).
\]

This forcing is even. Consequently the sheet-odd norm difference is an odd
integral:

\[
\int_{\mathbb R}
\left[(aq-1)^2-(-aq-1)^2\right]f_{\rm bil}(q)^2\,dq
=-4a\int_{\mathbb R}qf_{\rm bil}(q)^2\,dq=0.
\]

Thus the correction above is resolved, but only at the completed bilateral
level. The cancellation is not available in either primitive one-sided chart.

Equivalently, let (H_a^+(z)) denote the right-half Clark feature. Evenness
of the completed source gives the exact sewing formula

\[
\boxed{
E_a(z)=H_a^+(z)+H_{-a}^+(-z).
}
\]

The reflected Clark sheet is

\[
E_{-a}(z)=H_{-a}^+(z)+H_a^+(-z).
\]

Therefore the two one-sided norm defects occur as the same sum
(c_a+c_{-a}) on both sheets and cancel in the de Branges antisymmetrization.
This proves the cancellation without pretending that (c_a=c_{-a}) on one
chart.

## The remaining object is the mixed sewing kernel

The bilateral formula also exposes an uncomputed term. Expanding

\[
E_a(z)\overline{E_a(w)}
-E_{-a}(z)\overline{E_{-a}(w)}
\]

contains:

1. two same-chart differences, controlled by the sheared positive Green
   identities; and
2. right--left cross terms such as
   \(H_a^+(z)\overline{H_{-a}^+(-w)}\).

The separate chart identities do not determine the sign of the second group.
For the underlying tail flows, their scale exponents add as

\[
s_z+\overline{s_{-w}}=1+i(z+\bar w),
\]

so their natural Green denominator involves (z+\bar w), whereas the de
Branges kernel requires (ar w-z). The conversion between these two
denominators is precisely the mixed modular-sewing map.

Hence the live theorem is no longer cancellation of the sheet-odd moment; it
is

\[
\boxed{
\text{derive the mixed right--left Green identity and show that its
cross terms are positive, exact, or absorbed by the primitive seam.}
}
\]

If a second independent indefinite polarization survives this mixed identity,
the arithmetic shear is insufficient. If it reduces to the declared primitive
seam, the positive-commutator architecture closes to one intrinsic defect.

## Iterated prime-power filtration

Iterating the recursion yields

\[
\Phi(u)=\sum_{j=0}^{J-1}p^{-j/2}
\Phi_{p\nmid}(u+j\ell)
+p^{-J/2}\Phi(u+J\ell).
\]

Superexponential decay removes the terminal term as (J\to\infty). Hence

\[
h_a(u)=\sum_{j\ge0}p^{-j/2}
\left[
h_{a,p\nmid}(u+j\ell)
+aj\ell\,\Phi_{p\nmid}(u+j\ell)
\right],
\]

where

\[
h_{a,p\nmid}(t)=(1-at)\Phi_{p\nmid}(t).
\]

Every depth (j>0) therefore carries a forced positive displacement term.
This is a filtration by (p)-adic valuation on the source labels, not a
chosen analytic decomposition.

## Sharp next test

The live question is whether the prime-recursive identity becomes a positive
Hardy-space or de Branges energy after bilateral modular sewing. A valid
construction must:

1. retain the labels (p\nmid n) and (v_p(n)=j);
2. include the (u=0) sewing current rather than extending the positive
   chamber by hand;
3. reproduce exactly the Clark denominator
   \(E_a(z)=\frac12\int_{\mathbb R}h_a(u)e^{izu}du\);
4. turn the displacement terms into a positive bulk or boundary form; and
5. leave no untyped primitive-prime signed remainder.

The sharp falsifier is a source-recursive positive even density satisfying
the same prime-translation identities and sewing law whose one-fold transform
still has an upper-half-plane zero. Until that class is excluded—or an exact
positive energy is derived—the recursion is a promising mechanism, not an RH
proof.

## Interpretation

The one-fold geometry identifies the defect but does not repair it. The
modular arithmetic labels add a canonical hierarchy of displaced copies, and
the displacement of the fold itself generates positive correction terms.
This is the closest current analogue of the prime-two pattern:

\[
\boxed{
\text{source-labelled defect}
+\text{scale transport}
\longrightarrow
\text{forced repair current}.
}
\]
