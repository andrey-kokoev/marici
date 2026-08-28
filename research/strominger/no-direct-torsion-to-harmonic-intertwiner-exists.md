# No Direct Torsion-to-Harmonic Intertwiner Exists

## No-go theorem

Let

\[
A_s=\operatorname{coker}F_s\cong\mathbb Z/(4s-1)
\]

be the affine discriminant group and let (mathcal H_{2s-1}) be the complex harmonic carrier. There is no nonzero additive attachment in either direction.

If (f:A_s\to\mathcal H_{2s-1}) is additive, every (a\in A_s) obeys (na=0), where (n=4s-1). Hence

\[
n f(a)=f(na)=0.
\]

The additive group of a complex vector space is torsion-free, so (f(a)=0).

Conversely, every additive map (mathcal H_{2s-1}\to A_s) is zero by divisibility of the complex vector space. Complexifying the affine group does not help:

\[
A_s\otimes_{\mathbb Z}\mathbb C=0,
\]

because (n) becomes invertible.

Therefore the desired intertwiner

\[
T:B_{\mathrm{aff}}\longrightarrow\mathcal H_{2s-1}
\]

cannot use the torsion cokernel itself as (B_{\mathrm{aff}}).

## The required extra constructor

One can manufacture a vector carrier by applying the free complex vector-space functor:

\[
A_s\longmapsto\mathbb C[A_s].
\]

This group algebra has dimension (n) and carries the regular cyclic representation, so an equivariant isomorphism

\[
\mathbb C[A_s]\cong\mathcal H_{2s-1}|_{C_n}
\]

exists.

But this is a new constructor. It replaces finite charge labels with arbitrary complex superpositions of formal basis vectors. Mathematical functoriality does not establish that these formal superpositions are the physical harmonic amplitudes.

## Symmetry does not select the intertwiner

Cyclic equivariance alone leaves an (n)-dimensional commutant: every circulant convolution is an equivariant endomorphism of the regular representation.

Adding reflection reduces but does not remove the ambiguity. For odd (n), matrices commuting with the dihedral permutation action are constant on the inversion orbits of cyclic differences. Their parameter count is

\[
\frac{n+1}{2}.
\]

At spin two, (n=7), reflection still leaves a four-dimensional family. Hence rotation and reflection symmetry do not canonically determine (T).

If one additionally demands that each labelled character line map to the identically labelled harmonic line, (T) remains diagonal in the character basis. Reflection pairs the coefficients at (r) and (-r), again leaving four independent normalizations at (n=7). A source pairing, cyclic vector, amplitude normalization, or executable preparation rule is required to select one.

## Aspect disposition

The group-algebra proposal is well typed, has a discriminating target, and is nonredundant. It presently fails source provenance: no Bondi constructor turns affine torsion classes into a physical complex superposition carrier. It also lacks an operational witness and bounded physical test.

Under Aspect's updated admission governance, the proposal is therefore `reject`, not merely `defer`. The smaller set-level projector-label candidate remains deferred; the stronger linear intertwiner is rejected until a source-authorized linearization is supplied.

This separates two missing steps:

```text
affine odd residue set
  -> character-projector labels             deferred

affine torsion group
  -> physical complex harmonic carrier      rejected
       requires source-authorized linearization and normalization
```

## Consequence

The equality

\[
\lvert A_s\rvert=\dim_{\mathbb C}\mathcal H_{2s-1}
\]

does not provide a linear attachment. It compares cardinality of a finite group with dimension of a vector space—different invariants in different categories. Passing from one to the other is exactly the constructor that had been hidden.

## Evidence replay

The checker records the two additive no-go proofs, the vanishing complexification, and the cyclic and reflection-equivariant commutant dimensions for (1\leq s\leq20). It also applies Aspect's updated six-gate disposition.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/torsion_to_harmonic_intertwiner_no_go_checks.py
```

Machine-readable results are written to `research/strominger/results/torsion_to_harmonic_intertwiner_no_go_checks.json`.
