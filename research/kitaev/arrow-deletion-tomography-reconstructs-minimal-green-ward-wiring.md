# Arrow-deletion tomography reconstructs the minimal Green–Ward wiring

## Question

Which incidence arrows are forced by the existing theta/Tate source, endpoint, seam, and orientation results, and what failure signature appears when each arrow is removed?

## Claim boundary

The smallest wiring supported by existing packets is not a linear chain. It is a directed network with six typed arrows:

\[
\text{labelled source}
\xrightarrow{F}
\text{tail state}
\xrightarrow{E}
\text{endpoint packet}
\xrightarrow{C}
\text{seam feature},
\]

together with

\[
\text{reciprocal tail pair}
\xrightarrow{O}
\text{odd orientation},
\]

\[
\text{labelled endpoint packet}
\xrightarrow{A}
\text{cross-label arithmetic coherence},
\]

and the backward comparison arrow

\[
\text{boundary defect}
\xrightarrow{R}
\text{source Ward packet}.
\]

Here \(F\) is forward forcing incidence, \(E\) endpoint evaluation, \(C\) the Clark endpoint-to-seam differential, \(O\) reciprocal-odd comparison, \(A\) arithmetic coupling before scalar summation, and \(R\) reverse source incidence. The final Green–Ward mate requires the two directed routes to agree on the scalar-null pullback.

### Delete the forward forcing arrow F

Without \(F\), the source currents do not generate the tail state. A tail realization may still be postulated and propagated, but it has lost provenance from the labelled source.

Shadow:

- controllability or synthesis cokernel in the tail-state space;
- endpoint and Green identities can remain true for freely chosen states;
- determinant or scalar output becomes a model of the plant rather than a source realization.

This deletion is detected by source reachability, not by output rank.

### Delete endpoint evaluation E

Without \(E\), nonzero tails with distinct boundary values become behaviorally indistinguishable. The scalar completed section and the endpoint term in the Green identity lose their source-facing port.

Shadow:

- an observation kernel consisting of states with the same retained bulk features but different endpoint values;
- downstream Clark seam data cannot be derived, because \(C\) acts on the endpoint germ;
- the adjoint bulk energy may remain positive while the Evans/Tate scalar is no longer represented.

This is the established separation between source autocorrelation and endpoint evaluation.

### Delete the Clark seam arrow C

The identity

\[
\mathcal C_aG(0,z)=H_{1,a}(z)
\]

identifies the surviving Green seam defect with the primitive signed Clark feature. Removing \(C\) leaves endpoint evaluation intact but disconnects it from that seam type.

Shadow:

- one complex primitive seam defect line remains unmatched;
- reflection still cancels the common forcing-norm line, so the defect rank drops from two complex lines to exactly one;
- scalar endpoint values can remain correct while the typed Green boundary identity fails.

This is a rank-one complex, or rank-two real, mate defect.

### Delete the reciprocal-odd comparison arrow O

Write the two reciprocal tails and seam as \((P,Q,M)\). The even observations

\[
A=P+Q+M,\qquad M
\]

have kernel

\[
\operatorname{span}\{(1,-1,0)\}.
\]

Removing \(O(P,Q,M)=P-Q\) therefore leaves all completed and seam-even data unchanged while erasing orientation.

Shadow:

- a one-dimensional antisymmetric logical fiber;
- exact reciprocal-even coherence with no Krein orientation;
- inability of any additional even scalar row to repair the loss.

This is the cleanest behavior-side kernel in the network.

### Delete the cross-label arithmetic arrow A

Labelwise tail dynamics allow

\[
G_1(0)=a,\qquad G_2(0)=-a
\]

with exact local equations and zero aggregate endpoint readout. A label-separating Ward port remains nonzero.

Shadow:

- scalar cancellation between nonzero labelled endpoints;
- a cross-label coherence kernel invisible to every independent labelwise equation;
- failure of the null pullback to factor through the Ward kernel.

Thus \(A\) is horizontal incidence between labels. It is not another state tower and cannot be replaced by requiring each endpoint to vanish separately.

### Delete the reverse incidence arrow R

On the minimal even Fourier chart, forward incidence \(N_f\) and Fourier transport obey

\[
F_+N_fF_+-N_f^*
=
\frac f3
\begin{pmatrix}
\sqrt2&-1\\
-1&-\sqrt2
\end{pmatrix},
\]

a rank-two residual for \(f\ne0\). Fourier boundary symmetry therefore does not manufacture the reverse source coupling.

Shadow:

- the complete forward Tate/Poisson construction and its scalar section remain intact;
- the boundary condition may remain Fourier-rigid and Lagrangian;
- the backward Green defect cannot be identified with the source Ward packet;
- the adjoint comparison residual is full rank already on the smallest even chart.

This is the only deletion in the atlas that preserves the whole forward observable construction while destroying precisely the final cross-tower mate. It is therefore the best current localization of the missing constructor.

### Dependency order

The arrows are not interchangeable. Their logical order is:

1. \(F\) establishes source provenance and reachability.
2. \(E\) exposes boundary values.
3. \(C\) types the primitive seam defect.
4. \(O\) retains reciprocal orientation before even aggregation.
5. \(A\) couples labels before scalar cancellation.
6. \(R\) returns the typed boundary defect to the source Ward packet.

Only after all six are present can the final mate compare forward and backward constructions. The first five do not compose automatically into the sixth.

### What the modular tail can repair

The all-label modular tail naturally acts on forward sewing and therefore can repair defects in \(C\), or contribute to the cross-label naturality of \(A\). It cannot by its mere presence construct \(R\). To close the final mate, its image must be carried through an independently derived reverse-incidence map.

Consequently the decisive test is

\[
R_X\Delta_X
=
W_X-B_{X,s}
\]

as a typed character-valued identity natural in cutoff. If \(R_X\) is undefined, the equality cannot be inferred from scalar seam cancellation. If \(R_X\Delta_X=0\) while the mate residual is nonzero, the tail is only a forward syzygy.

## Disposition

Arrow deletion reconstructs a six-edge minimal wiring and isolates the active missing edge as reverse source incidence \(R\). Deleting \(F,E,C,O,A\) reproduces already known controllability, observability, seam-rank, orientation, and cross-label cancellation witnesses. Deleting \(R\) uniquely leaves the entire forward scalar construction coherent while preventing the Green defect from becoming a Ward statement.

The programme should now stop searching for an extra scalar dimension. The next source calculation must construct \(R\) on the typed primitive, square, seam, archimedean, and connected-tail packet, then evaluate the modular residue through it. This is the smallest arrow whose restoration could turn the existing forward coherencer into the final mate.