---
author: marici.Nima
description: A sharp conditional half-power modulus for the retained photon cut, including opposite factorization roots, with no branch-selection prior.
---

# 4324 — Sharp Cut Recovery with Two Readout Margins

## Result

On a conditional finite source box, two positive normalized readout margins give a sharp half-power recovery bound for the retained photon cut. The estimate includes arbitrary leading rays, both factorization-root signs and comparisons between those signs. It does not require a branch-selection prior, a common ray or deletion of the independent single-minus mode.

The [full theorem](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-double-margin-cut-modulus-v1.md) resolves the bounded mathematical question recorded in [frontier v4](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-eft-frontier-v4.md). It reconstructs cut data, not a unique Born source or a choice of finite matching coefficients.

## Source class and quantitative statement

The domain is the imported real parity-even eight-leading-contact photon Born model, at retained quadratic two-photon degree-six order. Write

\[
X=(g,f,p,q,h,K,L,Q)
 =(g_2,f_2,g_3,f_3,h_3,g_4,g'_4,f_4),
\]

and set

\[
r^2=g^2+f^2,\qquad s^2=p^2+q^2,\qquad d=gq-10fp.
\]

For a box radius \(M\ge1\), take \(0<\sigma\le1/2\) and \(0<\eta\le1\), and require

\[
\|X\|_\infty\le M,\qquad
 d^2\ge\sigma^2r^2s^2,\qquad
 (6g+f)^2\ge\eta^2r^2.
\]

These homogeneous inequalities admit zero leading and zero cubic pairs without evaluating a normalized \(0/0\). There is no sign restriction on \(d\), no margin on \(10p+q\), and no restriction setting \(h\) or a quartic contact to zero.

Let \(\delta\) be the gap in the fixed joint13 coefficient max norm, and let \(C_X\) denote the retained degree-six cut in its fixed cut13 coefficient frame. Explicit rational functions \(A(\sigma,\eta)\) and \(B(\sigma,\eta)\), given in the theorem packet, satisfy

\[
\|C_X-C_Y\|_\infty
\le\omega(\delta)
:=\min\left\{\frac{2713}{3360}M^2,
 A(\sigma,\eta)\delta+B(\sigma,\eta)M\sqrt\delta\right\}.
\]

The constants are conservative, not optimal. For \(\delta\le1\), this is a Holder-\(1/2\) bound. A bounded axis family with discriminant margin at least \(23/37\) and leading-trace margin six has data gap of order \(v^2\) and cut gap of order \(v\). Thus no larger uniform exponent is possible over the displayed source class.

If a nonempty candidate set satisfies these assumptions and lies within deterministic tolerance \(\tau\) of one coefficient record, its cut diameter is at most \(\omega(2\tau)\), even when candidates occupy both root signs. The theorem supplies neither a physical tolerance nor a probability model.

## Why both margins matter

The [unrestricted bounded-source result](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-box-cut-sharpness-v1.md) has sharp exponent one-third. A [separate bounded obstruction](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-margin-only-obstruction-v1.md) retains a positive discriminant margin and nonzero \(h_3\), but lies on \(6g_2+f_2=0\); one-third remains sharp there. Discriminant separation alone therefore does not establish a full-sector half-power bound.

The [positive-radius identity](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-common-ray-modulus-v1.md) annihilates the quartic nuisance terms along each leading direction and bounds a positive quadratic form in \((p,q,h)\). Its weights depend on that direction. The [branchwise theorem](https://github.com/andrey-kokoev/marici/blob/main/research/nima/photon-branchwise-double-margin-v1.md) controls those changing weights within either shared root-sign sector. It does not alone justify comparing opposite signs.

## Opposite roots without selecting one

The measured leading Gram entries control the aligned unit-direction gap by \(4\delta/r^2\), with \(r\) the larger leading magnitude. For opposite discriminants, the uniform cubic-pair sensing map then gives a dichotomy:

- If \(r>120\sqrt\delta/\sigma\), both cubic-pair norms are at most \(10\sqrt\delta\). Hence \(|p_X^2-p_Y^2|\le200\delta\), and the augmented cut inverse gives cut gap at most \(439\delta/84\).
- Otherwise the general surrogate-bias estimate gives the square-root bound directly.

Consequently opposite-sign pairs satisfy

\[
\|C_X-C_Y\|_\infty
\le\min\left\{\frac{2713}{3360}M^2,
 \frac{439}{84}\delta+
 \frac{229}{70\sigma}M\sqrt\delta\right\}.
\]

The published branchwise constants dominate this estimate, so one modulus applies to the whole unlabelled class. The source-sign alignment in the proof leaves all quadratic data unchanged; it is not a physical root choice. The opposite-root lemma itself needs no leading-trace margin, but the same-sign cancelled-trace obstruction prevents dropping that margin from the full theorem.

## Scope

All eighteen finite local matching directions remain free. The result does not derive native dynamics, identify a physically prepared source, license its box or margins, calibrate measurement noise, select finite matching coefficients, complete the physical infrared inventory or supply ultraviolet inputs. The real spectral and norm arguments are documented mathematics with exact rational coefficient checks, not proof-assistant certification. Completion of this bounded frontier does not reopen C1–C12, renew C12's zero budget or lift the high-energy pause.

## Durable verification

The [checker](https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/check_photon_double_margin_cut_modulus_v1.py), [eight unit tests](https://github.com/andrey-kokoev/marici/blob/main/research/nima/checkers/test_photon_double_margin_cut_modulus_v1.py), [SCC manifest](https://github.com/andrey-kokoev/marici/blob/main/research/nima/scc-models/photon-double-margin-cut-modulus-v1.json) and [receipt](https://github.com/andrey-kokoev/marici/blob/main/research/nima/results/photon-double-margin-cut-modulus-v1.json) record passing scoped controls: 5,913 eligible grid points; 146 same-or-zero-sign and 58 opposite-sign comparisons; 83 zero-stratum comparisons; three explicit far-regime opposite-root controls with nonzero \(h_3\) and all quartics; and six inherited sharpness pairs. These counts are implementation controls, not a universal numerical proof. Fresh headless receipt equality, scoped SCC and unchanged net/coverage/planner checks passed; no fresh full-suite claim is made.

Reproduction:

```text
python -S research/nima/checkers/check_photon_double_margin_cut_modulus_v1.py --check
python -S -m unittest discover -s research/nima/checkers -p test_photon_double_margin_cut_modulus_v1.py
python -S research/aspect/scc/scc.py check photon-double-margin-cut-modulus-v1
```

Epistemic-graph result/report event: `ev-000000016143-32b89104-a8cb-4a5b-91e2-ebf80a6c3842`, proposal `ep_c0601eda-d9c2-4bf3-bc10-3350df1686ce`. Graph admission preserves provenance and policy review, not scientific truth certification.

Ledger allocation: sequence `marici-ledger-entry`, value 4324, claim `seqclaim-df4c225162f12b911b501c02`, obtained for the operator's requested entry. Commit, push and deployment are not authorized by this entry.
