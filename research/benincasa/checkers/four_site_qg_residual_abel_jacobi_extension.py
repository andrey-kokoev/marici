"""Type the residual odd classes against their three elliptic pair faces."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
COH = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"
PAIRS = ROOT / "research/benincasa/results/four-site-qg-pair-curve-types.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-residual-abel-jacobi-extension.json"

coh = json.loads(COH.read_text())
pairs = json.loads(PAIRS.read_text())
pair_terms = {x["term_index"]: x for x in pairs["term_packets"]}
packets = []

for term in coh["term_packets"]:
    if term["deck_minus"]["H2"] != 1:
        continue
    index = term["term_index"]
    rep = term["deck_minus"]["representatives"][0]
    assert len(rep) == 1 and rep[0]["coefficient"] == 1
    triple = [tuple(group) for group in rep[0]["triple"]]
    pair_lookup = {
        frozenset(tuple(group) for group in row["marks"]): row
        for row in pair_terms[index]["pairs"]
    }
    faces = []
    for omitted, sign in zip(range(3), (1, -1, 1)):
        face = [triple[i] for i in range(3) if i != omitted]
        row = pair_lookup[frozenset(face)]
        is_elliptic = row["curve_type"] == "smooth elliptic double cover"
        if is_elliptic:
            assert row["shared_node_count"] == 0
            section = "off branch: p_plus != p_minus"
            extension = "cech_sign * AJ([p_plus]-[p_minus])"
        else:
            assert row["curve_type"].startswith("split rational")
            section = "global split deck components"
            extension = "exact H0_minus pair boundary"
        faces.append({
            "marks": [list(group) for group in face],
            "cech_sign": sign,
            "curve_type": row["curve_type"],
            "triple_section": section,
            "extension_class": extension,
            "generic_nonzero": is_elliptic,
        })
    elliptic = [face for face in faces if face["generic_nonzero"]]
    split = [face for face in faces if not face["generic_nonzero"]]
    assert len(elliptic) == 2 and len(split) == 1
    packets.append({"term_index": index, "triple": [list(x) for x in triple],
                    "oriented_faces": faces, "elliptic_faces": 2,
                    "split_exact_faces": 1, "nonzero_components": 2})

assert len(packets) == 8
packet = {
    "schema": "marici.benincasa.four_site_qg_residual_abel_jacobi_extension.v1",
    "residual_terms": len(packets),
    "components_per_term": 2,
    "orientation": "standard alternating deletion signs (+,-,+)",
    "nonvanishing_argument": "For a smooth genus-one curve, the Abel map C -> Pic^1(C) is injective. Hence [p_plus]-[p_minus] is zero in Pic^0 only if p_plus=p_minus; every retained triple is off the branch.",
    "conclusion": "The residual Gram-Kummer associated grade has two generically nonzero Abel-Jacobi extension components into its incident elliptic H1 systems; its third face is an exact split-pair H0 boundary. A canonical split coefficient module is falsified.",
    "term_packets": packets,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"terms": len(packets), "components": 2 * len(packets),
                  "all_generically_nonzero": True}))
