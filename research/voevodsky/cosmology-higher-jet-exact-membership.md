# Exact higher-jet membership through degree six

## Result

All 90,576 bounded order-three through order-six seed derivatives are exact in the unchanged A12 rational source image.

| order | targets | raw zeros | nonzero exact words |
|---:|---:|---:|---:|
| 3 | 12,240 | 9,600 | 2,640 |
| 4 | 18,360 | 14,400 | 3,960 |
| 5 | 25,704 | 20,992 | 4,712 |
| 6 | 34,272 | 28,072 | 6,200 |

In total, 73,064 targets vanish as raw rows and 17,512 have exact rational words. Each nonzero target was reconstructed from four-prime CRT integer rows and replayed with zero residual. Words use at most 12 source rows; the largest absolute numerator is 47,410,973 and largest denominator is 4,870,886,400.

## Claim boundary

This is exact membership of raw higher derivatives in the unchanged A12 image. It supplies no higher-jet extension, coherent primitive selector, admissibility rule, or connecting morphism. All-even transport remains to be checked.

## Verification

- `research/voevodsky/check_cosmology_higher_jet_exact_membership.py`
- `research/voevodsky/results/cosmology_higher_jet_exact_membership.json` — passed
- `research/voevodsky/results/cosmology_higher_jet_exact_certificate_words.json` — 17,512 nonzero exact words
