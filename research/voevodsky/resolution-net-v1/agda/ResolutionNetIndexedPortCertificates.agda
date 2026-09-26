{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetIndexedPortCertificates where
open import Cubical.Foundations.Prelude
open import CoherenceResolutionClosure
open import ResolutionNetLocalSimulation
open import ResolutionNetCompression
data Pkg : Type where
  p0 p1 p2 p3 p4 : Pkg
data U : Pkg → Pkg → Type where
  rule1 : U p3 p1
  rule2 : U p4 p2
data V : Pkg → Pkg → Pkg → Type where
  rule0 : V p1 p2 p0
data Evidence : Pkg → Type where
  evidence0 : Evidence p3
  evidence1 : Evidence p4
  evidence2 : Evidence p3
open Closure Pkg U V public
open Local Pkg U V Evidence public
open Compression Pkg U V Evidence public

-- Packet SHA256: 821679018a1ab201a5ca3ceb8ce3593c2993d84cc2b513d81a64da4e3ced7f8a

before0 after0 : Term p0
before0 = (pending (binary rule0 (unary rule1 (seed (seed evidence0))) (unary rule2 (seed (seed evidence1)))))
after0 = (two rule0 (pending (unary rule1 (seed (seed evidence0)))) (pending (unary rule2 (seed (seed evidence1)))))
proof0 : RepresentedStep before0 after0
proof0 = represented (F-binary rule0 (unary rule1 (seed (seed evidence0))) (unary rule2 (seed (seed evidence1)))) (in-two rule0 same same)
sound0 : interpret before0 ≡ interpret after0
sound0 = represented-sound proof0

before1 after1 : Term p0
before1 = (two rule0 (pending (unary rule1 (seed (seed evidence0)))) (pending (unary rule2 (seed (seed evidence1)))))
after1 = (two rule0 (one rule1 (pending (seed (seed evidence0)))) (pending (unary rule2 (seed (seed evidence1)))))
proof1 : RepresentedStep before1 after1
proof1 = represented (under-left rule0 (pending (unary rule2 (seed (seed evidence1)))) (F-unary rule1 (seed (seed evidence0)))) (in-two rule0 (in-one rule1 same) same)
sound1 : interpret before1 ≡ interpret after1
sound1 = represented-sound proof1

before2 after2 : Term p0
before2 = (two rule0 (one rule1 (pending (seed (seed evidence0)))) (pending (unary rule2 (seed (seed evidence1)))))
after2 = (two rule0 (one rule1 (pending (seed (seed evidence0)))) (one rule2 (pending (seed (seed evidence1)))))
proof2 : RepresentedStep before2 after2
proof2 = represented (under-right rule0 (one rule1 (pending (seed (seed evidence0)))) (F-unary rule2 (seed (seed evidence1)))) (in-two rule0 (in-one rule1 same) (in-one rule2 same))
sound2 : interpret before2 ≡ interpret after2
sound2 = represented-sound proof2

before3 after3 : Term p0
before3 = (two rule0 (one rule1 (pending (seed (seed evidence0)))) (one rule2 (pending (seed (seed evidence1)))))
after3 = (two rule0 (keep (unary rule1 (seed evidence0))) (one rule2 (pending (seed (seed evidence1)))))
proof3 : RepresentedStep before3 after3
proof3 = represented (under-left rule0 (one rule2 (pending (seed (seed evidence1)))) (under-one rule1 (F-seed (seed evidence0)))) (in-two rule0 (chain (in-one rule1 same) (pack-one rule1 (seed evidence0))) (in-one rule2 same))
sound3 : interpret before3 ≡ interpret after3
sound3 = represented-sound proof3

before4 after4 : Term p0
before4 = (two rule0 (keep (unary rule1 (seed evidence0))) (one rule2 (pending (seed (seed evidence1)))))
after4 = (keep (binary rule0 (unary rule1 (seed evidence0)) (unary rule2 (seed evidence1))))
proof4 : RepresentedStep before4 after4
proof4 = represented (under-right rule0 (keep (unary rule1 (seed evidence0))) (under-one rule2 (F-seed (seed evidence1)))) (chain (in-two rule0 same (chain (in-one rule2 same) (pack-one rule2 (seed evidence1)))) (pack-two rule0 (unary rule1 (seed evidence0)) (unary rule2 (seed evidence1))))
sound4 : interpret before4 ≡ interpret after4
sound4 = represented-sound proof4
