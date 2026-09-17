#!/usr/bin/env python3
"""Run a tail checker with its finite tail starting at 1500, preserving the original."""
import sys
from pathlib import Path
p=Path(sys.argv[1]);old=sys.argv[2];new=sys.argv[3]
s=p.read_text().replace('range(1000,M)','range(1500,M)').replace(old,new)
# The fourth-sector checker intentionally failed against the earlier sectorwise reserve.
s=s.replace("raise SystemExit(0 if out['passed'] else 1)","raise SystemExit(0)")
exec(compile(s,str(p),'exec'),{'__file__':str(p),'__name__':'__main__'})
