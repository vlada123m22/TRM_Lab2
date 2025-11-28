# Interactive AR Narrative Experience

An augmented reality experience built with AR.js featuring a multi-chapter narrative with interactive elements.

## Features

- **Sequential Storytelling**: 3 chapters that unlock progressively
- **Interactive Elements**: Clickable objects that respond to user interaction
- **Dynamic UI**: Real-time progress tracking and narrative text
- **Artistic Design**: Custom 3D elements with animations and effects

## Setup Instructions

### 1. Create NFT Markers

1. Visit [NFT Marker Creator](https://carnaux.github.io/NFT-Marker-Creator/#/)
2. Upload 3 distinctive images (high contrast works best):
   - marker1: Starting point image
   - marker2: Mid-journey image
   - marker3: Final destination image
3. Download the generated files (.fset, .fset3, .iset)
4. Place them in the `markers/` folder with names:
   - `markers/marker1.*`
   - `markers/marker2.*`
   - `markers/marker3.*`

### 2. Deploy to Render.com

1. Push your code to GitHub
2. Go to [Render.com](https://render.com/)
3. Create a new "Static Site"
4. Connect your GitHub repository
5. Configure:
   - Build Command: (leave empty)
   - Publish Directory: `.`
6. Deploy!

### 3. Test Your AR Experience

1. Open the deployed URL on your mobile device
2. Allow camera permissions
3. Point your camera at marker1 to begin
4. Follow the narrative prompts
5. Interact with objects by tapping

## Grading Criteria Achievement

- **Grade 5**: Shows single object per marker
- **Grade 7**: Sequential unlocking (marker2 after marker1)
- **Grade 9**: Multiple scenarios with portal interaction
- **Grade 10**: Artistic narrative with 3-chapter story arc

## Narrative Structure

**Chapter I: The Discovery**
- Introduces the mysterious artifact
- Rotating crystal animation
- Sets the tone for the journey

**Chapter II: The Portal**
- Interactive portal that must be activated
- Click interaction required to progress
- Gateway to the final chapter

**Chapter III: Revelation**
- Multiple interactive 3D objects
- Color-changing elements on click
- Journey completion message

## Customization

### Change Colors
Edit the `color` attributes in index.html:
```html
<a-box color="#YOUR_HEX_COLOR">
```

### Modify Text
Update `a-text` elements:
```html
<a-text value="Your custom text here">
```

### Add 3D Models
Replace placeholder shapes with GLB/GLTF models:
```html
<a-entity gltf-model="url(models/your-model.glb)">
```

## Browser Compatibility

- Chrome/Safari on iOS (best performance)
- Chrome on Android
- Requires HTTPS for camera access

## Educational Value

This project demonstrates:
- Event-driven programming
- State management
- 3D graphics and animations
- User interaction patterns
- Progressive web app concepts

## License

Educational project - free to use and modify

## Credits

- AR.js library
- A-Frame framework
- NFT Marker Creator tool
