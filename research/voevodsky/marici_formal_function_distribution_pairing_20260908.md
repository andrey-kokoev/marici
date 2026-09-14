# Formal functions, distributions, and the canonical-trace no-go

Date: 2026-09-08

## Canonical pairing

For

\[
\mathfrak X_k=\operatorname{Vect}_X(D_k),
\qquad
\operatorname{Distr}(\mathfrak X_k)\simeq\operatorname{Sym}^{c}_{!}(D_k),
\]

define formal functions intrinsically as the continuous IndCoh dual

\[
\mathcal O^{\mathrm{cont}}(\mathfrak X_k)
=
\operatorname{Hom}_{\operatorname{IndCoh}(X)}
(\operatorname{Sym}^{c}_{!}(D_k),\omega_X).
\]

When the relevant pieces are dualizable this is the completed symmetric algebra on the dual; the continuous-dual definition remains meaningful without pretending that the conductor-supported complex is perfect. Evaluation gives the canonical function/distribution pairing.

The weight-zero distribution is the zero-section delta distribution. Pairing against it and then applying the conductor residue defines the canonical vacuum trace.

## Q-closure and Bruce trace

The strict `Q` is linear and preserves symmetric weight. It kills the weight-zero unit. Therefore the vacuum trace is Q-closed. It satisfies the formal integration-by-parts identity, and hence is a valid shifted trace for Bruce's derived product.

However, it annihilates every Bruce product. If `a,b` have symmetric weights `i,j`, then `Q(a)b` has weight `i+j`. Vacuum evaluation can survive only when `i=j=0`, but `Q` vanishes there. Thus

\[
\tau_0(a\star b)=0
\]

for all formal functions.

## P24 consequence

The currently constructed outer-operation action is also linear and weight-preserving. For the P24 expression

\[
\phi_X(f_0,f_1)
=
\tau_0((-1)^{|f_0|}X(f_0f_1)),
\]

`X(f0 f1)` has the same positive weight as `f0 f1`, while `X` kills weight-zero constants. Hence

\[
\boxed{\phi_X=0}
\]

identically for the canonical vacuum trace and the current linear outer action.

This is not a failure to define the function/distribution pairing; that pairing is canonical. It is a no-go for extracting the desired nonzero P24 class from the purely linear formal-vector model with its canonical zero-section distribution.

## Required additional datum

A nonzero P24 value requires at least one of:

1. a non-vacuum Q-closed distribution with positive fiber moments;
2. an outer vector field with a weight-lowering translation/contraction term;
3. nonlinear terms in `Q` or a nonlinear formal geometry;
4. a separately specified compact/proper fiber integration not concentrated at the zero section.

Any candidate must retain conductor residue, reflection/polarity, operation bars and support. The next search should therefore target the physical outer field for a constant or contraction component, rather than seek another version of the already canonical vacuum pairing.

## Verification

```sh
python research/voevodsky/check_marici_formal_function_distribution_pairing_20260908.py \
  --root . \
  --output research/voevodsky/marici_formal_function_distribution_pairing_certificate_20260908.json
```

The checker audits all fiber-weight pairs from zero through six and performs 98 exact weight checks.
