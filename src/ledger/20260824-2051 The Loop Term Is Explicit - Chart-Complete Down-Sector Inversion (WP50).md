---
author: marici.Figueiredo
---

# 2051 - The Loop Term Is Explicit: Chart-Complete Down-Sector Inversion (WP50)

## Question

WP49 inverted the down sector rationally on the WP44 family (Hd_01 = 0)
and left the complement open: there the characteristic polynomial keeps
the loop-product term L = 2 Re(Hd_01 Hd_12 Hd_02*). WP48 open item 2
asked how M's loop piece is absorbed. WP50 closes the inversion on
every chart stratum and makes the loop's role exact.

## The three chart strata

The 848 block-diagonal sheets split by down-sector zero pattern in the
canonical (singlet-first) frame:

| stratum | pattern | sheets | loop |
|---|---|---|---|
| S1 chain-star | Hd_01 = 0 | 394 | dead (contains Hd_01) |
| S2 singlet-star | Hd_12 = 0 | 282 | dead (contains Hd_12), exactly 0.0 |
| S3 triangle | all entries nonzero | 172 | ALIVE |

## Universal identities (all 848 sheets, physical inputs only)

With u_j the singlet CKM row moduli and lam_j the down masses:

  d0 = sum u.lam,   beta = e3 . sum u/lam = M_00,
  K1 := |Hd_01|^2 + |Hd_02|^2 = beta + d0.e1' - e2,
  K2 := d0.beta - e3 = d1.|Hd_02|^2 + d2.|Hd_01|^2 - L,

max rel err 2.2e-11. The loop enters the chart moduli system through
exactly one place: the determinant form K2.

## Full-chart identity

Every chart entry (not just moduli) is an explicit algebraic function of
physical data:

  Hd_flavor = Uu . (V_CKM . diag(lam) . V_CKM^+) . Uu^+,

with Uu the up-eigenvector matrix in the weak basis. Max entry deviation
2.2e-15 over all 848 sheets.

## Strata inversions for the moduli

  S1: x = 0, d1 = K2/K1 (the WP49 linear formula), 1.1e-11.
  S2: loop exactly zero; x from the chart identity;
      d1 = (K2 - e1'.x)/(v2 - x), linear, 2.2e-11.
  S3: d1 is a root of the explicit quadratic

      [d1(v2-x) + e1'.x - K2]^2 = 4.x.v2.(d1(e1'-d1) - beta) - Ls^2,

      Ls = 2 Im(loop); root match 3.5e-12. The S1 formula is the
      degenerate double-root limit (x -> 0 collapses the quadratic to
      d1 = K2/v2), and the physical root is the one nearer the
      family-limit estimate d1^0 = K2/v2 on 172/172 sheets - continuity
      with S1 selects the branch, no extra input needed.
      Then L = d1(v2-x) + e1'.x - K2 (det identity, 1.7e-12) and
      |Ls| = sqrt(4.x.v2.w2 - L^2). The sign of Ls is the CP
      orientation: the ONLY J-sensitive input in the whole inversion.
      Every modulus is CP-even physical data.

      Auxiliary identity (1e-15): the up-mass block-block modulus
      mu12 = [st.ct.(d2-d1) + (ct^2-st^2).Re Z]^2 + Im(Z)^2 with
      Z = e^{-i.psi}.Hd_12, psi = arg(HuC_12), th = atan2(2|c|, a-b)/2.

## Answer to the WP48 loop question

The loop piece of M is absorbed as follows: the purity C_class is built
from v2 and w2, which the inversion gives from CP-even physical data on
every stratum; the loop's real part L is fixed by the determinant form;
its imaginary part's modulus is fixed by the moduli; only its sign -
the orientation - is CP-odd. So J enters the chart reconstruction only
as an orientation bit, and the WP48 parameter-free complement
prediction is explained: there was never any chart freedom left for the
loop to disturb.

## Boundary and open items

1. The WP48 chain q = J.blockgap.Dd/(v2.sqrt(w2)) is an S1-chart
   identity (8e-13). On S2/S3 the chain involves different edge
   products - on S2 the up-down MIXED loop must carry J, since w2 = 0
   but J != 0. Those per-stratum chain monomials are open chart algebra.
2. The S3 quadratic needs Ls as input; physically Ls is supplied by the
   CP-odd invariant (J) up to the down-sector determination of |Ls|.
   A fully explicit J-to-Ls chart formula is part of item 1.
3. Why the purity function F evaluates within 1e-2 of 1 for all three
   anchors remains the open residue from ledger 2035.

## Verification

`./.venv/Scripts/python checkers/wp50_complement_inversion.py`
reproduces `results/wp50_complement_inversion.json` (8/8 gates, exit 0).
