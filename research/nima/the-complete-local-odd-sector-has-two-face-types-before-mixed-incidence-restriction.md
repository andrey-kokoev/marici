# The complete local odd sector has two face types before mixed-incidence restriction

## Rank question on the four-chart carrier

The local source carrier factors as

\[
E_{\mathrm{sheet}}\otimes E_{\mathrm{face}},
\]

with sheet basis \((e_+,e_-)\) and face basis \((e_{\mathrm{in}},e_{\mathrm{out}})\).

Reciprocal-odd sheet parity is one-dimensional:

\[
r_-=e_+-e_-.
\]

But the face space has two independent types:

\[
s=e_{\mathrm{in}}+e_{\mathrm{out}},
\qquad
a=e_{\mathrm{out}}-e_{\mathrm{in}}.
\]

Therefore the full reciprocal-odd local chart sector is

\[
E_{\mathrm{odd}}^{\mathrm{chart}}
=
\operatorname{span}
\{r_-\otimes s,\ r_-\otimes a\},
\]

and has dimension two.

## Meanings of the two odd directions

The two basis vectors are not duplicate coordinates.

### Odd overlap direction

\[
r_-\otimes s
\]

is reciprocal-odd and face-symmetric. Its face component is the constant fifth-wall overlap, paired by Fourier transport with the delta boundary.

### Odd oriented-bulk direction

\[
r_-\otimes a
\]

is reciprocal-odd and face-antisymmetric. Its face component differentiates to the positive Gaussian density and carries the Wronskian orientation current.

Thus the complete relative cell contains two possible odd incidence types:

\[
\text{sheet odd}\otimes\text{wall},
\qquad
\text{sheet odd}\otimes\text{oriented bulk}.
\]

A one-dimensional odd theorem requires a source restriction eliminating or identifying one of them. It does not follow from reciprocal parity alone.

## Consequence for \(\mathcal V_{\mathrm{odd}}\)

Let

\[
\mathcal V_{\mathrm{odd}}
=
\left\{
\frac{B-B^*}{2i}:B\in\mathcal V_{\mathrm{mix}}
\right\}.
\]

Current source evidence gives the bound

\[
\dim\mathcal V_{\mathrm{odd}}\le2
\]

for one prime and one adjacent valuation cell, after restricting to the minimal four-chart carrier.

It does not yet justify

\[
\dim\mathcal V_{\mathrm{odd}}=1.
\]

That equality holds only if the mixed primitive-to-square constructor is proven to land entirely in one face type, most naturally the oriented-bulk line \(r_-\otimes a\), with the overlap routed as a separate diagonal boundary block.

If the mixed block may couple the constant wall, the odd rank is two.

## Port incidence matrix

The three source-derived odd readouts should be assembled into a matrix on the ordered basis

\[
(k_{\mathrm{wall}},k_{\mathrm{bulk}})
=
(r_-\otimes s,r_-\otimes a).
\]

Write

\[
\mathcal J_p
=
\begin{pmatrix}
J_{\mathrm{zero}}(k_{\mathrm{wall}})
&
J_{\mathrm{zero}}(k_{\mathrm{bulk}})
\\
J_{\gamma}(k_{\mathrm{wall}})
&
J_{\gamma}(k_{\mathrm{bulk}})
\\
J_{\mathrm{Wr}}(k_{\mathrm{wall}})
&
J_{\mathrm{Wr}}(k_{\mathrm{bulk}})
\end{pmatrix}.
\]

Source typing suggests, but does not yet prove:

- the Wronskian/PV centroid primarily detects \(k_{\mathrm{bulk}}\);
- the constant–delta boundary orbit is needed to detect \(k_{\mathrm{wall}}\);
- the reciprocal Euler ratio may mix both after arithmetic pushforward;
- the zero-section position probe is sheet-odd but its face incidence must still be specified.

Joint faithfulness in the rank-two case is exactly

\[
\operatorname{rank}\mathcal J_p=2.
\]

## Minimal rank hostile

Take

\[
k_1=r_-\otimes a,
\qquad
k_2=r_-\otimes s.
\]

Suppose all three ports were calibrated only on \(k_1\):

\[
J_j(k_1)=c_j\ne0,
\qquad
J_j(k_2)=0.
\]

Every tested scalar current then appears proportional and correctly oriented on \(k_1\), while the independent odd wall direction \(k_2\) remains invisible.

This is Kitaev's hidden-second-direction hostile in the actual source chart types.

## Completion hostile

Even if finite rank is one, write

\[
J_X(k_X)=c_X.
\]

If

\[
c_X\ne0
\quad\text{for every finite }X,
\qquad
c_X\to0,
\]

then finite identification survives while the completed odd coordinate becomes dark.

For rank two, the correct quantity is the smallest singular value:

\[
\sigma_{\min}(\mathcal J_{p,X}|_{\mathcal V_{\mathrm{odd}}}).
\]

Completion requires a uniform positive lower bound after source normalization.

## Immediate source calculation

The rank theorem now reduces to one typing decision:

> Does the primitive-to-square mixed block couple the face-symmetric constant-wall channel, or is that channel routed entirely into diagonal boundary data?

The source boundary formula for the relative Green matrix must answer this before linking coefficients are computed.

- If wall coupling is forbidden, \(\mathcal V_{\mathrm{odd}}\) is at most one-dimensional and one nonzero calibrated odd port suffices.
- If wall coupling is authorized, the local odd rank is two and the three-port incidence matrix must have rank two.
- If the formula is absent, the odd rank remains undefined within the mixed-incidence subspace, despite the ambient two-dimensional upper bound.

## Current classification

The ambient complete local odd sector is exactly two-dimensional. The source-authorized mixed odd sector is not yet frozen because the wall-versus-mixed routing law is missing.

Therefore the next datum is not another scalar calibration. It is the block-support theorem for \(B_{\alpha,p}\) relative to

\[
E_{\mathrm{face}}
=
\operatorname{span}\{s\}
\oplus
\operatorname{span}\{a\}.
\]

That theorem determines whether the linking problem is rank one or rank two.
