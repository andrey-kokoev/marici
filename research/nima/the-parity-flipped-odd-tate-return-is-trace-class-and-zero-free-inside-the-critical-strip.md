# The parity-flipped odd Tate return is trace class and zero-free inside the critical strip

## Conductor-one local packet

Fix an odd prime and take

\[
\eta=p^{-1}u,
\qquad
h=u^{-1},
\]

so that

\[
\eta h=p^{-1}.
\]

Let

\[
f_\eta^{\mathrm{odd}}
=
\frac{f_\eta-f_{-\eta}}{2i},
\qquad
f_\eta^{\mathrm{even}}
=
\frac{f_\eta+f_{-\eta}}2.
\]

The canonical finite difference satisfies

\[
P_\eta f_\eta^{\mathrm{odd}}
=
2\sin\left(\frac{2\pi}{p}\right)
f_\eta^{\mathrm{even}}.
\]

## Multiplicative Tate observation

Opposite character twists have equal local Tate integrals, so

\[
Z_p(f_\eta^{\mathrm{even}},s)
=
Z_p(f_\eta,s).
\]

For conductor one,

\[
Z_p(f_\eta,s)
=
\frac{p^{-s}}{1-p^{-s}}
-
\frac1{p-1}.
\]

Therefore the parity-flipped odd return observed by the local Tate port is

\[
c_p(s)
=
2\sin\left(\frac{2\pi}{p}\right)
\left(
\frac{p^{-s}}{1-p^{-s}}
-
\frac1{p-1}
\right).
\]

This is the first explicit nonzero scalar shadow of the odd-to-even mixed return.

## Relative form

Since

\[
Z_p(f_0,s)=\frac1{1-p^{-s}},
\]

we have

\[
\frac{c_p(s)}{Z_p(f_0,s)}
=
2\sin\left(\frac{2\pi}{p}\right)
\frac{p^{1-s}-1}{p-1}.
\]

The odd return is therefore a source-derived ramified relative factor multiplied by the canonical parity coefficient.

## Zero locus

The sine coefficient is nonzero for odd \(p\). The remaining factor vanishes exactly when

\[
p^{1-s}=1.
\]

Thus

\[
s
=
1-\frac{2\pi i n}{\log p},
\qquad
n\in\mathbb Z.
\]

All local zeros lie on

\[
\operatorname{Re}s=1.
\]

Consequently

\[
c_p(s)\ne0
\]

throughout the open critical strip

\[
0<\operatorname{Re}s<1.
\]

The parity-flipped port imports no local zero into the interior of the strip.

## All-prime trace-class bound

Fix a compact set \(C\) with

\[
\operatorname{Re}s\ge\varepsilon>0.
\]

Then

\[
|1-p^{-s}|
\ge
1-p^{-\varepsilon}.
\]

Using

\[
2\left|\sin\left(\frac{2\pi}{p}\right)\right|
\le
\frac{4\pi}{p},
\]

we obtain, uniformly on \(C\),

\[
|c_p(s)|
\le
\frac{4\pi}{p}
\left(
\frac{p^{-\varepsilon}}{1-p^{-\varepsilon}}
+
\frac1{p-1}
\right).
\]

For all sufficiently large primes,

\[
|c_p(s)|
\le
C_\varepsilon
\left(
p^{-1-\varepsilon}
+
p^{-2}
\right).
\]

Hence

\[
\sum_p\sup_{s\in C}|c_p(s)|<\infty.
\]

The all-prime diagonal mixed-return family

\[
C_{\mathrm{odd}}(s)e_p=c_p(s)e_p
\]

is trace class and analytic, locally uniformly throughout \(\operatorname{Re}s>0\).

## Determinant consequence

The Fredholm determinant

\[
\det(I+\lambda C_{\mathrm{odd}}(s))
\]

is well-defined and analytic on the right open half-plane for fixed \(\lambda\).

This determinant is an auxiliary odd-return determinant, not the completed zeta determinant. Its source role is to orient a boundary block without adding critical-strip local divisors.

## Boundary behavior

The local return vanishes on \(\operatorname{Re}s=1\), including at \(s=1\). Therefore no estimate can demand a uniform inverse through that boundary.

On compact subsets strictly inside

\[
0<\operatorname{Re}s<1,
\]

every local coefficient is nonzero, but the all-prime minimum modulus still vanishes because \(c_p(s)\to0\).

Thus:

- local zero-freeness holds;
- trace-class completion holds;
- global Hilbert coercivity still fails.

## Operator qualification

The scalar calculation uses the local Tate observer after the parity-changing incidence. It proves that one explicit mixed boundary functional is nonzero.

It does not yet prove that the complete wall–jump Green observer equals this Tate functional or that the corresponding operator block is minimal.

The required source square is

\[
\text{odd character port}
\xrightarrow{P_\eta}
\text{even ramified port}
\xrightarrow{\text{Tate/Green comparison}}
\text{wall–jump boundary}.
\]

The second arrow remains to be identified at operator level.

## Hostiles

1. Attribute the local \(\operatorname{Re}s=1\) zeros to the completed zeta section.
2. infer an all-prime lower frame from local zero-freeness.
3. call the auxiliary Fredholm determinant the \(\Xi\) determinant.
4. omit the subtraction \(1/(p-1)\) in the ramified local integral.
5. identify the Tate observer with the Green wall observer without an intertwining theorem.

## Verdict

The canonical parity flip converts the divisor-free odd port into an even ramified port whose Tate return is explicit, nonzero throughout the open critical strip, and trace class after all-prime assembly.

This closes the scalar mixed-return existence and completion gates. The remaining step is the operator-level Tate-to-Green wall comparison.
