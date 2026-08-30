# Spectral-projector selector (WP323)

## Relational source operation

Let the Hermitian reference have spectrum ((-1,0,1)). Its negative-eigenspace
projector is the polynomial

\[
p_-(X)=\frac{X(X-I)}{2}.
\]

For binary Hermitian projectors (B) diagonal in the reference frame, define

\[
V_X(B)=\operatorname{Tr}\left[(B-p_-(X))^2\right].
\]

This positive energy has the unique zero-energy solution (B=p_-(X)). The
checker enumerates all eight binary occupancies and verifies that the other
seven have strictly positive integer energy.

## Descent and classification

Under simultaneous conjugation, (X), (p_-(X)), and (B) transform
covariantly, while (V_X(B)) is invariant. The selector therefore descends on
the relational quotient of pairs ((X,B)).

It is both a presentation rigidifier and a genuine selector conditional on
the reference. It is not an absolute generation selector: swapping reference
eigenvectors changes the literal selected word while preserving the relational
pair. The spectrum of (X) and the choice of its negative spectral subspace
carry source authority.

## Remaining gate

A physical claim requires a source-derived field (X), its nondegenerate
spectrum, a binary field (B), and an executable positive coupling realizing
the potential. No map from this selected projector to flux magnitude 64 or to
`physical16` has been supplied.

Run `uv run --with sympy python
research/flavor/checkers/wp323_spectral_projector_selector.py` to regenerate
the exact audit.
