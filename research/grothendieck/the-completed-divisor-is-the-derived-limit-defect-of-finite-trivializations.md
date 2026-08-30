# The Completed Divisor Is the Derived-Limit Defect of Finite Trivializations

## Finite coherence cannot by itself survive completion

For every finite prime set $X$, the Euler section

$$
E_X(s)=\prod_{p\in X}(1-p^{-s})^{-1}
$$

is holomorphic and nonvanishing throughout $\operatorname{Re}s>0$. Its
primitive, square, and third-order determinant components are normalized at
$+\infty$ and have exact identity holonomy under every prime-addition square.

Suppose these normalized sections converged locally uniformly on a domain
$U\subset\{\operatorname{Re}s>1/2\}$ to a nonzero holomorphic section $E$.
Hurwitz's theorem would force $E$ to remain zero-free on $U$.

Therefore an off-seam zero of the completed section can arise only because at
least one of the following fails:

- the finite sections converge locally uniformly;
- their normalized trivializations remain invertible;
- the completion map preserves the finite determinant line;
- the regularized logarithmic connections converge uniformly on loops;
- the boundary-current subtraction is a single-valued holomorphic operation.

This is not an incidental analytic defect. It is the only place where the
divisor can be born.

## The completion anomaly

Let

$$
\omega_X=d\log E_X
$$

be the exact finite logarithmic connection. Every finite loop has zero
holonomy. The completed logarithmic connection is

$$
\omega_{\mathrm{comp}}=d\log\Xi_{\mathrm{framed}}
$$

where defined. The difference

$$
\mathfrak A
=\omega_{\mathrm{comp}}-\operatorname*{reglim}_X\omega_X
$$

is the completion anomaly. Around a loop $\gamma$ avoiding poles,

$$
\frac1{2\pi i}\oint_\gamma\mathfrak A
$$

is exactly the divisor created by completion, because every finite connection
has trivial period.

Equivalently, the compatible finite trivializations form a projective system
whose ordinary limit need not remain invertible. The obstruction to choosing
one completed trivialization is a derived-limit class. This is the determinant
line version of the earlier acyclic-complex hostile

$$
\mathbb C\xrightarrow{\varepsilon_X}\mathbb C,
\qquad \varepsilon_X\to0:
$$

every finite stage is invertible, while the limiting inverse escapes to
infinite norm and a kernel appears.

## Meaning for RH

The primitive-current result identifies the anomaly exactly in the open right
sector: its integer periods count off-seam zeta zeros. Reciprocal sewing gives
the left-sector copy. Hence RH is equivalent to the statement that the
completion anomaly has no integer period in either open sector after the
known pole carrier is removed.

This is more precise than saying that completion must be exact. The required
property is:

> The normalized prime trivializations are completion-stable on every compact
> loop contained in an open reciprocal sector.

A sufficient analytic certificate would be uniform convergence of the
regularized logarithmic connections on such loops, together with uniform
control of their primitive and square boundary coordinates. But proving that
certificate directly from $\zeta'/\zeta$ would be circular.

## Source-level target

The theta/Tate construction must supply an independent contraction or
conservation law showing that the completion anomaly is supported only on the
common seam. In the three-tower language:

1. the finite arithmetic tower has identity holonomy;
2. the spectral tower has a self-adjoint real boundary;
3. the comparison tower must prove that its derived-limit defect is carried
   only by that boundary.

This is the exact point where the operator and arithmetic programmes meet.
The self-adjoint operator does not need to reproduce ordinary finite Euler
divisors. It must realize the derived-limit defect of their normalized
trivializations as its boundary index.

## Falsifier

Construct a source-admissible compact loop wholly inside an open half-sector
and a normalized sequence of finite trivializations whose inverse norms
diverge along that loop. If the divergence survives every primitive, square,
det3, seam, and archimedean control seminorm, then the comparison tower can
acquire off-seam index and the proposed completion-stability theorem fails.

Conversely, a uniform graph-norm bound on the completed trivializations over
each compact loop would kill the derived-limit class and exclude off-seam
zeros. That bound, not finite holonomy, is the next genuine theorem.
