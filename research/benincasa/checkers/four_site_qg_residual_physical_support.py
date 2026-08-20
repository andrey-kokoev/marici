"""Audit residual four-site supports against the literal positive OFPT chain."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-full-cech-h2.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-residual-physical-support.json"


def denominator(label):
    if label.startswith("G_minus_e"):
        edge = int(re.findall(r"\d", label)[0]) - 1
        y = [0, 0, 0, 0]
        y[edge] = 2
        return {"label": label, "site_coefficients": [1, 1, 1, 1],
                "edge_coefficients": y, "kind": "full graph with one opened edge"}
    sites = {int(x) - 1 for x in re.findall(r"\d", label)}
    assert sites
    x = [1 if i in sites else 0 for i in range(4)]
    y = [0, 0, 0, 0]
    for edge in range(4):
        if (edge in sites) != ((edge + 1) % 4 in sites):
            y[edge] = 1
    return {"label": label, "site_coefficients": x,
            "edge_coefficients": y, "kind": "connected partial energy"}


source = json.loads(SOURCE.read_text())
records = []
for term in source["term_packets"]:
    if term["deck_minus"]["H2"] != 1:
        continue
    rep = term["deck_minus"]["representatives"][0]
    assert len(rep) == 1
    groups = rep[0]["triple"]
    # Coincident labels denote the same geometric denominator wall; retain
    # every source occurrence in the packet but choose the first for evaluation.
    forms = [denominator(group[0]) for group in groups]
    full = [form for form in forms if form["kind"].startswith("full graph")]
    assert len(full) == 1
    assert full[0]["site_coefficients"] == [1, 1, 1, 1]
    assert all(c >= 0 for form in forms
               for c in form["site_coefficients"] + form["edge_coefficients"])
    records.append({
        "term_index": term["term_index"],
        "triple_occurrence_groups": groups,
        "denominator_forms": forms,
        "physical_interior_intersection": False,
        "closure_implication": "q_(G\\e)=0 with X_i,y_e>=0 forces X1=X2=X3=X4=0 and the labelled opened edge y_e=0",
    })

assert len(records) == 8
packet = {
    "schema": "marici.benincasa.four_site_qg_residual_physical_support.v1",
    "records": records,
    "literal_positive_chain_pairing": "zero before analytic continuation",
    "closure_support": "existing all-site-soft plus labelled edge-soft support",
    "qualification": "This does not define an analytically continued weighted relative cycle or select a boundary value on the deep soft closure.",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"terms": len(records), "interior_hits": 0,
                  "closure": packet["closure_support"]}))
