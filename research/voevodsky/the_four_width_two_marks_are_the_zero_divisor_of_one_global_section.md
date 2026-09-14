# The four width-two marks are the zero divisor of one global section

Restrict the first total-energy smoothing coefficient to the conductor conic and use its rational parameter \(m\). The exact factorization is

\[
\left.\partial_EG_E\right|_{E=0,\mathcal C}
=
32x^3y^3(x+y)
\left[
\frac{m(m+1)(x-my)}{(m^2y+x)^2}
\right]^2.
\]

Define

\[
g(m)=\frac{m(m+1)(x-my)}{(m^2y+x)^2}.
\]

Then

\[
\left.\partial_EG_E\right|_{\mathcal C}
=U\,g(m)^2,
\qquad
U=32x^3y^3(x+y).
\]

The zeros of \(g\) are precisely

\[
\begin{array}{c|c}
p_{-+}&m=0\\
p_{++}&m=-1\\
p_{--}&m=x/y\\
p_{+-}&m=\infty.
\end{array}
\]

Each is simple for \(g\), hence double for the smoothing section. Therefore the four local models \(XY=Es^2\) are restrictions of one global square-root datum; they are not four independent local choices.

After the quadratic base change \(E=\varepsilon^2\), the first-order normalization separates schematically as

\[
Q\pm \varepsilon\sqrt{-U}\,g(m).
\]

Thus the integral gluing information is encoded by how the sign of this single section is continued across the four zeros. This is exactly the sort of global datum absent from pointwise residues and permutation shadows.

The next calculation is now a concrete Čech problem on the marked conductor \(\mathbb P^1\): cover the four complementary intervals/arcs, choose the two normalized branches \(Q\pm\varepsilon\sqrt{-U}g\), and compute their sign transitions across consecutive zeros. The resulting cocycle is the candidate specialization map into the integral kernel.

Certificate:

- `research/voevodsky/checkers/square_root_smoothing_section_on_conductor.py`;
- `research/voevodsky/results/conductor_smoothing_square_root.json`.
