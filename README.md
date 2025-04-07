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

Step 4: Check for Other Issues
If you’re still seeing warnings like:

WARNING: Ignoring invalid distribution ~ip (C:\Python312\Lib\site-packages)
It suggests that there’s some problem with your pip installation. To fix this:

Clear pip’s cache:
python -m pip cache purge

Upgrade pip:
python -m pip install --upgrade pip

Reinstall pip: If the issue persists, you can reinstall pip by running:
python -m ensurepip --upgrade

