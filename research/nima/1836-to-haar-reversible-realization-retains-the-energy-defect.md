# The 1836 constructor lifts reversibly to Haar, but retains its energy defect

## Question and disposition

The operator asks to carry the reversibility of the 1836 proton-like constructor into the Xi/relative-Haar energy comparison. Use the actual source-derived tetrahedral projector, not the separate 1836-arrow Fourier phase net, and do not choose a target metric to force confinement.

**Constructed:** a bounded, isometric realization and recovery of the relative-Haar carrier in the retained mode of the native 36-coordinate constructor, with exact prime intertwining. The entire history factor remains present.

**Not constructed:** an independent source law making the two Xi route energies equal. The reversible lift preserves their difference exactly. Native internal return is not the same operation as prime translation of the retained history.

**Rejected under specified hypotheses:** replacing the whole Haar prime representation by a fixed finite-dimensional unitary carrier. This is stronger than the RH-bearing reduced-fiber energy condition and is not necessary for RH. Its failure is not a no-go for energy equality at Xi zeros, a parameterized family, or a rigged realization with a separately justified energy domain.

No proton mass, unique 1836 minimality, RH, or zero simplicity is inferred.

## 1. Source-derived internal type

Reconstruct the twelve triangle frames and eighteen shared-edge wires from the existing seed rotations. The shared-edge Laplacian has spectrum 0,1,3,4,5. Its spectral zero-mode projection, transported through the source frames, gives G. The kernels of the local positive constraint operators D*D give P in the declared oriented cyclic sector. Thus

\[
P=P^*=P^2,\quad G=G^*=G^2,\quad
N=GP=PG=N^*=N^2,\quad \operatorname{rank}N=1.
\]

The compiled coefficient supports are 108,432,1296, totaling 1836. The chiral sector and dense-feedback architecture are the previously declared model choices; this audit does not derive their uniqueness.

Take a nonzero column w of the newly computed N. The exact checker obtains

\[
w=Ne_0,\qquad \nu=w^*w=1/180,\qquad v=w/\sqrt\nu,\qquad N=vv^*.
\]

This normalization is determined by the native projector, before any arithmetic state or spectral parameter is supplied. It is not fitted to an Xi energy. P,G,N each fix v.

## 2. Reversible realization, with the history retained

Let H_E be the energy completion of the admitted relative-Haar core. In logarithmic pair coordinates this is represented by L2(R2,dq dr); the second slot retains the source conjugate-slot convention. For actual Xi histories all uses below are restricted to their already admitted finite-energy domain. No common neighborhood extension of those histories is claimed.

Set V=C36 and define

\[
\mathcal J:H_E\longrightarrow V\otimes H_E,
\qquad \mathcal J h=v\otimes h,
\qquad \mathcal R=\mathcal J^*=v^*\otimes I.
\]

Then

\[
\mathcal R\mathcal J=I,
\qquad \mathcal J\mathcal R=N\otimes I,
\qquad \|\mathcal J h\|^2=\|h\|^2.
\]

This is a genuine Hilbert-space isomorphism onto the closed retained sector (im N) tensor H_E. It is not an isomorphism onto the entire ambient V tensor H_E. Orthogonal internal components are discarded by recovery, but no source history is discarded by realization followed by recovery.

The three native stages lift to P tensor I, G tensor I, N tensor I. These are 1836 operator-valued arrows, each carrying its scalar native coefficient times the history identity. This is not a finite-dimensional realization or a claim of 1836 total implementation cost for the full source. The stages fix every realized state v tensor h. Thus the native source type survives realization and return without needing to assert that prime translation fixes h.

For any source operator A on its declared domain, use I_V tensor A with domain V tensor D(A). The finite-dimensional tensor factor introduces no new domain choice:

\[
(I_V\otimes A)\mathcal J=\mathcal J A,
\qquad
\mathcal R(I_V\otimes A)=A\mathcal R.
\]

If A is closed, its finite-copy amplification is closed. No inverse or spectral projection of the arithmetic operator is used. The construction copies whatever source operator and residual are supplied; it does not independently construct a conservative arithmetic operator.

## 3. Actual relative-Haar prime action

