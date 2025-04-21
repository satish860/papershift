"""
Run tests for the image_to_markdown module.

This script runs both unit tests and integration tests for the image_to_markdown module.
"""
import os
import sys
import unittest
import argparse

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def run_unit_tests():
    """Run unit tests for the image_to_markdown module."""
    print("Running unit tests for image_to_markdown module...")
    from tests.test_image_to_markdown import TestImageToMarkdown
    
    # Create a test suite with all tests from TestImageToMarkdown
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageToMarkdown)
    
    # Run the tests
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    return result.wasSuccessful()


def run_integration_tests():
    """Run integration tests for the image_to_markdown module."""
    print("Running integration tests for image_to_markdown module...")
    from tests.integration_test_image_to_markdown import TestImageToMarkdownIntegration
    
    # Create a test suite with all tests from TestImageToMarkdownIntegration
    suite = unittest.TestLoader().loadTestsFromTestCase(TestImageToMarkdownIntegration)
    
    # Run the tests
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    return result.wasSuccessful()


def main():
    """Run the tests based on command line arguments."""
    parser = argparse.ArgumentParser(description='Run tests for the image_to_markdown module')
    parser.add_argument('--unit-only', action='store_true', help='Run only unit tests')
    parser.add_argument('--integration-only', action='store_true', help='Run only integration tests')
    args = parser.parse_args()
    
    # Check if OpenRouter API key is set for integration tests
    if not args.unit_only and not os.environ.get('OPENROUTER_API_KEY'):
        print("WARNING: OPENROUTER_API_KEY environment variable not set.")
        print("Integration tests will be skipped unless --unit-only is specified.")
        print("Set the OPENROUTER_API_KEY environment variable to run integration tests.")
        print("Example: export OPENROUTER_API_KEY=your_api_key")
        return False
    
    # Run the appropriate tests
    if args.unit_only:
        return run_unit_tests()
    elif args.integration_only:
        return run_integration_tests()
    else:
        # Run both unit and integration tests
        unit_success = run_unit_tests()
        integration_success = run_integration_tests()
        return unit_success and integration_success


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
