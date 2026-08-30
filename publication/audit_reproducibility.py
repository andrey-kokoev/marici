#!/usr/bin/env python3
"""Audit RH theorem dependencies, evidence receipts, source hygiene, and builds."""
import hashlib, json, shutil, subprocess, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/"publication/rh-proof-ledger.json"

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def build_tex(source):
    engine=shutil.which("pdflatex")
    if not engine: return {"status":"blocked","reason":"pdflatex_not_available"}
    with tempfile.TemporaryDirectory(prefix="marici-rh-build-") as tmp:
        proc=subprocess.run([engine,"-interaction=nonstopmode","-halt-on-error","-output-directory",tmp,str(source)],
                            cwd=source.parent,capture_output=True,text=True,timeout=120)
        pdf=Path(tmp)/(source.stem+".pdf")
        return {"status":"passed" if proc.returncode==0 and pdf.is_file() else "failed",
                "exit_code":proc.returncode,"pdf_sha256":sha(pdf) if pdf.is_file() else None,
                "stderr_tail":proc.stderr[-1000:]}

def main():
    data=json.loads(LEDGER.read_text(encoding="utf-8")); gates={x["id"] for x in data["gates"]}; results={x["id"] for x in data["established_results"]}
    known=gates|results; claims=data.get("theorem_claims",[])
    claim_checks={x["id"]:{"dependencies_present":bool(x.get("dependencies")),
                            "dependencies_resolve":set(x.get("dependencies",[])).issubset(known)} for x in claims}
    receipts={}
    for item in data["established_results"]+data["withdrawn_claims"]:
        path=ROOT/item["evidence"]; actual=sha(path) if path.is_file() else None
        receipts[item["id"]]={"exists":path.is_file(),"expected_sha256":item.get("evidence_sha256"),
                              "actual_sha256":actual,"matches":actual==item.get("evidence_sha256")}
    manuscripts={k:ROOT/v for k,v in data["package_shape"].items()}
    hygiene={}
    forbidden=["\\write18","\\includegraphics{http","C:\\\\","/home/"]
    for name,path in manuscripts.items():
        text=path.read_text(encoding="utf-8") if path.is_file() else ""
        hygiene[name]={"exists":path.is_file(),"forbidden_tokens": [x for x in forbidden if x in text],
                       "internal_draft_marker":"not for submission" in text.lower()}
    builds={name:build_tex(path) for name,path in manuscripts.items() if path.is_file()}
    checks={"all_claims_mapped":bool(claims) and all(all(v.values()) for v in claim_checks.values()),
            "all_evidence_receipts_match":all(x["matches"] for x in receipts.values()),
            "source_hygiene":all(x["exists"] and not x["forbidden_tokens"] and x["internal_draft_marker"] for x in hygiene.values()),
            "both_packages_build":len(builds)==2 and all(x["status"]=="passed" for x in builds.values()),
            "maximal_domain_not_claimed":all("maximal-domain equivalence" not in p.read_text(encoding="utf-8").lower() for p in manuscripts.values())}
    out={"schema":"marici.rh-reproducibility-audit.v1","passed":all(checks.values()),"g6_ready":all(checks.values()),
         "checks":checks,"claim_checks":claim_checks,"evidence_receipts":receipts,"source_hygiene":hygiene,"builds":builds}
    result=ROOT/"publication/rh-reproducibility-audit.json"; result.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2)); return 0 if out["passed"] else 1
if __name__=="__main__": raise SystemExit(main())
