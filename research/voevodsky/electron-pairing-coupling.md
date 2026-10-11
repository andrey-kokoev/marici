# Electron coupling: retained phase versus neutral pair vertex

## Question and claim boundary

Following the request to implement a coupling, inspect the existing retained attachment before adding an interaction. The active obligation is **attachment transport before charge readout**.

Conjecture: the existing phase registration already supplies opposite variable phase weights and can be carried into the new spinor construction.

Rivals: a frozen complex-linear frame map; a state-dependent charged phase link; and a new bilinear singlet vertex. These have different input types. No value of electrical charge is inferred from the previously failed sharp-charge flux test.

## 1. What the actual retained attachment does

The earlier attachment joins the original 1836-arrow vector protocol to its coefficient-conjugated copy. Its primitive port phases are

\[
D_a(v)=\frac{v_a}{\overline{v_a}},
\]

and every arrow satisfies

\[
hD_s=D_t\overline h.
\]

The new checker reconstructs all 1836 constraints on 108 connected typed ports from the retained source, rather than relying on the old result file.

When D is held fixed, it is complex-linear:

\[
D(\omega\overline v)=\omega v\ne\overline\omega v.
\]

All 108 ports reject interpreting this frozen map as conjugation of the freely varying amplitude. A fixed neutral intertwiner between two fields requires equal phase weights.

## 2. A source-anchored opposite-phase candidate

The primitive formula has another interpretation if evaluated on the actual field p=zv rather than frozen at the reference v:

\[
D(zv)=\frac{z}{\overline z}D(v).
\]

Under z→exp(iθ)z, this map acquires exp(2iθ). It has **phase weight two**. The matching equation

\[
D(p)e=p
\]

is then satisfied by e=conjugate(p), which has the opposite variable phase weight.

This identity works on the nonzero source mode line, where all port components are nonzero. The source's non-unit-amplitude control is included; this is not restricted to one selected root of unity.

Crucially, **both interpretations satisfy all 1836 arrow constraints**. Those equations determine only relative port phases. Dividing D(p) by its value at the retained root cancels z/conjugate(z), erasing exactly the common phase that distinguishes the charged-link interpretation.

Thus the existing formula supplies a candidate without fitting a new coefficient table, but the old normalized protocol does not select whether D is a fixed frame or a field-dependent attachment. The first missing rule is that choice of contract. The arrow equations alone cannot make it.

This calculation concerns the earlier vector/conjugate-vector attachment. It does not supply a map into the new eight-coordinate spinor carrier. Its one-dimensional selected source cannot simply be identified with a two-dimensional logical doublet.

## 3. The spinor coupling that would impose opposite weights

For two fundamental spinors, the rotation-invariant bilinear space is one-dimensional. Its representative is

\[
B(p,e)=p_0e_1-p_1e_0=p^T\epsilon e,
\qquad
\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Exact linear algebra over all 24 binary tetrahedral rotations verifies uniqueness up to scalar. The scalar linear intertwiner T=cI also exists and is unique up to scalar; symmetry alone does not choose between these two operations.

The bilinear phase law is

\[
B(e^{iq_p\theta}p,e^{iq_e\theta}e)
=e^{i(q_p+q_e)\theta}B(p,e).
\]

Therefore an independently neutral output requires q_e=−q_p. If q_p=+1 is supplied, q_e=−1 follows. The old geometric flux is not used to supply that normalization.

A corresponding equivariant antilinear relation is

\[
C=-\epsilon K,\qquad C^2=-I,
\]

where K conjugates the amplitude. It satisfies B(p,Cp)=||p||² and genuinely reverses variable phase. This is different from conjugating a fixed reference vector while retaining the same amplitude.

## 4. Two constraints on implementing that vertex

### The proton must also have a spinorial input

The old proton carrier is central-even under the double cover; the electron spinor is central-odd. One of each cannot contract to a central-even scalar.

An explicit repair is to tensor the proton's selected line with a spinor doublet. It changes coherent rank from one to two, typed ports from 108 to 216, and coefficient-transfer support from 1836 to **3672**. These are counts of a declared enlargement, not a physical mass calculation.

Using the retained embeddings, the proposed pair contraction expands to **576 nonzero bilinear monomials** between the enlarged proton and the eight-coordinate electron. They are binary-input terms, not 576 ordinary arrows in the existing linear grammar. The two logical singlet terms cannot stand in for the omitted raw interface.

### An antilinear state relation is not a deterministic spin-flip gate

On an unknown individual spinor density matrix, C induces a transpose map. Its normalized Choi matrix has eigenvalue **−1/2**, so it is not a completely positive quantum channel.

The normalized singlet contraction instead has a valid rank-one projector effect. It is a pair operation with a success subspace, not deterministic conjugation of one arbitrary input. This does not forbid charge conjugation on a larger particle/antiparticle field space; it rejects silently substituting that operation for the present one-spinor map.

## 5. The minimal mass attempt does not produce the required hierarchy

As a diagnostic, interpret the sole neutral off-diagonal pair as a quadratic species mass matrix:

\[
M=\begin{pmatrix}0&g\\g&0\end{pmatrix},
\qquad M^\dagger M=|g|^2I.
\]

Its two singular mass parameters are equal, and the scale g is free. This does not produce different proton and electron masses. It is a test of this particular additional mass interpretation, not a derivation of relativistic dynamics.

Antisymmetry of a spin contraction between distinct species also does not select fermionic exchange statistics.

## Disposition

The frozen-frame version of the conjecture is rejected. A retained, field-dependent common phase supplies a source-anchored **opposite-phase attachment candidate**, but the original coefficient constraints cannot distinguish it from the normalized frozen-frame rival.

For the spinor construction, a **neutral bilinear pair vertex** fixes opposite relative weights once its spinorial inputs and neutral output are supplied. It is an explicit new operation, not one already present in the old linear return. Neither this vertex nor the retained phase link fixes mass or statistics.

Reopening requires a source rule selecting the state-dependent attachment and transporting its phase action to the spinorial carriers, or a source-authorized binary neutral-output vertex with its embeddings. No further charge or mass claim is promoted by choosing the desired branch.

## Reproduction

```text
python research/voevodsky/checkers/check_electron_pairing_coupling.py
```

Seventeen exact checks pass. Artifact: `results/electron_pairing_coupling.json`. Source and prior spinor store remain unchanged. An intermediate run exposed a checker-order defect—root normalization was attempted before the root entry had been populated; normalization now runs after the complete table is built. It was not a scientific counterexample or a changed test.
