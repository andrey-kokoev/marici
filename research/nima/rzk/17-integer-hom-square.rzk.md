# Square zero for the assembled integer Hom differential

The proofs below use the actual index translations and transports from module
15. Component zero maps and differentials are explicit. This does not turn
raw Hom into RHom or supply the physical polynomial coefficient modules.

```rzk
#lang rzk-1

#define nima-z-transport-zero
  (M : MariciInt -> U) (zero : (i : MariciInt) -> M i)
  (i j : MariciInt) (p : i = j)
  : nima-hom-transport MariciInt M i j p (zero i) = zero j
  := idJ (MariciInt, i,
       (\ j' p' -> nima-hom-transport MariciInt M i j' p' (zero i) = zero j'), refl, j, p)

#define nima-z-transport-operation
  (M : MariciInt -> U) (op : (i : MariciInt) -> M i -> M i -> M i)
  (i j : MariciInt) (p : i = j) (a b : M i)
  : nima-hom-transport MariciInt M i j p (op i a b)
    = op j (nima-hom-transport MariciInt M i j p a) (nima-hom-transport MariciInt M i j p b)
  := idJ (MariciInt, i,
       (\ j' p' -> nima-hom-transport MariciInt M i j' p' (op i a b)
         = op j' (nima-hom-transport MariciInt M i j' p' a)
           (nima-hom-transport MariciInt M i j' p' b)), refl, j, p)

#define nima-z-transport-differential
  (M : MariciInt -> U) (d : (i : MariciInt) -> M i -> M (nima-z-next i))
  (i j : MariciInt) (p : i = j) (x : M i)
  : d j (nima-hom-transport MariciInt M i j p x)
    = nima-hom-transport MariciInt M (nima-z-next i) (nima-z-next j)
        (nima-frame-ap MariciInt MariciInt nima-z-next i j p) (d i x)
  := idJ (MariciInt, i,
       (\ j' p' -> d j' (nima-hom-transport MariciInt M i j' p' x)
         = nima-hom-transport MariciInt M (nima-z-next i) (nima-z-next j')
           (nima-frame-ap MariciInt MariciInt nima-z-next i j' p') (d i x)), refl, j, p)

#define nima-z-transport-composite
  (M : MariciInt -> U) (i j k : MariciInt) (p : i = j) (q : j = k) (x : M i)
  : nima-hom-transport MariciInt M j k q (nima-hom-transport MariciInt M i j p x)
    = nima-hom-transport MariciInt M i k (nima-frame-concat MariciInt i j k p q) x
  := idJ (MariciInt, i,
       (\ j' p' -> (q' : j' = k) ->
         nima-hom-transport MariciInt M j' k q' (nima-hom-transport MariciInt M i j' p' x)
         = nima-hom-transport MariciInt M i k (nima-frame-concat MariciInt i j' k p' q') x),
       (\ q' -> refl), j, p) q

#define nima-z-two-transports-agree
  (M : MariciInt -> U) (i j k l : MariciInt)
  (p : i = j) (q : j = l) (r : i = k) (s : k = l) (x : M i)
  : nima-hom-transport MariciInt M j l q (nima-hom-transport MariciInt M i j p x)
    = nima-hom-transport MariciInt M k l s (nima-hom-transport MariciInt M i k r x)
  := nima-frame-concat (M l)
       (nima-hom-transport MariciInt M j l q (nima-hom-transport MariciInt M i j p x))
       (nima-hom-transport MariciInt M i l (nima-frame-concat MariciInt i j l p q) x)
       (nima-hom-transport MariciInt M k l s (nima-hom-transport MariciInt M i k r x))
       (nima-z-transport-composite M i j l p q x)
       (nima-frame-concat (M l)
         (nima-hom-transport MariciInt M i l (nima-frame-concat MariciInt i j l p q) x)
         (nima-hom-transport MariciInt M i l (nima-frame-concat MariciInt i k l r s) x)
         (nima-hom-transport MariciInt M k l s (nima-hom-transport MariciInt M i k r x))
         (nima-z-transport-coherent M i l
           (nima-frame-concat MariciInt i j l p q) (nima-frame-concat MariciInt i k l r s) x)
         (nima-frame-rev (M l)
           (nima-hom-transport MariciInt M k l s (nima-hom-transport MariciInt M i k r x))
           (nima-hom-transport MariciInt M i l (nima-frame-concat MariciInt i k l r s) x)
           (nima-z-transport-composite M i k l r s x)))

#define nima-integer-hom-post
  (L M : MariciInt -> U) (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (n : MariciInt) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := \ i x -> nima-hom-transport MariciInt M
       (nima-z-next (nima-z-shift n i)) (nima-z-shift (nima-z-next n) i)
       (nima-z-target-step n i) (dM (nima-z-shift n i) (f i x))

#define nima-integer-hom-pre
  (L M : MariciInt -> U) (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (n : MariciInt) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := \ i x -> nima-hom-transport MariciInt M
       (nima-z-shift n (nima-z-next i)) (nima-z-shift (nima-z-next n) i)
       (nima-z-source-step n i) (f (nima-z-next i) (dL i x))

#define nima-integer-hom-operation
  (L M : MariciInt -> U) (op : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (f g : nima-integer-hom L M n) : nima-integer-hom L M n
  := \ i x -> op (nima-z-shift n i) (f i x) (g i x)

#define nima-integer-hom-post-operation
  (L M : MariciInt -> U) (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (op : (i : MariciInt) -> M i -> M i -> M i)
  (preserve : (i : MariciInt) -> (a b : M i) -> dM i (op i a b) = op (nima-z-next i) (dM i a) (dM i b))
  (n : MariciInt) (f g : nima-integer-hom L M n) (i : MariciInt) (x : L i)
  : nima-integer-hom-post L M dM n (nima-integer-hom-operation L M op n f g) i x
    = op (nima-z-shift (nima-z-next n) i)
      (nima-integer-hom-post L M dM n f i x) (nima-integer-hom-post L M dM n g i x)
  := nima-frame-concat (M (nima-z-shift (nima-z-next n) i))
       (nima-integer-hom-post L M dM n (nima-integer-hom-operation L M op n f g) i x)
       (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift n i)) (nima-z-shift (nima-z-next n) i)
         (nima-z-target-step n i)
         (op (nima-z-next (nima-z-shift n i)) (dM (nima-z-shift n i) (f i x)) (dM (nima-z-shift n i) (g i x))))
       (op (nima-z-shift (nima-z-next n) i)
         (nima-integer-hom-post L M dM n f i x) (nima-integer-hom-post L M dM n g i x))
       (nima-frame-ap (M (nima-z-next (nima-z-shift n i))) (M (nima-z-shift (nima-z-next n) i))
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift n i)) (nima-z-shift (nima-z-next n) i) (nima-z-target-step n i))
         (dM (nima-z-shift n i) (op (nima-z-shift n i) (f i x) (g i x)))
         (op (nima-z-next (nima-z-shift n i)) (dM (nima-z-shift n i) (f i x)) (dM (nima-z-shift n i) (g i x)))
         (preserve (nima-z-shift n i) (f i x) (g i x)))
       (nima-z-transport-operation M op (nima-z-next (nima-z-shift n i)) (nima-z-shift (nima-z-next n) i)
         (nima-z-target-step n i) (dM (nima-z-shift n i) (f i x)) (dM (nima-z-shift n i) (g i x)))

#define nima-integer-hom-pre-operation
  (L M : MariciInt -> U) (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (op : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (f g : nima-integer-hom L M n) (i : MariciInt) (x : L i)
  : nima-integer-hom-pre L M dL n (nima-integer-hom-operation L M op n f g) i x
    = op (nima-z-shift (nima-z-next n) i)
      (nima-integer-hom-pre L M dL n f i x) (nima-integer-hom-pre L M dL n g i x)
  := nima-z-transport-operation M op (nima-z-shift n (nima-z-next i)) (nima-z-shift (nima-z-next n) i)
       (nima-z-source-step n i) (f (nima-z-next i) (dL i x)) (g (nima-z-next i) (dL i x))

#define nima-z-two-transports-zero
  (M : MariciInt -> U) (zero : (i : MariciInt) -> M i)
  (a b c : MariciInt) (p : a = b) (q : b = c) (x : M a) (vanishes : x = zero a)
  : nima-hom-transport MariciInt M b c q (nima-hom-transport MariciInt M a b p x) = zero c
  := nima-frame-concat (M c)
       (nima-hom-transport MariciInt M b c q (nima-hom-transport MariciInt M a b p x))
       (nima-hom-transport MariciInt M b c q (nima-hom-transport MariciInt M a b p (zero a))) (zero c)
       (nima-frame-ap (M a) (M c) (\ t -> nima-hom-transport MariciInt M b c q (nima-hom-transport MariciInt M a b p t))
         x (zero a) vanishes)
       (nima-frame-concat (M c)
         (nima-hom-transport MariciInt M b c q (nima-hom-transport MariciInt M a b p (zero a)))
         (nima-hom-transport MariciInt M b c q (zero b)) (zero c)
         (nima-frame-ap (M b) (M c) (nima-hom-transport MariciInt M b c q)
           (nima-hom-transport MariciInt M a b p (zero a)) (zero b) (nima-z-transport-zero M zero a b p))
         (nima-z-transport-zero M zero b c q))

#define nima-z-post-step-square-zero
  (M : MariciInt -> U) (zero : (i : MariciInt) -> M i)
  (d : (i : MariciInt) -> M i -> M (nima-z-next i))
  (square : (i : MariciInt) -> (x : M i) -> d (nima-z-next i) (d i x) = zero (nima-z-next (nima-z-next i)))
  (a b c : MariciInt) (p : nima-z-next a = b) (q : nima-z-next b = c) (x : M a)
  : nima-hom-transport MariciInt M (nima-z-next b) c q
      (d b (nima-hom-transport MariciInt M (nima-z-next a) b p (d a x))) = zero c
  := nima-frame-concat (M c)
       (nima-hom-transport MariciInt M (nima-z-next b) c q
         (d b (nima-hom-transport MariciInt M (nima-z-next a) b p (d a x))))
       (nima-hom-transport MariciInt M (nima-z-next b) c q
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-next a)) (nima-z-next b)
           (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-next a) b p) (d (nima-z-next a) (d a x))))
       (zero c)
       (nima-frame-ap (M (nima-z-next b)) (M c) (nima-hom-transport MariciInt M (nima-z-next b) c q)
         (d b (nima-hom-transport MariciInt M (nima-z-next a) b p (d a x)))
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-next a)) (nima-z-next b)
           (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-next a) b p) (d (nima-z-next a) (d a x)))
         (nima-z-transport-differential M d (nima-z-next a) b p (d a x)))
       (nima-z-two-transports-zero M zero (nima-z-next (nima-z-next a)) (nima-z-next b) c
         (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-next a) b p) q
         (d (nima-z-next a) (d a x)) (square a x))

#define nima-integer-hom-post-square
  (L M : MariciInt -> U) (zeroM : (i : MariciInt) -> M i)
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (squareM : (i : MariciInt) -> (x : M i) -> dM (nima-z-next i) (dM i x) = zeroM (nima-z-next (nima-z-next i)))
  (n : MariciInt) (f : nima-integer-hom L M n) (i : MariciInt) (x : L i)
  : nima-integer-hom-post L M dM (nima-z-next n) (nima-integer-hom-post L M dM n f) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := nima-z-post-step-square-zero M zeroM dM squareM
       (nima-z-shift n i) (nima-z-shift (nima-z-next n) i) (nima-z-shift (nima-z-next (nima-z-next n)) i)
       (nima-z-target-step n i) (nima-z-target-step (nima-z-next n) i) (f i x)

#define nima-integer-hom-pre-square
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (n : MariciInt) (f : nima-integer-hom L M n)
  (fzero : (j : MariciInt) -> f j (zeroL j) = zeroM (nima-z-shift n j))
  (i : MariciInt) (x : L i)
  : nima-integer-hom-pre L M dL (nima-z-next n) (nima-integer-hom-pre L M dL n f) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := nima-z-two-transports-zero M zeroM
       (nima-z-shift n (nima-z-next (nima-z-next i)))
       (nima-z-shift (nima-z-next n) (nima-z-next i)) (nima-z-shift (nima-z-next (nima-z-next n)) i)
       (nima-z-source-step n (nima-z-next i)) (nima-z-source-step (nima-z-next n) i)
       (f (nima-z-next (nima-z-next i)) (dL (nima-z-next i) (dL i x)))
       (nima-frame-concat (M (nima-z-shift n (nima-z-next (nima-z-next i))))
         (f (nima-z-next (nima-z-next i)) (dL (nima-z-next i) (dL i x)))
         (f (nima-z-next (nima-z-next i)) (zeroL (nima-z-next (nima-z-next i))))
         (zeroM (nima-z-shift n (nima-z-next (nima-z-next i))))
         (nima-frame-ap (L (nima-z-next (nima-z-next i))) (M (nima-z-shift n (nima-z-next (nima-z-next i))))
           (f (nima-z-next (nima-z-next i))) (dL (nima-z-next i) (dL i x))
           (zeroL (nima-z-next (nima-z-next i))) (squareL i x))
         (fzero (nima-z-next (nima-z-next i))))

#define nima-integer-hom-post-pre
  (L M : MariciInt -> U)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (n : MariciInt) (f : nima-integer-hom L M n) (i : MariciInt) (x : L i)
  : nima-integer-hom-post L M dM (nima-z-next n) (nima-integer-hom-pre L M dL n f) i x
    = nima-integer-hom-pre L M dL (nima-z-next n) (nima-integer-hom-post L M dM n f) i x
  := nima-frame-concat (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (nima-integer-hom-post L M dM (nima-z-next n) (nima-integer-hom-pre L M dL n f) i x)
       (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift (nima-z-next n) i))
         (nima-z-shift (nima-z-next (nima-z-next n)) i) (nima-z-target-step (nima-z-next n) i)
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift n (nima-z-next i)))
           (nima-z-next (nima-z-shift (nima-z-next n) i))
           (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-shift n (nima-z-next i))
             (nima-z-shift (nima-z-next n) i) (nima-z-source-step n i))
           (dM (nima-z-shift n (nima-z-next i)) (f (nima-z-next i) (dL i x)))))
       (nima-integer-hom-pre L M dL (nima-z-next n) (nima-integer-hom-post L M dM n f) i x)
       (nima-frame-ap (M (nima-z-next (nima-z-shift (nima-z-next n) i)))
         (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift (nima-z-next n) i))
           (nima-z-shift (nima-z-next (nima-z-next n)) i) (nima-z-target-step (nima-z-next n) i))
         (dM (nima-z-shift (nima-z-next n) i) (nima-integer-hom-pre L M dL n f i x))
         (nima-hom-transport MariciInt M (nima-z-next (nima-z-shift n (nima-z-next i)))
           (nima-z-next (nima-z-shift (nima-z-next n) i))
           (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-shift n (nima-z-next i))
             (nima-z-shift (nima-z-next n) i) (nima-z-source-step n i))
           (dM (nima-z-shift n (nima-z-next i)) (f (nima-z-next i) (dL i x))))
         (nima-z-transport-differential M dM (nima-z-shift n (nima-z-next i))
           (nima-z-shift (nima-z-next n) i) (nima-z-source-step n i) (f (nima-z-next i) (dL i x))))
       (nima-z-two-transports-agree M (nima-z-next (nima-z-shift n (nima-z-next i)))
         (nima-z-next (nima-z-shift (nima-z-next n) i))
         (nima-z-shift (nima-z-next n) (nima-z-next i)) (nima-z-shift (nima-z-next (nima-z-next n)) i)
         (nima-frame-ap MariciInt MariciInt nima-z-next (nima-z-shift n (nima-z-next i))
           (nima-z-shift (nima-z-next n) i) (nima-z-source-step n i))
         (nima-z-target-step (nima-z-next n) i) (nima-z-target-step n (nima-z-next i))
         (nima-z-source-step (nima-z-next n) i) (dM (nima-z-shift n (nima-z-next i)) (f (nima-z-next i) (dL i x))))

#define nima-pointed-integer-hom
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (n : MariciInt) : U
  := Sigma (f : nima-integer-hom L M n), (i : MariciInt) -> f i (zeroL i) = zeroM (nima-z-shift n i)

#define nima-actual-integer-hom-square-even
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (squareM : (i : MariciInt) -> (x : M i) -> dM (nima-z-next i) (dM i x) = zeroM (nima-z-next (nima-z-next i)))
  (dsub : (i : MariciInt) -> (a b : M i) -> dM i (sub i a b) = sub (nima-z-next i) (dM i a) (dM i b))
  (subzero : (i : MariciInt) -> (a : M i) -> sub i a (zeroM i) = a)
  (inverse : (i : MariciInt) -> (a : M i) -> add i (sub i (zeroM i) a) a = zeroM i)
  (n : MariciInt) (f : nima-pointed-integer-hom L M zeroL zeroM n) (i : MariciInt) (x : L i)
  : nima-integer-hom-differential-odd L M dL dM add (nima-z-next n)
      (nima-integer-hom-differential-even L M dL dM sub n (first f)) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := nima-hom-square-even
       (nima-pointed-integer-hom L M zeroL zeroM n) (nima-integer-hom L M (nima-z-next n))
       (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (\ w -> nima-integer-hom-post L M dM n (first w))
       (\ w -> nima-integer-hom-pre L M dL n (first w))
       (\ g -> nima-integer-hom-post L M dM (nima-z-next n) g i x)
       (\ g -> nima-integer-hom-pre L M dL (nima-z-next n) g i x)
       (nima-integer-hom-operation L M sub (nima-z-next n))
       (add (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (sub (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (\ g h -> nima-integer-hom-post-operation L M dM sub dsub (nima-z-next n) g h i x)
       (\ g h -> nima-integer-hom-pre-operation L M dL sub (nima-z-next n) g h i x)
       (\ w -> nima-integer-hom-post-square L M zeroM dM squareM n (first w) i x)
       (\ w -> nima-integer-hom-pre-square L M zeroL zeroM dL squareL n (first w) (second w) i x)
       (\ w -> nima-integer-hom-post-pre L M dL dM n (first w) i x)
       (subzero (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (inverse (nima-z-shift (nima-z-next (nima-z-next n)) i)) f

#define nima-actual-integer-hom-square-odd
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (squareM : (i : MariciInt) -> (x : M i) -> dM (nima-z-next i) (dM i x) = zeroM (nima-z-next (nima-z-next i)))
  (dadd : (i : MariciInt) -> (a b : M i) -> dM i (add i a b) = add (nima-z-next i) (dM i a) (dM i b))
  (leftzero : (i : MariciInt) -> (a : M i) -> add i (zeroM i) a = a)
  (rightzero : (i : MariciInt) -> (a : M i) -> add i a (zeroM i) = a)
  (self : (i : MariciInt) -> (a : M i) -> sub i a a = zeroM i)
  (n : MariciInt) (f : nima-pointed-integer-hom L M zeroL zeroM n) (i : MariciInt) (x : L i)
  : nima-integer-hom-differential-even L M dL dM sub (nima-z-next n)
      (nima-integer-hom-differential-odd L M dL dM add n (first f)) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := nima-hom-square-odd
       (nima-pointed-integer-hom L M zeroL zeroM n) (nima-integer-hom L M (nima-z-next n))
       (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (\ w -> nima-integer-hom-post L M dM n (first w))
       (\ w -> nima-integer-hom-pre L M dL n (first w))
       (\ g -> nima-integer-hom-post L M dM (nima-z-next n) g i x)
       (\ g -> nima-integer-hom-pre L M dL (nima-z-next n) g i x)
       (nima-integer-hom-operation L M add (nima-z-next n))
       (add (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (sub (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (\ g h -> nima-integer-hom-post-operation L M dM add dadd (nima-z-next n) g h i x)
       (\ g h -> nima-integer-hom-pre-operation L M dL add (nima-z-next n) g h i x)
       (\ w -> nima-integer-hom-post-square L M zeroM dM squareM n (first w) i x)
       (\ w -> nima-integer-hom-pre-square L M zeroL zeroM dL squareL n (first w) (second w) i x)
       (\ w -> nima-integer-hom-post-pre L M dL dM n (first w) i x)
       (leftzero (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (rightzero (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (self (nima-z-shift (nima-z-next (nima-z-next n)) i)) f

#define nima-integer-hom-parity-operator
  (L M : MariciInt -> U)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (n : MariciInt) (p : NimaDegreeParity) (f : nima-integer-hom L M n)
  : nima-integer-hom L M (nima-z-next n)
  := match p into (\ _ -> nima-integer-hom L M (nima-z-next n))
       (nima-degree-even => nima-integer-hom-differential-even L M dL dM sub n f
       | nima-degree-odd => nima-integer-hom-differential-odd L M dL dM add n f)

#define nima-integer-hom-square-by-parity
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (squareM : (i : MariciInt) -> (x : M i) -> dM (nima-z-next i) (dM i x) = zeroM (nima-z-next (nima-z-next i)))
  (dadd : (i : MariciInt) -> (a b : M i) -> dM i (add i a b) = add (nima-z-next i) (dM i a) (dM i b))
  (dsub : (i : MariciInt) -> (a b : M i) -> dM i (sub i a b) = sub (nima-z-next i) (dM i a) (dM i b))
  (leftzero : (i : MariciInt) -> (a : M i) -> add i (zeroM i) a = a)
  (rightzero : (i : MariciInt) -> (a : M i) -> add i a (zeroM i) = a)
  (subzero : (i : MariciInt) -> (a : M i) -> sub i a (zeroM i) = a)
  (self : (i : MariciInt) -> (a : M i) -> sub i a a = zeroM i)
  (inverse : (i : MariciInt) -> (a : M i) -> add i (sub i (zeroM i) a) a = zeroM i)
  (n : MariciInt) (p : NimaDegreeParity) (f : nima-pointed-integer-hom L M zeroL zeroM n) (i : MariciInt) (x : L i)
  : nima-integer-hom-parity-operator L M dL dM add sub (nima-z-next n) (nima-degree-flip p)
      (nima-integer-hom-parity-operator L M dL dM add sub n p (first f)) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := match p
       (nima-degree-even => nima-actual-integer-hom-square-even L M zeroL zeroM dL dM add sub squareL squareM dsub subzero inverse n f i x
       | nima-degree-odd => nima-actual-integer-hom-square-odd L M zeroL zeroM dL dM add sub squareL squareM dadd leftzero rightzero self n f i x)

#define nima-integer-hom-differential-square
  (L M : MariciInt -> U) (zeroL : (i : MariciInt) -> L i) (zeroM : (i : MariciInt) -> M i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (dM : (i : MariciInt) -> M i -> M (nima-z-next i))
  (add sub : (i : MariciInt) -> M i -> M i -> M i)
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (squareM : (i : MariciInt) -> (x : M i) -> dM (nima-z-next i) (dM i x) = zeroM (nima-z-next (nima-z-next i)))
  (dadd : (i : MariciInt) -> (a b : M i) -> dM i (add i a b) = add (nima-z-next i) (dM i a) (dM i b))
  (dsub : (i : MariciInt) -> (a b : M i) -> dM i (sub i a b) = sub (nima-z-next i) (dM i a) (dM i b))
  (leftzero : (i : MariciInt) -> (a : M i) -> add i (zeroM i) a = a)
  (rightzero : (i : MariciInt) -> (a : M i) -> add i a (zeroM i) = a)
  (subzero : (i : MariciInt) -> (a : M i) -> sub i a (zeroM i) = a)
  (self : (i : MariciInt) -> (a : M i) -> sub i a a = zeroM i)
  (inverse : (i : MariciInt) -> (a : M i) -> add i (sub i (zeroM i) a) a = zeroM i)
  (n : MariciInt) (f : nima-pointed-integer-hom L M zeroL zeroM n) (i : MariciInt) (x : L i)
  : nima-integer-hom-differential L M dL dM add sub (nima-z-next n)
      (nima-integer-hom-differential L M dL dM add sub n (first f)) i x
    = zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i)
  := nima-frame-concat (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (nima-integer-hom-differential L M dL dM add sub (nima-z-next n)
         (nima-integer-hom-differential L M dL dM add sub n (first f)) i x)
       (nima-integer-hom-parity-operator L M dL dM add sub (nima-z-next n) (nima-degree-flip (nima-integer-parity n))
         (nima-integer-hom-differential L M dL dM add sub n (first f)) i x)
       (zeroM (nima-z-shift (nima-z-next (nima-z-next n)) i))
       (nima-frame-ap NimaDegreeParity (M (nima-z-shift (nima-z-next (nima-z-next n)) i))
         (\ p -> nima-integer-hom-parity-operator L M dL dM add sub (nima-z-next n) p
           (nima-integer-hom-differential L M dL dM add sub n (first f)) i x)
         (nima-integer-parity (nima-z-next n)) (nima-degree-flip (nima-integer-parity n)) (nima-integer-parity-next n))
       (nima-integer-hom-square-by-parity L M zeroL zeroM dL dM add sub squareL squareM
         dadd dsub leftzero rightzero subzero self inverse n (nima-integer-parity n) f i x)
```

