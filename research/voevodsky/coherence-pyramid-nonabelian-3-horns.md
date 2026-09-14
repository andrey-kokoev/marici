# Nonabelian 3-horns expose the whiskering gate

## Question

What replaces additive horn solving when planes compose noncommutatively?

## Claim boundary

This packet uses the finite group \(S_3\) as a nonabelian plane-label model. It tests the algebra required by categorical pasting; it does not construct the full coherence-pyramid 2-category.

## Pasting equation

Let \(L\) and \(R\) denote the left- and right-whiskering maps acting on plane labels. Tetrahedral coherence has the form

\[
R(h_{234})h_{124}=L(h_{123})h_{134}.
\]

If plane composition is invertible, define the required target

\[
y=L(h_{123})h_{134}h_{124}^{-1}.
\]

Recovering the missing face is then the lifting problem

\[
R(h_{234})=y.
\]

## Exact classification

The horn properties are properties of \(R\) at the required target:

- a filler exists exactly when \(y\) lies in the image of \(R\);
- the filler is unique exactly when the fiber of \(R\) over \(y\) is a singleton;
- invertible whiskering gives a unique filler

\[
h_{234}=R^{-1}(y).
\]

The checker instantiates \(R\) as conjugation in \(S_3\), recovers one missing face, and verifies the noncommutative pasting equation exactly.

## Hostile whiskering

For the nonfaithful map sending every plane label to the identity:

- a nonidentity target has no filler;
- the identity target has all six elements of \(S_3\) as fillers.

The same failure of whiskering therefore produces either nonexistence or ambiguity, depending on the target.

## Changed claim

The additive equation made unique horn filling look automatic because multiplication by \(1\) or \(-1\) is invertible. In the categorical form, the missing plane is not recovered merely from the tetrahedral equation. Recovery requires the relevant whiskering map to have a singleton fiber over the required pasted target.

## Disposition

The next typed obligation for the coherence pyramid is now explicit: for each proposed horn, construct the relevant whiskering functor and determine the required target's fiber. Declaring four planes and a tetrahedral equation does not prove a horn filler exists.

## Verification

```text
python research/voevodsky/checkers/check_coherence_pyramid_nonabelian_3_horns.py
```

Artifacts:

- `research/voevodsky/checkers/check_coherence_pyramid_nonabelian_3_horns.py`
- `research/voevodsky/results/coherence_pyramid_nonabelian_3_horns.json`