Put s=1/2+z, a=log p. After the source half-density normalization, the relative-Haar prime operation has the logarithmic form

\[
T_p(z)=p^{-z}S_a,\qquad
(S_a h)(q,r)=h(q+a,r+a).
\]

S_a is unitary in the relative-Haar energy norm. This is the normalized diagonal pair action, not the fixed-forcing one-leg translation. If a pointed graph description is used, its forcing base moves according to the already established source rule. Tensoring with the native mode does not identify these two different squares.

Define the realized prime operation by

\[
\widehat T_p(z)=I_V\otimes T_p(z).
\]

The realization and recovery intertwine T_p exactly. In particular

\[
\widehat{\mathcal E}(\widehat T_p(z)\mathcal J h)
=p^{-2\Re z}\widehat{\mathcal E}(\mathcal J h).
\]

The factor p^{-2 Re z} has not disappeared. Positive recovery and the reciprocal inverse exist for every z, while one-step isometry holds only at Re z=0 on a nonzero finite-energy state.

This makes two squares explicit:

- source type -> native realization -> source recovery: an isometric round trip;
- prime transport before versus after realization: an intertwining square that retains the original modular energy multiplier.

The first square does not turn the second square into an isometry. Replacing T_p(z) by the unitary p^{-i Im z} S_a would remove its real amplitude, but it would change the source action. With the same noncollapsed isometric J, that replacement breaks prime intertwining away from the seam. More generally, demanding a unitary target step W with W J=J T_p(z) on a nonzero state already implies ||T_p(z)h||=||h||. At an Xi zero this is precisely the missing conclusion, not an independent consequence of the native constructor.

## 4. The actual RH-bearing defect is unchanged

Write h_+(z),h_-(z) for the already realized relative-Haar coordinates of the two histories (including the source relative-Haar embedding where needed). On every admitted fiber, define

\[
\delta_p(z)=\mathcal E(h_+(z))-\mathcal E(T_p(z)h_-(z)).
\]

Use the tensor-product energy in the amplified carrier. The preceding identities give, without a zero assumption,

\[
\widehat\delta_p(z)
=\widehat{\mathcal E}(\mathcal J h_+(z))
-\widehat{\mathcal E}(\widehat T_p(z)\mathcal J h_-(z))
=\delta_p(z).
\]

Consequently the proposed native filler vanishes on the Xi fiber if and only if the old energy defect does. At a zero where the histories agree and have positive noncollapsed energy,

\[
\widehat\delta_p(z)=\delta_p(z)
=(1-p^{-2\Re z})\mathcal E(h_z).
\]

No independently unproved energy equation has been smuggled into the realization. Conversely, no new reason for this equation to vanish has been obtained. Any local regularity or ideal-membership properties of the scalar defect are unchanged; this tensor lift does not repair the prior nonreduced multiplicity obstruction.

A nonzero vector residual also survives: J r=0 iff r=0 and ||J r||=||r||. Thus isometric amplification cannot repair a failed source relation by relabeling it.

## 5. Why finite cyclic closure cannot replace Haar history

### An explicit periodic-target hostile

For one prime p let a=log p and define the normalized Haar-core functions

\[
e_n(q,r)=a^{-1}\mathbf1_{[na,(n+1)a)}(q)
                       \mathbf1_{[na,(n+1)a)}(r).
\]

They are orthonormal and S_a e_n=e_{n-1}. Each belongs to the mixed-Haar and relative-Haar energy-form domains. These discontinuous probes are not asserted to belong to a differential Evans-operator domain. A normalized smooth function supported strictly inside one square, with its translates, gives the same orthogonality and periodic-target obstruction. In particular

\[
\|S_a^{12}e_0-e_0\|^2=\|e_{-12}-e_0\|^2=2.
\]

If a proposed realization F intertwines this source action with a target W satisfying W^12=I, then

\[
F(S_a^{12}e_0-e_0)=(W^{12}-I)Fe_0=0.
\]

It cannot have a left inverse on this source domain. This applies, for example, if one identifies prime transport with the twelve-step-return operation of the **separate** Fourier phase-net model. The projector model is not being conflated with that model. Identifying prime transport with the identity action of a complete native retained-mode feedback cycle fails by the same argument already at one step.

