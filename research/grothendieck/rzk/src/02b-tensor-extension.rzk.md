# Conditional tensor extension

## Question and boundary

Formalize tensoring a supplied chain map with the identity endpoint map, and
the signed contraction calculation from Section 4 of
`research/chatgpt/rees-physical-extension/rees_physical_extension.md`.
The tensor types, Leibniz equations, addition/subtraction laws, and signed
expansion laws are explicit inputs. They are not a constructed tensor-product
library or a physical comparison. The degree-local chain theorem works on
pure tensors; a separate, universally quantified detection interface is
required for promotion to all elements. No finite sample supplies detection.

```rzk
#lang rzk-1

#define marici-ap-binary
  (X Y Z : U) (f : X -> Y -> Z)
  (x x' : X) (y y' : Y) (p : x = x') (q : y = y')
  : f x y = f x' y'
  := concat Z (f x y) (f x' y) (f x' y')
    (ap X Z x x' (\ a -> f a y) p)
    (ap Y Z y y' (f x') q)

#define marici-tensor-chain-on-generators
  (A Ap B Bp E Ep T Tp V Vp : U)
  (da : A -> Ap) (db : B -> Bp) (de : E -> Ep)
  (f : A -> B) (fp : Ap -> Bp)
  (t : A -> E -> T) (tl : Ap -> E -> Tp) (tr : A -> Ep -> Tp)
  (v : B -> E -> V) (vl : Bp -> E -> Vp) (vr : B -> Ep -> Vp)
  (dt : T -> Tp) (dv : V -> Vp) (F : T -> V) (Fp : Tp -> Vp)
  (at : Tp -> Tp -> Tp) (av : Vp -> Vp -> Vp)
  (st : Tp -> Tp) (sv : Vp -> Vp)
  (chain : (a : A) -> db (f a) = fp (da a))
  (leibniz-t : (a : A) -> (e : E) -> dt (t a e) = at (tl (da a) e) (st (tr a (de e))))
  (leibniz-v : (b : B) -> (e : E) -> dv (v b e) = av (vl (db b) e) (sv (vr b (de e))))
  (F-pure : (a : A) -> (e : E) -> F (t a e) = v (f a) e)
  (Fp-left : (a : Ap) -> (e : E) -> Fp (tl a e) = vl (fp a) e)
  (Fp-right : (a : A) -> (e : Ep) -> Fp (tr a e) = vr (f a) e)
  (Fp-add : (x y : Tp) -> Fp (at x y) = av (Fp x) (Fp y))
  (Fp-sign : (x : Tp) -> Fp (st x) = sv (Fp x))
  (a : A) (e : E)
  : Fp (dt (t a e)) = dv (F (t a e))
  := concat Vp (Fp (dt (t a e)))
    (av (vl (fp (da a)) e) (sv (vr (f a) (de e)))) (dv (F (t a e)))
    (concat Vp (Fp (dt (t a e)))
      (Fp (at (tl (da a) e) (st (tr a (de e)))))
      (av (vl (fp (da a)) e) (sv (vr (f a) (de e))))
      (ap Tp Vp (dt (t a e)) (at (tl (da a) e) (st (tr a (de e)))) Fp (leibniz-t a e))
      (concat Vp (Fp (at (tl (da a) e) (st (tr a (de e)))))
        (av (Fp (tl (da a) e)) (Fp (st (tr a (de e)))))
        (av (vl (fp (da a)) e) (sv (vr (f a) (de e))))
        (Fp-add (tl (da a) e) (st (tr a (de e))))
        (marici-ap-binary Vp Vp Vp av
          (Fp (tl (da a) e)) (vl (fp (da a)) e)
          (Fp (st (tr a (de e)))) (sv (vr (f a) (de e)))
          (Fp-left (da a) e)
          (concat Vp (Fp (st (tr a (de e)))) (sv (Fp (tr a (de e)))) (sv (vr (f a) (de e)))
            (Fp-sign (tr a (de e)))
            (ap Vp Vp (Fp (tr a (de e))) (vr (f a) (de e)) sv (Fp-right a (de e)))))))
    (rev Vp (dv (F (t a e))) (av (vl (fp (da a)) e) (sv (vr (f a) (de e))))
      (concat Vp (dv (F (t a e))) (dv (v (f a) e))
        (av (vl (fp (da a)) e) (sv (vr (f a) (de e))))
        (ap V Vp (F (t a e)) (v (f a) e) dv (F-pure a e))
        (concat Vp (dv (v (f a) e))
          (av (vl (db (f a)) e) (sv (vr (f a) (de e))))
          (av (vl (fp (da a)) e) (sv (vr (f a) (de e))))
          (leibniz-v (f a) e)
          (ap Bp Vp (db (f a)) (fp (da a))
            (\ b -> av (vl b e) (sv (vr (f a) (de e)))) (chain a)))))
```

The operators st and sv represent the same Koszul parity on corresponding
right-factor summands. Fp-sign is required; neither a grading nor its sign is
silently erased. For Psi = Phi tensor identity, chain is the supplied Phi
chain-map law. This proves the tensor inference independently of how Phi's
filler was constructed.

## Extending generator equations

