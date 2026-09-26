{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetPortCertificates where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Nat.Base using (ℕ)
open import CoherenceResolutionClosure
open import ResolutionNetLocalSimulation
open import ResolutionNetCompression
open Closure Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ)
open Local Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ) (λ _ → ℕ)
open Compression Unit (λ _ _ → ℕ) (λ _ _ _ → ℕ) (λ _ → ℕ)

-- Concrete packet SHA256: 3960012a40cb26f8a89f1e8af15bb1366264efb7aaad992139acde290a41499e

before0 after0 : Term tt
before0 = (pending (binary 0 (unary 1 (seed (seed 0))) (binary 0 (seed (seed 0)) (unary 1 (seed (seed 0))))))
after0 = (two 0 (pending (unary 1 (seed (seed 0)))) (pending (binary 0 (seed (seed 0)) (unary 1 (seed (seed 0))))))
proof0 : RepresentedStep before0 after0
proof0 = represented (F-binary 0 (unary 1 (seed (seed 0))) (binary 0 (seed (seed 0)) (unary 1 (seed (seed 0))))) (in-two 0 same same)
sound0 : interpret before0 ≡ interpret after0
sound0 = represented-sound proof0

before1 after1 : Term tt
before1 = (two 0 (pending (unary 1 (seed (seed 0)))) (pending (binary 0 (seed (seed 0)) (unary 1 (seed (seed 0))))))
after1 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (pending (unary 1 (seed (seed 0))))))
proof1 : RepresentedStep before1 after1
proof1 = represented (under-right 0 (pending (unary 1 (seed (seed 0)))) (F-binary 0 (seed (seed 0)) (unary 1 (seed (seed 0))))) (in-two 0 same (in-two 0 same same))
sound1 : interpret before1 ≡ interpret after1
sound1 = represented-sound proof1

before2 after2 : Term tt
before2 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (pending (unary 1 (seed (seed 0))))))
after2 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (one 1 (pending (seed (seed 0))))))
proof2 : RepresentedStep before2 after2
proof2 = represented (under-right 0 (pending (unary 1 (seed (seed 0)))) (under-right 0 (pending (seed (seed 0))) (F-unary 1 (seed (seed 0))))) (in-two 0 same (in-two 0 same (in-one 1 same)))
sound2 : interpret before2 ≡ interpret after2
sound2 = represented-sound proof2

before3 after3 : Term tt
before3 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (one 1 (pending (seed (seed 0))))))
after3 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (keep (unary 1 (seed 0)))))
proof3 : RepresentedStep before3 after3
proof3 = represented (under-right 0 (pending (unary 1 (seed (seed 0)))) (under-right 0 (pending (seed (seed 0))) (under-one 1 (F-seed (seed 0))))) (in-two 0 same (in-two 0 same (chain (in-one 1 same) (pack-one 1 (seed 0)))))
sound3 : interpret before3 ≡ interpret after3
sound3 = represented-sound proof3

before4 after4 : Term tt
before4 = (two 0 (pending (unary 1 (seed (seed 0)))) (two 0 (pending (seed (seed 0))) (keep (unary 1 (seed 0)))))
after4 = (two 0 (pending (unary 1 (seed (seed 0)))) (keep (binary 0 (seed 0) (unary 1 (seed 0)))))
proof4 : RepresentedStep before4 after4
proof4 = represented (under-right 0 (pending (unary 1 (seed (seed 0)))) (under-left 0 (keep (unary 1 (seed 0))) (F-seed (seed 0)))) (in-two 0 same (chain (in-two 0 same same) (pack-two 0 (seed 0) (unary 1 (seed 0)))))
sound4 : interpret before4 ≡ interpret after4
sound4 = represented-sound proof4

before5 after5 : Term tt
before5 = (two 0 (pending (unary 1 (seed (seed 0)))) (keep (binary 0 (seed 0) (unary 1 (seed 0)))))
after5 = (two 0 (one 1 (pending (seed (seed 0)))) (keep (binary 0 (seed 0) (unary 1 (seed 0)))))
proof5 : RepresentedStep before5 after5
proof5 = represented (under-left 0 (keep (binary 0 (seed 0) (unary 1 (seed 0)))) (F-unary 1 (seed (seed 0)))) (in-two 0 (in-one 1 same) same)
sound5 : interpret before5 ≡ interpret after5
sound5 = represented-sound proof5

before6 after6 : Term tt
before6 = (two 0 (one 1 (pending (seed (seed 0)))) (keep (binary 0 (seed 0) (unary 1 (seed 0)))))
after6 = (keep (binary 0 (unary 1 (seed 0)) (binary 0 (seed 0) (unary 1 (seed 0)))))
proof6 : RepresentedStep before6 after6
proof6 = represented (under-left 0 (keep (binary 0 (seed 0) (unary 1 (seed 0)))) (under-one 1 (F-seed (seed 0)))) (chain (in-two 0 (chain (in-one 1 same) (pack-one 1 (seed 0))) same) (pack-two 0 (unary 1 (seed 0)) (binary 0 (seed 0) (unary 1 (seed 0)))))
sound6 : interpret before6 ≡ interpret after6
sound6 = represented-sound proof6
