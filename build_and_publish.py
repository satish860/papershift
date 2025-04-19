"""
Build and publish the PaperShift package to PyPI.

Usage:
    python build_and_publish.py [--test]

Options:
    --test  Upload to TestPyPI instead of PyPI
"""
import os
import sys
import shutil
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get PyPI token from environment variable
PYPI_TOKEN = os.environ.get("PYPI_TOKEN")

def clean_build_dirs():
    """Remove build directories."""
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for dir_name in dirs_to_clean:
        if '*' in dir_name:
            # Handle wildcard pattern
            import glob
            for path in glob.glob(dir_name):
                if os.path.isdir(path):
                    shutil.rmtree(path)
        elif os.path.exists(dir_name):
            shutil.rmtree(dir_name)
    print("✓ Cleaned build directories")

def build_package():
    """Build the package."""
    print("Building package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "build"])
    subprocess.check_call([sys.executable, "-m", "build"])
    print("✓ Package built successfully")

def publish_package(test=False):
    """Publish the package to PyPI or TestPyPI."""
    print("Publishing package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "twine"])
    
    if not PYPI_TOKEN:
        print("Error: PYPI_TOKEN environment variable not set.")
        print("Please add your PyPI token to the .env file:")
        print("PYPI_TOKEN=your-token-here")
        return False
    
    # Create .pypirc file with token
    pypirc_path = os.path.expanduser("~/.pypirc")
    with open(pypirc_path, "w") as f:
        f.write("[pypi]\n")
        f.write("username = __token__\n")
        f.write(f"password = {PYPI_TOKEN}\n")
    
    try:
        if test:
            print("Publishing to TestPyPI...")
            subprocess.check_call([
                sys.executable, "-m", "twine", "upload", 
                "--repository-url", "https://test.pypi.org/legacy/", 
                "dist/*"
            ])
            print("✓ Package published to TestPyPI")
            print("\nTo install from TestPyPI:")
            print(f"pip install --index-url https://test.pypi.org/simple/ papershift")
        else:
            print("Publishing to PyPI...")
            subprocess.check_call([
                sys.executable, "-m", "twine", "upload",
                "--username", "__token__",
                "--password", PYPI_TOKEN,
                "dist/*"
            ])
            print("✓ Package published to PyPI")
            print("\nTo install from PyPI:")
            print(f"pip install papershift")
        return True
    finally:
        # Remove the .pypirc file for security
        if os.path.exists(pypirc_path):
            os.remove(pypirc_path)

def main():
    # Check if we should publish to test PyPI
    test_mode = "--test" in sys.argv
    
    # Clean build directories
    clean_build_dirs()
    
    # Build the package
    build_package()
    
    # Publish the package
    success = publish_package(test=test_mode)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
