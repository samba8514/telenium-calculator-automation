# Contributing to Telenium Calculator Automation

Thank you for your interest in contributing! This project demonstrates UI automation with Telenium and Kivy.

## 🚀 Getting Started

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/telenium-calculator-automation.git
   cd telenium-calculator-automation
   ```

3. **Set up the environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Test the setup:**
   ```bash
   # Terminal 1: Start the calculator
   python CalcApplication.py
   
   # Terminal 2: Run tests
   pytest tests/ -v
   ```

## 🛠️ Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use descriptive variable names
- Add docstrings for new functions
- Keep KV files clean and well-commented

### Testing
- Add tests for new features
- Ensure all existing tests pass
- Use meaningful test names and descriptions
- Add screenshots for visual validation

### Commit Messages
- Use clear, descriptive commit messages
- Format: `type(scope): description`
- Examples:
  - `feat(calculator): add scientific notation support`
  - `fix(tests): resolve button discovery timeout`
  - `docs(readme): update installation instructions`

## 📋 Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Add/update tests as needed
4. Update documentation if necessary
5. Run the full test suite: `pytest tests/ -v`
6. Commit your changes with descriptive messages
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request with:
   - Clear description of changes
   - Screenshots if UI changes
   - Test results

## 🧪 Testing Guidelines

- Test both positive and negative scenarios
- Include edge cases (division by zero, long numbers)
- Test UI responsiveness and error handling
- Validate automation reliability

## 🐛 Bug Reports

When reporting bugs, please include:
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version)
- Screenshots if applicable
- Error logs

## 💡 Feature Requests

For new features:
- Describe the use case clearly
- Explain the expected behavior
- Consider backward compatibility
- Provide examples if possible

## 📚 Areas for Contribution

- **Calculator Features**: Scientific operations, memory functions, history
- **Test Coverage**: Edge cases, stress testing, performance tests
- **Documentation**: Tutorials, API docs, examples
- **UI Improvements**: Themes, accessibility, mobile support
- **Automation**: CI/CD, cross-platform testing

## ❓ Questions?

Feel free to open an issue for questions or join discussions in existing issues.

Thank you for contributing! 🎉