# An independent projective tensor repairs the even-flag CP obstruction algebraically: WP957

## Question

WP956 proved that the even functional calculus of the single projective flag
operator cannot support three-family CP.  Is the obstruction intrinsic to
projective descent, or only to the one-generator algebra?

## Constructor

Retain the exact WP350 up operator and the sign-blind flag square

\[
Y_u=I+P+Q+R,\qquad B=P-Q,\qquad B^2=\operatorname{diag}(1/2,1/2,0).
\]

Add an independent rank-one projector

\[
W=\frac{ww^\dagger}{w^\dagger w},\qquad w=(1,2,i)^T,
\]

and define

\[
Y_d=2I+B^2+W.
\]

Both `B^2` and `W` are projective data: they are unchanged by `B -> -B` and
`w -> lambda w` for nonzero complex `lambda`.  Under a common weak-basis
change they transform by conjugation, so the Gram invariants descend.

## Exact result

The down characteristic discriminant is `575/1728`, hence its spectrum is
simple.  For the Gram pair the commutator has rank three and

\[
\operatorname{Tr}[H_u,H_d]^3=-\frac{12866425}{3456}i.
\]

Thus projective sign blindness does not itself forbid three-family CP.  The
WP956 obstruction was exactly the closure of the one-generator even algebra.

## Hostile control

Replacing `W` by the already-used projector `R` yields a simple down spectrum
but zero CP cubic.  Spectral splitting alone is therefore insufficient; the
second tensor must also be relationally independent of the up construction.

## Authority boundary

This is an algebraic existence result, not a flavor selector.  The vector `w`
was chosen as an exact hostile witness and is not derived from an admitted
source action, geometry, RG operation, threshold grammar, or instrument.
Nothing licenses its numerical coordinates.  The next gate is a source rule
that produces a second projective tensor independently of the desired readout,
then survives completion and has an experimentally typed probe.

No composition here is assigned physical time or causality.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp957_independent_projective_tensor_cp_sufficiency.py

Generated result: `research/flavor/results/wp957_independent_projective_tensor_cp_sufficiency.json`.
