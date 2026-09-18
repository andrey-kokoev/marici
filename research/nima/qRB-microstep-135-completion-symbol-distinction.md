# qRB microstep 135: completion-symbol distinction

There are two different completion symbols:

1. the shifted-Gaussian section, whose endpoint term is

$$
 e^{t/4-t\xi^2}\cos(t\xi);
$$

2. the character-weighted centered section, whose endpoint term is

$$
 e^{t/4}\cosh(d/2).
$$

They are related by the imaginary-character pullback and gauge transformation, but they are not interchangeable pointwise on real parameters.

Therefore the all-character positivity test must first specify which section represents the translate Gram. Substituting the shifted symbol into the centered character test would create a normalization error.

Status: completion-symbol ambiguity removed; the character-section gamma and endpoint package is the correct input for the translate-Gram interface.
