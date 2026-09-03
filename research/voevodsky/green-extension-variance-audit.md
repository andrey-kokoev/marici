# Variance audit of the Stieltjes Green extension

## Question

Does the enlarged Stieltjes Green construction provide an actual over-extension classified by \(\operatorname{Map}(X,K[1])\), or an under-category embedding?

## Claim boundary

This packet audits only the bridge in `research/nima/the-stieltjes-incidence-closes-the-cyclic-prime-lift-but-not-its-enlarged-green-extension.md`. It does not prove the uniform Schur-return estimate or construct the full Green cell.

## Source data

For each prime, the proposed map is

\[
\iota_p:\mathcal G_p^{\rm cyc}\longrightarrow\mathcal G_p^{\rm full},
\]

where the full reduced Green form has block matrix

\[
G_p^{\rm full}=
\begin{pmatrix}
A_p&C_p\\
C_p^*&D_p
\end{pmatrix}.
\]

The required theorem asks that \(\iota_p\) preserve the polarized Green form, trace, radical separation, typed ports, and sewing.

## Over-extension test

A contravariantly classified extension requires a structured fiber sequence

\[
\mathcal G_p^{\rm aux}\longrightarrow E_p
\xrightarrow{\pi_p}
\mathcal G_p^{\rm cyc}
\]

with a declared projection, kernel identification, and structure-preserving pullback.

The vector-space decomposition of \(\mathcal G_p^{\rm full}\) supplies an algebraic coordinate projection, but the source does not establish that it is a morphism of polarized Green objects. Indeed, for \((x,u)\), the cross term \(C_pu\) contributes to pairing against cyclic vectors. Unless \(C_p=0\) on the relevant support, projection forgets structured pairing data. The weaker Schur condition \(\|K_p^{\rm return}\|<1\) preserves a lower bound but does not make the projection form-preserving.

Therefore the enlarged Green object is not presently an object of the over-extension sector.

## Under-attachment test

The declared arrow \(\iota_p:\mathcal G_p^{\rm cyc}\to\mathcal G_p^{\rm full}\) has under-category variance. It can be treated as an attachment under the cyclic object once the full object and embedding are constructed.

However, functorial pushout reindexing is not yet available: the category of polarized Green spaces has no declared pushouts preserving positivity, radicals, typed ports, and sewing. Thus this gives a typed under-object, not yet a covariant displayed functor.

## Strongest falsification attempt

Impose the exact-restriction condition

\[
C_pD_p^\dagger C_p^*=0.
\]

This makes the Schur correction vanish on the cyclic incidence range, but it still does not imply \(C_p=0\), a structured projection, or a source-derived kernel sequence. Hence even the strongest proposed decoupling condition does not automatically promote \(\iota_p\) to an over-extension.

Conversely, if one adds a Green-form-preserving projection \(\pi_p\) with \(\pi_p\iota_p=\mathrm{id}\), the sequence splits in the structured category and its ordinary extension class is trivial. The live datum is then the admissible embedding and Schur loading, not a nontrivial \(\operatorname{Ext}^1\) class.

## Disposition

The object called an enlarged Green extension is presently an under-category embedding problem. It does not supply the requested first example of \(\operatorname{Att}^{\rm over}\). This survives the revised two-sector architecture but sharpens the terminology:

- under sector: construct \(\iota_p\) and control Schur loading;
- over sector: require an independently sourced structured projection and kernel sequence.

The first obstruction is the absent structure-preserving projection \(\pi_p\), not displayed univalence.

## Verification

- `research/voevodsky/checkers/check_green_extension_variance.py`
- `research/voevodsky/results/green_extension_variance.json`
- `research/nima/the-stieltjes-incidence-closes-the-cyclic-prime-lift-but-not-its-enlarged-green-extension.md`
