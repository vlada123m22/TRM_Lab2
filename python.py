#!/usr/bin/env python3
"""
AR Project Setup and Management Script
Helps automate the setup process for the AR narrative project
"""

import os
import json
import subprocess
import sys
from pathlib import Path


class ARProjectSetup:
    def __init__(self):
        self.project_root = Path.cwd()
        self.markers_dir = self.project_root / "markers"
        self.models_dir = self.project_root / "models"

    def create_directory_structure(self):
        """Create necessary directories"""
        print("📁 Creating directory structure...")

        directories = [
            self.markers_dir,
            self.models_dir,
            self.project_root / "assets",
            self.project_root / "css",
            self.project_root / "js"
        ]

        for directory in directories:
            directory.mkdir(exist_ok=True)
            print(f"   ✓ {directory.name}/")

        print("✅ Directory structure created!\n")

    def create_readme(self):
        """Create a comprehensive README"""
        readme_content = """# Interactive AR Narrative Experience

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
"""

        with open(self.project_root / "README.md", "w") as f:
            f.write(readme_content)

        print("README.md created!\n")

    def create_gitignore(self):
        """Create .gitignore file"""
        gitignore_content = """# Dependencies
node_modules/
npm-debug.log
yarn-error.log

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Build
dist/
build/

# Temporary files
*.tmp
*.log
"""

        with open(self.project_root / ".gitignore", "w") as f:
            f.write(gitignore_content)

        print(".gitignore created!\n")

    def create_render_config(self):
        """Create render.yaml for Render.com deployment"""
        render_config = {
            "services": [
                {
                    "type": "web",
                    "name": "ar-narrative-experience",
                    "env": "static",
                    "buildCommand": "",
                    "staticPublishPath": ".",
                    "headers": [
                        {
                            "path": "/*",
                            "name": "X-Frame-Options",
                            "value": "SAMEORIGIN"
                        },
                        {
                            "path": "/*",
                            "name": "X-Content-Type-Options",
                            "value": "nosniff"
                        }
                    ]
                }
            ]
        }

        with open(self.project_root / "render.yaml", "w") as f:
            json.dump(render_config, f, indent=2)

        print("render.yaml created!\n")

    def check_git_setup(self):
        """Check if git is initialized"""
        if not (self.project_root / ".git").exists():
            print("Git not initialized. Run: git init")
            return False
        print("Git repository detected\n")
        return True

    def display_next_steps(self):
        """Display next steps for the user"""
        steps = """
╔══════════════════════════════════════════════════════════════╗
║                     NEXT STEPS                               ║
╚══════════════════════════════════════════════════════════════╝

1. 📸 Create Your NFT Markers:
   → Visit: https://carnaux.github.io/NFT-Marker-Creator/#/
   → Upload 3 distinctive images
   → Download and place files in markers/ folder

2. 🎨 Customize Your Experience:
   → Edit index.html to change text and colors
   → Add your own 3D models to models/ folder
   → Modify the narrative to tell your story

3. 📤 Push to GitHub:
   git add .
   git commit -m "Initial AR project setup"
   git push origin main

4. 🚀 Deploy on Render.com:
   → Go to https://render.com/
   → Create new Static Site
   → Connect your GitHub repository
   → Deploy!

5. 📱 Test Your AR:
   → Open deployed URL on mobile
   → Allow camera permissions
   → Point at markers to experience the story

💡 Tips:
   - Use high-contrast images for markers
   - Test on mobile for best experience
   - Markers should be at least 10cm in size when printed
   - Good lighting improves tracking

🎯 Your project aims for Grade 10 with:
   ✓ Sequential narrative
   ✓ Interactive elements
   ✓ Multiple scenarios
   ✓ Artistic storytelling

Good luck with your AR project! 🌟
"""
        print(steps)

    def run_setup(self):
        """Run the complete setup process"""
        print("\n" + "=" * 60)
        print("🚀 AR NARRATIVE PROJECT SETUP")
        print("=" * 60 + "\n")

        self.create_directory_structure()
        self.create_readme()
        self.create_gitignore()
        self.create_render_config()
        self.check_git_setup()
        self.display_next_steps()


def main():
    """Main entry point"""
    setup = ARProjectSetup()
    setup.run_setup()


if __name__ == "__main__":
    main()