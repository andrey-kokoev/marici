import * as T from 'three';

// Weighted blended order-independent transparency. Accumulate premultiplied
// color/weight and transmittance separately; resolve once in linear color space.
// This approximates layer colors, but does not depend on triangle draw order.
export function createFaceCompositor(renderer){
  if(!renderer.extensions.has('EXT_color_buffer_float'))return null;
  const size=new T.Vector2();
  const base=new T.WebGLRenderTarget(1,1,{type:T.HalfFloatType,depthBuffer:true});
  base.depthTexture=new T.DepthTexture(1,1,T.UnsignedIntType);
  const accumulation=new T.WebGLRenderTarget(1,1,{type:T.HalfFloatType,depthBuffer:false,minFilter:T.NearestFilter,magFilter:T.NearestFilter});
  const revealage=new T.WebGLRenderTarget(1,1,{depthBuffer:false,minFilter:T.NearestFilter,magFilter:T.NearestFilter});
  const uniforms={opaqueDepth:{value:base.depthTexture},resolution:{value:size}};
  const vertexShader=`attribute vec4 color;
    varying vec4 faceColor;
    void main(){faceColor=color;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`;
  const fragmentHeader=`uniform sampler2D opaqueDepth;
    uniform vec2 resolution;
    varying vec4 faceColor;
    void main(){
      if(gl_FragCoord.z>texture2D(opaqueDepth,gl_FragCoord.xy/resolution).r+0.000001)discard;
      float a=clamp(faceColor.a,0.0,1.0);`;
  const common={uniforms,vertexShader,transparent:true,depthTest:false,depthWrite:false,side:T.DoubleSide,forceSinglePass:true,blending:T.CustomBlending,blendEquation:T.AddEquation,toneMapped:false};
  const accumulateMaterial=new T.ShaderMaterial({...common,blendSrc:T.OneFactor,blendDst:T.OneFactor,
    fragmentShader:fragmentHeader+`float w=clamp(1.0/(0.01+gl_FragCoord.z*gl_FragCoord.z),1.0,100.0);
      gl_FragColor=vec4(faceColor.rgb*a*w,a*w);}`});
  const revealMaterial=new T.ShaderMaterial({...common,blendSrc:T.ZeroFactor,blendDst:T.OneMinusSrcAlphaFactor,
    fragmentShader:fragmentHeader+'gl_FragColor=vec4(0.0,0.0,0.0,a);}'});
  const faceScene=new T.Scene(),faceMesh=new T.Mesh(undefined,accumulateMaterial);faceMesh.frustumCulled=false;faceScene.add(faceMesh);
  // The temporary default geometry is not used; the source owns face geometry.
  faceMesh.geometry.dispose();
  const resolveMaterial=new T.ShaderMaterial({depthTest:false,depthWrite:false,
    uniforms:{baseColor:{value:base.texture},accumulation:{value:accumulation.texture},revealage:{value:revealage.texture}},
    vertexShader:'varying vec2 uvOut;void main(){uvOut=uv;gl_Position=vec4(position.xy,0.0,1.0);}',
    fragmentShader:`uniform sampler2D baseColor,accumulation,revealage;varying vec2 uvOut;
      void main(){
        vec4 accum=texture2D(accumulation,uvOut);
        float transmittance=texture2D(revealage,uvOut).r;
        vec3 color=accum.rgb/max(accum.a,0.00001);
        gl_FragColor=vec4(color*(1.0-transmittance)+texture2D(baseColor,uvOut).rgb*transmittance,1.0);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`});
  const resolveScene=new T.Scene(),quad=new T.Mesh(new T.PlaneGeometry(2,2),resolveMaterial),quadCamera=new T.Camera();
  quad.frustumCulled=false;resolveScene.add(quad);
  return {
    resize(){renderer.getDrawingBufferSize(size);for(const target of [base,accumulation,revealage])target.setSize(size.x,size.y);},
    render(scene,camera,source,opaque=false){
      // Weighted blending is not valid for opaque surfaces: their nearest
      // depth must win, rather than averaging all contributing colors.
      if(opaque){
        const transparent=source.material.transparent,depthWrite=source.material.depthWrite;
        source.material.transparent=false;source.material.depthWrite=true;
        try{renderer.render(scene,camera);}finally{source.material.transparent=transparent;source.material.depthWrite=depthWrite;}
        return;
      }
      const autoClear=renderer.autoClear,background=scene.background,mask=camera.layers.mask,visible=source.visible;
      const clearColor=renderer.getClearColor(new T.Color()),clearAlpha=renderer.getClearAlpha();
      renderer.autoClear=false;
      try{
        camera.layers.set(0);source.visible=false;
        renderer.setRenderTarget(base);renderer.clear(true,true,true);renderer.render(scene,camera);
        faceMesh.geometry=source.geometry;
        faceMesh.material=accumulateMaterial;
        renderer.setRenderTarget(accumulation);renderer.setClearColor(0x000000,0);renderer.clear(true,false,false);renderer.render(faceScene,camera);
        faceMesh.material=revealMaterial;
        renderer.setRenderTarget(revealage);renderer.setClearColor(0xffffff,1);renderer.clear(true,false,false);renderer.render(faceScene,camera);
        renderer.setRenderTarget(null);renderer.render(resolveScene,quadCamera);
        // Labels remain on top, rather than being tinted by the face resolve.
        scene.background=null;camera.layers.set(1);renderer.render(scene,camera);
      }finally{
        source.visible=visible;scene.background=background;camera.layers.mask=mask;
        renderer.setRenderTarget(null);renderer.setClearColor(clearColor,clearAlpha);renderer.autoClear=autoClear;
      }
    },
    dispose(){for(const target of [base,accumulation,revealage])target.dispose();accumulateMaterial.dispose();revealMaterial.dispose();resolveMaterial.dispose();quad.geometry.dispose();},
  };
}
