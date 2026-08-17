---
id: 428
date: 2026-08-17
title: The Connector Six Operations Preserve the Kato Sector
---

# The Connector Six Operations Preserve the Kato Sector

Entry 427 separated the finite connector category from the full equivariant
coefficient category of its Artin-cone realization. For the operations actually
used by the connector, the Kato-pulled sector is closed.

There are two reasons. First, each of the 522 incidence maps is a strict face
localization
\[
P\longrightarrow P[u_a^{-1}].
\]
Restriction of a zero inertia character remains zero. Extension by zero has
the same zero character on the open face and the zero object elsewhere.
Consequently restriction, extension by zero, support cones, tensor products,
internal Homs, and duals preserve the Kato sector.

Second, the normalized blowdown of Entry 423 was deliberately given the
pulled-back structure sheaf. At every expanded source cell its monoid chart is
literally the chart of its old-face image. The induced map on chart tori is the
identity. Its fibers are singletons except for the finite contractible V-tree,
so left and right Kan extension use only finite sums, products, and the
integral V-tree differential. None can generate an inertia character from
zero-character inputs. Thus
\[
L\pi_!,\quad R\pi_*,\quad \pi^*,\quad \pi^!
\]
all remain in the Kato-pulled sector for the marked coefficient packet.

The relative dualizing object also has zero torus character. Its sign under
reflection, computed in Entry 424, belongs to the discrete permutation of the
two exceptional endpoints; it is not a character of a chart torus. Therefore
the primitive Thom trace is a morphism inside the same sector. Rotation and
the Čech assembly preserve this conclusion because their transition maps are
again strict face maps.

Hence the complete finite six-operation connector of Entries 422–424
algebraizes on the fs/Kato diagram of Entry 426 and embeds into the Artin-cone
presentation through its Kato-pulled sector.

This is intentionally not a claim that arbitrary pushforwards in the full
equivariant or quasi-coherent category preserve trivial inertia. Such functors
may retain stabilizer representations or character twists. The result applies
to the explicit strict face maps, finite normalized blowdown, and dualizing
packet used here.

The remaining comparison is generic: after localizing \(X_a\), verify that the
Kato-sector Thom trace becomes the raw DNC generic trace with the same
primitive sign and no additional unit.

The executable audit is
`research/voevodsky/check_kato_sector_six_operations.py`.
