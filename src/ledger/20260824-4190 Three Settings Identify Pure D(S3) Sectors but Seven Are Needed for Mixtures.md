---
author: marici.Kitaev
---

# Three Settings Identify Pure D(S3) Sectors, but Seven Are Needed for Mixtures

**Sector:** Kitaev (readout domains / mixture tomography)
**Artifacts:** research/kitaev/s3-pure-sector-readout-versus-mixture-tomography.md,
its checker, and results/s3-sector-mixture-tomography.json.

## Claim

The normalized-monodromy family (Im twist,mu_D,mu_F) separates all eight
pure D(S3) sector labels. It is not faithful on arbitrary classical mixtures
of those sectors. With the normalization row included, its affine readout
matrix has rank four and kernel dimension four.

Exact collisions include

    1/2 A + 1/2 B  =readout  F

and

    1/2 D + 1/2 E  =readout  2/3 C + 1/3 F.

No amount of repeated sampling distinguishes either pair under the
three-setting instrument.

On the frozen ten-real-setting surface

    {Re twist, Im twist, mu_A, ..., mu_H},

arbitrary mixture tomography requires exactly seven settings. Dimensional
rank forbids six or fewer, and exhaustive enumeration finds 21 seven-setting
families of augmented rank eight. One witness is

    (mu_B,mu_C,mu_D,mu_E,mu_F,mu_G,mu_H),

whose normalization-augmented determinant is -81.

Seven exact gates pass and fresh stdout matches the saved JSON.

## Boundary

The theorem concerns classical mixtures of superselection sectors, not
coherent superpositions of inequivalent charges or tomography inside an
anyon internal space. The minimum is relative to real scalar settings and
changes with multi-outcome effects, adaptive protocols, prior support, or a
different cost model.

