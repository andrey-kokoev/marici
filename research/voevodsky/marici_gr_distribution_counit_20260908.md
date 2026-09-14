# GR distribution counit for the Marici formal vector prestack

Date: 2026-09-08

## Construction

Let `X=Spec B` and regard the strict target `D_k` as an object of `IndCoh(X)`. Define

\[
\mathfrak X_k=\operatorname{Vect}_X(D_k).
\]

Gaitsgory–Rozenblyum, Volume II, Chapter 7, Proposition 1.4.7 proves that the counit

\[
\operatorname{Distr}^{\mathrm{Cocom}}_{\mathrm{aug}}
 (\operatorname{Vect}_X(F))\longrightarrow\operatorname{Sym}(F)
\]

is an isomorphism. Therefore

\[
\operatorname{Distr}^{\mathrm{Cocom}}_{\mathrm{aug}}(\mathfrak X_k)
\simeq \operatorname{Sym}^{c}_{!}(D_k).
\]

Here the symmetric object is an augmented cocommutative coalgebra for the `!`-tensor structure. Its augmentation is the canonical formal-fiber distribution counit

\[
\epsilon_{\mathrm{fib}}:\operatorname{Sym}^{c}_{!}(D_k)\to\omega_X.
\]

It is identity on symmetric weight zero and zero on every positive symmetric weight. This is exactly the first arrow left speculative in the earlier sweep; no properness of an affine fiber and no dualization of `D_k` are required.

Compose with conductor support and the already normalized node residue:

\[
R\Gamma_{\mathfrak m}\operatorname{Distr}(\mathfrak X_k)
\xrightarrow{R\Gamma_{\mathfrak m}(\epsilon_{\mathrm{fib}})}
R\Gamma_{\mathfrak m}(\omega_B)
\xrightarrow{\operatorname{Res}_{0,2,4,1,3,5}}
C\Pi^{\otimes ?}.
\]


## Q-closure

The strict differential on `D_k` induces a linear coderivation of its symmetric coalgebra. It preserves symmetric weight, has no constant term, and is zero on the weight-zero dualizing unit. Consequently

\[
\epsilon_{\mathrm{fib}}Q=0.
\]

The conductor residue is already closed for the node dual differential. Their composite is therefore a Q-closed supported distribution functional. The same argument applies to `D35` and `D04`, and the eight strict spatial maps are compatible by functoriality.

## Boundary

This does **not** yet give Bruce's trace on functions. It is a functional on the distribution coalgebra and kills positive formal-fiber symmetric weights. A bridge from the function-side Bruce product to this distributional functional requires a pairing between functions and distributions, a declared class of functions/completion, and an integration-by-parts theorem. In particular no nonzero P24 deformation value follows from the counit alone.

## Verification

```sh
python research/voevodsky/check_marici_gr_distribution_counit_20260908.py \
  --root . \
  --output research/voevodsky/marici_gr_distribution_counit_certificate_20260908.json
```

The integration audit performs 65 checks and explicitly records that P24 detection remains unproved.