The obstruction is loss of history, not failure of positive energy on the seam. Imposing a finite cyclic boundary on the logarithmic source would change that source.

### General fixed finite-unitary target

A nonzero translation S_a on L2(R2) has no L2 eigenvectors. Use coordinates t=q, d=r-q: translation sends t to t+a while d is fixed. An eigenvector would have |h(t,d)| periodic in t. Equal integrals over all translated strips force either zero or infinite total squared norm. Thus only the zero L2 vector can be an eigenvector.

Suppose a bounded F:H_E -> K, with K finite dimensional and W unitary, satisfies F S_a=W F on all of H_E. Taking adjoints and using both unitarities gives S_a F*=F* W. If F is nonzero, ran F* is a nonzero finite-dimensional S_a-invariant space. Its restriction has an eigenvector, contradicting the preceding result. Hence F=0. The reverse-direction bounded intertwiner K -> H_E likewise must be zero.

Scope: this is a statement about the full Haar representation, not just a selected non-invariant collection of Xi states. It does not exclude retaining an infinite history/parameter base, using a moving fiber, or using distributions with new domain proofs. The constructed J does retain that history and is therefore not a counterexample.

## 6. Exact tests versus general proofs

Run:

```text
python research/nima/checkers/check_1836_haar_reversible_amplification.py
```

The dependency-free exact-arithmetic checker:

1. Reconstructs native P,G,N from the source constraints, verifies ranks 12,3,1 and support counts 108,432,1296, and derives w from N rather than importing the old mode.
2. Checks the realization/recovery and Gram identities on three- and four-cell Haar cores. Normalization by sqrt(nu) is certified algebraically by J_unscaled* J_unscaled=nu I; no floating square root is used.
3. Checks prime intertwining between the distinct source cells {0,1,2} and target cells {-1,0,1,2}. The shift is rectangular and no endpoint is wrapped or silently truncated. Its reverse identity is asserted only on the transported subspace.
4. Retains a nonzero residual of squared norm 14 through realization and recovery.
5. Exhibits the norm-2 orbit difference killed by the period-12 quotient.
6. Checks positive reciprocal energy cancellation, but failure of one-step isometry away from the seam, for four primes and five centered real parts.
7. Checks exact scalar energy-defect preservation on 24 equal/different-history fixtures, and checks that unitarizing the prime step breaks intertwining away from the seam. Equal-history fixtures are not asserted to be actual Xi zeros.
8. Retains two off-seam controls strictly inside the critical strip: at p=2 choose the real amplitude a=4/5 or 5/4, so Re z=-log(a)/log(2) lies strictly between -1/2 and 1/2 because 1/2<a^2<2. A state of energy 14 has defect 126/25 or -63/8 respectively, unchanged by the native lift, although inverse transport recovers the state exactly. These are Haar-transport controls, not asserted Xi zeros or RH counterexamples.

Results: `results/1836-haar-reversible-amplification.json`.

The infinite-dimensional extension, exact scalar-defect identity, and finite-unitary obstruction follow from the displayed arguments, not extrapolation from finite tests. The checker does not construct or numerically evaluate Xi histories.

## Corrected next target

The type-to-object round trip is now explicitly available with the native retained mode. Adding more internal return witnesses does not change the arithmetic defect. To advance confinement one needs a source-derived relation between the two Xi history routes that independently proves equality of their prime energy readouts on the reduced zero fiber. Neither forgetting the history into a finite loop nor tensoring it with a reversible internal mode supplies that relation.

Sources:

- [Source-derived native constructor](lrg-1836.md).
- [Separate Fourier phase net](1836-phase-interaction-net.md).
- [Fixed-base versus diagonal prime squares](fixed-forcing-placement-and-diagonal-haar-transport-are-different-squares.md).
- [Energy equality, not vector invariance](correction-haar-cycle-closure-is-energy-equality-not-state-equality.md).
- [Nonreduced energy-ideal obstruction](haar-energy-ideal-coherence-would-add-a-zero-simplicity-theorem.md).
