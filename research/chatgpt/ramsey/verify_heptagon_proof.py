#!/usr/bin/env python3
"""Bind a proof-checker run to exact formula/proof digests and save its receipt."""
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import time
HERE=Path(__file__).resolve().parent

def verify(path,checker):
    path=Path(path);record=json.loads(path.read_text())
    assert record['status']=='UNSAT'
    for field,digest in [('cnf_file','cnf_sha256'),('proof_file','proof_sha256')]:
        assert sha256((HERE/record[field]).read_bytes()).hexdigest()==record[digest]
    command=[str(checker.resolve()),str(HERE/record['cnf_file']),str(HERE/record['proof_file'])]
    start=time.monotonic();run=subprocess.run(command,text=True,capture_output=True,check=True)
    assert run.stdout.startswith('VERIFIED UNSAT:')
    record['proof_independently_checked']=True
    record['independent_check']={'checker':'dratify 0.1.11 via ramsey-drat-checker 0.1.0',
        'stdout':run.stdout.strip(),'stderr':run.stderr.strip(),'exit_code':run.returncode,
        'wall_seconds':time.monotonic()-start,'checker_executable_sha256':sha256(checker.read_bytes()).hexdigest(),
        'frontend_source_sha256':sha256((HERE/'drat-checker/src/main.rs').read_bytes()).hexdigest(),
        'cargo_lock_sha256':sha256((HERE/'drat-checker/Cargo.lock').read_bytes()).hexdigest(),
        'cnf_sha256':record['cnf_sha256'],'proof_sha256':record['proof_sha256']}
    path.write_text(json.dumps(record,indent=2)+'\n');print(path.name,run.stdout.strip(),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('records',nargs='+',type=Path)
    parser.add_argument('--checker',type=Path,default=HERE/('drat-checker/target/release/ramsey-drat-checker'+('.exe' if os.name=='nt' else '')))
    args=parser.parse_args()
    for path in args.records:verify(path,args.checker)
