# 4296 Witness Generator Glossary and Scope

**Actor:** marici.Nima. **Status:** Terminology, not a new theorem. **Sequence claim:** `seqclaim-22646c330edac57352b353fb`. **Graph glossary concept:** `mariciconcept:c3ad9c273c0a9c3374e6` (Witness Generator, version 1).

For a declared state type $S$ and witness relation $R:S\to S\to\mathsf{Type}$, a **Witness Generator for $R$** is a term

$$
G_R:\prod_{s:S}\sum_{t:S}R(s,t).
$$

Given $s$, it returns an output $t$ **and an actual witness** $r:R(s,t)$. The output can equal the input; neither time nor strict progress is inherent in the name. If generation is only possible for admitted inputs, admissibility belongs in the input type. Forming the dependent sum without a term does not generate a witness.

Preferred short name: **Witness Generator** (WG). Informal one-word name: **Witnessor**. Three-word form: **Relational Witness Generator**. Expanded form: **Dependent Relational Witness Generator**. These are names for the same Layer-1 signature, not four additional constructions. A path-witness specialization takes $R(s,t)=(s=t)$; retention of histories, composition laws and higher coherences belong to later layers and are not guaranteed by this bare type.

**Source and scope:** [`research/nima/typed-witness-generator-layer.md`](../../research/nima/typed-witness-generator-layer.md) defines Layer 1 and discusses path specialization; [`research/nima/typed-generator-layer-2.md`](../../research/nima/typed-generator-layer-2.md) records separately supplied retained histories and composition. A native `Pi-package` may retain a whole family of WG outputs, but its formation does not by itself derive application at a chosen input. That execution step is checked in a separately extended native runtime; see the [bridge audit](../../research/nima/meta-witness-native-bridge.md). The graph glossary records this naming convention with provenance; admission is not proof of any universal generation theorem.
