# Contributing to Images to PDF

Thank you for considering contributing to Images to PDF! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [UV](https://github.com/astral-sh/uv) (recommended) or pip
- Git

### Setting Up Development Environment

1. Fork the repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/images-to-pdf.git
   cd images-to-pdf
   ```

3. Install dependencies:
   ```bash
   uv sync --all-extras
   # or
   pip install -e ".[dev]"
   ```

4. Test the installation:
   ```bash
   images-to-pdf --version
   ```

## 🔧 Development Workflow

### Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. Make your changes in the `src/images_to_pdf/` directory

3. Test your changes:
   ```bash
   # Test CLI
   images-to-pdf --help

   # Test with sample images
   mkdir test-images
   # Add some test images
   images-to-pdf test-images/ -o test.pdf
   ```

4. Format your code:
   ```bash
   uv run black src/
   uv run ruff check src/
   ```

### Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions
- Keep functions focused and single-purpose

### Commit Messages

Write clear commit messages:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs when applicable

Examples:
```
Add support for TIFF images
Fix aspect ratio calculation for portrait images
Update README with new examples
```

## 📝 Pull Request Process

1. Update the README.md with details of changes if applicable
2. Ensure your code follows the style guidelines
3. Test your changes thoroughly
4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request from your fork to the main repository
6. Describe your changes clearly in the PR description
7. Link any related issues

### PR Guidelines

- Keep PRs focused on a single feature or fix
- Include a clear description of what changed and why
- Add examples or screenshots if applicable
- Be responsive to feedback and questions

## 🐛 Reporting Bugs

When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)
- Environment details (OS, Python version, package version)
- Sample images (if relevant and safe to share)

## 💡 Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature has already been suggested
- Clearly describe the feature and its benefits
- Explain use cases
- Consider implementation complexity

## 📋 Areas to Contribute

Here are some areas where contributions are especially welcome:

### Code
- Bug fixes
- New features (e.g., custom page sizes, watermarks, compression)
- Performance improvements
- Test coverage

### Documentation
- README improvements
- Code comments
- Usage examples
- Tutorial content

### Testing
- Add test cases
- Test on different platforms
- Report bugs

## 🤔 Questions?

If you have questions:
- Check existing issues
- Read the README thoroughly
- Open a new issue with the "question" label

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. We pledge to:
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
