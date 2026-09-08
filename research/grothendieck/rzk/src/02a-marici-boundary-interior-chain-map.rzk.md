# Conditional boundary-interior chain map

## Question and claim boundary

Formalize Section 3 of `research/chatgpt/boundary-interior/boundary_interior_extension.md`.
This is a degree-local theorem, universally parameterized by the three interior
and two overlap degrees needed for the equation. Apply it at each cohomological
degree of the supplied complexes. No integer grading implementation is needed.

Inputs are the chart chain-map law, discrepancy chain-map law, additive
subtraction laws, annihilation of the primitive projection by the discrepancy,
and the contraction identity in the rearranged form dH = (1 - Hd) - i epsilon.
The target chain-map equation and the overlap homotopy are not assumptions.
The matrices, square-zero laws, physical comparison, and global assembly of
these degree windows are not verified here. Subtraction laws below hold in
abelian groups; they are explicit hypotheses, not newly derived group axioms.

```rzk
#lang rzk-1

#section marici-boundary-interior-window
#variable Im : U
#variable I : U
#variable Ip : U
#variable Vm : U
#variable Vp : U
#variable Em : U
#variable E : U
#variable di : I -> Ip
#variable dm : Im -> I
#variable h : I -> Im
#variable hp : Ip -> I
#variable c : I -> I
#variable rho : I -> Vm
#variable rhop : Ip -> Vp
#variable dv : Vm -> Vp
#variable delta : Vm -> E
#variable m : I -> E
#variable mm : Im -> Em
#variable de : Em -> E
#variable si : I -> I -> I
#variable se : E -> E -> E
#variable ze : E
#variable contraction : (x : I) -> dm (h x) = si (si x (hp (di x))) (c x)
#variable m-sub : (x y : I) -> m (si x y) = se (m x) (m y)
#variable m-primitive-zero : (x : I) -> m (c x) = ze
#variable sub-zero : (u : E) -> se u ze = u
#variable sub-sub : (u v : E) -> se u (se u v) = v
#variable m-chain : (y : Im) -> de (mm y) = m (dm y)
#variable discrepancy : (x : I) -> delta (rho x) = m x
#variable rho-chain : (x : I) -> dv (rho x) = rhop (di x)

#define marici-bi-ell uses (Im) (x : I) : Em := mm (h x)
#define marici-bi-ell-next uses (I) (y : Ip) : E := m (hp y)

#define marici-bi-contracted-discrepancy uses (Im Ip) (x : I)
  : m (dm (h x)) = se (m x) (m (hp (di x)))
  := concat E
    (m (dm (h x))) (m (si (si x (hp (di x))) (c x))) (se (m x) (m (hp (di x))))
    (ap I E (dm (h x)) (si (si x (hp (di x))) (c x)) m (contraction x))
    (concat E
      (m (si (si x (hp (di x))) (c x)))
      (se (m (si x (hp (di x)))) (m (c x))) (se (m x) (m (hp (di x))))
      (m-sub (si x (hp (di x))) (c x))
      (concat E
        (se (m (si x (hp (di x)))) (m (c x)))
        (se (se (m x) (m (hp (di x)))) (m (c x))) (se (m x) (m (hp (di x))))
        (ap E E (m (si x (hp (di x)))) (se (m x) (m (hp (di x))))
          (\ u -> se u (m (c x))) (m-sub x (hp (di x))))
        (concat E
          (se (se (m x) (m (hp (di x)))) (m (c x)))
          (se (se (m x) (m (hp (di x)))) ze) (se (m x) (m (hp (di x))))
          (ap E E (m (c x)) ze (se (se (m x) (m (hp (di x))))) (m-primitive-zero x))
          (sub-zero (se (m x) (m (hp (di x))))))))

#define marici-bi-overlap-homotopy uses (Im I Ip Em E di h hp m mm de se ze c si contraction m-sub m-primitive-zero sub-zero) (x : I)
  : de (marici-bi-ell x) = se (m x) (marici-bi-ell-next (di x))
  := concat E (de (marici-bi-ell x)) (m (dm (h x)))
    (se (m x) (marici-bi-ell-next (di x)))
    (m-chain (h x)) (marici-bi-contracted-discrepancy x)

#define marici-bi-edge-equation uses (Im I Ip Vm Em E di h hp rho delta m mm de se ze c si dm contraction m-sub m-primitive-zero sub-zero m-chain) (x : I)
  : se (delta (rho x)) (de (marici-bi-ell x)) = marici-bi-ell-next (di x)
  := concat E
    (se (delta (rho x)) (de (marici-bi-ell x)))
    (se (m x) (de (marici-bi-ell x))) (marici-bi-ell-next (di x))
    (ap E E (delta (rho x)) (m x) (\ u -> se u (de (marici-bi-ell x))) (discrepancy x))
    (concat E (se (m x) (de (marici-bi-ell x)))
      (se (m x) (se (m x) (marici-bi-ell-next (di x)))) (marici-bi-ell-next (di x))
      (ap E E (de (marici-bi-ell x)) (se (m x) (marici-bi-ell-next (di x)))
        (se (m x)) (marici-bi-overlap-homotopy x))
      (sub-sub (m x) (marici-bi-ell-next (di x))))

#define marici-bi-Phi uses (Im mm h) (x : I) : Sigma (_ : Vm), Em
  := (rho x, marici-bi-ell x)
#define marici-bi-Phi-next uses (I m hp) (y : Ip) : Sigma (_ : Vp), E
  := (rhop y, marici-bi-ell-next y)
#define marici-bi-D (b : Sigma (_ : Vm), Em) : Sigma (_ : Vp), E
  := (dv (first b), se (delta (first b)) (de (second b)))

#define marici-bi-DPhi-equals-Phi-d uses (Im I Ip Vm Vp Em E di h hp rho rhop dv delta m mm de se ze c si dm contraction m-sub m-primitive-zero sub-zero sub-sub m-chain discrepancy rho-chain) (x : I)
  : marici-bi-D (marici-bi-Phi x) = marici-bi-Phi-next (di x)
  := marici-assemble-from-filler I Ip Vm Vp Em E
    di dv de rho rhop delta marici-bi-ell marici-bi-ell-next se sub-sub rho-chain
    (\ y -> concat E (de (marici-bi-ell y))
      (se (m y) (marici-bi-ell-next (di y)))
      (se (delta (rho y)) (marici-bi-ell-next (di y)))
      (marici-bi-overlap-homotopy y)
      (ap E E (m y) (delta (rho y))
        (\ u -> se u (marici-bi-ell-next (di y)))
        (rev E (delta (rho y)) (m y) (discrepancy y)))) x
#end marici-boundary-interior-window
```

## Disposition

The proof constructs ell = m H and Phi = (rho, ell); it does not infer strict
overlap agreement. Fresh headless Rzk verification passed (exit 0, `Everything
is ok!`) on 2026-09-06. The closure consists of pinned sHoTT commit
`52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2` files `src/hott/00-common.rzk.md`
and `src/hott/01-paths.rzk.md`, followed by `02a-boundary-interfaces.rzk.md`
and this file, passed as explicit arguments to `rzk typecheck`.
The final theorem now invokes `marici-assemble-from-filler`; contraction is
only the producer of its homotopy witness. Localization, filtration, and
symmetry certificates remain separate from this theorem. Shell execution was explicitly authorized by the
operator after structured-command refused direct Rzk execution. Initial
failures exposed grouped-variable syntax, unsupported inference placeholders,
and missing section dependency declarations; these were repaired without
adding mathematical hypotheses. This certifies the conditional degree-local
path theorem, not the source matrices or their physical interpretation.
