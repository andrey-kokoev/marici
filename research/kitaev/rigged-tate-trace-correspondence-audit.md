# Rigged Tate trace correspondence requires a typed primitive boundary current

Owner: `marici.Kitaev`

## Verdict

The missing map is not a bounded operator obtained by restricting additive
adelic (L^2).  Its smallest legal source is the Schwartz--Bruhat test space,
and its first target is a typed idelic boundary rigging:

\[
 \mathcal S(\mathbb A)\xrightarrow{J_{\rm rel}}
 \mathcal T_{\rm rel}(\mathbb A^\times)
 \xrightarrow{(B_s,C_s)}\mathcal Y_s'.
\]

Here \(\mathcal T_{\rm rel}\) is the local restricted-product trace space
enlarged by an independent seam coordinate and by the relative primitive
transition current.  The square current is tempered; the primitive current is
Laplace/exponentially rigged.  A single common tempered topology is therefore
rejected.

The requested trichotomy is decided at the typing gate:

The classification is: **closable only after adjoining a typed boundary
current**.

This is a necessary architectural classification, not a proof that the
theta lift is closable.  After the enlargement, closability remains the exact
dense-adjoint-domain problem for the source-derived tail and seam operators.

## Why additive Hilbert restriction is impossible

Let \(q:\mathcal S(\mathbb A)\to L^2(\mathbb A,dx)\) be additive completion.
If a boundary trace descended through it, then

\[
 \ker q\subseteq\ker J.
\]

But the ideles are additive-Haar null, so additive (L^2) identifies functions
which may have different idelic traces.  The two-coordinate finite model

\[
 q(x,y)=x,\qquad J(x,y)=y
\]

has \(q(0,1)=0\) and \(J(0,1)=1\).  It is the smallest exact descent
falsifier.  Restriction must precede completion.

## Minimal source and target

The minimal presently authorized source is the nuclear LF test space
\(E=\mathcal S(\mathbb A)\), with local restriction transported to the local
boundary test spaces.  The algebraic restricted product retains finite Euler
incidence, Fourier--Tate covariance, and endpoint germs.  It does not carry
the global primitive anomaly continuously.

The smallest target packet therefore has distinct typed coordinates

\[
 \mathcal T_{\rm rel}=
 \mathcal T_0\oplus \mathcal C_P^{\rm rel}
 \oplus\mathcal C_Q^{\rm temp}\oplus\mathcal C_{\rm seam}
 \oplus\mathcal C_{\rm end}.
\]

The primitive coordinate is relative/affine: under cutoff enlargement,

\[
 C_{1,Y}=C_{1,X}+\Delta C_{1;X,Y}.
\]

It is not an absolute tempered scalar.  The square coordinate is a tempered
linear current.  The seam and endpoint coordinates remain independent even
when a scalar Tate functional later annihilates or identifies them.

## Domain, adjoint domain, and graph closure

Choose Hilbert pivots (H\) and (Y_s\) only after (J_{\rm rel}\) is defined
on (E\).  For (T_s=(B_s,C_s)J_{\rm rel}\), set

\[
 \operatorname{Dom}T_s=
 \{\phi\in E:T_s\phi\in Y_s\}\subset H.
\]

Its Hilbert adjoint domain is

\[
 \operatorname{Dom}T_s^*=
 \left\{y\in Y_s:\phi\mapsto
 \langle T_s\phi,y\rangle_{Y_s}
 \text{ is represented by an element of }H\right\}.
\]

The closed graph candidate is

\[
 \overline{\operatorname{Graph}T_s}=
 \{(h,y):\exists\phi_n\in\operatorname{Dom}T_s,
 \ \phi_n\to h,\ T_s\phi_n\to y\}.
\]

It is the graph of an operator exactly when it contains no \((0,y\ne0)\),
equivalently when \(\operatorname{Dom}T_s^*\) is dense in (Y_s\).

For the tail--seam relation \(\Gamma_0(Gc)=Hc\), the already-derived formula
specializes this to

\[
 \operatorname{Dom}\Gamma_0^*
 =\{y:H^*y\in\operatorname{Ran}G\}.
\]

Thus the remaining theta theorem is density of this set after all typed
boundary coordinates are retained.  Finite-cutoff matrix boundedness cannot
replace it.

## Smallest hostile graph

On finite sequences in \(\ell^2\), define

\[
 T e_n=e_1.
\]

For \(x_N=N^{-1}\sum_{n=1}^N e_n\),

\[
 \|x_N\|=N^{-1/2}\to0,\qquad Tx_N=e_1.
\]

So the graph is nonclosable.  Moreover

\[
 \operatorname{Dom}T^*=e_1^\perp,
\]

a nondense codimension-one subspace.  Every finite truncation is a bounded
matrix, so this also falsifies inference from cutoffwise graph convergence.
It models an absolute scalar summation assembled only after completion.

Recording the increments by (Re_n=e_n\) gives a closable isometry.  Scalar
summation may then remain a partial functional on the typed increment space.
This is the finite model for adjoining the relative primitive current; it is
not a derivation of Grothendieck's eventual (B_s,C_s\).

## Primitive versus square topology

For a cutoff primitive row with coefficients (2^n\), a polynomially weighted
tempered pivot gives domination constants diverging exponentially.  The
Laplace weight (16^n\) gives

\[
 \sum_{n\ge1}\frac{4^n}{16^n}=\frac13.
\]

Thus the primitive row is uniformly continuous in the exponential rigging
but not in a common tempered rigging.  The square row may remain in its
tempered coordinate.  Neither topology may be silently substituted for the
other.

## Scalar readout is not an operator lift

Let

\[
 J_+(x,y)=(x,y),\qquad J_-(x,y)=(x,-y),\qquad \tau(x,y)=x.
\]

Then \(\tau J_+=\tau J_-\), although the seam character differs.  Likewise
the erasure (E(x,y)=(x,0)\) preserves the scalar section while destroying the
seam.  Hence the completed Tate section cannot reconstruct the boundary
trace or the tail--seam pair.

## Exact falsifiers and unresolved theorem

- **Bounded additive restriction:** fails the kernel descent test.
- **Completion before restriction:** loses boundary values before (J\) acts.
- **Common tempered (P/Q) topology:** primitive domination constants diverge.
- **Scalar convergence:** does not imply a closable graph.
- **Finite cutoff graphs:** may converge to a graph with nondense adjoint domain.
- **Scalar equality:** permits inequivalent seam traces and seam erasure.
- **Typed relative repair:** removes the elementary absolute-sum obstruction,
  but does not establish the theta range theorem.

The exact unresolved analytic falsifier is either a nonzero (c\) with
\(Gc=0\), (Hc\ne0\), or a proof that

\[
 \{y:H^*y\in\operatorname{Ran}G\}
\]

is not dense.  A positive result must prove density in the source-authorized
rigging and verify Fourier--Tate covariance, endpoint continuity, and the
primitive transition cocycle on the closed graph.

## Verification

The exact finite witnesses are checked by
`research/kitaev/checkers/check_rigged_tate_trace_correspondence.py`; its
machine-readable result is
`research/kitaev/results/rigged-tate-trace-correspondence.json`.
