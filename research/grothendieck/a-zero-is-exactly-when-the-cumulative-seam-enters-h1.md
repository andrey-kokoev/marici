# A Zero Is Exactly When the Cumulative Seam Enters H1

## Cumulative seam profile

Let the decaying source be (A(y)), with transform at a fixed spectral parameter written as

\[
F=\int_0^\infty A(y)\,dy.
\]

Define the cumulative seam profile

\[
B(L)=\int_0^L A(y)\,dy
=
F-G(L),
\qquad
G(L)=\int_L^\infty A(y)\,dy.
\]

Assume (A\in L^2(0,\infty)), (G\in L^2(0,\infty)), and (G(L)\to0). These conditions hold for the rapidly decaying theta-tail source at each fixed parameter in its admitted domain.

Since (B'=A), the only obstruction to (B\in H^1(0,\infty)) is its nonzero asymptotic constant. Therefore

\[
B\in H^1(0,\infty)
\quad\Longleftrightarrow\quad
F=0.
\]

A scalar zero is thus exactly the event where the expanding seam profile changes from an affine boundary state with a constant mode into an ordinary finite-energy graph state.

## Logarithmic prime sampling theorem

The primitive prime port samples the seam at (L=\log p) with Hilbert amplitude (p^{-1/2}B(\log p)). For every (b\in H^1(0,\infty)),

\[
\sum_p\frac{|b(\log p)|^2}{p}
\le
3\|b\|_{H^1(0,\infty)}^2.
\]

The proof does not require prime-gap information. Enlarge the sum to all integers (n\ge2), put (x_n=\log n), and let (\Delta_n=x_{n+1}-x_n). Then

\[
\frac{1}{n}\le\frac32\Delta_n,
\qquad
\Delta_n<1.
\]

The one-dimensional trace estimate on each cell gives

\[
\Delta_n|b(x_n)|^2
\le
2\int_{x_n}^{x_{n+1}}|b|^2
+
2\Delta_n^2\int_{x_n}^{x_{n+1}}|b'|^2.
\]

Summing the disjoint cells proves the bound.

Consequently, at a scalar zero the primitive sampled seam is automatically a Hilbert vector. Away from a zero, (B(\log p)\to F\ne0), and

\[
\sum_p\frac{|B(\log p)|^2}{p}
\]

diverges with the prime harmonic series.

## What this explains

The earlier statement that a zero upgrades the primitive current's completion class now has an exact geometric mechanism:

1. expanding seams accumulate toward the full transform;
2. a nonzero transform leaves a constant boundary mode;
3. that mode is outside (H^1) and produces primitive divergence;
4. a zero removes the constant mode;
5. the remaining tail profile lies in (H^1), where logarithmic prime sampling is bounded.

The primitive current is therefore not intrinsically distributional. Its regularity depends on whether the cumulative seam carries the constant transform mode.

## Scope boundary

This theorem characterizes every scalar zero; it does not confine zeros to the critical seam. The RH-bearing statement must still explain why the (H^1) class upgrade is compatible with both reciprocal sector orientations only when (Re s=1/2).

The prime-square determinant current also remains separate. Its Hilbert sampling can converge even with a constant mode, while its scalar coefficient sum is not trace class. Hilbert regularity and determinant regularity must not be conflated.

## Next theorem

Apply reciprocal Fourier–Tate sewing to the two cumulative seam profiles (B_+) and (B_-). Determine whether simultaneous (H^1) admission and source-adjoint interface matching force the two affine origins to meet only on the unitary seam.

## Verification

The dependency-free checker `research/grothendieck/checkers/primitive_log_prime_h1_sampling.py` verifies the logarithmic-mesh constants through 200,000 cells and the divergent constant-profile witness. The sampling inequality itself is proved above cell by cell.
