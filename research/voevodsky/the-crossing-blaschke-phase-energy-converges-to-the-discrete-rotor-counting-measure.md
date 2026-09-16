# The crossing Blaschke phase energy converges to the discrete rotor counting measure

## Key observation

The ordinary Plancherel bulk and the observer sewing form do not control point evaluation. However, the local phase-energy construction attached to the crossing factor itself has a different limit: its positive density becomes a delta measure.

Thus the discrete rotor sector need not be inserted arbitrarily. It is the singular limit of the positive Hardy phase-energy row of the crossing divisor.

## One crossing factor

Fix \(a\ne0\) and define the unimodular boundary phase

\[
\gamma_a(t)
=
\frac{
t-ia
}
{
t+ia
}.
\]

Changing \(a\) to \(-a\) reverses the phase orientation but leaves its positive phase energy unchanged.

The local phase-energy density is

\[
\kappa_a(t)
=
\frac1{4\pi^2}
\int_{\mathbb R}
\frac{
|\gamma_a(s)-
\gamma_a(t)|^2
}
{
|s-t|^2
}
\,ds.
\]

## Exact computation

One has

\[
\gamma_a(s)-
\gamma_a(t)
=
\frac{
2ia(s-t)
}
{
(s+ia)(t+ia)
}.
\]

Therefore

\[
\frac{
|\gamma_a(s)-
\gamma_a(t)|^2
}
{
|s-t|^2
}
=
\frac{
4a^2
}
{
(s^2+a^2)(t^2+a^2)
}.
\]

Using

\[
\int_{\mathbb R}
\frac{ds}{s^2+a^2}
=
\frac\pi{|a|},
\]

we obtain

\[
\boxed{
\kappa_a(t)
=
\frac1\pi
\frac{|a|}{t^2+a^2}.
}
\]

Thus the positive phase-energy density is exactly the normalized Poisson kernel.

In particular,

\[
\int_{\mathbb R}
\kappa_a(t)
\,dt
=1.
\]

## Atomic limit

As \(a\to0\),

\[
\kappa_a(t)
\,dt
\longrightarrow
\delta_0
\]

strongly in the Schwartz dual and weakly as probability measures.

For every Mellin--Schwartz observer \(m\),

\[
\boxed{
\lim_{a\to0}
\int
\kappa_a(t)
|m(t)|^2
\,dt
=
|m(0)|^2.
}
\]

This is precisely the positive Gram of the discrete character line at the crossing point.

## Translated crossing

For a divisor crossing at \(t=\gamma\), replace \(t\) by \(t-\gamma\):

\[
\kappa_{a,\gamma}(t)
=
\frac1\pi
\frac{|a|}{(t-\gamma)^2+a^2}.
\]

Then

\[
\kappa_{a,\gamma}(t)
\,dt
\longrightarrow
\delta_\gamma,
\]

and

\[
\lim_{a\to0}
\int
\kappa_{a,\gamma}(t)
|m(t)|^2dt
=
|m(\gamma)|^2.
\]

## Symmetry-completed rotor

For the paired crossings at \(\gamma\) and \(-\gamma\), use the strict local direct-sum phase feature

\[
D_{a,\gamma}^{rot}
=
D_{a,+\gamma}
\oplus
D_{a,-\gamma}.
\]

Its positive Gram density is

\[
\kappa_{a,+\gamma}(t)
+
\kappa_{a,-\gamma}(t).
\]

Therefore

\[
\boxed{
(
\kappa_{a,+\gamma}
+
\kappa_{a,-\gamma}
)
dt
\longrightarrow
\delta_\gamma
+
\delta_{-\gamma}.
}
\]

For source observers,

\[
\lim_{a\to0}
\|D_{a,\gamma}^{rot}M_m\|_2^2
=
|m(\gamma)|^2
+
|m(-\gamma)|^2
\]

up to the fixed Hadamard normalization already declared for local difference rows.

This is exactly the counting-norm Gram of the discrete rotor plane

\[
\mathbb C_\gamma
\oplus
\mathbb C_{-\gamma}.
\]

## Orientation and positivity separate

The signed phase current is

\[
\nu_{a,\gamma}(t)
=
-
\operatorname{sgn}(a)
\kappa_{a,\gamma}(t)
\]

for the normalized one-factor convention.

Hence its one-sided limits are

\[
\nu_{0^-}
=+
\delta_\gamma,
\qquad
\nu_{0^+}
=-
\delta_\gamma.
\]

By contrast, the positive phase energy satisfies

\[
\kappa_{0^-}
=
\kappa_{0^+}
=
\delta_\gamma.
\]

Therefore:

