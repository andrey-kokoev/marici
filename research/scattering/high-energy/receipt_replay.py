"""Compare complete numerical audit receipts, without treating tolerance as proof."""
import math


def assert_receipt_matches(saved, fresh, path='$', *, rtol=1e-8, atol=1e-10):
    if isinstance(fresh, dict):
        assert isinstance(saved, dict) and saved.keys()==fresh.keys(), f'{path}: keys differ'
        for key in fresh:
            assert_receipt_matches(saved[key], fresh[key], f'{path}.{key}', rtol=rtol, atol=atol)
    elif isinstance(fresh, list):
        assert isinstance(saved, list) and len(saved)==len(fresh), f'{path}: list differs'
        for i,(a,b) in enumerate(zip(saved,fresh)):
            assert_receipt_matches(a,b,f'{path}[{i}]',rtol=rtol,atol=atol)
    elif isinstance(fresh, float):
        assert isinstance(saved,(int,float)) and not isinstance(saved,bool), f'{path}: type differs'
        assert math.isfinite(saved) and math.isfinite(fresh), f'{path}: nonfinite'
        assert math.isclose(saved,fresh,rel_tol=rtol,abs_tol=atol), f'{path}: {saved} != {fresh}'
    else:
        assert type(saved) is type(fresh) and saved==fresh, f'{path}: value differs'
