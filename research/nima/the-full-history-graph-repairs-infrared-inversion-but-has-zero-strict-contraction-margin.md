# The full history graph repairs infrared inversion but has zero strict contraction margin

## Scope

Retaining the (L^2) mass in the history graph repairs the zero-frequency failure of the derivative energy. It does not, by itself, produce the strict contraction margin required by the enlarged Adams cell.

Let

[
mathsf D:H^1_{mathrm{even}}(mathbb R)	o L^2_{mathrm{odd}}(mathbb R)
]

be the closed derivative and define the history metric

[
G=I+mathsf D^*mathsf D.
]

## Infrared repair

The form inequality

[
Gge I
]

gives a bounded inverse

[
|G^{-1}|le1.
]

Thus the graph metric controls both the state and its derivative:

[
|f|_G^2=|f|_2^2+|mathsf Df|_2^2.
]

This removes the infrared defect of attempting to invert (mathsf D^*mathsf D) alone. In particular, one-dimensional endpoint traces are continuous in the graph norm.

## Normalized derivative loading

The canonical normalized derivative incidence is

[
K=mathsf D,G^{-1/2}.
]

Functional calculus gives

[
K^*K
=
rac{mathsf D^*mathsf D}
{I+mathsf D^*mathsf D}.
]

Hence (K) is contractive:

[
|K|le1.
]

However, the derivative Laplacian has unbounded spectrum. For the scalar function

[
r(lambda)=rac{lambda}{1+lambda},
]

one has

[
sup_{lambdage0}r(lambda)=1.
]

Therefore

[
|K|=1.
]

The contraction is non-strict.

## Explicit ultraviolet hostile

Choose a nonzero smooth compactly supported function (phi), modulate it at frequency (N), and symmetrize to the required parity. After normalization, the resulting packet (f_N) has

[
|mathsf Df_N|_2asymp N|f_N|_2.
]

Consequently,

[
rac{|mathsf Df_N|_2^2}
{|f_N|_2^2+|mathsf Df_N|_2^2}
longrightarrow1.
]

Every finite spectral cutoff has a strict margin, but the completed margin collapses as the cutoff admits higher frequencies.

## Consequence for the Adams cell

The history graph provides:

- a closed source domain;
- infrared coercivity;
- bounded endpoint traces;
- a bounded normalized derivative incidence.

It does not provide

[
|K|le1-arepsilon
]

for any (arepsilon>0) on the full completed history.

Thus a strict auxiliary or endpoint-loading margin must come from additional source structure, for example:

- a bounded-frequency source subspace;
- an extra higher-order graph energy;
- a genuinely smoothing incidence;
- or a source projection whose spectral support stays uniformly below infinity.

Such a restriction must be derived from the theta/Adams constructor. It cannot be inserted merely to obtain strictness.

## Higher-order comparison

If the source metric were

[
G_m=I+mathsf D^*mathsf D+(mathsf D^*mathsf D)^m
]

with (m>1), then the normalized first-derivative loading would satisfy

[
sup_{lambdage0}
rac{lambda}
{1+lambda+lambda^m}
<1.
]

This shows exactly what is missing analytically: superlinear ultraviolet energy relative to the first-order incidence. It does not show that the source authorizes such an energy.

## Result

The full (H^1) history graph solves the infrared inverse problem but leaves a distinct ultraviolet saturation:

[
G^{-1} 	ext{bounded},
qquad
|mathsf D G^{-1/2}|=1.
]

The next source audit must determine whether the actual theta history carries a higher-order or smoothing term that creates a uniform strict margin. Otherwise finite-cutoff strictness disappears at completion.
