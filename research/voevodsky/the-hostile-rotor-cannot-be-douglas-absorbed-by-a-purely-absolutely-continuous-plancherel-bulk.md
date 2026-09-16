# The hostile rotor cannot be Douglas-absorbed by a purely absolutely continuous Plancherel bulk

## Objective

Test the decisive physical gate

\[
b_\gamma b_\gamma^*
\preceq
C
\]

when \(C\) is supplied only by an absolutely continuous real-axis Plancherel bulk and \(b_\gamma\) is the hostile boundary-evaluation row.

The result is negative. An atomic rotor cannot be Douglas-dominated by a bare absolutely continuous \(L^2\) form.

## Bare bulk

Let

\[
C_w(f,f)
=
\int_{\mathbb R}
w(t)
|f(t)|^2
\,dt,
\]

where \(w\ge0\) is locally integrable and has no atom at \(\gamma\).

Assume, locally near \(\gamma\), that

\[
\int_{
\gamma-\varepsilon
}^{
\gamma+\varepsilon
}
w(t)
\,dt
\longrightarrow
0
\]

as \(\varepsilon\downarrow0\). This holds for every locally integrable density.

Define the point-evaluation row

\[
b_\gamma(f)
=
f(\gamma)
\]

on the Schwartz test core.

## Concentrating test sequence

Choose \(\psi\in C_c^\infty(\mathbb R)\) with

\[
\psi(0)=1
\]

and support in \([-1,1]\). Set

\[
f_\varepsilon(t)
=
\psi
\left(
\frac{t-\gamma}{\varepsilon}
\right).
\]

Then

\[
b_\gamma(f_\varepsilon)
=1
\]

for every \(\varepsilon>0\), while

\[
C_w(f_\varepsilon,f_\varepsilon)
\le
\|\psi\|_\infty^2
\int_{
\gamma-\varepsilon
}^{
\gamma+\varepsilon
}
w(t)
\,dt
\longrightarrow
0.
\]

Therefore no finite constant \(M\) can satisfy

\[
|f(\gamma)|^2
\le
M
C_w(f,f)
\]

on the Schwartz core.

In particular,

\[
\boxed{
b_\gamma b_\gamma^*
\npreceq
C_w.
}
\]

## Symmetry-completed rotor

For

\[
b_{\pm\gamma}(f)
=
\begin{pmatrix}
f(\gamma)\\
f(-\gamma)
\end{pmatrix},
\]

the rotor norm is

\[
\|b_{\pm\gamma}(f)\|^2
=
|f(\gamma)|^2
+
|f(-\gamma)|^2.
\]

A test sequence concentrating at either point proves

\[
\boxed{
b_{\pm\gamma}b_{\pm\gamma}^*
\npreceq
C_w.
}
\]

Thus dagger pairing of the two atoms does not repair the failure.

## Douglas consequence

Douglas factorization would require a contraction \(c_\gamma\) with

\[
b_\gamma
=
C_w^{1/2}c_\gamma.
\]

The concentrating sequence proves that no such bounded factorization exists.

Hence a physical common bulk whose graph norm is equivalent only to an absolutely continuous weighted \(L^2\) norm cannot absorb the hostile rotor.

## Von Neumann-algebra formulation

In the regular spectral representation,

\[
U(h)
\longleftrightarrow
M_{\widehat h}
\]

on \(L^2(\mathbb R,dt)\). The generated commutative von Neumann algebra is

\[
L^\infty(\mathbb R,dt).
\]

Every normal positive functional on this algebra has the form

\[
F_\rho(M_\phi)
=
\int
\phi(t)
\rho(t)
\,dt
\]

for some \(\rho\in L^1_+\).

Point evaluation

\[
M_\phi
\longmapsto
\phi(\gamma)
\]

is not even well-defined on arbitrary Lebesgue equivalence classes and is singular relative to the regular representation. Consequently there is no trace-class operator \(T_\gamma\) on ambient \(L^2\) such that

\[
\operatorname{Tr}
(T_\gamma M_\phi)
=
\phi(\gamma)
\]

for every admitted multiplier.

This operator-algebraic singularity is the global version of the concentrating-sequence obstruction.

## Why finite windows do not contradict the theorem

On \(PW_L\), point evaluation is bounded and represented by

\[
k_{\gamma,L}.
\]

The associated rank-one operator is trace class, but

\[
\|k_{\gamma,L}\|^2
=
\frac L\pi
\longrightarrow
\infty.
\]

Thus finite-window representability is compatible with failure of an ambient bounded row. The diverging reproducing-kernel norm is exactly the Douglas leverage constant escaping to infinity.

## Minimal ways to reopen the gate

The negative theorem leaves three genuine possibilities.

### Add atomic spectral mass

Replace the measure by

\[
w(t)dt
+
\alpha_\gamma
\delta_\gamma
+
\alpha_{-\gamma}
\delta_{-\gamma},
\qquad
\alpha_{\pm\gamma}>0.
\]

Then

\[
|f(\gamma)|^2
\le
\alpha_\gamma^{-1}
\|f\|^2_{L^2(wdt+\alpha_\gamma\delta_\gamma)}.
\]

This is the discrete rotor-sector completion. Its atomic masses require physical justification.

### Strengthen the bulk graph norm

Use a Sobolev or reproducing-kernel graph bulk \(C_{graph}\) for which evaluation is continuous. In one real dimension, a local \(H^s\) norm with

\[
s>
\frac12
\]

controls point evaluation.

One must then prove that this stronger norm is supplied by the actual Green/cutoff operator rather than imposed externally.

### Retain finite resolution

Keep \(L<\infty\). The rotor is then bounded and trace class, but the resulting theorem is regulator-dependent and does not survive unrenormalized cutoff removal.

## Tetrahedral consequence

The ordinary \(H_{234}\) Plancherel bulk cannot be the desired rotor absorber. The terminal horn cannot be filled positively by using only the existing absolutely continuous volume row.

A positive filler must contain one of:

1. an atomic geometric rotor sector;
2. a graph-regularity row of order greater than one half;
3. a permanently finite-resolution carrier.

Therefore faithful horn recovery determines the signed rotor functional, but positivity forces an enlargement of the analytic type of vertex \(V_2\) or of the common bulk.

## Refined open theorem

The physical question is no longer whether the bare Plancherel bulk happens to dominate the rotor. It cannot.

The correct question is

\[
\boxed{
\text{Does the physical Green/prolate geometry naturally generate atomic spectral mass or more than one-half derivative of boundary control?}
}
\]

Only such a mechanism can produce the required Douglas contraction.

## Relation to the fixed endpoint channel

The same principle explains why off-real endpoint evaluation is unbounded on bare boundary \(L^2\). The fixed endpoint graph and the moving real-boundary rotor both require graph enhancement, but they are different rows:

1. the endpoint row is off-real analytic evaluation and has exponential finite-window growth;
2. the rotor row is real-boundary evaluation and has linear finite-window growth.

They cannot be merged merely because both are singular relative to ambient \(L^2\).

## Disposition

The principal Douglas gate is closed negatively for every purely absolutely continuous Plancherel bulk:

\[
\boxed{
\text{atomic rotor}
\not\preceq
\text{bare absolutely continuous bulk}.
}
\]

Any successful physical absorption theorem must exhibit an actual atomic sector or a stronger graph norm. This requirement is structural, not a missing estimate within the existing \(L^2\) model.
