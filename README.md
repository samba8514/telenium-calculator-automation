# Telenium Calculator Automation Example

A comprehensive demonstration of UI automation testing using **Telenium** with a modern Kivy calculator application. This project showcases best practices for automated testing, performance optimization, KV file architecture, and robust error handling.

## 📋 Overview

**Telenium** is a powerful tool for automating Kivy applications. This example provides a complete, production-ready testing framework that can serve as a template for your own UI automation projects.

### Key Features Demonstrated

- ✅ **Modern Kivy Architecture** - Separation of UI (KV files) from logic (Python)
- ✅ **Smart Button Discovery** - Automatically finds and maps UI elements
- ✅ **Robust Error Handling** - Comprehensive validation and error messages
- ✅ **Multiple Test Types** - Unit tests, integration tests, and workflows

## 📁 Project Structure

```
📦 telenium_test/
├── 🖥️ CalcApplication.py                  # Python logic (business logic)
├── 🎨 calcapplication.kv                  # Kivy UI definition (layout & styling)
├── 📋 requirements.txt                  # Python dependencies
├── 📋 pyproject.toml                    # Project configuration
├── 💻 .vscode/launch.json              # VS Code debug configuration
├── 🚫 .gitignore                       # Git ignore rules
├── 📖 README.md                        # This documentation
└── 🧪 tests/
    └── 🔬 test_CalcApplication.py       # Pytest automation tests
```

## 🎨 Architecture: KV + Python

This project demonstrates modern Kivy architecture with **separation of concerns**.

### 📄 `calcapplication.kv` - UI Definition
```kv
<CalcApplicationWidget>:
    orientation: 'vertical'
    spacing: 5
    padding: 10

    Label:
        id: display
        text: '0'
        font_size: 32
        # ... styling and layout

    GridLayout:
        cols: 4
        Button:
            text: 'C'
            on_press: root.on_button(self)
            # ... more buttons
```

### 🐍 `CalcApplication.py` - Business Logic
```python
class CalcApplicationWidget(BoxLayout):
    def on_button(self, instance):
        """Handle button presses - called from KV"""
        btn_text = instance.text
        # ... business logic only

    def update_display(self, text):
        """Update display using KV ids"""
        self.ids.display.text = str(text)
```

### Benefits of KV Architecture:
- 🎯 **Clean Separation** - UI markup separate from Python logic
- 🔧 **Easy Styling** - CSS-like properties in KV files
- 🚀 **Faster Development** - Hot reload and visual design
- 🛠️ **Maintainable** - Easier to modify layouts without touching logic

## 🧪 Test Files Overview

This project includes a **professional pytest-based test suite**:

### 📄 `tests/test_CalcApplication.py` (Tests Directory)
- **Pytest Framework** - Professional test organization
- **Class-based Structure** - Clean, maintainable test suite
- **Performance Optimized** - Shared setup for faster execution
- **CI/CD Ready** - Designed for automated testing pipelines
- **Comprehensive Coverage** - Tests all calculator operations

## 🚀 Quick Start

### Prerequisites

Install required packages:
```bash
pip install -r requirements.txt
# or individually:
pip install kivy telenium pytest
```

### Running the Example

#### 🧪 Method 1: Pytest Framework (Recommended)
```bash
# Start calculator app (Terminal 1)
python CalcApplication.py

# Run with pytest (Terminal 2)
pytest tests/test_CalcApplication.py -v

# Generate HTML report
pytest tests/test_CalcApplication.py --html=reports/pytest_report.html
```

#### 🔧 Method 2: Run Individual Tests
```bash
# Start calculator app (Terminal 1)
python CalcApplication.py

# Run specific test methods (Terminal 2)
cd tests
pytest test_CalcApplication.py::TestCalculatorApp::test_addition -v
pytest test_CalcApplication.py::TestCalculatorApp::test_multiplication -v
```

### Expected Output

```
🚀 Starting Telenium Calculator Test Suite
🔌 Connecting to Calculator app via Telenium...
✅ Connected successfully!
🔍 Waiting for CalcApplicationWidget...
✅ Calculator widget found!
🔍 Auto-discovering calculator buttons...
  📍 Button 0: '7'
  📍 Button 1: '8'
  📍 Button 2: '9'
  📍 Button 3: 'Div'
  ...
📋 Button mapping complete in 0.15s
📊 Discovered 17 buttons total

🧮 Testing Addition: 5 + 3 = 8
  📺 Current display: '0'
  ✓ Clicked Clear button
  ✓ Clicked number 5
  Display after 5: '5'
  ✓ Clicked Add button
  ✓ Clicked number 3
  Display after 3: '3'
  ✓ Clicked Equals button
  Final result: '8'
  ✅ Addition test PASSED!
```

