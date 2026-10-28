import assert from 'node:assert/strict';

export async function testFaceCompositor(page){
 await page.addScriptTag({type:'importmap',content:JSON.stringify({imports:{three:'/node_modules/three/build/three.module.js'}})});
 const result=await page.evaluate(async()=>{
  const T=await import('three');
  const {createFaceCompositor}=await import('/examples/normal-ray/face-compositor.js');
  const renderer=new T.WebGLRenderer({antialias:false,preserveDrawingBuffer:true});renderer.setSize(32,32);
  const compositor=createFaceCompositor(renderer);
  if(!compositor){renderer.dispose();throw Error('OIT test requires float color buffers');}
  compositor.resize();
  const camera=new T.OrthographicCamera(-1,1,1,-1,.1,20);camera.position.z=5;camera.updateMatrixWorld();
  const scene=new T.Scene();scene.background=new T.Color(0x0b1120);
  const positions=[],colors=[],layers=[{rgb:[1,0,0],a:.2,z:-1},{rgb:[0,1,0],a:.4,z:-2},{rgb:[0,0,1],a:.6,z:-3},{rgb:[1,1,0],a:.3,z:-4}];
  for(const layer of layers){positions.push(-1,-1,layer.z,1,-1,layer.z,0,1,layer.z);for(let i=0;i<3;i++)colors.push(...layer.rgb,layer.a);}
  const geometry=new T.BufferGeometry().setAttribute('position',new T.Float32BufferAttribute(positions,3)).setAttribute('color',new T.Float32BufferAttribute(colors,4));
  const material=new T.MeshBasicMaterial(),source=new T.Mesh(geometry,material);scene.add(source);
  const read=()=>{const pixel=new Uint8Array(4);renderer.getContext().readPixels(16,16,1,1,renderer.getContext().RGBA,renderer.getContext().UNSIGNED_BYTE,pixel);return [...pixel];};
  const render=order=>{geometry.setIndex(order.flatMap(i=>[3*i,3*i+1,3*i+2]));compositor.render(scene,camera,source);return read();};
  const results=[];
  for(const count of [1,2,3,4]){
   const order=Array.from({length:count},(_,i)=>i),forward=render(order),reverse=render([...order].reverse());
   const numerator=[0,0,0];let denominator=0,transmittance=1;
   for(const layer of layers.slice(0,count)){
    const z=new T.Vector3(0,0,layer.z).project(camera).z*.5+.5,w=Math.max(1,Math.min(100,1/(.01+z*z)));
    layer.rgb.forEach((x,i)=>numerator[i]+=x*layer.a*w);denominator+=layer.a*w;transmittance*=1-layer.a;
   }
   const background=scene.background.toArray();
   const expected=new T.Color().setRGB(...numerator.map((x,i)=>x/denominator*(1-transmittance)+background[i]*transmittance)).convertLinearToSRGB().toArray().map(x=>Math.round(x*255));
   results.push({count,forward,reverse,expected});
  }
  const occluder=new T.Mesh(new T.PlaneGeometry(2,2),new T.MeshBasicMaterial({color:0x22bb44}));scene.add(occluder);
  const occluded=render([0,1,2,3]);scene.remove(occluder);
  geometry.setIndex([]);compositor.render(scene,camera,source);const background=read();
  const colorAttribute=geometry.getAttribute('color');
  for(let i=0;i<colorAttribute.count;i++)colorAttribute.setW(i,1);colorAttribute.needsUpdate=true;
  material.vertexColors=true;material.side=T.DoubleSide;material.needsUpdate=true;
  const opaquePixels=[];
  for(const order of [[0,1,2,3],[3,2,1,0]]){
   geometry.setIndex(order.flatMap(i=>[3*i,3*i+1,3*i+2]));compositor.render(scene,camera,source,true);opaquePixels.push(read());
  }
  compositor.dispose();geometry.dispose();material.dispose();occluder.geometry.dispose();occluder.material.dispose();renderer.dispose();
  return {results,occluded,background,opaquePixels};
 });
 for(const {count,forward,reverse,expected} of result.results)for(let i=0;i<3;i++){
  assert(Math.abs(forward[i]-reverse[i])<=2,`${count} face layers must not depend on order`);
  assert(Math.abs(forward[i]-expected[i])<=3,`${count} layers must resolve in linear space with multiplicative transmittance`);
 }
 assert.deepEqual(result.occluded,[0x22,0xbb,0x44,255]);
 assert.deepEqual(result.background,[0x0b,0x11,0x20,255]);
 for(const pixel of result.opaquePixels)assert.deepEqual(pixel,[255,0,0,255],'At full opacity only the nearest red face is visible, in either draw order');
}
