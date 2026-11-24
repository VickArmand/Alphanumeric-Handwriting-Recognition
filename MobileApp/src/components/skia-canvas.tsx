import { AlphaType, Canvas, ColorType, useCanvasRef } from "react-native-skia";
    
const ref = useCanvasRef();

const getPixelData = () => {
    const image = ref.current?.makeImageSnapshot();
    if (!image) return;
    const width = image.width();
    const height = image.height();
    const pixels = image.readPixels(0, 0, 
        { width, height, colorType: ColorType.RGBA_8888, alphaType: AlphaType.Unpremul}
    )
    console.log(pixels)
    return pixels
}

export default function SkiaCanvas() {

    return (
        <Canvas ref={ref}>

        </Canvas>
    );
}