# common_utils
Install in editable mode (for local development and updates)
python -m pip install -e C:/A/Pro/flow/common_utils

Step 1: Check Editable Install
First, let's confirm if your editable install worked:

Verify installation by running the following in your flow project:

pip list
Check if common_utils is listed there, and verify the version or path is correct.

If the version looks correct, proceed to the next step.

Step 2: Refresh pip Cache
Sometimes, pip might be using cached files, so let’s clear it and reinstall:

python -m pip uninstall common_utils
python -m pip install -e C:/A/Pro/flow/common_utils
This forces pip to reinstall the editable version.

Step 3: Check for Changes
If you still don't see the changes:

Verify the changes in common_utils by checking the file directly.

Ensure there are no issues like circular imports or issues in common_utils/__init__.py.

After making sure the changes are there, you can restart the Python environment 
(e.g., if you're using Jupyter, an IDE, or a Python shell). 
This ensures that it picks up the new state of the package.
