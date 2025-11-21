"""Command-line interface for images-to-pdf converter."""

import argparse
import sys
from pathlib import Path
from .core import create_pdf_from_images
from . import __version__


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert images in a folder to PDF slides with automatic analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  images-to-pdf                        # Use default 'images' folder
  images-to-pdf photos/                # Convert images from 'photos' folder
  images-to-pdf pics/ -o slides.pdf    # Custom output filename
        """
    )

    parser.add_argument(
        "images_folder",
        nargs="?",
        default="images",
        help="Folder containing images (default: images)",
    )

    parser.add_argument(
        "-o", "--output",
        default="output_slides.pdf",
        help="Output PDF filename (default: output_slides.pdf)",
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"images-to-pdf {__version__}",
    )

    args = parser.parse_args()

    # Validate input folder exists
    images_path = Path(args.images_folder)
    if not images_path.exists():
        print(f"Error: Folder '{args.images_folder}' does not exist", file=sys.stderr)
        return 1

    if not images_path.is_dir():
        print(f"Error: '{args.images_folder}' is not a directory", file=sys.stderr)
        return 1

    try:
        create_pdf_from_images(args.images_folder, args.output)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
