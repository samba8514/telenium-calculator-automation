# Calculator App Automation Test with pytest

import time
import pytest
import telenium


class TestCalculatorApp:
    """Test class for Calculator App automation using Telenium"""

    # Class variables to share across all tests
    cli = None
    button_map = {}
    _setup_done = False

    @classmethod
    def setup_class(cls):
        """Setup once for all tests - OPTIMIZED!"""
        print("\nStarting Calculator Test Suite")
        try:
            print("Connecting to Calculator app...")
            cls.cli = telenium.connect()
            print("Connected successfully!")

            # Wait until the calculator widget appears
            print("Waiting for CalcApplicationWidget...")
            cls.cli.wait("//CalcApplicationWidget", timeout=10)
            print("Calculator found!")

            # Discover button layout ONCE for all tests
            cls.discover_buttons()
            cls._setup_done = True

        except Exception as e:
            pytest.fail(f"Failed to setup test class: {e}")

    @classmethod
    def discover_buttons(cls):
        """Discover and map all calculator buttons - RUNS ONCE ONLY"""
        print("Discovering button layout...")
        start_time = time.time()

        try:
            for i in range(20):  # Check first 20 buttons
                try:
                    text = cls.cli.getattr(f"//Button[{i}]", "text")
                    cls.button_map[text] = i
                    print(f"  Button {i}: '{text}'")
                except Exception:
                    break
        except Exception as e:
            pytest.fail(f"Failed to discover buttons: {e}")

        discovery_time = time.time() - start_time
        print(f"Button mapping complete in {discovery_time:.2f}s")

    def setup_method(self):
        """Quick setup before each test method"""
        if not self._setup_done:
            pytest.fail("Class setup failed, cannot run tests")

        # Just ensure we're still connected (very fast check)
        try:
            display_value = self.__class__.cli.getattr("//Label", "text")
            print(f"Current display: {display_value}")
        except Exception as e:
            pytest.fail(f"Calculator connection lost: {e}")

    def safe_click(self, button_text, description):
        """Safely click a button with error handling"""
        if button_text not in self.__class__.button_map:
            pytest.fail(f"Button '{button_text}' not found in calculator")

        try:
            selector = f"//Button[{self.__class__.button_map[button_text]}]"
            self.__class__.cli.click_on(selector)
            print(f"  ✓ Clicked {description}")
            time.sleep(0.3)
            return True
        except Exception as e:
            pytest.fail(f"Failed to click {description}: {e}")

    def get_display_value(self):
        """Get current calculator display value"""
        try:
            return self.__class__.cli.getattr("//Label", "text")
        except Exception as e:
            pytest.fail(f"Failed to read display: {e}")

    def clear_calculator(self):
        """Clear the calculator"""
        self.safe_click('C', "Clear button")
        time.sleep(0.5)

    def test_addition(self):
        """Test addition: 5 + 3 = 8"""
        print("\nTesting Addition: 5 + 3 = 8")

        self.clear_calculator()

        # Perform calculation
        self.safe_click('5', "number 5")
        display = self.get_display_value()
        print(f"  Display after 5: {display}")

        self.safe_click('Add', "Add button")
        self.safe_click('3', "number 3")
        display = self.get_display_value()
        print(f"  Display after 3: {display}")

        self.safe_click('Eq', "Equals button")
        time.sleep(0.5)

        result = self.get_display_value()
        print(f"  Final result: {result}")

        assert result == "8", f"Expected 8, got {result}"
        print("Addition test PASSED!")

    def test_multiplication(self):
        """Test multiplication: 4 × 6 = 24"""
        print("\nTesting Multiplication: 4 × 6 = 24")

        self.clear_calculator()

        self.safe_click('4', "number 4")
        self.safe_click('Mul', "Multiply button")
        self.safe_click('6', "number 6")
        self.safe_click('Eq', "Equals button")
        time.sleep(0.5)

        result = self.get_display_value()
        print(f"  Result: {result}")

        assert result == "24", f"Expected 24, got {result}"
        print("Multiplication test PASSED!")

    def test_division(self):
        """Test division: 15 ÷ 3 = 5"""
        print("\nTesting Division: 15 ÷ 3 = 5")

        self.clear_calculator()

        self.safe_click('1', "number 1")
        self.safe_click('5', "number 5")
        self.safe_click('Div', "Divide button")
        self.safe_click('3', "number 3")
        self.safe_click('Eq', "Equals button")
        time.sleep(0.5)

        result = self.get_display_value()
        print(f"  Result: {result}")

        assert result == "5", f"Expected 5, got {result}"
        print("Division test PASSED!")

    def test_subtraction(self):
        """Test subtraction: 10 - 4 = 6"""
        print("\nTesting Subtraction: 10 - 4 = 6")

        self.clear_calculator()

        self.safe_click('1', "number 1")
        self.safe_click('0', "number 0")
        self.safe_click('Sub', "Subtract button")
        self.safe_click('4', "number 4")
        self.safe_click('Eq', "Equals button")
        time.sleep(0.5)

        result = self.get_display_value()
        print(f"  Result: {result}")

        assert result == "6", f"Expected 6, got {result}"
        print("Subtraction test PASSED!")

    def test_decimal_addition(self):
        """Test decimal addition: 2.5 + 1.5 = 4"""
        print("\nTesting Decimal: 2.5 + 1.5 = 4")

        self.clear_calculator()

        self.safe_click('2', "number 2")
        self.safe_click('Dot', "decimal point")
        self.safe_click('5', "number 5")
        self.safe_click('Add', "Add button")
        self.safe_click('1', "number 1")
        self.safe_click('Dot', "decimal point")
        self.safe_click('5', "number 5")
        self.safe_click('Eq', "Equals button")
        time.sleep(0.5)

        result = self.get_display_value()
        print(f"  Result: {result}")

        assert result == "4", f"Expected 4, got {result}"
        print("Decimal test PASSED!")

    def test_clear_functionality(self):
        """Test clear functionality"""
        print("\nTesting Clear Functionality")

        # Enter some numbers
        self.safe_click('1', "number 1")
        self.safe_click('2', "number 2")
        self.safe_click('3', "number 3")

        display = self.get_display_value()
        print(f"  Display before clear: {display}")

        # Clear
        self.safe_click('C', "Clear button")

        result = self.get_display_value()
        print(f"  Display after clear: {result}")

        assert result == "0", f"Expected 0 after clear, got {result}"
        print("Clear test PASSED!")

    @classmethod
    def teardown_class(cls):
        """Cleanup after all tests"""
        print("\nTaking final screenshot...")
        try:
            if cls.cli:
                result = cls.cli.screenshot("pytest_calculator_final.png")
                print(f"  Screenshot saved: {result['filename']}")
        except Exception as e:
            print(f"  Screenshot failed: {e}")

        print("Calculator Test Suite Complete!")


# For running individual tests or the old way
def main():
    """Run tests the old way if called directly"""
    print("Tip: Use 'pytest' command for better test reporting!")
    test_class = TestCalculatorApp()
    test_class.setup_class()
    test_class.setup_method()

    tests = [
        test_class.test_addition,
        test_class.test_multiplication,
        test_class.test_division,
        test_class.test_subtraction,
        test_class.test_decimal_addition,
        test_class.test_clear_functionality,
    ]

    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"Test failed: {e}")

    test_class.teardown_class()


if __name__ == "__main__":
    main()