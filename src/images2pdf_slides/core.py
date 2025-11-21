"""Core functionality for converting images to PDF slides."""

from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas


def analyze_image(image_path):
    """Analyze image properties.

    Args:
        image_path: Path to the image file

    Returns:
        Dictionary containing image properties (width, height, mode, format, dpi, aspect_ratio)
    """
    with Image.open(image_path) as img:
        width, height = img.size
        mode = img.mode
        format_type = img.format

        # Calculate DPI (if available)
        dpi = img.info.get('dpi', (72, 72))

        return {
            'path': image_path,
            'width': width,
            'height': height,
            'mode': mode,
            'format': format_type,
            'dpi': dpi,
            'aspect_ratio': width / height
        }


def create_pdf_from_images(images_folder, output_pdf):
    """Create a PDF with each image as a slide.

    Args:
        images_folder: Path to folder containing images
        output_pdf: Output PDF filename
    """
    images_path = Path(images_folder)

    # Find all image files
    image_files = sorted([
        f for f in images_path.glob('*')
        if f.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    ])

    if not image_files:
        print(f"No images found in {images_folder}")
        return

    print(f"\nFound {len(image_files)} images\n")
    print("=" * 80)

    # Analyze all images first
    image_info = []
    for img_file in image_files:
        info = analyze_image(img_file)
        image_info.append(info)
        print(f"Image: {img_file.name}")
        print(f"  Resolution: {info['width']} x {info['height']} pixels")
        print(f"  Format: {info['format']}")
        print(f"  Color Mode: {info['mode']}")
        print(f"  DPI: {info['dpi']}")
        print(f"  Aspect Ratio: {info['aspect_ratio']:.2f}")
        print()

    print("=" * 80)
    print(f"\nCreating PDF: {output_pdf}\n")

    # Determine page size based on first image's aspect ratio
    first_img_info = image_info[0]

    # Use the first image dimensions to determine page size
    # Scale to fit within reasonable PDF dimensions
    max_width = 11 * 72  # 11 inches in points (letter width)
    max_height = 8.5 * 72  # 8.5 inches in points (letter height landscape)

    # Calculate page size maintaining aspect ratio
    aspect = first_img_info['aspect_ratio']
    if aspect > 1:  # Landscape
        page_width = max_width
        page_height = page_width / aspect
    else:  # Portrait
        page_height = max_height
        page_width = page_height * aspect

    page_size = (page_width, page_height)

    # Create PDF
    c = canvas.Canvas(str(output_pdf), pagesize=page_size)

    # Add each image as a page
    for idx, info in enumerate(image_info, 1):
        print(f"Adding slide {idx}/{len(image_info)}: {info['path'].name}")

        # Calculate dimensions to fit the page while maintaining aspect ratio
        img_width = info['width']
        img_height = info['height']
        img_aspect = info['aspect_ratio']

        # Scale image to fit page
        if img_aspect > page_width / page_height:
            # Image is wider relative to page
            draw_width = page_width
            draw_height = page_width / img_aspect
        else:
            # Image is taller relative to page
            draw_height = page_height
            draw_width = page_height * img_aspect

        # Center the image on the page
        x = (page_width - draw_width) / 2
        y = (page_height - draw_height) / 2

        # Draw image
        c.drawImage(str(info['path']), x, y, width=draw_width, height=draw_height)

        # Move to next page if not the last image
        if idx < len(image_info):
            c.showPage()

    # Save PDF
    c.save()
    print(f"\n✓ PDF created successfully: {output_pdf}")
    print(f"  Total pages: {len(image_info)}")
