# Student Management System - CI/CD Pipeline Setup

A robust Continuous Integration (CI) pipeline for a Python-based **Student Management System** using **GitHub Actions** and **pytest**. This configuration automates software verification, ensures code quality, and guards the codebase from unstable regressions by executing automated test blocks before code integration.

---

## 🚀 Project Architecture & Setup

### 1. File Structure
The project repository contains the following core components:
*   `student.py`: Contains the core application logic and data models for managing and querying student profiles.
*   `test_student.py`: A comprehensive test suite containing modular unit tests executed via `pytest`.
*   `requirements.txt`: Defines external dependencies required for the execution environment.
*   `.github/workflows/python.yml`: Configuration file driving the automated GitHub Actions runner environment.

### 2. CI/CD Workflow Configuration (`python.yml`)
The pipeline runs on an isolated Ubuntu environment every time code is pushed or a pull request is created. Here is the final robust workflow architecture:

```yaml
name: Student System CI

on:
  push:
    branches: [ "main", "feature-student-search" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository code
      uses: actions/checkout@v4

    - name: Set up Python 3.10
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install pytest
        if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi

    - name: Run validation tests with pytest
      run: |
        python -m pytest
```

---

## 🛠️ Git Commands Reference

Below are the exact Git commands utilized to manage the feature branch lifecycle, stage updates, track adjustments, resolve directory bugs, and synchronize local code blocks with the upstream remote repository:

### 1. Branch Management
Switch to or isolate a local development workspace:
```bash
git checkout feature-student-search
```

### 2. Local Cleanup
Remove accidental duplicate un-tracked folders without structural metadata:
```bash
rm -rf github/
```

### 3. Staging and Committing Changes
Stage all modified layers and apply descriptive, message-oriented check-ins:
```bash
# Stage all updated files
git add .

# Commit changes with targeted notes
git commit -m "Fix: Explicitly install pytest via python -m pip in CI workflow"
```

### 4. Code Synchronization
Push local commits securely up to the GitHub cloud:
```bash
git push origin feature-student-search
```

---

## 🔄 Pipeline Workflow Lifecycle

The CI workflow implements a complete validation, inspection, and integration path consisting of four major operational phases:

### Phase 1: Feature Isolation & Successful Build
Development takes place on `feature-student-search`. When pushed, GitHub Actions instantly provisions a cloud node, installs required dependencies via `pip`, and runs tests. All unit tests successfully complete, registering a **Green Status Checkmark**.

### Phase 2: Pull Request Verification
A formal code verification request is established by mapping a Pull Request (PR) tracking `feature-student-search` $\leftarrow$ `main`. This allows reviewers to audit performance parameters prior to merging code blocks.

### Phase 3: Defensive Bug Interception (Failing State)
To validate pipeline defense mechanisms, a logical error is intentionally injected into the core querying functionality (`student.py`), returning an invalid string structure. Upon pushing, the automated suite runs, isolates the test regressions, stops execution gracefully, and drops an explicit **Red Cross Failure Alert (Exit Code 1)**, successfully blocking the broken build.

### Phase 4: Resolution & Final Integration
The core application logic is immediately restored to baseline, verified locally, and pushed. The pipeline automatically evaluates the updated codebase, returns to a **Passing Green State**, and allows the administrator to safely click **Merge Pull Request**, perfectly synchronizing the feature additions back into production (`main`).
