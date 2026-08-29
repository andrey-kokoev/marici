# Riesz defect charge is an additive functor on the parameter-cutoff path category

## Record

The cutoff variable is directed and discrete. It is therefore incorrect to propagate a Riesz rank by informally calling the cutoff family connected. The correct carrier is an admitted path category (or its realized cell complex) whose edges certify that one common contour remains in the resolvent.

Fix a contour \(\Gamma\) enclosing \(1\). Define \(\mathcal P_\Gamma\) as follows.

- An object is a typed pair \((X,s)\) together with its reduced Green carrier and operator \(K_X(s)\).
- A parameter edge is a path \(t\mapsto (X,s(t))\) for which \(\Gamma\subset\rho(K_X(s(t)))\).
- A cutoff edge \((X,s)\to(Y,s)\) includes the authorized carrier comparison and spectral-exactness cell, again with \(\Gamma\) in the resolvent throughout its realization.
- Reciprocal edges carry \(s\) to \(1-s\) and include the specified intertwiner.
- Composition is admitted only when carriers, comparison maps, and contour data match.

For every object set
\[
P_X(s)=\frac{1}{2\pi i}\int_\Gamma (z-K_X(s))^{-1}\,dz,
\qquad
\mathcal D_X(s)=\operatorname{ran}P_X(s).
\]
Functional calculus and the comparison cell transport \(\mathcal D\) isomorphically along every edge. Hence
\[
\mathcal D:\mathcal P_\Gamma\longrightarrow \mathrm{FinVect}
\]
is the defect-mode functor, and
\[
q_X(s)=\dim\mathcal D_X(s)
\]
is its locally constant integer decategorification. A zero anchor propagates only along paths admitted by \(\mathcal P_\Gamma\); no claim is made between disconnected components.

## Multiplicity law

For uncoupled instruments,
\[
K=K_1\oplus K_2,\qquad
P=P_1\oplus P_2,\qquad
q=q_1+q_2.
\]
Thus direct sum is the monoidal operation for extensive defect charge.

An either/branching instrument is different. Before a direct-sum totalization is explicitly supplied, its invariant is a tagged charge
\[
(1,q_1)\quad\text{or}\quad(2,q_2),
\]
not \(q_1+q_2\). Coproduct syntax alone does not authorize additive totalization.

Now let
\[
K(t)=
\begin{pmatrix}
K_1(t)&C_{12}(t)\\
C_{21}(t)&K_2(t)
\end{pmatrix}.
\]
If \(\Gamma\subset\rho(K(t))\) for all \(t\), the Riesz ranges form a finite-rank bundle and total \(q\) is constant. Sectorwise ranks need not remain defined: coupling can mix or transfer defect modes while conserving the total charge. If an eigenvalue crosses \(\Gamma\), the path leaves \(\mathcal P_\Gamma\); the crossing is the precise charge-creation, charge-annihilation, or charge-transfer witness.

## Reciprocal compatibility

A reciprocal intertwiner \(J_X(s)K_X(s)=K_X(1-s)J_X(s)\) transports the contour calculus:
\[
J_X(s)P_X(s)=P_X(1-s)J_X(s).
\]
When \(J_X(s)\) is invertible on the reduced carrier, reciprocal objects have equal total charge. Any sector tag must be transported explicitly rather than silently forgotten.

## Charge and determinant volume

The two coherence coordinates are independent.

- \(q\) counts the finite-dimensional defect modes enclosed by \(\Gamma\).
- The determinant line records accumulated volume and orientation distortion of carrier comparisons.

It is possible to have \(q=0\) while determinant comparisons collapse, and possible to have nonzero \(q\) with perfectly controlled determinant transport. A categorical RH certificate needs both: zero defect charge on the admitted component and nondegenerate determinant-line coherence.

## Hostile checks

1. **Discrete-cutoff fallacy.** A directed cutoff set is not connected merely because it is cofinal.
2. **Missing comparison cell.** A cutoff inclusion without a carrier intertwiner does not induce Riesz transport.
3. **Branch-sum fallacy.** Tagged alternatives cannot be summed before a monoidal totalization is declared.
4. **Coupling fallacy.** Off-diagonal homotopy preserves charge only while one common contour stays in the resolvent.
5. **Sector bookkeeping fallacy.** Total charge can remain constant while component labels cease to be invariant.
6. **Reciprocal erasure.** Equality of total ranks does not by itself identify reciprocal sector tags.
7. **Volume-rank conflation.** Rank stability does not control determinant-frame collapse.

## Next constructor

Construct the parameter-cutoff-reciprocal two-complex explicitly and prove that each generating square gives the same isomorphism of Riesz ranges. Its obstruction is a finite-dimensional holonomy representation
\[
\pi_1(|\mathcal P_\Gamma|)\longrightarrow \mathrm{GL}(\mathcal D),
\]
whose dimension is fixed by \(q\) but whose determinant supplies the missing volume coordinate. Triviality, or a controlled reciprocal character, of this holonomy is the next categorical coherence cell toward the RH certificate.
