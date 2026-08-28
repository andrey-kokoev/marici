# The Right-Sector Completion Obstruction Is Exactly the Primitive-Prime Current

## Euler-grade separation

For a finite prime cutoff \(X\), write

\[
\log E_X(s)
=
P_X(s)+H_{2,X}(s),
\]

where

\[
P_X(s)=\sum_{p\le X}p^{-s}
\]

is the primitive-prime current and

\[
H_{2,X}(s)
=
\sum_{p\le X}\sum_{k\ge2}\frac{p^{-ks}}{k}
\]

contains the square and all higher cyclic returns.

Let

\[
D_+=\{s:1/2<\Re s<1\}.
\]

On every compact \(K\subset D_+\), choose
\(\sigma_K>1/2\) with \(\Re s\ge\sigma_K\) on \(K\). Then

\[
\sum_p\sum_{k\ge2}\frac{|p^{-ks}|}{k}
\le
\sum_p\frac{p^{-2\sigma_K}}{1-p^{-\sigma_K}},
\]

and the right side converges. Therefore \(H_{2,X}\) converges locally
uniformly on \(D_+\) to a holomorphic function \(H_2\). Its exponential is
a nowhere-zero holomorphic unit.

Thus every square, higher prime power, and connected determinant return is
already strictly complete in the right sector. Only \(P_X\) can obstruct
normal completion there.

## Prime-zeta continuation carries the divisor

In \(\Re s>1\), the prime zeta function

\[
P(s)=\sum_p p^{-s}
\]

satisfies

\[
\log\zeta(s)=P(s)+H_2(s).
\]

Equivalently, Möbius inversion gives

\[
P(s)
=
\sum_{m\ge1}\frac{\mu(m)}{m}\log\zeta(ms).
\]

For \(s\in D_+\) and every \(m\ge2\), one has \(\Re(ms)>1\).
Consequently \(\zeta(ms)\) is holomorphic and nowhere zero, and all
\(m\ge2\) logarithmic terms admit unambiguous holomorphic branches on
\(D_+\). The only possible branch obstruction is the \(m=1\) term
\(\log\zeta(s)\).

Because \(D_+\) is simply connected, \(\log\zeta\) has a holomorphic
branch there exactly when \(\zeta\) is nowhere zero there. Hence:

> The primitive-prime current admits a holomorphic right-sector branch
> compatible with the Euler identity exactly when the right sector is
> zero-free.

Reciprocal functional symmetry transfers the same statement to the left
sector. Subject to the standard critical-strip localization, this branch
existence is equivalent to RH.

## Relation to strict completion

The Hurwitz programme can now be factored:

\[
E_X(s)
=
\exp(P_X(s))\exp(H_{2,X}(s)).
\]

The second factor already converges locally uniformly to a unit on \(D_+\).
Therefore every source-derived unit renormalization needed for strict
completion can be concentrated on \(\exp(P_X)\). No additional square,
higher-depth, or mixed prime-power port can repair the remaining obstruction;
those grades are already normal.

## Circular and noncircular constructions

Defining

\[
P_+(s)=\log\zeta(s)-H_2(s)
\]

after assuming zero-freeness merely restates the desired branch and is
circular. Likewise, using the Möbius formula with a chosen branch of
\(\log\zeta(s)\) imports the divisor.

The noncircular target is narrower:

1. construct a renormalized primitive current from labelled prime incidence
   and the theta boundary data;
2. prove that its exponential is a holomorphic unit on \(D_+\);
3. prove agreement with \(\exp(P_X)\) in the Euler chamber through a
   source-derived continuation law;
4. obtain the left-sector unit by reciprocal sewing.

Hurwitz then supplies zero confinement without another positivity theorem.

## Meaning

The distributional \(k=1\) current is not merely the first troublesome term
in a long list. It is the unique carrier of the right-sector divisor
obstruction. The \(k=2\) threshold matters for determinant regularity, but
not for zero creation once \(\Re s>1/2\).

This explains why repeated attempts to combine primitive and square channels
produced exact or nonfaithful structures: the square channel renormalizes
volume, while only the primitive channel can fail strict invertible descent
in the RH sector.

## Falsifier

Any proposed primitive-current construction fails if it:

- uses \(\log\zeta(s)\) or its zeros to choose a branch;
- is not a unit on all compact subsets of \(D_+\);
- depends on prime exhaustion;
- disagrees with \(\sum_p p^{-s}\) in \(\Re s>1\);
- or needs an independently added \(k\ge2\) repair after \(H_2\) has been
  retained.

