# A Marked Axis Constructs the Grade-Changing Endpoint Correspondence

## Covariant no-go

The grade-(r) ladder cokernel is the irreducible rotation representation

\[
C_{s,r}=\mathcal H_l^{(l)},
\qquad
l=s+r-1.
\]

The next cokernel is (C_{s,r+1}=\mathcal H_{l+1}^{(l+1)}). Since (mathcal H_l) and (mathcal H_{l+1}) are inequivalent irreducible (SO(3)) representations, Schur's lemma gives

\[
\operatorname{Hom}_{SO(3)}(C_{s,r},C_{s,r+1})=0.
\]

The native ladder raising operator does not evade this result. On the endpoint, its coefficient contains

\[
l-l=0,
\]

so (eth) annihilates the entire grade-(r) cokernel.

Thus no nonzero fully rotation-natural grade-changing map exists.

## Axis-marked construction

Let (hat n) be a marked unit axis and let (M_{hat n\cdot x}) denote multiplication by its degree-one scalar harmonic. Define

\[
J_{\hat n}
=eth\,\Pi_{l+1}M_{\hat n\cdot x},
\]

where (Pi_{l+1}) projects to spherical degree (l+1). The multiplication first moves the endpoint away from the raising wall; (eth) then raises its spin weight from (l) to (l+1).

On the declared endpoint domain the projection is redundant. The spin-weighted multiplication recurrence also has a same-degree branch, but subsequent application of (eth) annihilates it; its lower-degree branch vanishes because the input spin already equals its degree. Hence, on \(\mathcal H_l^{(l)}\),

\[
J_{\hat n}=\eth\,M_{\hat n\cdot x}.
\]

In an axial weight basis, the spin-weighted multiplication recurrence gives

\[
\Pi_{l+1}(\cos\theta\,Y_{lm})
=a_{l+1,m}Y_{l+1,m},
\]

with

\[
a_{l+1,m}^2
=\frac{(l+1)^2-m^2}{(l+1)^2(2l+3)}.
\]

The subsequent raising coefficient has square (2(l+1)). Therefore

\[
\lvert J_{\hat n}(l,m)\rvert^2
=\frac{2((l+1)^2-m^2)}{(l+1)(2l+3)},
\]

which is strictly positive for every (-l\leq m\leq l). Hence (J_{\hat n}) is injective.

Its image contains precisely the target weights

\[
-l,-l+1,\ldots,l,
\]

and its cokernel is the two-dimensional extremal packet

\[
\operatorname{span}\{|l+1,-(l+1)\rangle,|l+1,l+1\rangle\}.
\]

This explains the universal dimension increment

\[
\dim C_{s,r+1}-\dim C_{s,r}=2.
\]

## Spin-two grade change

For (s=2,r=2), one has (l=3). The construction gives

\[
J_{\hat n}:\mathcal H_3^{(3)}\hookrightarrow\mathcal H_4^{(4)}
\]

with rank seven inside a nine-dimensional target. The two new grade-three endpoint directions are the axial weights (m=\pm4).

Thus a separate grade-changing correspondence can be constructed. It transports the seven-dimensional grade-two endpoint into the grade-three endpoint while explicitly recording the two directions that grade three adds.

## Price of the construction

The map is not (SO(3))-natural. It depends on a marked axis and is only equivariant under its stabilizer. Reversing the oriented axis changes the multiplication operator's sign. The spectral projection is also a global constructor, not part of the local ladder word.

These are features, not removable presentation details: full rotation covariance forbids every nonzero map. The marked axis is the exact extra datum that permits one.

## Aspect disposition

The construction has geometric provenance, correct typing, a discriminating target, nonredundancy, and an exact bounded coefficient test. It still lacks an operational witness showing that multiplication, global degree projection, and spin raising are jointly executable on the same prepared Bondi packet.

Under Aspect's updated tester, its disposition is therefore `defer`.

This disposition applies to interpreting (J_{\hat n}) as a physical field-changing operation. A narrower derived-readout implementation is now admitted: seven existing executable (l=3) low-mode ports, followed by finite authorized linear processing, compute the seven coefficients in the image of (J_{\hat n}). See `seven-low-mode-ports-execute-the-grade-change-as-a-derived-readout.md`. That admission supplies no target actuator and no independent spin-4 field measurement.

### Full Aspect tower attack

> Correction after executable mutation semantics: the first v1 adapter below used a declared observation matrix and overstated the unresolved kernel as three-dimensional. The exact v2 fixture finds only one admitted blind hostile. Projection deletion is an alias, constructor-order swap is rank-visible, and singular extension lies outside the declared endpoint domain.

The initial structure was compiled as a fixture against Aspect's executable five-rung tower, rather than only evaluated by a locally copied rule. Its declared observation matrix reported three invisible directions:

- weight-dependent phase twist;
- constructor-order swap;
- singular domain extension.

That first adapter synthesized three corresponding obligations:

- phase-sensitive weight interference;
- constructor-word continuation testing;
- graph-domain and singular-support testing.

Executable mutation semantics revise this result. Of the eight proposed mutations, six are admitted hostiles, one is an exact alias, and one is outside the declared domain. Five hostiles are already detected. The sole blind hostile is a nonconstant weight-dependent phase twist.

The source-derived repair is the rank-one tensor-family law

\[
J_{a\hat n+b\hat n'}=aJ_{\hat n}+bJ_{\hat n'},
\qquad
U(R)J_{\hat n}U(R)^{-1}=J_{R\hat n}.
\]

Adjacent weights form a connected chain, so compatibility forces all phase multipliers to agree. The repair removes nonconstant phase twists while retaining one common scalar normalization. The exact frozen kernel is then zero. Rung five still returns `defer` because no operational witness exists.

The exact fixture, checker, and result are:

- `contracts/axis-marked-grade-change-aspect-fixture.v1.json`;
- `checkers/axis_marked_grade_change_aspect_tower_checks.py`;
- `results/axis_marked_grade_change_aspect_tower_checks.json`.

The corrected executable-semantics packet is:

- `contracts/axis-marked-grade-change-aspect-exact-fixture.v2.json`;
- `checkers/axis_marked_grade_change_aspect_exact_checks.py`;
- `results/axis_marked_grade_change_aspect_exact_checks.json`.

This does not restore a map from affine torsion classes to harmonic vectors. Rather, it provides the previously missing cross-grade arrow within the harmonic tower:

```text
affine order seven
  = grade-two endpoint dimension

grade-two endpoint H3 --J_axis--> grade-three endpoint H4
                                      + two extremal directions
```

The torsion-to-vector-space no-go remains unchanged.

## Evidence replay

The checker verifies the exact coefficient formula, injectivity, the two extremal complement weights, and the Aspect disposition for (1\leq l\leq20).

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/axis_marked_grade_change_correspondence_checks.py
```

Machine-readable results are written to `research/strominger/results/axis_marked_grade_change_correspondence_checks.json`.
