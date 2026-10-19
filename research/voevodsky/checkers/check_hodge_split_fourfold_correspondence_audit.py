"""Retained theorem integrity and applicability; not verification of the cited proof."""
from hashlib import sha256
from pathlib import Path
import json


def main():
    root=Path(__file__).resolve().parents[3]
    snapshot=json.loads((root/'research/voevodsky/inputs/hodge-literature-v1/sources.json').read_text(encoding='utf-8'))
    expected={
        'markman-2502.03415v2':('8155aa33870069b8381efe9a53adf091ce28a6a518311d768e0248abb2e675ba',9,'e0bc1f549139470cef0637aca9bb59909e84d9d790257e55f675ee5931aa8963'),
        'markman-2509.23403v2':('3151aee3307548da8f89b7b8d396db6e6c6fb6753cf76d152ad4b52b944252f5',3,'b742dd7512d96573035aafe2d70b8060f2e9fc5d05dd414e9aeb233bfdbb20ca')}
    texts={}
    for sid,(pdfhash,page,pagehash) in expected.items():
        source=next(s for s in snapshot['sources'] if s['id']==sid)
        assert source['sha256']==pdfhash
        pdf=(root/source['pdf']).read_bytes()
        assert pdf.startswith(b'%PDF-') and sha256(pdf).hexdigest()==pdfhash
        entry=next(p for p in source['pages'] if p['pdf_page']==page)
        data=(root/entry['path']).read_bytes()
        assert entry['sha256']==pagehash and sha256(data).hexdigest()==pagehash
        texts[sid]=' '.join(data.decode('utf-8-sig').split())
    primary=texts['markman-2502.03415v2']
    assert 'Corollary 1.6.1. The Hodge conjecture holds for abelian fourfolds.' in primary
    assert 'for every abelian fourfold of Weil-type' in primary
    assert 'for all imaginary quadratic number fields, and for all discriminants' in primary
    assert 'simple abelian 3-fold and E is an elliptic curve' in primary
    survey=texts['markman-2509.23403v2']
    assert 'Theorem 1.2.' in survey and 'The Weil classes for abelian fourfolds of Weil type' in survey
    assert 'abelian sixfolds of split Weil type' in survey
    control=json.loads((root/'research/voevodsky/results/hodge-joint-odd-sector-correspondence-v1.json').read_text(encoding='utf-8'))
    assert control['passed'] and control['correspondence_codimension']==2
    assert control['ambient_Weil_signature']==[2,2] and control['Hermitian_determinant']==1
    assert control['elliptic_K_embedding']=='conjugate' and control['explicit_split_plane_checked']
    # The older receipt honestly describes what that earlier turn constructed.
    assert control['algebraic_correspondence_constructed'] is False
    result={'passed':True,'classification':'imported_fourfold_theorem_applies_to_control_correspondence',
        'verified_pdf_count':2,'verified_extracted_page_count':2,
        'primary_result':'Markman arXiv:2502.03415v2 Corollary1.6.1, PDF9',
        'decomposable_control_covered':True,'both_Weil_components_covered':True,
        'gamma_algebraic_by_imported_theorem':True,'explicit_cycle_equations_constructed':False,
        'cited_proof_independently_verified':False,'new_network_literature_refresh':False,
        'original_nonsplit_sixfold_covered':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Pull back the algebraic correspondence and multiply inactive divisors to realize the joint-control K1,K2 classes.'}
    (root/'research/voevodsky/results/hodge-split-fourfold-correspondence-audit-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
