# The two-chart relative cell has a unique oriented linking matrix

Index the adjacent-cell boundary packet by

$$
(F_{\rm in},F_{\rm out},W_{\rm const}).
$$

The overlap law

$$
h_-+h_+=-1
$$

is the chain relation

$$
r=(1,1,1)^T=0
$$

in the relative quotient. Any boundary form descending to that quotient must annihilate `r`.

## Positive reflection-even block

Let reflection exchange `F_in` and `F_out` and fix the constant wall. A real symmetric reflection-invariant Gram has the form

$$
G=
\begin{pmatrix}
a&b&c\\b&a&c\\c&c&g
\end{pmatrix}.
$$

The quotient condition `Gr=0` forces

$$
b=-a-c,
\qquad
g=-2c.
$$

Thus the positive relative Gram has only two scalar degrees of freedom. In particular its entrance/exit mixed entry is real. It cannot encode reciprocal orientation.

## Ordered reflection-odd block

Let `Omega` be a real skew form, require

$$
\Omega r=0,
$$

and require reflection to reverse its sign. These conditions force

$$
\boxed{
\Omega=\omega
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix}
}
$$

for one real source coefficient `omega`.

Hence the complete relative cell is not one Hermitian Gram guessed from scalar outputs. It is the typed pair

$$
(G,\Omega),
$$

where `G` is reflection-even positive data and `Omega` is the unique ordered linking polarization. In a Hermitian realization the latter enters as `i Omega`.

The forcing difference can couple only to `Omega`, not to the real mixed entry of `G`. Prime pushforward naturality therefore reduces in the oriented lane to preservation of one coefficient:

$$
\omega_p^{\rm arith}=\omega_p^{\rm source},
$$

while retaining the displayed matrix and the primitive-to-square direction.

The half-density four-front trace computes the source-side oriented readout, and the Wronskian return computes the arithmetic-side readout. Equality of their scalar values is necessary, but source provenance is the statement that the entire skew matrix is transported by the typed incidence maps.

This gives a finite checker: construct the three face incidence columns, form the pushed-forward `3x3` skew matrix, and compare it with the displayed canonical matrix times the independently computed Wronskian coefficient. Any transpose error changes `Omega` to `-Omega` and is detected.

Status: relative-cell matrix shape and orientation uniquely determined; the single source coefficient and its pairing/pushforward naturality remain to be identified by the constructor.
