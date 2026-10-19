"""Preserve/verify/restore source replay assets; never overwrite differing live files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import zipfile
from high_energy_scattering_net import ROOT,HOME,digest

ARCHIVE=HOME/'results/scattering-replay-cache.v1.zip'
MANIFEST=HOME/'results/scattering-replay-cache.v1.json'
BASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
SHORT=ROOT/'.ai/tmp/scattering-response128/relativistic_entrance.py'


def disk(path):
    return Path(chr(92)*2+'?'+chr(92)+str(path.resolve())) if os.name=='nt' else path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['preserve','check','restore']);a=p.parse_args()
    if a.action=='preserve':
        assert not ARCHIVE.exists(),'existing archive must not be silently replaced'
        files=sorted(p for p in BASE.rglob('*') if p.is_file() and '__pycache__' not in p.parts)+[SHORT]
        records={}
        with zipfile.ZipFile(ARCHIVE,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
            for path in files:
                name=path.relative_to(ROOT).as_posix()
                z.write(disk(path),name)
                records[name]=digest(disk(path))
        MANIFEST.write_text(json.dumps({'schema':'marici.scattering.replay-cache.v1','archive_sha256':digest(ARCHIVE),'files':records},indent=2)+'\n')
    manifest=json.loads(MANIFEST.read_text())
    assert digest(ARCHIVE)==manifest['archive_sha256'],'archive hash mismatch'
    with zipfile.ZipFile(ARCHIVE) as z:
        assert set(z.namelist())==set(manifest['files']),'archive inventory mismatch'
        for name,expected in manifest['files'].items():
            rel=Path(name)
            assert not rel.is_absolute() and '..' not in rel.parts and name.startswith('.ai/tmp/scattering-')
            h=hashlib.sha256()
            with z.open(name) as f:
                for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
            assert h.hexdigest()==expected,'member hash mismatch: '+name
            if a.action=='restore':
                target=disk(ROOT/rel)
                # engine_path is machine-specific; it is normalized below.
                if name.endswith('/engine_path.txt'):continue
                if target.exists():assert digest(target)==expected,'refuse to overwrite: '+name
                else:
                    target.parent.mkdir(parents=True,exist_ok=True)
                    with z.open(name) as source,target.open('wb') as out:
                        import shutil
                        shutil.copyfileobj(source,out)
    if a.action=='restore':
        disk(BASE/'engine_path.txt').write_text(str(disk(BASE/'cache/source_work/engine')),encoding='utf-8')
    print(json.dumps({'status':'pass','action':a.action,'preserved_files':len(manifest['files']),'archive':str(ARCHIVE.relative_to(ROOT))}))


if __name__=='__main__':main()
