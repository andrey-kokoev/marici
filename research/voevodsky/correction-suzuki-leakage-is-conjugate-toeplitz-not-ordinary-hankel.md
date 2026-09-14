# Correction: Suzuki leakage is conjugate-Toeplitz, not an ordinary Hankel operator

## Error corrected

The note `closed-range-hankel-theory-splits-the-suzuki-coercivity-gate.md` classified

\[
L=P_-K|_{H_+},
\qquad
K=\mathcal F^{-1}M_\Theta J\mathcal F,
\]

as though it were the ordinary linear Hankel compression `P_- M_Theta|H_+`. This drops the essential conjugation/reflection `J`.

That classification is not valid. The compact-Hankel/Hartman fork stated there does not apply directly to Suzuki's leakage and must not be used.

## Correct Hardy typing

Boundary conjugation exchanges the two Hardy half-spaces:

\[
J:H_+\longrightarrow H_-.
\]

Therefore the frequency-side leakage has the form

\[
L_\Theta=P_-M_\Theta J|_{H_+}.
\]

It is conjugate-linear from `H_+` to `H_-`. After composing with the natural antiunitary identification of `H_-` with `H_+`, it becomes a Toeplitz-type compression, equivalent up to convention to

\[
T_{\bar\Theta}=P_+M_{\bar\Theta}|_{H_+},
\]

not to the Hankel operator `P_-M_Theta|H_+`.

This typing is forced by Suzuki's model-space result: under innerness, the kernel of the linearized leakage is the model space

\[
K(\Theta)=H^2\ominus\Theta H^2,
\]

and the standard identity is

\[
K(\Theta)=\ker T_{\bar\Theta}.
\]

## Inner case is closed-range, not compact infinite-rank

If `Theta` is inner, multiplication

\[
T_\Theta:H^2\to H^2,
\qquad f\mapsto\Theta f,
\]

is an isometry and

\[
T_{\bar\Theta}=T_\Theta^*.
\]

Hence

\[
T_{\bar\Theta}T_\Theta=I.
\]

Therefore `T_barTheta` is a coisometry and is surjective. In particular,

\[
\boxed{
\operatorname{ran}T_{\bar\Theta}=H^2
\quad\text{and the range is closed.}
}
\]

Its kernel is exactly `K(Theta)`. Thus under the RH/Hermite--Biehler condition, the desired closed-range property holds in the strongest possible form.

This contradicts the heuristic suggestion that infinite oscillation of `Theta` should make the relevant leakage compact infinite-rank and nonclosed-range. That suggestion arose from using the wrong operator class.

## Projection formula in the inner case

For a coisometry `L` with `LL^*=I`, the short formula simplifies to

\[
P_{\ker L}=I-L^*L.
\]

Applied to `L=T_barTheta`,

\[
\boxed{
P_{K(\Theta)}=I-T_\Theta T_{\bar\Theta}.
}
\]

This is the standard model-space projection. Its reproducing kernel is

\[
k_\Theta(z,w)
=
\frac{1-\Theta(z)\overline{\Theta(w)}}{-i(z-\bar w)}
\]

up to normalization. Therefore the earlier projected-resolvent construction correctly recovers the de Branges--Rovnyak kernel under innerness, but through a Toeplitz coisometry rather than a Hankel pseudoinverse.

## Non-inner meromorphic case

Boundary unimodularity still makes multiplication by `Theta` unitary on `L^2`, but `Theta` need not define an analytic Hardy multiplier. The Toeplitz compression `T_barTheta` remains bounded from its `L^infinity` boundary symbol, while the identities

\[
T_{\bar\Theta}=T_\Theta^*,
\qquad
T_{\bar\Theta}T_\Theta=I
\]

cannot be interpreted using analytic multiplication `T_Theta f=Theta f` unless `Theta in H^infinity`.

The correct unconditional questions are therefore:

1. is the conjugate-Toeplitz leakage `L_Theta` surjective or at least closed-range?
2. what is `ker L_Theta`?
3. does the source image lie in that kernel?
4. can `LL*` be identified from endpoint--gamma--prime data?

These are Wiener--Hopf/Toeplitz factorization questions, not Hartman compactness questions.

## Role of the no-limit theorem

The proof that `Theta(x)` has no limit at infinity remains correct. It rules out raw continuity on the compactified line, but it says nothing adverse about analytic innerness: nonconstant inner functions commonly have oscillatory unimodular boundary values. Under RH, `Theta` is precisely such an inner function.

Thus the no-limit result cannot be used as evidence against closed range of Suzuki's actual leakage.

## Corrected analytic fork

The relevant symbol theorem is a Wiener--Hopf factorization

\[
\Theta=\Theta_-^{-1}D\Theta_+,
\]

where `Theta_+` and `Theta_-` are bounded analytic factors in opposite half-planes and `D` carries the index/divisor. Closed range and Fredholm behavior of the Toeplitz compression are controlled by factorization and corona bounds for these factors.

For the completed-zeta symbol, producing this factorization without extracting the forbidden divisor remains the analytic gate. In the inner case it collapses to the coisometric model above.

## Disposition

The correct operator identity is

\[
\boxed{
\text{Suzuki leakage}
\sim
T_{\bar\Theta},
\quad
\text{not an ordinary Hankel operator}.
}
\]

Accordingly:

- withdraw the compact-infinite-rank closed-range obstruction for this operator;
- retain the projection-short formulas as general Hilbert identities;
- replace Hartman-symbol analysis by Toeplitz/Wiener--Hopf factorization;
- under innerness, use the exact coisometry and model-space projection formulas.
