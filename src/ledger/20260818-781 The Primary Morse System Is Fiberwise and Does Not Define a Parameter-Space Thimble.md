# 20260818-781 The Primary Morse System Is Fiberwise and Does Not Define a Parameter-Space Thimble

## Question

Entry 779 extracts the canonical exceptional coefficient line

\[
\ell_{\rm exc}=\mathbf Q\langle(0,1,0,-3)\rangle.
\]

Does the frozen one-loop Bunch--Davies integral independently define a
parameter-space thimble whose weighted exceptional image can be tested against
this line?

Entry 780 further shows that the admissible weighted tangents form the
contractible ray

\[
t=ic,\qquad c>0,
\]

which avoids \(t=\pm1\). It fixes the projective direction
\([0:1:0:-3]\), but leaves the coefficient \(1/(1+c^2)\) variable.

## Frozen source and variance

The primary source is Benincasa--Brunello--Mandal--Mastrolia--Vazao,
*On one-loop corrections to the Bunch-Davies wavefunction of the universe*,
arXiv:2408.16386.

Its cosmological integral integrates the site weights \(x_s\) and loop edge
weights \(y_e\). The external site and edge kinematics \((X_s,P_i)\) are
parameters. In the twisted-period formulation,

\[
I(X)=\int_{\Gamma_X} u_\tau(y;X)\,\varphi(y;X),
\]

\(\Gamma_X\) is a twisted cycle in the integration-variable fiber. The source
Morse equations

\[
\omega_\tau=d_y\log u_\tau=0
\]

are equations in the loop variables \(y_e\). Differentiation in external
kinematics gives Gauss--Manin transport of these fiber periods.

The source does **not** define any of the following on the external parameter
base containing the weighted normal coordinates \((u,y)\):

- a Morse/phase function;
- a gradient-flow metric and stable manifold;
- a parameter-space relative current;
- a weighted exceptional boundary of such a current.

The word *thimble* therefore cannot be moved from the integration fiber to the
parameter base without adding new data.

## Type gate

A family of fiber thimbles transported along a chosen parameter path has
variance

\[
\text{path in the base}
\longmapsto
\text{parallel transport of a fiber cycle}.
\]

It is not itself a relative chain in the base. Conversely, Entry 779's
\(\ell_{\rm exc}\) is a coefficient target and cannot select a source current.
Using it to choose the thimble would reverse the required derivation.

Entry 780 makes the normalization obstruction explicit: homotopy of the
contractible ray can at most preserve the projective class. It cannot choose
among

\[
\frac{1}{1+c^2}(0,1,0,-3),\qquad c>0.
\]

Thus even a parameter-space construction defined only up to homotopy would be
insufficient. A valid construction must additionally derive an intersection
normalization, measure, or asymptotic coefficient.

Hence the requested data have the following status:

\[
J_{\rm thimble}:\text{undefined},\qquad
\operatorname{Exc}(J_{\rm thimble}):\text{undefined},\qquad
\chi_{\mu_2}(J_{\rm thimble}):\text{undefined}.
\]

Consequently the membership statement

\[
\operatorname{Exc}(J_{\rm thimble})\stackrel?\in\ell_{\rm exc}
\]

is presently untyped, rather than false.

## Narrow result

\[
\boxed{
\text{The frozen primary integral defines fiberwise Morse cycles and their
Gauss--Manin transport, but no parameter-space thimble current.}
}
\]

This closes the proposed derivation from the primary integral. It does not
prove that no physical weighted relative current exists. Such a current must
come from an independently source-derived construction of the analytically
continued Bunch--Davies relative chain, including its weighted lift,
exceptional boundary, \(\mu_2\)-trace, and overlap homotopy.

Until then, the supported physical pairing remains undefined--not zero and not
nonzero--and no \(\mathcal Q\)-support test is authorized.

Topology nevertheless explains the stable projective direction found in Entry
779. What remains absent is both a source current and its scalar normalization.

## Evidence packet

- `research/benincasa/parameter-space-thimble-type-gate.json`
- Primary source: arXiv:2408.16386, especially the cosmological-integral and
  twisted-period/Morse-system definitions in Sections 2--3.

## Next falsifier

Find a primary construction that actually defines a relative current in the
external kinematic base. Freeze its phase, chain variance, regulator data, and
weighted lift before computing. Only then:

1. derive its exceptional boundary independently of \(\ell_{\rm exc}\);
2. compute its deck character;
3. test membership in \(\ell_{\rm exc}\);
4. if membership holds, derive normalization and regulator-hierarchy
   invariance.

No selected regulator path, matching projective direction, or fitted boundary
current may substitute for this source object.
