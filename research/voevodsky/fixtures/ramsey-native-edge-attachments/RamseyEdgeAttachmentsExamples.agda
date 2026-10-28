{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEdgeAttachmentsExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
open import RamseySingleFrameFaces using (c0; m0; c1; m1)
open import RamseyUniformRelative using (first; next)
import RamseyRequestedPortExamples as C
open import RamseyNativeEdgeAttachments
module A = Attachments C.Chart C.Permit C.packet
att-0-0-3 : A.EdgePermit C.q0 e12
att-0-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-0-0-3-native : A.S.R.Resolve (A.S.port-package C.q0 e12 att-0-0-3)
att-0-0-3-native = A.S.port-proof C.q0 e12 att-0-0-3
att-0-0-4 : A.EdgePermit C.q0 e13
att-0-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-0-0-4-native : A.S.R.Resolve (A.S.port-package C.q0 e13 att-0-0-4)
att-0-0-4-native = A.S.port-proof C.q0 e13 att-0-0-4
att-0-0-5 : A.EdgePermit C.q0 e23
att-0-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-0-0-5-native : A.S.R.Resolve (A.S.port-package C.q0 e23 att-0-0-5)
att-0-0-5-native = A.S.port-proof C.q0 e23 att-0-0-5
att-0-2-0 : A.EdgePermit C.q0 e01
att-0-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-0-2-0-native : A.S.R.Resolve (A.S.port-package C.q0 e01 att-0-2-0)
att-0-2-0-native = A.S.port-proof C.q0 e01 att-0-2-0
att-0-2-2 : A.EdgePermit C.q0 e03
att-0-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-0-2-2-native : A.S.R.Resolve (A.S.port-package C.q0 e03 att-0-2-2)
att-0-2-2-native = A.S.port-proof C.q0 e03 att-0-2-2
att-0-2-4 : A.EdgePermit C.q0 e13
att-0-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-0-2-4-native : A.S.R.Resolve (A.S.port-package C.q0 e13 att-0-2-4)
att-0-2-4-native = A.S.port-proof C.q0 e13 att-0-2-4
att-1-0-3 : A.EdgePermit C.q1 e12
att-1-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-1-0-3-native : A.S.R.Resolve (A.S.port-package C.q1 e12 att-1-0-3)
att-1-0-3-native = A.S.port-proof C.q1 e12 att-1-0-3
att-1-0-4 : A.EdgePermit C.q1 e13
att-1-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-1-0-4-native : A.S.R.Resolve (A.S.port-package C.q1 e13 att-1-0-4)
att-1-0-4-native = A.S.port-proof C.q1 e13 att-1-0-4
att-1-0-5 : A.EdgePermit C.q1 e23
att-1-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-1-0-5-native : A.S.R.Resolve (A.S.port-package C.q1 e23 att-1-0-5)
att-1-0-5-native = A.S.port-proof C.q1 e23 att-1-0-5
att-1-3-0 : A.EdgePermit C.q1 e01
att-1-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-1-3-0-native : A.S.R.Resolve (A.S.port-package C.q1 e01 att-1-3-0)
att-1-3-0-native = A.S.port-proof C.q1 e01 att-1-3-0
att-1-3-1 : A.EdgePermit C.q1 e02
att-1-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-1-3-1-native : A.S.R.Resolve (A.S.port-package C.q1 e02 att-1-3-1)
att-1-3-1-native = A.S.port-proof C.q1 e02 att-1-3-1
att-1-3-3 : A.EdgePermit C.q1 e12
att-1-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-1-3-3-native : A.S.R.Resolve (A.S.port-package C.q1 e12 att-1-3-3)
att-1-3-3-native = A.S.port-proof C.q1 e12 att-1-3-3
att-2-0-3 : A.EdgePermit C.q2 e12
att-2-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-2-0-3-native : A.S.R.Resolve (A.S.port-package C.q2 e12 att-2-0-3)
att-2-0-3-native = A.S.port-proof C.q2 e12 att-2-0-3
att-2-0-4 : A.EdgePermit C.q2 e13
att-2-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-2-0-4-native : A.S.R.Resolve (A.S.port-package C.q2 e13 att-2-0-4)
att-2-0-4-native = A.S.port-proof C.q2 e13 att-2-0-4
att-2-0-5 : A.EdgePermit C.q2 e23
att-2-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-2-0-5-native : A.S.R.Resolve (A.S.port-package C.q2 e23 att-2-0-5)
att-2-0-5-native = A.S.port-proof C.q2 e23 att-2-0-5
att-2-1-1 : A.EdgePermit C.q2 e02
att-2-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-2-1-1-native : A.S.R.Resolve (A.S.port-package C.q2 e02 att-2-1-1)
att-2-1-1-native = A.S.port-proof C.q2 e02 att-2-1-1
att-2-1-2 : A.EdgePermit C.q2 e03
att-2-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-2-1-2-native : A.S.R.Resolve (A.S.port-package C.q2 e03 att-2-1-2)
att-2-1-2-native = A.S.port-proof C.q2 e03 att-2-1-2
att-2-1-5 : A.EdgePermit C.q2 e23
att-2-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-2-1-5-native : A.S.R.Resolve (A.S.port-package C.q2 e23 att-2-1-5)
att-2-1-5-native = A.S.port-proof C.q2 e23 att-2-1-5
att-3-0-3 : A.EdgePermit C.q3 e12
att-3-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-3-0-3-native : A.S.R.Resolve (A.S.port-package C.q3 e12 att-3-0-3)
att-3-0-3-native = A.S.port-proof C.q3 e12 att-3-0-3
att-3-0-4 : A.EdgePermit C.q3 e13
att-3-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-3-0-4-native : A.S.R.Resolve (A.S.port-package C.q3 e13 att-3-0-4)
att-3-0-4-native = A.S.port-proof C.q3 e13 att-3-0-4
att-3-0-5 : A.EdgePermit C.q3 e23
att-3-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-3-0-5-native : A.S.R.Resolve (A.S.port-package C.q3 e23 att-3-0-5)
att-3-0-5-native = A.S.port-proof C.q3 e23 att-3-0-5
att-3-3-0 : A.EdgePermit C.q3 e01
att-3-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-3-3-0-native : A.S.R.Resolve (A.S.port-package C.q3 e01 att-3-3-0)
att-3-3-0-native = A.S.port-proof C.q3 e01 att-3-3-0
att-3-3-1 : A.EdgePermit C.q3 e02
att-3-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-3-3-1-native : A.S.R.Resolve (A.S.port-package C.q3 e02 att-3-3-1)
att-3-3-1-native = A.S.port-proof C.q3 e02 att-3-3-1
att-3-3-3 : A.EdgePermit C.q3 e12
att-3-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-3-3-3-native : A.S.R.Resolve (A.S.port-package C.q3 e12 att-3-3-3)
att-3-3-3-native = A.S.port-proof C.q3 e12 att-3-3-3
att-4-0-3 : A.EdgePermit C.q4 e12
att-4-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-4-0-3-native : A.S.R.Resolve (A.S.port-package C.q4 e12 att-4-0-3)
att-4-0-3-native = A.S.port-proof C.q4 e12 att-4-0-3
att-4-0-4 : A.EdgePermit C.q4 e13
att-4-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-4-0-4-native : A.S.R.Resolve (A.S.port-package C.q4 e13 att-4-0-4)
att-4-0-4-native = A.S.port-proof C.q4 e13 att-4-0-4
att-4-0-5 : A.EdgePermit C.q4 e23
att-4-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-4-0-5-native : A.S.R.Resolve (A.S.port-package C.q4 e23 att-4-0-5)
att-4-0-5-native = A.S.port-proof C.q4 e23 att-4-0-5
att-4-1-1 : A.EdgePermit C.q4 e02
att-4-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-4-1-1-native : A.S.R.Resolve (A.S.port-package C.q4 e02 att-4-1-1)
att-4-1-1-native = A.S.port-proof C.q4 e02 att-4-1-1
att-4-1-2 : A.EdgePermit C.q4 e03
att-4-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-4-1-2-native : A.S.R.Resolve (A.S.port-package C.q4 e03 att-4-1-2)
att-4-1-2-native = A.S.port-proof C.q4 e03 att-4-1-2
att-4-1-5 : A.EdgePermit C.q4 e23
att-4-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-4-1-5-native : A.S.R.Resolve (A.S.port-package C.q4 e23 att-4-1-5)
att-4-1-5-native = A.S.port-proof C.q4 e23 att-4-1-5
att-5-0-3 : A.EdgePermit C.q5 e12
att-5-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-5-0-3-native : A.S.R.Resolve (A.S.port-package C.q5 e12 att-5-0-3)
att-5-0-3-native = A.S.port-proof C.q5 e12 att-5-0-3
att-5-0-4 : A.EdgePermit C.q5 e13
att-5-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-5-0-4-native : A.S.R.Resolve (A.S.port-package C.q5 e13 att-5-0-4)
att-5-0-4-native = A.S.port-proof C.q5 e13 att-5-0-4
att-5-0-5 : A.EdgePermit C.q5 e23
att-5-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-5-0-5-native : A.S.R.Resolve (A.S.port-package C.q5 e23 att-5-0-5)
att-5-0-5-native = A.S.port-proof C.q5 e23 att-5-0-5
att-5-2-0 : A.EdgePermit C.q5 e01
att-5-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-5-2-0-native : A.S.R.Resolve (A.S.port-package C.q5 e01 att-5-2-0)
att-5-2-0-native = A.S.port-proof C.q5 e01 att-5-2-0
att-5-2-2 : A.EdgePermit C.q5 e03
att-5-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-5-2-2-native : A.S.R.Resolve (A.S.port-package C.q5 e03 att-5-2-2)
att-5-2-2-native = A.S.port-proof C.q5 e03 att-5-2-2
att-5-2-4 : A.EdgePermit C.q5 e13
att-5-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-5-2-4-native : A.S.R.Resolve (A.S.port-package C.q5 e13 att-5-2-4)
att-5-2-4-native = A.S.port-proof C.q5 e13 att-5-2-4
att-6-1-1 : A.EdgePermit C.q6 e02
att-6-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-6-1-1-native : A.S.R.Resolve (A.S.port-package C.q6 e02 att-6-1-1)
att-6-1-1-native = A.S.port-proof C.q6 e02 att-6-1-1
att-6-1-2 : A.EdgePermit C.q6 e03
att-6-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-6-1-2-native : A.S.R.Resolve (A.S.port-package C.q6 e03 att-6-1-2)
att-6-1-2-native = A.S.port-proof C.q6 e03 att-6-1-2
att-6-1-5 : A.EdgePermit C.q6 e23
att-6-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-6-1-5-native : A.S.R.Resolve (A.S.port-package C.q6 e23 att-6-1-5)
att-6-1-5-native = A.S.port-proof C.q6 e23 att-6-1-5
att-6-2-0 : A.EdgePermit C.q6 e01
att-6-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-6-2-0-native : A.S.R.Resolve (A.S.port-package C.q6 e01 att-6-2-0)
att-6-2-0-native = A.S.port-proof C.q6 e01 att-6-2-0
att-6-2-2 : A.EdgePermit C.q6 e03
att-6-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-6-2-2-native : A.S.R.Resolve (A.S.port-package C.q6 e03 att-6-2-2)
att-6-2-2-native = A.S.port-proof C.q6 e03 att-6-2-2
att-6-2-4 : A.EdgePermit C.q6 e13
att-6-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-6-2-4-native : A.S.R.Resolve (A.S.port-package C.q6 e13 att-6-2-4)
att-6-2-4-native = A.S.port-proof C.q6 e13 att-6-2-4
att-7-1-1 : A.EdgePermit C.q7 e02
att-7-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-7-1-1-native : A.S.R.Resolve (A.S.port-package C.q7 e02 att-7-1-1)
att-7-1-1-native = A.S.port-proof C.q7 e02 att-7-1-1
att-7-1-2 : A.EdgePermit C.q7 e03
att-7-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-7-1-2-native : A.S.R.Resolve (A.S.port-package C.q7 e03 att-7-1-2)
att-7-1-2-native = A.S.port-proof C.q7 e03 att-7-1-2
att-7-1-5 : A.EdgePermit C.q7 e23
att-7-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-7-1-5-native : A.S.R.Resolve (A.S.port-package C.q7 e23 att-7-1-5)
att-7-1-5-native = A.S.port-proof C.q7 e23 att-7-1-5
att-7-3-0 : A.EdgePermit C.q7 e01
att-7-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-7-3-0-native : A.S.R.Resolve (A.S.port-package C.q7 e01 att-7-3-0)
att-7-3-0-native = A.S.port-proof C.q7 e01 att-7-3-0
att-7-3-1 : A.EdgePermit C.q7 e02
att-7-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-7-3-1-native : A.S.R.Resolve (A.S.port-package C.q7 e02 att-7-3-1)
att-7-3-1-native = A.S.port-proof C.q7 e02 att-7-3-1
att-7-3-3 : A.EdgePermit C.q7 e12
att-7-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-7-3-3-native : A.S.R.Resolve (A.S.port-package C.q7 e12 att-7-3-3)
att-7-3-3-native = A.S.port-proof C.q7 e12 att-7-3-3
att-8-1-1 : A.EdgePermit C.q8 e02
att-8-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-8-1-1-native : A.S.R.Resolve (A.S.port-package C.q8 e02 att-8-1-1)
att-8-1-1-native = A.S.port-proof C.q8 e02 att-8-1-1
att-8-1-2 : A.EdgePermit C.q8 e03
att-8-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-8-1-2-native : A.S.R.Resolve (A.S.port-package C.q8 e03 att-8-1-2)
att-8-1-2-native = A.S.port-proof C.q8 e03 att-8-1-2
att-8-1-5 : A.EdgePermit C.q8 e23
att-8-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-8-1-5-native : A.S.R.Resolve (A.S.port-package C.q8 e23 att-8-1-5)
att-8-1-5-native = A.S.port-proof C.q8 e23 att-8-1-5
att-8-0-3 : A.EdgePermit C.q8 e12
att-8-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-8-0-3-native : A.S.R.Resolve (A.S.port-package C.q8 e12 att-8-0-3)
att-8-0-3-native = A.S.port-proof C.q8 e12 att-8-0-3
att-8-0-4 : A.EdgePermit C.q8 e13
att-8-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-8-0-4-native : A.S.R.Resolve (A.S.port-package C.q8 e13 att-8-0-4)
att-8-0-4-native = A.S.port-proof C.q8 e13 att-8-0-4
att-8-0-5 : A.EdgePermit C.q8 e23
att-8-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-8-0-5-native : A.S.R.Resolve (A.S.port-package C.q8 e23 att-8-0-5)
att-8-0-5-native = A.S.port-proof C.q8 e23 att-8-0-5
att-9-1-1 : A.EdgePermit C.q9 e02
att-9-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-9-1-1-native : A.S.R.Resolve (A.S.port-package C.q9 e02 att-9-1-1)
att-9-1-1-native = A.S.port-proof C.q9 e02 att-9-1-1
att-9-1-2 : A.EdgePermit C.q9 e03
att-9-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-9-1-2-native : A.S.R.Resolve (A.S.port-package C.q9 e03 att-9-1-2)
att-9-1-2-native = A.S.port-proof C.q9 e03 att-9-1-2
att-9-1-5 : A.EdgePermit C.q9 e23
att-9-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-9-1-5-native : A.S.R.Resolve (A.S.port-package C.q9 e23 att-9-1-5)
att-9-1-5-native = A.S.port-proof C.q9 e23 att-9-1-5
att-9-3-0 : A.EdgePermit C.q9 e01
att-9-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-9-3-0-native : A.S.R.Resolve (A.S.port-package C.q9 e01 att-9-3-0)
att-9-3-0-native = A.S.port-proof C.q9 e01 att-9-3-0
att-9-3-1 : A.EdgePermit C.q9 e02
att-9-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-9-3-1-native : A.S.R.Resolve (A.S.port-package C.q9 e02 att-9-3-1)
att-9-3-1-native = A.S.port-proof C.q9 e02 att-9-3-1
att-9-3-3 : A.EdgePermit C.q9 e12
att-9-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-9-3-3-native : A.S.R.Resolve (A.S.port-package C.q9 e12 att-9-3-3)
att-9-3-3-native = A.S.port-proof C.q9 e12 att-9-3-3
att-10-1-1 : A.EdgePermit C.q10 e02
att-10-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-10-1-1-native : A.S.R.Resolve (A.S.port-package C.q10 e02 att-10-1-1)
att-10-1-1-native = A.S.port-proof C.q10 e02 att-10-1-1
att-10-1-2 : A.EdgePermit C.q10 e03
att-10-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-10-1-2-native : A.S.R.Resolve (A.S.port-package C.q10 e03 att-10-1-2)
att-10-1-2-native = A.S.port-proof C.q10 e03 att-10-1-2
att-10-1-5 : A.EdgePermit C.q10 e23
att-10-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-10-1-5-native : A.S.R.Resolve (A.S.port-package C.q10 e23 att-10-1-5)
att-10-1-5-native = A.S.port-proof C.q10 e23 att-10-1-5
att-10-0-3 : A.EdgePermit C.q10 e12
att-10-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-10-0-3-native : A.S.R.Resolve (A.S.port-package C.q10 e12 att-10-0-3)
att-10-0-3-native = A.S.port-proof C.q10 e12 att-10-0-3
att-10-0-4 : A.EdgePermit C.q10 e13
att-10-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-10-0-4-native : A.S.R.Resolve (A.S.port-package C.q10 e13 att-10-0-4)
att-10-0-4-native = A.S.port-proof C.q10 e13 att-10-0-4
att-10-0-5 : A.EdgePermit C.q10 e23
att-10-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-10-0-5-native : A.S.R.Resolve (A.S.port-package C.q10 e23 att-10-0-5)
att-10-0-5-native = A.S.port-proof C.q10 e23 att-10-0-5
att-11-1-1 : A.EdgePermit C.q11 e02
att-11-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-11-1-1-native : A.S.R.Resolve (A.S.port-package C.q11 e02 att-11-1-1)
att-11-1-1-native = A.S.port-proof C.q11 e02 att-11-1-1
att-11-1-2 : A.EdgePermit C.q11 e03
att-11-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-11-1-2-native : A.S.R.Resolve (A.S.port-package C.q11 e03 att-11-1-2)
att-11-1-2-native = A.S.port-proof C.q11 e03 att-11-1-2
att-11-1-5 : A.EdgePermit C.q11 e23
att-11-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-11-1-5-native : A.S.R.Resolve (A.S.port-package C.q11 e23 att-11-1-5)
att-11-1-5-native = A.S.port-proof C.q11 e23 att-11-1-5
att-11-2-0 : A.EdgePermit C.q11 e01
att-11-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-11-2-0-native : A.S.R.Resolve (A.S.port-package C.q11 e01 att-11-2-0)
att-11-2-0-native = A.S.port-proof C.q11 e01 att-11-2-0
att-11-2-2 : A.EdgePermit C.q11 e03
att-11-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-11-2-2-native : A.S.R.Resolve (A.S.port-package C.q11 e03 att-11-2-2)
att-11-2-2-native = A.S.port-proof C.q11 e03 att-11-2-2
att-11-2-4 : A.EdgePermit C.q11 e13
att-11-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-11-2-4-native : A.S.R.Resolve (A.S.port-package C.q11 e13 att-11-2-4)
att-11-2-4-native = A.S.port-proof C.q11 e13 att-11-2-4
att-12-2-0 : A.EdgePermit C.q12 e01
att-12-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-12-2-0-native : A.S.R.Resolve (A.S.port-package C.q12 e01 att-12-2-0)
att-12-2-0-native = A.S.port-proof C.q12 e01 att-12-2-0
att-12-2-2 : A.EdgePermit C.q12 e03
att-12-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-12-2-2-native : A.S.R.Resolve (A.S.port-package C.q12 e03 att-12-2-2)
att-12-2-2-native = A.S.port-proof C.q12 e03 att-12-2-2
att-12-2-4 : A.EdgePermit C.q12 e13
att-12-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-12-2-4-native : A.S.R.Resolve (A.S.port-package C.q12 e13 att-12-2-4)
att-12-2-4-native = A.S.port-proof C.q12 e13 att-12-2-4
att-12-1-1 : A.EdgePermit C.q12 e02
att-12-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-12-1-1-native : A.S.R.Resolve (A.S.port-package C.q12 e02 att-12-1-1)
att-12-1-1-native = A.S.port-proof C.q12 e02 att-12-1-1
att-12-1-2 : A.EdgePermit C.q12 e03
att-12-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-12-1-2-native : A.S.R.Resolve (A.S.port-package C.q12 e03 att-12-1-2)
att-12-1-2-native = A.S.port-proof C.q12 e03 att-12-1-2
att-12-1-5 : A.EdgePermit C.q12 e23
att-12-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-12-1-5-native : A.S.R.Resolve (A.S.port-package C.q12 e23 att-12-1-5)
att-12-1-5-native = A.S.port-proof C.q12 e23 att-12-1-5
att-13-2-0 : A.EdgePermit C.q13 e01
att-13-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-13-2-0-native : A.S.R.Resolve (A.S.port-package C.q13 e01 att-13-2-0)
att-13-2-0-native = A.S.port-proof C.q13 e01 att-13-2-0
att-13-2-2 : A.EdgePermit C.q13 e03
att-13-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-13-2-2-native : A.S.R.Resolve (A.S.port-package C.q13 e03 att-13-2-2)
att-13-2-2-native = A.S.port-proof C.q13 e03 att-13-2-2
att-13-2-4 : A.EdgePermit C.q13 e13
att-13-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-13-2-4-native : A.S.R.Resolve (A.S.port-package C.q13 e13 att-13-2-4)
att-13-2-4-native = A.S.port-proof C.q13 e13 att-13-2-4
att-13-3-0 : A.EdgePermit C.q13 e01
att-13-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-13-3-0-native : A.S.R.Resolve (A.S.port-package C.q13 e01 att-13-3-0)
att-13-3-0-native = A.S.port-proof C.q13 e01 att-13-3-0
att-13-3-1 : A.EdgePermit C.q13 e02
att-13-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-13-3-1-native : A.S.R.Resolve (A.S.port-package C.q13 e02 att-13-3-1)
att-13-3-1-native = A.S.port-proof C.q13 e02 att-13-3-1
att-13-3-3 : A.EdgePermit C.q13 e12
att-13-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-13-3-3-native : A.S.R.Resolve (A.S.port-package C.q13 e12 att-13-3-3)
att-13-3-3-native = A.S.port-proof C.q13 e12 att-13-3-3
att-14-2-0 : A.EdgePermit C.q14 e01
att-14-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-14-2-0-native : A.S.R.Resolve (A.S.port-package C.q14 e01 att-14-2-0)
att-14-2-0-native = A.S.port-proof C.q14 e01 att-14-2-0
att-14-2-2 : A.EdgePermit C.q14 e03
att-14-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-14-2-2-native : A.S.R.Resolve (A.S.port-package C.q14 e03 att-14-2-2)
att-14-2-2-native = A.S.port-proof C.q14 e03 att-14-2-2
att-14-2-4 : A.EdgePermit C.q14 e13
att-14-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-14-2-4-native : A.S.R.Resolve (A.S.port-package C.q14 e13 att-14-2-4)
att-14-2-4-native = A.S.port-proof C.q14 e13 att-14-2-4
att-14-0-3 : A.EdgePermit C.q14 e12
att-14-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-14-0-3-native : A.S.R.Resolve (A.S.port-package C.q14 e12 att-14-0-3)
att-14-0-3-native = A.S.port-proof C.q14 e12 att-14-0-3
att-14-0-4 : A.EdgePermit C.q14 e13
att-14-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-14-0-4-native : A.S.R.Resolve (A.S.port-package C.q14 e13 att-14-0-4)
att-14-0-4-native = A.S.port-proof C.q14 e13 att-14-0-4
att-14-0-5 : A.EdgePermit C.q14 e23
att-14-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-14-0-5-native : A.S.R.Resolve (A.S.port-package C.q14 e23 att-14-0-5)
att-14-0-5-native = A.S.port-proof C.q14 e23 att-14-0-5
att-15-2-0 : A.EdgePermit C.q15 e01
att-15-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-15-2-0-native : A.S.R.Resolve (A.S.port-package C.q15 e01 att-15-2-0)
att-15-2-0-native = A.S.port-proof C.q15 e01 att-15-2-0
att-15-2-2 : A.EdgePermit C.q15 e03
att-15-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-15-2-2-native : A.S.R.Resolve (A.S.port-package C.q15 e03 att-15-2-2)
att-15-2-2-native = A.S.port-proof C.q15 e03 att-15-2-2
att-15-2-4 : A.EdgePermit C.q15 e13
att-15-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-15-2-4-native : A.S.R.Resolve (A.S.port-package C.q15 e13 att-15-2-4)
att-15-2-4-native = A.S.port-proof C.q15 e13 att-15-2-4
att-15-3-0 : A.EdgePermit C.q15 e01
att-15-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-15-3-0-native : A.S.R.Resolve (A.S.port-package C.q15 e01 att-15-3-0)
att-15-3-0-native = A.S.port-proof C.q15 e01 att-15-3-0
att-15-3-1 : A.EdgePermit C.q15 e02
att-15-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-15-3-1-native : A.S.R.Resolve (A.S.port-package C.q15 e02 att-15-3-1)
att-15-3-1-native = A.S.port-proof C.q15 e02 att-15-3-1
att-15-3-3 : A.EdgePermit C.q15 e12
att-15-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-15-3-3-native : A.S.R.Resolve (A.S.port-package C.q15 e12 att-15-3-3)
att-15-3-3-native = A.S.port-proof C.q15 e12 att-15-3-3
att-16-2-0 : A.EdgePermit C.q16 e01
att-16-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-16-2-0-native : A.S.R.Resolve (A.S.port-package C.q16 e01 att-16-2-0)
att-16-2-0-native = A.S.port-proof C.q16 e01 att-16-2-0
att-16-2-2 : A.EdgePermit C.q16 e03
att-16-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-16-2-2-native : A.S.R.Resolve (A.S.port-package C.q16 e03 att-16-2-2)
att-16-2-2-native = A.S.port-proof C.q16 e03 att-16-2-2
att-16-2-4 : A.EdgePermit C.q16 e13
att-16-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-16-2-4-native : A.S.R.Resolve (A.S.port-package C.q16 e13 att-16-2-4)
att-16-2-4-native = A.S.port-proof C.q16 e13 att-16-2-4
att-16-0-3 : A.EdgePermit C.q16 e12
att-16-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-16-0-3-native : A.S.R.Resolve (A.S.port-package C.q16 e12 att-16-0-3)
att-16-0-3-native = A.S.port-proof C.q16 e12 att-16-0-3
att-16-0-4 : A.EdgePermit C.q16 e13
att-16-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-16-0-4-native : A.S.R.Resolve (A.S.port-package C.q16 e13 att-16-0-4)
att-16-0-4-native = A.S.port-proof C.q16 e13 att-16-0-4
att-16-0-5 : A.EdgePermit C.q16 e23
att-16-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-16-0-5-native : A.S.R.Resolve (A.S.port-package C.q16 e23 att-16-0-5)
att-16-0-5-native = A.S.port-proof C.q16 e23 att-16-0-5
att-17-2-0 : A.EdgePermit C.q17 e01
att-17-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-17-2-0-native : A.S.R.Resolve (A.S.port-package C.q17 e01 att-17-2-0)
att-17-2-0-native = A.S.port-proof C.q17 e01 att-17-2-0
att-17-2-2 : A.EdgePermit C.q17 e03
att-17-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-17-2-2-native : A.S.R.Resolve (A.S.port-package C.q17 e03 att-17-2-2)
att-17-2-2-native = A.S.port-proof C.q17 e03 att-17-2-2
att-17-2-4 : A.EdgePermit C.q17 e13
att-17-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-17-2-4-native : A.S.R.Resolve (A.S.port-package C.q17 e13 att-17-2-4)
att-17-2-4-native = A.S.port-proof C.q17 e13 att-17-2-4
att-17-1-1 : A.EdgePermit C.q17 e02
att-17-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-17-1-1-native : A.S.R.Resolve (A.S.port-package C.q17 e02 att-17-1-1)
att-17-1-1-native = A.S.port-proof C.q17 e02 att-17-1-1
att-17-1-2 : A.EdgePermit C.q17 e03
att-17-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-17-1-2-native : A.S.R.Resolve (A.S.port-package C.q17 e03 att-17-1-2)
att-17-1-2-native = A.S.port-proof C.q17 e03 att-17-1-2
att-17-1-5 : A.EdgePermit C.q17 e23
att-17-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-17-1-5-native : A.S.R.Resolve (A.S.port-package C.q17 e23 att-17-1-5)
att-17-1-5-native = A.S.port-proof C.q17 e23 att-17-1-5
att-18-3-0 : A.EdgePermit C.q18 e01
att-18-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-18-3-0-native : A.S.R.Resolve (A.S.port-package C.q18 e01 att-18-3-0)
att-18-3-0-native = A.S.port-proof C.q18 e01 att-18-3-0
att-18-3-1 : A.EdgePermit C.q18 e02
att-18-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-18-3-1-native : A.S.R.Resolve (A.S.port-package C.q18 e02 att-18-3-1)
att-18-3-1-native = A.S.port-proof C.q18 e02 att-18-3-1
att-18-3-3 : A.EdgePermit C.q18 e12
att-18-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-18-3-3-native : A.S.R.Resolve (A.S.port-package C.q18 e12 att-18-3-3)
att-18-3-3-native = A.S.port-proof C.q18 e12 att-18-3-3
att-18-1-1 : A.EdgePermit C.q18 e02
att-18-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-18-1-1-native : A.S.R.Resolve (A.S.port-package C.q18 e02 att-18-1-1)
att-18-1-1-native = A.S.port-proof C.q18 e02 att-18-1-1
att-18-1-2 : A.EdgePermit C.q18 e03
att-18-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-18-1-2-native : A.S.R.Resolve (A.S.port-package C.q18 e03 att-18-1-2)
att-18-1-2-native = A.S.port-proof C.q18 e03 att-18-1-2
att-18-1-5 : A.EdgePermit C.q18 e23
att-18-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-18-1-5-native : A.S.R.Resolve (A.S.port-package C.q18 e23 att-18-1-5)
att-18-1-5-native = A.S.port-proof C.q18 e23 att-18-1-5
att-19-3-0 : A.EdgePermit C.q19 e01
att-19-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-19-3-0-native : A.S.R.Resolve (A.S.port-package C.q19 e01 att-19-3-0)
att-19-3-0-native = A.S.port-proof C.q19 e01 att-19-3-0
att-19-3-1 : A.EdgePermit C.q19 e02
att-19-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-19-3-1-native : A.S.R.Resolve (A.S.port-package C.q19 e02 att-19-3-1)
att-19-3-1-native = A.S.port-proof C.q19 e02 att-19-3-1
att-19-3-3 : A.EdgePermit C.q19 e12
att-19-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-19-3-3-native : A.S.R.Resolve (A.S.port-package C.q19 e12 att-19-3-3)
att-19-3-3-native = A.S.port-proof C.q19 e12 att-19-3-3
att-19-2-0 : A.EdgePermit C.q19 e01
att-19-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-19-2-0-native : A.S.R.Resolve (A.S.port-package C.q19 e01 att-19-2-0)
att-19-2-0-native = A.S.port-proof C.q19 e01 att-19-2-0
att-19-2-2 : A.EdgePermit C.q19 e03
att-19-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-19-2-2-native : A.S.R.Resolve (A.S.port-package C.q19 e03 att-19-2-2)
att-19-2-2-native = A.S.port-proof C.q19 e03 att-19-2-2
att-19-2-4 : A.EdgePermit C.q19 e13
att-19-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-19-2-4-native : A.S.R.Resolve (A.S.port-package C.q19 e13 att-19-2-4)
att-19-2-4-native = A.S.port-proof C.q19 e13 att-19-2-4
att-20-3-0 : A.EdgePermit C.q20 e01
att-20-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-20-3-0-native : A.S.R.Resolve (A.S.port-package C.q20 e01 att-20-3-0)
att-20-3-0-native = A.S.port-proof C.q20 e01 att-20-3-0
att-20-3-1 : A.EdgePermit C.q20 e02
att-20-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-20-3-1-native : A.S.R.Resolve (A.S.port-package C.q20 e02 att-20-3-1)
att-20-3-1-native = A.S.port-proof C.q20 e02 att-20-3-1
att-20-3-3 : A.EdgePermit C.q20 e12
att-20-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-20-3-3-native : A.S.R.Resolve (A.S.port-package C.q20 e12 att-20-3-3)
att-20-3-3-native = A.S.port-proof C.q20 e12 att-20-3-3
att-20-0-3 : A.EdgePermit C.q20 e12
att-20-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-20-0-3-native : A.S.R.Resolve (A.S.port-package C.q20 e12 att-20-0-3)
att-20-0-3-native = A.S.port-proof C.q20 e12 att-20-0-3
att-20-0-4 : A.EdgePermit C.q20 e13
att-20-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-20-0-4-native : A.S.R.Resolve (A.S.port-package C.q20 e13 att-20-0-4)
att-20-0-4-native = A.S.port-proof C.q20 e13 att-20-0-4
att-20-0-5 : A.EdgePermit C.q20 e23
att-20-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-20-0-5-native : A.S.R.Resolve (A.S.port-package C.q20 e23 att-20-0-5)
att-20-0-5-native = A.S.port-proof C.q20 e23 att-20-0-5
att-21-3-0 : A.EdgePermit C.q21 e01
att-21-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-21-3-0-native : A.S.R.Resolve (A.S.port-package C.q21 e01 att-21-3-0)
att-21-3-0-native = A.S.port-proof C.q21 e01 att-21-3-0
att-21-3-1 : A.EdgePermit C.q21 e02
att-21-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-21-3-1-native : A.S.R.Resolve (A.S.port-package C.q21 e02 att-21-3-1)
att-21-3-1-native = A.S.port-proof C.q21 e02 att-21-3-1
att-21-3-3 : A.EdgePermit C.q21 e12
att-21-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-21-3-3-native : A.S.R.Resolve (A.S.port-package C.q21 e12 att-21-3-3)
att-21-3-3-native = A.S.port-proof C.q21 e12 att-21-3-3
att-21-2-0 : A.EdgePermit C.q21 e01
att-21-2-0 = c1 , (refl , (((first) , refl) , ((next first) , refl)))
att-21-2-0-native : A.S.R.Resolve (A.S.port-package C.q21 e01 att-21-2-0)
att-21-2-0-native = A.S.port-proof C.q21 e01 att-21-2-0
att-21-2-2 : A.EdgePermit C.q21 e03
att-21-2-2 = c1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-21-2-2-native : A.S.R.Resolve (A.S.port-package C.q21 e03 att-21-2-2)
att-21-2-2-native = A.S.port-proof C.q21 e03 att-21-2-2
att-21-2-4 : A.EdgePermit C.q21 e13
att-21-2-4 = c1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-21-2-4-native : A.S.R.Resolve (A.S.port-package C.q21 e13 att-21-2-4)
att-21-2-4-native = A.S.port-proof C.q21 e13 att-21-2-4
att-22-3-0 : A.EdgePermit C.q22 e01
att-22-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-22-3-0-native : A.S.R.Resolve (A.S.port-package C.q22 e01 att-22-3-0)
att-22-3-0-native = A.S.port-proof C.q22 e01 att-22-3-0
att-22-3-1 : A.EdgePermit C.q22 e02
att-22-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-22-3-1-native : A.S.R.Resolve (A.S.port-package C.q22 e02 att-22-3-1)
att-22-3-1-native = A.S.port-proof C.q22 e02 att-22-3-1
att-22-3-3 : A.EdgePermit C.q22 e12
att-22-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-22-3-3-native : A.S.R.Resolve (A.S.port-package C.q22 e12 att-22-3-3)
att-22-3-3-native = A.S.port-proof C.q22 e12 att-22-3-3
att-22-0-3 : A.EdgePermit C.q22 e12
att-22-0-3 = c0 , (refl , (((first) , refl) , ((next first) , refl)))
att-22-0-3-native : A.S.R.Resolve (A.S.port-package C.q22 e12 att-22-0-3)
att-22-0-3-native = A.S.port-proof C.q22 e12 att-22-0-3
att-22-0-4 : A.EdgePermit C.q22 e13
att-22-0-4 = c0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-22-0-4-native : A.S.R.Resolve (A.S.port-package C.q22 e13 att-22-0-4)
att-22-0-4-native = A.S.port-proof C.q22 e13 att-22-0-4
att-22-0-5 : A.EdgePermit C.q22 e23
att-22-0-5 = c0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-22-0-5-native : A.S.R.Resolve (A.S.port-package C.q22 e23 att-22-0-5)
att-22-0-5-native = A.S.port-proof C.q22 e23 att-22-0-5
att-23-3-0 : A.EdgePermit C.q23 e01
att-23-3-0 = m1 , (refl , (((first) , refl) , ((next first) , refl)))
att-23-3-0-native : A.S.R.Resolve (A.S.port-package C.q23 e01 att-23-3-0)
att-23-3-0-native = A.S.port-proof C.q23 e01 att-23-3-0
att-23-3-1 : A.EdgePermit C.q23 e02
att-23-3-1 = m1 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-23-3-1-native : A.S.R.Resolve (A.S.port-package C.q23 e02 att-23-3-1)
att-23-3-1-native = A.S.port-proof C.q23 e02 att-23-3-1
att-23-3-3 : A.EdgePermit C.q23 e12
att-23-3-3 = m1 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-23-3-3-native : A.S.R.Resolve (A.S.port-package C.q23 e12 att-23-3-3)
att-23-3-3-native = A.S.port-proof C.q23 e12 att-23-3-3
att-23-1-1 : A.EdgePermit C.q23 e02
att-23-1-1 = m0 , (refl , (((first) , refl) , ((next first) , refl)))
att-23-1-1-native : A.S.R.Resolve (A.S.port-package C.q23 e02 att-23-1-1)
att-23-1-1-native = A.S.port-proof C.q23 e02 att-23-1-1
att-23-1-2 : A.EdgePermit C.q23 e03
att-23-1-2 = m0 , (refl , (((first) , refl) , ((next (next first)) , refl)))
att-23-1-2-native : A.S.R.Resolve (A.S.port-package C.q23 e03 att-23-1-2)
att-23-1-2-native = A.S.port-proof C.q23 e03 att-23-1-2
att-23-1-5 : A.EdgePermit C.q23 e23
att-23-1-5 = m0 , (refl , (((next first) , refl) , ((next (next first)) , refl)))
att-23-1-5-native : A.S.R.Resolve (A.S.port-package C.q23 e23 att-23-1-5)
att-23-1-5-native = A.S.port-proof C.q23 e23 att-23-1-5
triple : A.S.Triple C.q0 C.q2 C.q0
triple = e13 , (att-0-2-4 , (att-2-0-4 , att-0-0-4))
native-composition : A.S.R.Resolve (A.S.composition-package C.q0 C.q2 C.q0 triple)
native-composition = A.S.composition-proof C.q0 C.q2 C.q0 triple
vertex-composition : A.V.R.Resolve (A.V.composition-package C.q0 C.q2 C.q0 (A.restrict-triple false {a = C.q0} {b = C.q2} {c = C.q0} triple))
vertex-composition = A.V.composition-proof C.q0 C.q2 C.q0 (A.restrict-triple false {a = C.q0} {b = C.q2} {c = C.q0} triple)
