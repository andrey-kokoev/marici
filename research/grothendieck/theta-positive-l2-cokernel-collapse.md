# Positive semilocal L2 topology collapses the Xi cokernel

Author: marici.Grothendieck

## 1. The proposed descent

The Euler source orbit gives a nontrivial quotient in an entire-function
topology:

\[
 \mathcal E^+/\overline{\xi\,\mathbb C[w]},
 \qquad w=s(s-1).
\]

The tempting next step is to import the positive Hilbert norm of the
semilocal scaling representation and take the same quotient there. This
cannot work.

## 2. Dense-range theorem

Let \((X,\mu)\) be a measure space and let \(m\) be a measurable function
which is nonzero almost everywhere. Consider the maximal multiplication
operator \(M_m\) on \(L^2(X,\mu)\).

**Theorem.**

\[
 \overline{\operatorname{Ran}M_m}=L^2(X,\mu).
\]

Indeed,

\[
 (\operatorname{Ran}M_m)^\perp=\ker M_{\overline m}.
\]

Since \(m\ne0\) almost everywhere, this kernel is zero. Hence the Hilbert
cokernel of \(M_m\) is trivial.

Equivalently, for any \(f\in L^2\), the functions

\[
 f_n=f\,\mathbf1_{\{|m|\ge1/n\}}
\]

converge to \(f\), and each \(f_n=m(f_n/m)\) lies in the range.

## 3. Application to the completed zeta multiplier

On the real scaling axis, the completed function

\[
 \Xi(t)=\xi(\tfrac12+it)
\]

is real analytic and not identically zero. Its real zero set is discrete and
therefore Lebesgue-null. Every finite semilocal CCM measure is mutually
absolutely continuous with Lebesgue measure. Consequently,

\[
\boxed{
\overline{\Xi L^2(\mathbb R,dm_S)}
=L^2(\mathbb R,dm_S).}
\]

Thus

\[
 L^2(\mathbb R,dm_S)/
 \overline{\Xi L^2(\mathbb R,dm_S)}
=0.
\]

No ordinary positive semilocal \(L^2\) quotient can retain the discrete zero
modes. Enlarging the finite set of places changes the weight but not this
conclusion.

The same obstruction persists for any positive measure equivalent to
Lebesgue measure. A scalar reweighting cannot turn measure-zero evaluations
into Hilbert vectors.

## 4. Why the entire quotient survives

The CCM zero quotient uses a topology on entire functions, not the ambient
semilocal \(L^2\) topology. Point evaluation is continuous there. At a zero
\(\rho\),

\[
 (\Xi F)(\rho)=0,
\]

so evaluation descends to a nonzero cokernel functional.

This exposes the exact role of topology:

\[
\boxed{
\text{positive }L^2\text{ topology forgets discrete zeros;}
\qquad
\text{analytic topology remembers them}.}
\]

The desired RH space must carry both properties at once: continuous analytic
evaluation and a positive norm compatible with the quotient dynamics.

## 5. Consequence for the quarter-floor operator

The algebraic relation

\[
 B=-M_{s(s-1)}
\]

still descends on the analytic cokernel. But it cannot inherit
self-adjointness by ordinary Hilbert quotient from the positive ambient
scaling representation, because that quotient is zero.

Therefore any nontrivial Hilbert realization must use a new norm or boundary
completion. Natural candidates are a reproducing-kernel space, a de Branges
space, a graph-norm boundary space, or a Krein-to-Hilbert positive descent.
Proving positivity of the required analytic boundary norm is the
RH-strength step.

## 6. The defect is not finite rank

The mismatch between the positive semilocal space and the analytic zero
cokernel is not a finite collection of boundary channels. It is a change of
topological category:

\[
 L^2\text{ equivalence classes}
\quad\longrightarrow\quad
\text{analytic functions with continuous evaluation}.
\]

Point evaluation is unbounded on ordinary \(L^2\). No finite-rank correction
to its norm can make all complex evaluations continuous while retaining the
same completion. Hence the prime-two pattern of a positive bulk repaired by
finitely many channels does not transfer directly at this stage.

The more plausible analogue is a boundary triple or reproducing-kernel
dilation whose boundary space is infinite-dimensional from the start.

## 7. Deutsch--Popperian reformulation

**Analytic-boundary Hilbertization conjecture.** The adelic rational boundary
canonically supplies an analytic graph norm on the Euler-orbit cokernel such
that:

1. point evaluations are continuous;
2. the source image has a nontrivial closed cokernel;
3. \(B=-M_{s(s-1)}\) is essentially self-adjoint; and
4. \(B\ge1/4\).

The norm must be derived before zero locations. It must not be the semilocal
\(L^2\) norm plus a finite-rank adjustment, and it must not be defined by a
sum over the zero divisor.

The sharp falsifier is a proof that every source-authorized analytic graph
norm either makes the source image dense, loses positivity, or fails
invariance under \(M_{s(s-1)}\).

## 8. Next target

The immediate object is the boundary trace map omitted by \(L^2\):

\[
 \Gamma:\operatorname{Dom}T_{\max}\longrightarrow\mathcal B_{\mathrm{an}}.
\]

Derive it from rational-boundary summation and the maximal scaling generator,
then compute its Green form. The key question is whether the analytic
cokernel is a boundary space of a positive symmetric bulk operator, rather
than an imposed entire-function quotient.

## 9. Scope

The dense-range theorem and collapse of the ordinary semilocal Hilbert
cokernel are exact. They rule out direct inheritance of the positive
semilocal norm. They do not rule out a source-derived analytic boundary
Hilbert space, nor do they prove its positivity, self-adjointness, spectral
floor, or RH.
