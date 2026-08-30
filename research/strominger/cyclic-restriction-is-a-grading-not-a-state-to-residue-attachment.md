# Cyclic Restriction Is a Grading, Not a State-to-Residue Attachment

## Decisive typing correction

The restriction

\[
\mathcal H_l\big|_{C_n}\cong\mathbb C[C_n],
\qquad
l=2s-1,quad n=4s-1,
\]

is a correct representation-theoretic statement. It says that the harmonic carrier decomposes into one copy of each cyclic character:

\[
\mathcal H_l=\bigoplus_{r\in\mathbb Z/n}\mathcal H_{l,r},
\qquad
\dim_{\mathbb C}\mathcal H_{l,r}=1.
\]

It does not supply a function from physical states to residue classes.

Indeed, let (V) be any complex vector space and let

\[
f:(V,+)\longrightarrow\mathbb Z/n
\]

be additive. For any (v\in V), choose (w=v/n). Then

\[
f(v)=f(nw)=n f(w)=0.
\]

Thus every additive map from the state carrier to the finite label group is zero. In particular, no nontrivial linear or additive attachment

\[
\mathcal H_3\longrightarrow\mathbb Z/7
\]

can exist.

## Correct categorical object

The cyclic restriction provides spectral projectors

\[
P_r:\mathcal H_l\longrightarrow\mathcal H_{l,r}
\]

or, equivalently, a (C_n)-representation/coaction. A weight eigenvector lies in a labelled summand. A general physical state is a superposition across several summands and has no single residue label.

Therefore the relationship is

```text
physical harmonic carrier
  -> character-graded complex vector space
  -> family of spectral observation ports
```

and not

```text
physical state -> one finite residue
```

The affine cokernel can label the same abstract set of grades after choosing a comparison of cyclic generators. It does not follow that an affine lattice pair represents a physical state.

## Consequence for the five-primary conjecture

The formal reflected map

\[
(x,y)\longmapsto(3x-2y,3y-2x)
\]

acts on affine presentation classes. Its five-element kernel at (s\equiv4\pmod5) is therefore a kernel among grade labels or chart presentations. Cyclic restriction alone cannot promote those five representatives to five preparable state vectors.

This independently falsifies the strong Deutschean primitive-port conjecture. Even if a physical higher-spin carrier existed, the regular cyclic restriction would provide only its grading. A further source-derived correspondence would have to relate affine classes to spectral projectors, eigenspaces, or preparation procedures.

## Revised attachment problem

The missing constructor must have one of the following correctly typed forms:

1. a natural isomorphism between the affine residue set and the set of character projectors;
2. a coaction intertwiner between the boundary-operator carrier and the cyclic representation;
3. a preparation correspondence assigning an affine class to a nonzero state ray in the associated eigenspace;
4. an executable measurement whose outcomes are the projectors and whose action on the affine boundary data is derived independently.

Only the fourth form establishes operational distinguishability. None follows from equality of dimensions or regularity of the restricted representation.

## What remains true

The following facts survive unchanged:

- (lvert\det F_s\rvert=4s-1);
- (dim\mathcal H_{2s-1}=4s-1);
- restriction to (C_{4s-1}) is the regular representation;
- the reflected affine packet has a five-primary overlap exactly when (s\equiv4\pmod5).

What fails is the inference that these statements already provide a physical state-to-affine-class attachment.

## Evidence replay

The checker verifies the regular weight decomposition for (1\leq s\leq20) and records the divisibility proof excluding every nonzero additive map from the complex state carrier to a finite cyclic label group.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/cyclic_restriction_is_grading_not_state_map_checks.py
```

Machine-readable results are written to `research/strominger/results/cyclic_restriction_is_grading_not_state_map_checks.json`.
