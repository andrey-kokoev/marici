{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetDomainAdmission where
open import Cubical.Foundations.Prelude
import ResolutionNetIndexedPortCertificates as I
import ResolutionNetFootprints as F
import CoherenceResolutionClosure as C
data Token : Type where
  t0 t1 : Token
module R = F.Resources Token
module RC = C.Closure R.World R.U R.V
world : I.Pkg → R.World
world I.p0 t0 = F.spent
world I.p0 t1 = F.spent
world I.p1 t0 = F.spent
world I.p1 t1 = F.absent
world I.p2 t0 = F.absent
world I.p2 t1 = F.spent
world I.p3 t0 = F.free
world I.p3 t1 = F.absent
world I.p4 t0 = F.absent
world I.p4 t1 = F.free

unary-rule : {p q : I.Pkg} → I.U p q → R.U (world p) (world q)
unary-rule I.rule1 t0 = F.consume
unary-rule I.rule1 t1 = F.stay F.absent
unary-rule I.rule2 t0 = F.stay F.absent
unary-rule I.rule2 t1 = F.consume

binary-rule : {p q r : I.Pkg} → I.V p q r → R.V (world p) (world q) (world r)
binary-rule I.rule0 t0 = F.from-left F.spent
binary-rule I.rule0 t1 = F.from-right F.spent

seed-rule : {p : I.Pkg} → I.Evidence p → R.Initial (world p)
seed-rule I.evidence0 t0 = F.fresh-free
seed-rule I.evidence0 t1 = F.fresh-absent
seed-rule I.evidence1 t0 = F.fresh-absent
seed-rule I.evidence1 t1 = F.fresh-free
seed-rule I.evidence2 t0 = F.fresh-free
seed-rule I.evidence2 t1 = F.fresh-absent

translate : {p : I.Pkg} → I.Resolve I.Evidence p → RC.Resolve R.Initial (world p)
translate (I.seed e) = RC.seed (seed-rule e)
translate (I.unary u d) = RC.unary (unary-rule u) (translate d)
translate (I.binary v d e) = RC.binary (binary-rule v) (translate d) (translate e)

no-double-use : {p : I.Pkg} (d : I.Resolve I.Evidence p) (t : Token) → F.AtMostOne (R.uses (translate d) t)
no-double-use d t = R.no-double-spend (translate d) t
no-duplicate-origin : {p : I.Pkg} (d : I.Resolve I.Evidence p) (t : Token) → F.AtMostOne (R.origins (translate d) t)
no-duplicate-origin d t = R.no-duplicate-origin (translate d) t

domain-sound0 : translate (I.interpret I.before0) ≡ translate (I.interpret I.after0)
domain-sound0 = cong translate I.sound0

domain-sound1 : translate (I.interpret I.before1) ≡ translate (I.interpret I.after1)
domain-sound1 = cong translate I.sound1

domain-sound2 : translate (I.interpret I.before2) ≡ translate (I.interpret I.after2)
domain-sound2 = cong translate I.sound2

domain-sound3 : translate (I.interpret I.before3) ≡ translate (I.interpret I.after3)
domain-sound3 = cong translate I.sound3

domain-sound4 : translate (I.interpret I.before4) ≡ translate (I.interpret I.after4)
domain-sound4 = cong translate I.sound4

