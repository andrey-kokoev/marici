// Test a two-triangle boundary witness as an alternative representation of E.
// No tetrahedral E occupancy is assumed by the proposed representation; the
// saved tetrahedra provide reference data against which information loss is tested.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(input),samples=JSON.parse(bytes).rows;
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),sub=(a,b)=>a.map((x,i)=>x-b[i]),sq=(a,b)=>dot(sub(a,b),sub(a,b)),rows=[];
for(const sample of samples){
 const aliases=sample.bodies.find(b=>b.species==='electron').aliases,point=n=>aliases[n].split(',').map(Number),[a,b,c,d]=['C1','M1','C2','M2'].map(point),ab=sub(b,a),L2=dot(ab,ab),ac=sub(c,a),ad=sub(d,a),tc=dot(ac,ab)/L2,td=dot(ad,ab)/L2,vc=ac.map((x,i)=>x-tc*ab[i]),vd=ad.map((x,i)=>x-td*ab[i]),hc2=dot(vc,vc),hd2=dot(vd,vd),cos=dot(vc,vd)/Math.sqrt(hc2*hd2);
 assert.ok(hc2>0&&hd2>0&&Math.abs(cos)<1-1e-9);
 const reconstructed=(tc-td)**2*L2+hc2+hd2-2*Math.sqrt(hc2*hd2)*cos;assert.ok(Math.abs(reconstructed-sq(c,d))<1e-9);
 // Intrinsic unfolded disk: first apex above hinge, second below.
 const flat={C1:[0,0],M1:[Math.sqrt(L2),0],C2:[tc*Math.sqrt(L2),Math.sqrt(hc2)],M2:[td*Math.sqrt(L2),-Math.sqrt(hd2)]};
 const boundary=['C1','C2','M1','M2'],sides=boundary.map((n,i)=>sq(flat[n],flat[boundary[(i+1)%4]])),diagonals=[sq(flat.C1,flat.M1),sq(flat.C2,flat.M2)],square=sides.every(x=>Math.abs(x-sides[0])<1e-9)&&Math.abs(diagonals[0]-diagonals[1])<1e-9;
 rows.push({marking:sample.marking,referenceElectronGeometry:sample.electronGeometry,hydrogen1Attachment:['C1','M1'],hydrogen2Attachment:['M1','C1','C2'],proposedMembraneFaces:[['C1','M1','C2'],['C1','M1','M2']],flatCoordinates:flat,boundarySquaredLengths:sides,diagonalSquaredLengths:diagonals,intrinsicSquare:square,hingeCosine:cos,missingOppositeEdgeSquared:sq(c,d),hingeReconstructsMissingEdge:true});
}
// Same two equilateral triangles, same five intrinsic lengths. Different
// hinge angles give different fillings: the flat witness does not fix a volume.
const h=Math.sqrt(3)/2,examples=[0,Math.PI/3,Math.acos(1/3),Math.PI/2,Math.PI].map(angle=>({angle,hingeCosine:Math.cos(angle),boundarySideLengths:[1,1,1,1],hingeLength:1,oppositeEdgeLength:Math.sqrt(2*h*h*(1-Math.cos(angle))),enclosedTetrahedronVolume:h*h*Math.abs(Math.sin(angle))/6}));
assert.ok(examples[2].enclosedTetrahedronVolume>0);assert.equal(examples[0].enclosedTetrahedronVolume,0);assert.ok(Math.abs(examples[2].oppositeEdgeLength-1)<1e-10);
const out='research/strominger/results/e-boundary-geometry';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'boundary-witness-information-tested',source:input,sourceSha256:createHash('sha256').update(bytes).digest('hex'),rows,intrinsicSquares:rows.filter(r=>r.intrinsicSquare).length,hingedEquilateralExamples:examples,scope:'Alternative E representation as a two-face disk plus optional signed hinge and reader data. Tests intrinsic geometry and reconstruction information against all saved H1/H2 endpoint configurations. No new E particle occupancy/transfer rule or dimension-changing eversion admitted.'},null,2)+'\n');console.log(JSON.stringify({markings:rows.length,intrinsicSquares:rows.filter(r=>r.intrinsicSquare).length,hingeCosines:[...new Set(rows.map(r=>r.hingeCosine.toFixed(8)))],examples},null,2));
