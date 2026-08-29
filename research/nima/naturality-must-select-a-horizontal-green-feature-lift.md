# Naturality must select a horizontal Green-feature lift

## Advance

The factorization
\[
S_s=J_s^*\Lambda_s
\]
does not determine a full feature realization when \(J_s^*\) has a kernel. It determines only the quotient-valued lift. Therefore scalar Green domination and compactness cannot certify that the continuation-residue packet has been realized correctly.

The next constructor is not merely a bounded lift. It is a **natural horizontal lift** selected by cutoff, Real, reciprocal, and boundary-incidence transport.

## The realization fiber

Let
\[
N_s=\ker J_s^*\subset Z_s,\qquad Q_s=Z_s/N_s.
\]
If one lift exists, every lift is
\[
\Lambda_s+T,\qquad T\in\operatorname{Hom}(A,N_s).
\]
Hence the scalar synthesis operator determines a unique quotient class
\[
\bar\Lambda_s:A\longrightarrow Q_s,
\]
but leaves the affine realization fiber
\[
\mathfrak L_s=\Lambda_s+\operatorname{Hom}(A,N_s).
\]

The minimum-norm representative is characterized by
\[
\operatorname{ran}\Lambda_s^{\min}\subset N_s^\perp
=\overline{\operatorname{ran}J_s}.
\]
This is a mathematical gauge fixing. It is not yet a source authorization: an orthogonal complement supplied by the Hilbert metric need not agree with continuation, residue, or clutching transport.

## Horizontal selection datum

For every admitted structural arrow \(\alpha:s\to t\), let
\[
R_\alpha:Z_s\to Z_t,\qquad C_\alpha:A_s\to A_t
\]
be the feature and arithmetic transports. A full lift is natural when
\[
R_\alpha\Lambda_s=\Lambda_t C_\alpha.
\]

The required arrows include:

1. cutoff inclusions and cutoff retractions;
2. Real involution;
3. reciprocal-sheet transport \(s\leftrightarrow1-s\);
4. seam specialization;
5. endpoint and archimedean boundary maps;
6. prime-power incidence inclusions;
7. mixed comparison and clutching maps.

Modulo \(N_t\), these equations hold for the uniquely determined quotient lift if synthesis itself is natural. Their unresolved content is precisely the invisible component in \(N_t\).

Choose provisional representatives \(\Lambda_s^0\). Their naturality defects are
\[
\omega_\alpha
=
R_\alpha\Lambda_s^0-\Lambda_t^0C_\alpha
\in\operatorname{Hom}(A_s,N_t).
\]
Changing representatives by \(T_s:A_s\to N_s\) changes the defect by
\[
\omega_\alpha\mapsto
\omega_\alpha+R_\alpha T_s-T_tC_\alpha.
\]
Thus the invisible realization problem is a cocycle equation. A horizontal lift exists exactly when the defect cocycle is a coboundary in the typed naturality complex.

## Three outcomes

### Unique horizontal lift

The homogeneous naturality system
\[
R_\alpha T_s=T_tC_\alpha
\]
has only \(T=0\), and the defect cocycle vanishes in cohomology.

### Finite torsor

The obstruction vanishes, but the homogeneous solution space is finite-dimensional. Later wiring must either be invariant under this torsor or supply an additional normalization.

### Infinite invisible fiber

The homogeneous solution space is infinite-dimensional. Scalar domination then forgets uncontrolled continuation data and cannot support the categorical RH resolution without another observable.

## Hostile model

Take
\[
Z=\mathbb C^2,\qquad J^*(z_1,z_2)=z_1,\qquad A=\mathbb C,
\]
and \(S(c)=c\). Every
\[
\Lambda_\tau(c)=(c,\tau c)
\]
has \(J^*\Lambda_\tau=S\) and gives identical scalar Green domination.

Now introduce a later clutching map
\[
W(z_1,z_2)=z_1+z_2.
\]
Then
\[
W\Lambda_\tau(c)=(1+\tau)c.
\]
The invisible component is invisible only to \(J^*\); it changes later wiring. Minimum norm chooses \(\tau=0\), but this is not forced by \(S\). A structural transport requiring \(W\Lambda(c)=2c\) instead selects \(\tau=1\).

Therefore pseudoinverse selection and source-natural selection are logically distinct.

## Categorical resolution target

> The quotient arithmetic lift exists and is bounded; its naturality-defect cocycle vanishes; and the homogeneous invisible natural transformations are either zero or act trivially on every authorized downstream wiring.

This is stronger than Green domination but weaker and more accurate than demanding injectivity of \(J_s^*\). It permits harmless invisible gauge while excluding invisible states that alter reciprocal continuation, residues, or clutching.

## Next calculation

Construct the finite-cutoff naturality complex explicitly. For each prime-power generator:

1. compute its quotient feature lift;
2. evaluate cutoff, Real, reciprocal, seam, endpoint, and archimedean defects;
3. project each defect to \(N_s\);
4. solve the resulting cocycle equation;
5. test every residual homogeneous solution against downstream wiring.

The first nonzero obstruction class identifies the exact missing source channel. If the obstruction vanishes and the homogeneous kernel is wiring-trivial, the Green-feature lift is categorically well-defined even when it is not literally unique.
