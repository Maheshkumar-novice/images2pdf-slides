# Images to PDF Converter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern Python package that converts images in a folder into a professional PDF presentation, with each image displayed as a slide. Features automatic image analysis, resolution detection, and intelligent page sizing.

## ✨ Features

- 🖼️ **Multi-format Support**: PNG, JPG, JPEG, GIF, and BMP
- 📊 **Automatic Analysis**: Analyzes resolution, DPI, format, and aspect ratio
- 📐 **Smart Sizing**: Automatically adjusts PDF page size based on image dimensions
- 🎯 **Aspect Ratio Preservation**: Maintains image proportions and centers content
- ⚡ **Fast Processing**: Built with Pillow and ReportLab for optimal performance
- 🖥️ **CLI & API**: Use as command-line tool or Python library
- 📦 **Modern Packaging**: Built with UV and follows Python packaging best practices

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Python API](#python-api)
- [Requirements](#requirements)
- [Examples](#examples)
- [Development](#development)
- [Publishing](#publishing)
- [License](#license)

## 🚀 Installation

### From PyPI (once published)

```bash
pip install images-to-pdf
```

### From Source

#### Using UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/Maheshkumar-novice/images-to-pdf.git
cd images-to-pdf

# Install with UV
uv pip install -e .
```

#### Using pip

```bash
# Clone the repository
git clone https://github.com/Maheshkumar-novice/images-to-pdf.git
cd images-to-pdf

# Install in editable mode
pip install -e .
```

## 🏃 Quick Start

1. **Prepare your images**: Place images in a folder (e.g., `images/`)

2. **Run the converter**:
   ```bash
   images-to-pdf images/
   ```

3. **Get your PDF**: Find `output_slides.pdf` in the current directory

That's it! 🎉

## 📖 Usage

### Command Line Interface

The package installs the `images-to-pdf` command:

```bash
# Use default 'images' folder and output filename
images-to-pdf

# Specify a custom input folder
images-to-pdf photos/

# Specify custom input folder and output filename
images-to-pdf photos/ -o presentation.pdf

# Show help message
images-to-pdf --help

# Show version
images-to-pdf --version
```

#### CLI Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `images_folder` | - | Folder containing images | `images` |
| `--output` | `-o` | Output PDF filename | `output_slides.pdf` |
| `--version` | `-v` | Show version number | - |
| `--help` | `-h` | Show help message | - |

### Python API

Use the package in your Python scripts:

```python
from images_to_pdf import create_pdf_from_images, analyze_image

# Create PDF from all images in a folder
create_pdf_from_images("photos/", "output.pdf")

# Analyze a single image
info = analyze_image("photo.jpg")
print(f"Resolution: {info['width']}x{info['height']} pixels")
print(f"Format: {info['format']}")
print(f"DPI: {info['dpi']}")
print(f"Aspect Ratio: {info['aspect_ratio']:.2f}")
```

#### API Reference

##### `create_pdf_from_images(images_folder, output_pdf)`

Convert all images in a folder to a PDF presentation.

**Parameters:**
- `images_folder` (str): Path to folder containing images
- `output_pdf` (str): Output PDF filename

**Returns:** None

**Supported formats:** PNG, JPG, JPEG, GIF, BMP

##### `analyze_image(image_path)`

Analyze properties of a single image.

**Parameters:**
- `image_path` (str | Path): Path to image file

**Returns:** Dictionary with keys:
- `path`: Path to the image
- `width`: Image width in pixels
- `height`: Image height in pixels
- `mode`: Color mode (e.g., 'RGB', 'RGBA')
- `format`: Image format (e.g., 'PNG', 'JPEG')
- `dpi`: DPI tuple (x, y)
- `aspect_ratio`: Width/height ratio

## 📦 Requirements

- **Python**: 3.8 or higher
- **Dependencies**:
  - Pillow >= 10.0.0 (Image processing)
  - ReportLab >= 4.0.0 (PDF generation)

All dependencies are automatically installed when you install the package.

## 💡 Examples

### Example 1: Basic Usage

```bash
# Place images in 'images' folder
mkdir images
cp ~/Pictures/*.jpg images/

# Convert to PDF
images-to-pdf

# Output: output_slides.pdf created with all images as slides
```

### Example 2: Custom Output

```bash
# Create presentation with custom name
images-to-pdf vacation-photos/ -o vacation-2025.pdf
```

### Example 3: Python Script

```python
from pathlib import Path
from images_to_pdf import create_pdf_from_images, analyze_image

# Analyze all images first
image_folder = Path("screenshots")
for img_file in image_folder.glob("*.png"):
    info = analyze_image(img_file)
    print(f"{img_file.name}: {info['width']}x{info['height']}")

# Create PDF
create_pdf_from_images("screenshots", "documentation.pdf")
```

### Example Output

When you run the converter, you'll see detailed analysis:

```
Found 5 images

================================================================================
Image: Screenshot 2025-11-20 at 4.37.39 PM.png
  Resolution: 2880 x 1800 pixels
  Format: PNG
  Color Mode: RGBA
  DPI: (144.0, 144.0)
  Aspect Ratio: 1.60

Image: Screenshot 2025-11-20 at 4.37.47 PM.png
  Resolution: 2880 x 1800 pixels
  Format: PNG
  Color Mode: RGBA
  DPI: (144.0, 144.0)
  Aspect Ratio: 1.60

[... more images ...]

================================================================================

Creating PDF: output_slides.pdf

Adding slide 1/5: Screenshot 2025-11-20 at 4.37.39 PM.png
Adding slide 2/5: Screenshot 2025-11-20 at 4.37.47 PM.png
Adding slide 3/5: Screenshot 2025-11-20 at 4.38.08 PM.png
Adding slide 4/5: Screenshot 2025-11-20 at 4.38.16 PM.png
Adding slide 5/5: Screenshot 2025-11-20 at 4.38.44 PM.png

✓ PDF created successfully: output_slides.pdf
  Total pages: 5
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/Maheshkumar-novice/images-to-pdf.git
cd images-to-pdf

# Install with development dependencies using UV
uv sync --all-extras

# Or using pip
pip install -e ".[dev]"
```

### Project Structure

```
images-to-pdf/
├── src/
│   └── images_to_pdf/
│       ├── __init__.py      # Package initialization and exports
│       ├── core.py          # Core conversion logic
│       ├── cli.py           # Command-line interface
│       └── py.typed         # Type hints marker
├── dist/                     # Built distributions (gitignored)
├── pyproject.toml           # Package configuration
├── LICENSE                  # MIT License
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

### Development Workflow

```bash
# Format code with black
uv run black src/

# Lint code with ruff
uv run ruff check src/

# Run type checking with mypy
uv run mypy src/

# Run tests (if you add them)
uv run pytest

# Test the CLI locally
uv run images-to-pdf images/
```

### Adding Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes in `src/images_to_pdf/`
4. Test your changes locally
5. Submit a pull request

## 📤 Publishing

### Building the Package

```bash
# Build distribution files
uv build

# Output: dist/images_to_pdf-0.1.0-py3-none-any.whl
#         dist/images_to_pdf-0.1.0.tar.gz
```

### Publishing to PyPI

#### Prerequisites

1. Create accounts:
   - Test PyPI: https://test.pypi.org/account/register/
   - Production PyPI: https://pypi.org/account/register/

2. Enable 2FA (required)

3. Create API token:
   - Go to Account Settings → API tokens
   - Create token for this project

#### Publish Steps


```bash
# 1. Test on Test PyPI first (recommended)
uv publish --publish-url https://test.pypi.org/legacy/

# 2. Verify installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ images-to-pdf

# 3. If everything works, publish to production PyPI
uv publish

# 4. Install from PyPI
pip install images-to-pdf
```

#### Publishing with Token

```bash
# Set environment variable (recommended)
export UV_PUBLISH_TOKEN="pypi-..."
uv publish

# Or pass directly
uv publish --token pypi-...
```

### Version Management

Update version in `pyproject.toml`:

```toml
[project]
name = "images-to-pdf"
version = "0.2.0"  # Increment version
```

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes (e.g., 1.0.0 → 2.0.0)
- **MINOR**: New features, backward compatible (e.g., 1.0.0 → 1.1.0)
- **PATCH**: Bug fixes (e.g., 1.0.0 → 1.0.1)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs**: Open an issue describing the problem
2. **Suggest features**: Open an issue with your idea
3. **Submit PRs**: Fork, create a branch, make changes, submit PR
4. **Improve docs**: Help make documentation better

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes docstrings for functions
- Works with Python 3.8+

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Maheshkumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 🔗 Links

- **Homepage**: https://github.com/Maheshkumar-novice/images-to-pdf
- **PyPI**: https://pypi.org/project/images-to-pdf/ (once published)
- **Issues**: https://github.com/Maheshkumar-novice/images-to-pdf/issues
- **Documentation**: This README

## ❓ FAQ

### Q: What image formats are supported?

A: PNG, JPG, JPEG, GIF, and BMP formats are supported.

### Q: How are images ordered in the PDF?

A: Images are sorted alphabetically by filename. To control the order, name your files with prefixes like `01-image.png`, `02-image.png`, etc.

### Q: Can I customize page sizes?

A: Currently, page sizes are automatically calculated based on the first image's aspect ratio. For custom page sizes, you can modify the `core.py` file or use the Python API to build your own logic.

### Q: What if my folder has no images?

A: The program will display "No images found in {folder}" and exit gracefully.

### Q: Does this work with very large images?

A: Yes, but be aware that very large images will increase PDF file size. The images are not compressed beyond their original format.

### Q: Can I use this in my commercial project?

A: Yes! The MIT license allows commercial use. Just include the license notice.

## 🙏 Acknowledgments

Built with:
- [Pillow](https://python-pillow.org/) - Python Imaging Library
- [ReportLab](https://www.reportlab.com/) - PDF generation
- [UV](https://github.com/astral-sh/uv) - Fast Python package manager

---

Made with ❤️ by Maheshkumar

**Star ⭐ this repo if you find it helpful!**
