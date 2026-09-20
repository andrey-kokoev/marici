# Xi-torsion lift iteration 2: H-border is a bordered packet, not yet an element of the translated-theta common-history range

## Fresh source audit

The exact construction is shellwise:

\[
H_{a,b,c}(z)
=
T_{PB}^{\rm rig}
\bigl(e^{z\cdot}\otimes K_{1,c}\bigr),
\qquad
K_{1,c}=-\frac12|q-c|+\delta_c.
\]

After loading and cutoff completion,

\[
\Delta_{\rm ar}(z)=\tau(z)H_{\rm ar}(z).
\]

The target of `H_(a,b,c)` is the complete bordered packet with coordinates such
as `(rho_0,E,W,R)` in four Fourier-related charts. It is not presently the
common scalar history used by the translated-theta codiagonal.

## Type mismatch in the proposed membership statement

Iteration 1 proved strictness for

\[
J:K\to\mathcal E_{\rm exp},
\]

where

\[
Jc(\xi)=\sum_{p,k}\frac{e^{-L_{p,k}/2}}k
\left(c_{p,k}^+e^{i\xi L_{p,k}}
+c_{p,k}^-e^{-i\xi L_{p,k}}\right).
\]

By contrast,

\[
H_{\rm border}(z)
\in B_{\rm border}
\]

is a `z`-dependent vector-valued Green packet. Therefore

\[
H_{\rm border}\in\operatorname{im}J
\]

is not yet a typed assertion. A source map

\[
B:B_{\rm border}	o\mathcal E_{\rm exp}
\]

or a vector-valued enlargement of `J` must first be constructed.

## Explicit shell evidence

For seam `c=b` and first leg `f=e^{z\cdot}`, the delta coordinate contains

\[
R_{e^{z\cdot},\delta_b}(z)
=e^{zb}\frac{1-e^{-2z(b-a)}}{2z},
\]

and

\[
E_{e^{z\cdot},\delta_b}(z)
=\frac12e^{zb}-\frac12e^{z(2a-b)}.
\]

The absolute-value component adds polynomial/Laplace factors. These are finite
linear combinations of shell endpoint exponentials and divided differences,
not automatically translates of the fixed completed-theta atom `Phi`.

Prime-shell assembly may turn endpoint exponentials into Dirichlet-type sums,
but that does not identify the full bordered packet with a scalar translated-
theta history.

## Necessary bridge theorem

Objective 2 must be replaced by the typed square

\[
\begin{array}{ccc}
K_B&\xrightarrow{J_B}&B_{\rm border}\\
\downarrow r&&\downarrow B\\
K&\xrightarrow{J}&\mathcal E_{\rm exp},
\end{array}
\]

where:

1. `J_B` is a labelled synthesis of the actual shell packets
   `T_PB^rig(e^(z dot) tensor K_(1,c))`;
2. `B` is source-derived and commutes with cutoff, Fourier charts, and the
   spectral connection;
3. `B(H_border)` has two-line Köthe bounds;
4. either `B` is faithful on the bordered factor sector or `J_B` itself has a
   continuous recovery map.

Without this square, Fourier recovery of translated theta coefficients says
nothing about membership of `H_border`.

## Consequence for the torsion claim

The cokernel used in iterations 42--50 silently placed the bordered factor and
the translated-theta codiagonal in one module. The source audit shows that this
common ambient module has not yet been constructed. Hence the class

\[
[H_{\rm border}]\in\operatorname{coker}J
\]

is currently heuristic rather than typed.

The valid torsion problem must be formulated for `coker(J_B)` in the bordered
category, or after proving the bridge `B` above.

## Next executable step

Use the explicit `(rho_0,E,W,R)` shell formulas to define a vector-valued
labelled synthesis `J_B`, then test whether endpoint and absolute-value pieces
admit coefficient recovery with finite exponential-order loss. This avoids
assuming the missing common-history identification.