The pointed-family hypothesis states precisely the zero preservation used by
the proof. Linear maps meet it once their module laws are instantiated. The
result is pointwise in source degree and vector; no function extensionality
or derived-category localization is assumed. Closure under the differential
of the full linearity predicate is a separate DG-module packaging obligation.

## Existing coefficient pilot: actual specialization

This instantiates the target laws on module 16, rather than adding another
synthetic coefficient object. The source may be any pointed square-zero
integer-indexed complex. The original map is required to preserve zero.

```rzk
#define nima-z2-d-sub (a b : NimaZ2)
  : nima-z2-d (nima-z2-sub a b) = nima-z2-sub (nima-z2-d a) (nima-z2-d b)
  := refl

#define nima-z2-sub-inverse (a : NimaZ2)
  : nima-z2-add (nima-z2-sub nima-z2-zero a) a = nima-z2-zero
  := nima-frame-concat NimaZ2
       (nima-z2-add (nima-z2-sub nima-z2-zero a) a)
       (nima-z2-add a (nima-z2-neg a)) nima-z2-zero
       (nima-z2-comm (nima-z2-neg a) a) (nima-z2-inverse a)

#define nima-z2-target-hom-square
  (L : MariciInt -> U) (zeroL : (i : MariciInt) -> L i)
  (dL : (i : MariciInt) -> L i -> L (nima-z-next i))
  (squareL : (i : MariciInt) -> (x : L i) -> dL (nima-z-next i) (dL i x) = zeroL (nima-z-next (nima-z-next i)))
  (n : MariciInt) (f : nima-pointed-integer-hom L (\ _ -> NimaZ2) zeroL (\ _ -> nima-z2-zero) n)
  (i : MariciInt) (x : L i)
  : nima-integer-hom-differential L (\ _ -> NimaZ2) dL (\ _ -> nima-z2-d)
      (\ _ -> nima-z2-add) (\ _ -> nima-z2-sub) (nima-z-next n)
      (nima-integer-hom-differential L (\ _ -> NimaZ2) dL (\ _ -> nima-z2-d)
        (\ _ -> nima-z2-add) (\ _ -> nima-z2-sub) n (first f)) i x = nima-z2-zero
  := nima-integer-hom-differential-square L (\ _ -> NimaZ2) zeroL (\ _ -> nima-z2-zero)
       dL (\ _ -> nima-z2-d) (\ _ -> nima-z2-add) (\ _ -> nima-z2-sub)
       squareL (\ _ -> nima-z2-d-square) (\ _ -> nima-z2-d-add) (\ _ -> nima-z2-d-sub)
       (\ _ -> nima-z2-left-zero) (\ _ -> nima-z2-right-zero) (\ _ -> nima-z2-right-zero)
       (\ _ -> nima-z2-inverse) (\ _ -> nima-z2-sub-inverse) n f i x
```

