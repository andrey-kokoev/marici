# Owning tail compatibility has a two-coordinate marked-cut presentation

## Independently specified source

Use the owning three-bin rational moment relaxation from Grothendieck's ternary budget result: bin masses xi with 0<=xi<=ci, cumulative prefix bounds sum_(j<=i) xj<=Bi, and fixed scalar lower-functional coefficients li. The owning independent verifier passes freshly. This carrier is not the exact set of prime-realizable masses.

Freeze a two-scalar boundary representation before testing: zi=(si,ti), with z0=(0,0). Define indexed witnessed relations

    Ri(zi-1,zi;xi):
       0<=xi<=ci,
       si=si-1+xi,
       ti=ti-1+li*xi,
       si<=Bi.

These are compatibility equations between boundary values and a bin-mass witness. Their interpretation requires no privileged query direction.

## Exact continuum equivalence

Every admitted source triple supplies unique boundaries by cumulative sums. Conversely, a joined witnessed chain reconstructs xi=si-si-1 and satisfies exactly the source inequalities. The endpoint value is t3=sum li xi. Thus source triples and joined marked developments are in witness-preserving bijection.

Exact affine coefficient identities certify the cumulative and objective equations for all real inputs. The test also checks 126 rational candidate triples, including boundary points and the original pairwise-admitted globally impossible candidate; 22 pass source admission. The grid is a regression check, not the continuum proof.

For the original obstruction, the first two segments admit the assigned masses. The third segment rejects their combined total. Each coordinate-pair zero extension still passes the full source constraints, confirming that the missing obligation is precisely the cross-cut total budget.

## Composition and orientation

Regrouping adjacent segments changes the order of conjunction and existential elimination of shared boundary coordinates, retaining the same bin witnesses. Telescoping identities are checked for all cut triples. Logical reversal transposes each relation and reverses its order. It preserves the same equations and source witness tuples; it does not use the forward inequality rule with an untransformed reversed index.

Marked boundaries retain the objective offsets and cumulative constraints. Eliminating an interior boundary yields its exact endpoint relation while retaining or existentially quantifying the corresponding source witnesses according to the query. No independent witness is reselected at a join.

## DPC disposition

The compact coherent cut-presentation conjecture is corroborated on this owning analytical relaxation. Two scalar coordinates per cut suffice; their values are continuous, so this is a finite-dimensional representation rather than a finite-state one. Neither minimality nor a general bound for arbitrary higher-order constraints is established.

Together with the coupled protocol's finite residual construction, this identifies the same structure in two representation classes: source-compatible witnesses joined through sufficient boundary values. One uses finitely many behavioral states; the other uses two exact scalar coordinates. Both preserve the independently specified compatibility and observable distinctions under regrouping and logical reversal.

## Reproduction

    uv run --with python-flint python research/voevodsky/checkers/check_analytic_cut_compatibility.py

Artifacts:

- `results/analytic-cut-compatibility-contract.json`
- `results/analytic-cut-compatibility.json`