1. \(\kappa\) supplies the unoriented rotor norm;
2. \(\nu\) supplies crossing orientation;
3. the cumulative index cycle supplies affine clutching.

These are three related but noninterchangeable coordinates.

## Resolution of the trace-weight puzzle

The finite Paley--Wiener evaluation operator has trace norm proportional to \(L\) because it represents a delta functional inside the continuous Plancherel carrier.

The phase-energy measure instead satisfies

\[
\int
\kappa_{a,\gamma}(t)dt
=1
\]

at every \(a\ne0\). Its limit carries unit atomic mass without division by \(L\).

Thus the discrete counting trace is inherited canonically from conservation of phase-energy mass:

\[
\boxed{
\text{one simple crossing factor}
\longmapsto
\text{one unit rotor line}.
}
\]

For the symmetry-completed pair, the total mass is two.

This explains the counting normalization without artificially rescaling the Paley--Wiener rank-one operator.

## Multiplicity

A multiplicity-\(m\) crossing should be represented by the strict telescoping/direct sum of \(m\) elementary divisor factors. Each elementary factor contributes one unit phase-energy line.

The limiting rotor space is therefore

\[
\mathbb C^m_{\gamma}
\]

for one crossing center and

\[
\mathbb C^m_{\gamma}
\oplus
\mathbb C^m_{-\gamma}
\]

for its symmetry completion.

Using the phase \(\gamma_a^m\) as one unsplit row can hide this multiplicity in nonlinear cross terms. The strict local-energy construction avoids that ambiguity by retaining the elementary factors before summation.

## Hilbert-space convergence

Define the crossing energy form

\[
q_{a,\gamma}(m)
=
\int
\kappa_{a,\gamma}(t)
|m(t)|^2dt.
\]

On the Schwartz source core,

\[
q_{a,\gamma}(m)
\longrightarrow
q_{0,\gamma}(m)
:=
|m(\gamma)|^2.
\]

For the symmetry pair,

\[
q_{a,\pm\gamma}(m)
\longrightarrow
|m(\gamma)|^2
+
|m(-\gamma)|^2.
\]

This is convergence of positive quadratic forms on the common test core. A full Mosco theorem requires placing the varying \(L^2(\kappa_a dt)\) spaces in a common ambient measure or using a continuous field of Hilbert spaces. That packaging remains to be written, but the source-form limit is exact.

## Tetrahedral placement

The positive phase-energy row belongs to the source--spectral face \(H_{123}\) and its local Hardy realization. At the crossing stratum, its limiting target acquires the rotor fiber

\[
\mathcal R_\gamma
=
\mathbb C_\gamma
\oplus
\mathbb C_{-\gamma}.
\]

The signed current on \(H_{134}\) and the positive rotor norm on \(H_{123}\) are generated by the same elementary crossing factors.

The remaining \(H_{234}\) problem is therefore narrower: transport this canonically generated phase-energy rotor into the physical cutoff geometry. Its norm and counting weight are no longer arbitrary.

## Consequence for the Douglas gate

The earlier no-go theorem remains valid for the background absolutely continuous bulk. The new point is that the crossing factor itself generates an atomic positive bulk in the limit:

\[
C_{cross,a}
=
M_{
\kappa_{a,+\gamma}
+
\kappa_{a,-\gamma}
}
\longrightarrow
C_{cross,0}^{rot}.
\]

On the limiting rotor fiber,

\[
b_{\pm\gamma}
b_{\pm\gamma}^*
=
C_{cross,0}^{rot}
\]

with unit leverage. Thus the hostile rotor is exactly dominated by its own phase-energy completion.

What is not yet proved is that the physical \(C_{24}\) geometry contains this crossing phase-energy row rather than only its background Plancherel and critical sewing rows.

## Open gate

Construct a geometric transition

\[
J_{a,\gamma}^{phys}:
D_{a,\gamma}^{rot}
\longrightarrow
\mathcal H_{geom,a}
\]

that:

1. is isometric or contractive in the phase-energy norm;
2. respects dagger and the \(\pm\gamma\) pairing;
3. converges to the discrete rotor inclusion at \(a=0\);
4. intertwines the affine index clutching;
5. is natural under admitted source successors.

This is now the single physical transport problem for the hostile fixture.

## Disposition

The crossing factor itself canonically produces the missing atomic rotor mass:

\[
\boxed{
\kappa_{a,\gamma}(t)dt
\to
\delta_\gamma.
}
\]

Therefore the discrete rotor counting measure is analytically derived, not appended by hand. The remaining task is to identify this positive Hardy phase-energy line with a genuine geometric cutoff defect line.
