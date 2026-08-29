# Two-atom assembly is the first constructor-coherence falsifier

## Refinement

Atomwise realization is necessary but not sufficient. The arithmetic-to-Mellin rewrite must be monoidal with respect to every authorized assembly operation and must preserve mixed pairings.

For each prime power,
\[
e_{p^k}\longmapsto
\mathcal M_{p^k}
=
(P_{p^k},Q_{p^k},H_{p^k},E_{p^k},R_{p^k},G_{p^k}).
\]
The packet must preserve:

- incidence location \(k\log p\);
- coefficient \(\frac1k p^{-k/2}\);
- primitive versus square grade;
- sheet character;
- seam and endpoint incidence;
- cutoff inclusion;
- Fourier–Tate transport;
- scalar Euler/Mellin readout.

But constructor coherence begins only when two atoms are assembled.

## Two-atom comparison cell

For \(a=p^k\) and \(b=q^\ell\), let
\[
\mu_{a,b}:e_a\oplus e_b\longrightarrow e_a\star e_b
\]
denote an authorized source assembly and let
\[
\widehat\mu_{a,b}:
\mathcal M_a\oplus\mathcal M_b
\longrightarrow
\mathcal M_a\widehat\star\mathcal M_b
\]
denote analytic assembly.

The rewrite must provide a coherent square
\[
\rho_{a\star b}\,\mu_{a,b}
\simeq
\widehat\mu_{a,b}(\rho_a\oplus\rho_b).
\]
This cell must preserve the full interface and all mixed Green/seam terms. Scalar additivity is only one projection of the square.

## Mixed pairing obligation

Let \(b_G\) be the complete Green form. Assembly must satisfy a source-derived formula for
\[
b_G(\mathcal M_a,\mathcal M_b).
\]
The cross term cannot be chosen by polarization after scalar observation unless that polarization is itself source-authorized.

The two-atom Gram matrix
\[
\Gamma_{a,b}
=
\begin{pmatrix}
b_G(\mathcal M_a,\mathcal M_a)&
b_G(\mathcal M_a,\mathcal M_b)\\
b_G(\mathcal M_b,\mathcal M_a)&
b_G(\mathcal M_b,\mathcal M_b)
\end{pmatrix}
\]
is the first nontrivial constructor invariant. Correct diagonal packets do not determine its off-diagonal entries.

## Absence of primitive \(pq\) flux

For distinct primes \(p\neq q\), assembling primitive atoms must not silently create a primitive \(pq\) channel. The mixed packet may carry seam coupling or connected comparison data, but its primitive projection must satisfy the source incidence law
\[
\pi_{\mathrm{prim}}\,\widehat\mu(e_p,e_q)=0
\]
unless an independently authorized constructor creates such flux.

This is a typed absence statement. A scalar Euler observer may fail to detect an illicit primitive \(pq\) component if it cancels elsewhere.

## Authorized operations

Compositional realization requires the rewrite to intertwine:

1. finite direct sums;
2. grade-sensitive Adams operations;
3. cutoff inclusions;
4. source-action stacking;
5. Fourier–Tate transport;
6. seam clutching;
7. endpoint and archimedean attachment;
8. mixed Green pairings;
9. ordered composition where interchange is not authorized.

Additive, determinant, and ordered lenses remain distinct. Agreement under one does not close another.

## Minimal hostile

Take two source atoms \(e_a,e_b\). Let their individual packets be correct:
\[
\rho(e_a)=\mathcal M_a,\qquad
\rho(e_b)=\mathcal M_b,
\]
with exact scalar shadows and exact diagonal Green energies.

Define a defective assembled rewrite by adding an invisible mixed feature \(u\):
\[
\widetilde\rho(e_a\oplus e_b)
=
\mathcal M_a\oplus\mathcal M_b+u,
\]
where every atomwise observer annihilates \(u\), but
\[
b_G(u,\mathcal M_a)\neq0
\]
or the seam projection of \(u\) is nonzero.

Then all atom tests pass while the two-atom Gram matrix and seam incidence are wrong. If \(u\) lies in an illicit primitive \(pq\) port, the construction also violates the no-primitive-\(pq\)-flux rule.

This is the minimal constructor-coherence falsifier.

## Three levels of realization

### Atomic realization

Every \(p^k\) has a typed Mellin/Green normal form with correct interfaces and scalar shadows.

### Compositional realization

The rewrite is a typed monoidal or higher-coherent transformation intertwining sums, Adams operations, cutoff maps, transport, and mixed pairings.

### Completion realization

The finite coherent transformations form a compatible family as \(X\to\infty\), with uniform control in the projective exponential topology. No fixed polynomial rung is promoted, and finite/static verdicts remain distinct from completion.

## Completion control

Let \(\rho_X\) be the finite rewrite and \(I_{X,X'}\) the authorized inclusion. Require
\[
\rho_{X'}I_{X,X'}=
\widehat I_{X,X'}\rho_X
\]
including every two-atom comparison cell.

Uniform control must cover:

- projective seminorm transport;
- grade asymmetry;
- weighted type-fiber Adams naturality;
- moving-seam transport;
- Hilbert–Schmidt tail-seam coupling;
- discrete Fourier–Bohr valuation ports;
- archimedean and endpoint interfaces.

Atomwise norm bounds do not imply uniform control of mixed Gram blocks.

## Use of the constructed SCC pieces

The reported SCC state narrows the immediate construction:

- arithmetic-to-analytic incidence exists as a grade-preserving atom;
- moving-seam unitary transport exists;
- the weighted Adams cocycle exists;
- their grade-wise weighted/type-fiber naturality remains open;
- off-diagonal interaction remains independently typed;
- the common nine-operation graph domain remains open.

Therefore the next concrete cell is the naturality square joining the incidence atom, moving-seam transport, and Adams coefficient under two-atom assembly. The open off-diagonal block is not auxiliary; it is precisely where the two-atom hostile lives.

## Finite theorem target

> For every cutoff \(X\), the prime-power rewrite extends to the authorized finite assembly category as an interface-preserving coherent transformation. Its two-atom Gram and seam projections agree with source incidence, it creates no unauthorized primitive \(pq\) flux, and the family is natural under cutoff inclusion.

Only after this theorem may completion realization and the five-margin estimates be attempted.