## 🎯 Test Coverage

The automation tests comprehensively cover:

### Basic Operations
- ➕ **Addition** - 5 + 3 = 8
- ✖️ **Multiplication** - 4 × 6 = 24
- ➗ **Division** - 15 ÷ 3 = 5
- ➖ **Subtraction** - 10 - 4 = 6

## 🎓 Learning Highlights

### 1. Connection & Setup
```python
# Connect to Kivy app via Telenium
cls.cli = telenium.connect()

# Wait for specific widget
cls.cli.wait("//CalcApplicationWidget", timeout=10)
```

### 2. Smart Element Discovery
```python
# Auto-discover all buttons
for i in range(20):
    text = cls.cli.getattr(f"//Button[{i}]", "text")
    cls.button_map[text] = i
```

### 3. Safe UI Interactions
```python
# Click with error handling
selector = f"//Button[{self.button_map[button_text]}]"
self.cli.click_on(selector)

# Read display value
display = self.cli.getattr("//Label", "text")
```

### 4. Performance Optimization
```python
@classmethod
def setup_class(cls):
    # Runs once for all tests - major performance gain
    cls.discover_buttons()  # Only discover buttons once
```

## 🔧 Advanced Usage

### Running Specific Tests

```bash
# Run only addition test (pytest framework)
pytest tests/test_CalcApplication.py::TestCalculatorApp::test_addition -v

# Run tests by category (using markers)
pytest -m "ui" -v
pytest -m "calculator" -v
pytest -m "smoke" -v
```

### Generating Reports

```bash
# HTML report with coverage (pytest framework)
pytest tests/test_CalcApplication.py --html=reports/test_report.html --cov=CalcApplication

# JUnit XML for CI/CD
pytest tests/test_CalcApplication.py --junitxml=reports/junit.xml

# Multiple formats
pytest tests/test_CalcApplication.py --html=reports/report.html --junitxml=reports/junit.xml
```

## � Customization Guide

### Adding New Tests

```python
def test_your_feature(self):
    """Test your specific functionality"""
    print("\\n🎯 Testing Your Feature")

    self.clear_calculator()
    # Your test logic here
    self.safe_click('5', "number 5")

    result = self.get_display_value()
    assert result == "expected", f"Expected result, got {result}"
    print("  ✅ Your test PASSED!")
```

### Adapting for Your App

1. **Change Connection Target**: Update `//CalcApplicationWidget` to your widget
2. **Modify Discovery Logic**: Adapt button discovery for your UI elements
3. **Update Selectors**: Change XPath patterns for your app structure
4. **Add Your Actions**: Implement app-specific helper methods

## 🐛 Troubleshooting

### Connection Issues
- **Calculator not running** → Start with `python CalcApplication.py`
- **Port 9901 in use** → Restart calculator app
- **Connection timeout** → Check Telenium server message: `Started at 0.0.0.0:9901`

### Test Failures
- **Button not found** → Check button discovery output for correct names
- **Test timeout** → Increase wait times in `cls.cli.wait()`
- **JSON parsing errors** → Calculator app may need restart (avoid special characters)


### Debug Mode

```bash
# Run pytest with detailed output
pytest tests/test_CalcApplication.py -v -s --tb=long

# Run specific test with debugging
pytest tests/test_CalcApplication.py::TestCalculatorApp::test_addition -v -s
```

## �📦 Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `kivy` | GUI framework for calculator | `>=2.0.0` |
| `telenium` | UI automation and testing | `>=0.4.0` |
| `pytest` | Testing framework | `>=6.0.0` |
| `pytest-html` | HTML test reports | `>=3.0.0` |

Install all at once:
```bash
pip install -r requirements.txt
```

## � Performance Metrics

- **Setup Time**: ~60s (button discovery)
- **Test Execution**: ~100s for full suite

## 📚 Additional Resources

- [Telenium Documentation](https://github.com/kivy/telenium)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [pytest Documentation](https://docs.pytest.org/)


## 📄 License

This example code is provided as-is for educational purposes. Use and modify as needed for your projects.

---

**Happy Automating! 🎉**

*This example demonstrates production-ready UI automation with Telenium. Use it as a foundation for building robust, maintainable test suites for your Kivy applications.*