```rzk
#define marici-additive-map
  (T V : U) (zt : T) (zv : V) (at : T -> T -> T) (av : V -> V -> V)
  (f : T -> V) : U
  := Sigma (_ : f zt = zv), (x y : T) -> f (at x y) = av (f x) (f y)

#define marici-additive-generator-detection
  (P T V : U) (gen : P -> T) (zt : T) (zv : V)
  (at : T -> T -> T) (av : V -> V -> V) : U
  := (u v : T -> V) ->
     marici-additive-map T V zt zv at av u ->
     marici-additive-map T V zt zv at av v ->
     ((p : P) -> u (gen p) = v (gen p)) ->
     (x : T) -> u x = v x

#define marici-extend-tensor-equation
  (P T V : U) (gen : P -> T) (zt : T) (zv : V)
  (at : T -> T -> T) (av : V -> V -> V)
  (detect : marici-additive-generator-detection P T V gen zt zv at av)
  (u v : T -> V)
  (u-add : marici-additive-map T V zt zv at av u)
  (v-add : marici-additive-map T V zt zv at av v)
  (on-generators : (p : P) -> u (gen p) = v (gen p))
  (x : T) : u x = v x
  := detect u v u-add v-add on-generators x
```

P must index all relevant pure tensors in the declared total degree, including
all bidegrees, not an arbitrary tested subset. Detection is a source-presentation
obligation: this file does not claim to derive it from sampled generators.

## Signed contraction on generators

Write DH and HD for the two composites at one total degree. The two expansion
hypotheses retain the mixed term with opposite signs. In an actual cochain
tensor these follow from H(a tensor e)=(-1)^degree(a) a tensor h(e) and Leibniz.
We require those expansions explicitly rather than assume their cancellation
or claim to have implemented integer-indexed tensor grading.

```rzk
#define marici-tensor-contraction-on-generators
  (A E T : U) (t : A -> E -> T)
  (ae : E -> E -> E) (se : E -> E -> E)
  (at : T -> T -> T) (st : T -> T -> T)
  (dh hd projection : E -> E) (DH HD : T -> T) (mixed : A -> E -> T)
  (endpoint : (e : E) -> ae (dh e) (hd e) = se e (projection e))
  (tensor-add : (a : A) -> (e f : E) -> t a (ae e f) = at (t a e) (t a f))
  (tensor-sub : (a : A) -> (e f : E) -> t a (se e f) = st (t a e) (t a f))
  (expand-DH : (a : A) -> (e : E) -> DH (t a e) = at (t a (dh e)) (mixed a e))
  (expand-HD : (a : A) -> (e : E) -> HD (t a e) = st (t a (hd e)) (mixed a e))
  (cancel-mixed : (u v m : T) -> at (at u m) (st v m) = at u v)
  (a : A) (e : E)
  : at (DH (t a e)) (HD (t a e)) = st (t a e) (t a (projection e))
  := concat T (at (DH (t a e)) (HD (t a e)))
    (at (at (t a (dh e)) (mixed a e)) (st (t a (hd e)) (mixed a e)))
    (st (t a e) (t a (projection e)))
    (marici-ap-binary T T T at (DH (t a e)) (at (t a (dh e)) (mixed a e))
      (HD (t a e)) (st (t a (hd e)) (mixed a e)) (expand-DH a e) (expand-HD a e))
    (concat T (at (at (t a (dh e)) (mixed a e)) (st (t a (hd e)) (mixed a e)))
      (at (t a (dh e)) (t a (hd e))) (st (t a e) (t a (projection e)))
      (cancel-mixed (t a (dh e)) (t a (hd e)) (mixed a e))
      (concat T (at (t a (dh e)) (t a (hd e)))
        (t a (ae (dh e) (hd e))) (st (t a e) (t a (projection e)))
        (rev T (t a (ae (dh e) (hd e))) (at (t a (dh e)) (t a (hd e)))
          (tensor-add a (dh e) (hd e)))
        (concat T (t a (ae (dh e) (hd e))) (t a (se e (projection e)))
          (st (t a e) (t a (projection e)))
          (ap E T (ae (dh e) (hd e)) (se e (projection e)) (t a) (endpoint e))
          (tensor-sub a e (projection e)))))

#define marici-tensor-marking-extension
  (A B E T V : U) (t : A -> E -> T) (v : B -> E -> V)
  (f : A -> B) (F : T -> V)
  (F-pure : (a : A) -> (e : E) -> F (t a e) = v (f a) e)
  (a : A) (b : B) (z : E) (boundary : f a = b)
  : F (t a z) = v b z
  := concat V (F (t a z)) (v (f a) z) (v b z)
    (F-pure a z) (ap B V (f a) b (\ c -> v c z) boundary)
```

Here projection is z epsilon only when supplied as such by the endpoint
complex. The marking lemma retains z; it does not turn a common-conductor
unit into the endpoint unit. No claim of contractible extension spaces or of
five relative classes is inferred from these degree-local equations alone.

## Disposition

Fresh headless verification passed on 2026-09-06: exit 0, `Everything is ok!`.
Command: `rzk typecheck` with explicit ordered inputs consisting of pinned
sHoTT commit `52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2` files
`src/hott/00-common.rzk.md`, `src/hott/01-paths.rzk.md`, then our
`02a-boundary-interfaces.rzk.md`, `02a-marici-boundary-interior-chain-map.rzk.md`,
and this file. Shell Rzk execution follows the operator's explicit fallback
authorization. The seven new definitions and the earlier closure all pass.
Evidence log: `research/grothendieck/rzk/results/tensor-extension-typecheck.log`.
The missing Rees checker is not recreated or certified by this formalization. The logarithmic branch-selected physical comparison
remains outside the theorem's hypotheses and conclusions.
