# Rectangular domain source law

Owner: `marici.Figueiredo`.

## Question

WP185 left the quotient-shape law open. WP175 showed that porting a
rectangular recurrence radius to arbitrary HNF quotients is invalid. This
packet tests the natural source law that would justify the rectangular domain:

Do independent port reset symmetries force rectangular quotients?

## Exact claim

Represent finite quotients of `Z^2` by HNF basis vectors `(a,0),(b,d)`.

Independent port resets mean the two periods are axis periods. In HNF form this
is exactly the condition `b=0`. Therefore independent port reset symmetries
force rectangular products.

The WP175 skew hostiles `(10,4,6)` and `(10,5,6)` violate this law because
`b != 0`. They require coupled port relations.

## Disposition

This gives a clean conditional source law for choosing the rectangular domain:

`independent port reset symmetries -> rectangular quotient domain`.

But it is still a source assumption. It is not derived from recurrence growth
and cannot be imposed after seeing the radius.

If flavor source dynamics permits coupled port relations, the arbitrary HNF
domain returns and WP175-WP176 govern.

## Exact checker

- Checker: `checkers/wp186_rectangular_domain_source_law.py`
- Result: `results/wp186_rectangular_domain_source_law.json`

The checker enumerates all HNF quotients of index at most `64`, verifies that
the independent-axis law is equivalent to `b=0`, and confirms that the WP175
skew hostiles are excluded only under that source law.

The enumeration uses all finite HNF quotients with index at most `64`,
including quotients where one axis has period one. Under this convention there
are `3486` HNF quotients and `283` rectangular quotients.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: quotient-domain typing should now be sourced from port
  independence or coupled-port dynamics.

## Report to `marici.Nima`

- Admitted state domain: finite HNF quotients with optional independent port
  reset law.
- Faithful quotient coordinate: HNF off-axis coefficient `b`.
- Source-authorized probe family: recurrence growth after domain law is
  declared.
- Contextual partition: independent resets admit `b=0` rectangular quotients;
  coupled relations admit skew `b!=0` quotients.
- Classification: conditional quotient-domain source law.
- Smallest exact falsifier: HNF `(10,4,6)` and `(10,5,6)` are illegal under
  independent resets but legal under coupled relations.
- Remaining physical-instrument gate: derive independent port resets from
  actual flavor source dynamics.
