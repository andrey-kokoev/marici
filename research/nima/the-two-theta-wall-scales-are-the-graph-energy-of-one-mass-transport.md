# The two theta wall scales are the graph energy of one mass transport

## Wall transport

The completed-theta convolution decomposes as

\[
H_\Phi=M_\Phi I+B.
\]

On the pure wall channel, the history therefore acts by the scalar map

\[
J_{\mathrm{wall}}:
w\longmapsto M_\Phi w.
\]

This is the canonical comparison between the retained input wall and the
theta output wall. It is not an identification of the two coordinates.

## Graph realization

The wall transport has graph

\[
\Gamma(J_{\mathrm{wall}})
=
\{(w,M_\Phi w):w\in\mathcal W\}
\subset
\mathcal W_{\mathrm{in}}
\oplus
\mathcal W_{\mathrm{out}}.
\]

With the direct-sum source metric, its graph energy is

\[
\|(w,M_\Phi w)\|^2
=
(1+M_\Phi^2)\|w\|^2.
\]

This is exactly the coefficient of the scalar identity in

\[
I+H_\Phi^*H_\Phi.
\]

Therefore the two wall-scale contributions

\[
I,
\qquad
M_\Phi^2I
\]

are not duplicate walls. They are the input and output energies of one typed
wall transport.

## Tail loading

For a general vector,

\[
H_\Phi f=M_\Phi f+Bf.
\]

The full graph energy is

\[
\|f\|^2+|H_\Phi f\|^2
=
(1+M_\Phi^2)\|f\|^2
+
2M_\Phi\operatorname{Re}\langle f,Bf\rangle
+
\|Bf\|^2.
\]

Thus the terms

\[
M_\Phi(B+B^*),
\qquad
B^*B
\]

are precisely the wall--tail cross energy and tail output energy of the same
graph. No extra positive block is being adjoined.

## Coefficient-wall comparison

The multiplication-window theorem supplies an input wall represented by
\(I\). The theta convolution supplies the output transport
\(M_\Phi I\).

The minimal source comparison is therefore not

\[
I=M_\Phi I.
\]

It is the graph arrow

\[
I
\xrightarrow{\ M_\Phi\ }
M_\Phi I.
\]

At quadratic level, the authorized comparison should map the coefficient wall
projector to the graph projector or graph form of this arrow.

## Uniform frame control

If

\[
0<m_0\le M_\Phi\le M_1<\infty
\]

in the declared parameter family, then wall transport and its inverse are
uniformly bounded:

\[
\|J_{\mathrm{wall}}\|\le M_1,
\qquad
\|J_{\mathrm{wall}}^{-1}\|\le m_0^{-1}.
\]

For the fixed completed Riemann theta kernel, \(M_\Phi\) is one fixed
positive scalar, so no cutoff-dependent wall-frame collapse occurs.

This does not require rescaling the wall to unit mass.

## Reciprocal symmetry

Reflection fixes both wall coordinates and the scalar transport
\(M_\Phi\). Hence the wall graph is reciprocal-even. All reciprocal-odd
content remains in

\[
B-B^*.
\]

This cleanly separates wall normalization from orientation.

## Shifted-history square

The auxiliary blocks are the reciprocal polarizations of the same history
graph:

\[
D_\pm
=
\frac12(I\pm iH_\Phi)^*(I\pm iH_\Phi).
\]

The graph interpretation explains why both \(I\) and
\(H_\Phi^*H_\Phi\) are source-natural once the input wall and history
output are proven to be the two legs of one constructor.

## Remaining authority statement

The analytic graph is exact. The source theorem still must prove that the
coefficient-window wall is the input leg of this theta-history graph, rather
than merely an isomorphic one-dimensional wall from another carrier.

The required square is now only:

\[
\begin{array}{ccc}
\text{coefficient wall}
&\xrightarrow{\text{window--theta comparison}}&
\mathcal W_{\mathrm{in}}\\
&\searrow&\downarrow M_\Phi\\
&&\mathcal W_{\mathrm{out}}.
\end{array}
\]

Once the upper arrow is source-authorized, the lower wall transport and its
quadratic normalization are already fixed.

## Hostile

Identify input and output walls by an isometry and then also apply
\(M_\Phi\). This changes the graph coefficient from
\(1+M_\Phi^2\) to a fitted normalization while preserving one-dimensional
scalar observability.

## Frontier

The wall discrepancy has been reduced from two competing residues to one
typed graph:

\[
w\longmapsto(w,M_\Phi w).
\]

The remaining first-edge problem is the incidence of the coefficient-window
wall and front currents into this completed theta-history graph, followed by
quadratic Green descent.
