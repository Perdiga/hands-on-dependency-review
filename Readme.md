# Hands-On Dependency Review

This hands-on guide will help you understand how the Dependency Review action works. You'll begin by forking this repository to your own GitHub account, and then implement and test the action.

**Note:** Ensure that GitHub Actions is enabled for your forked repository.

## Steps

### Step 1: Fork the Repository

1. Click the "Fork" button at the top-right corner of this page to create a copy of this repository under your own GitHub account.

### Step 2: Add the Dependency Review Action to Your Forked Repository

1. Navigate to the `Actions` tab in your forked repository.
2. Search for "Dependency Review Action."
3. Locate the workflow managed by `GitHub Actions` and click on `Configure`. This will open the GitHub editor with the `Dependency Review` workflow.
4. Uncomment the `fail-on-severity` line to activate this feature.
5. Commit the changes directly to the `main` branch of your fork.

### Step 3: Test the Dependency Review

1. Create a new branch from `main` in your forked repository.
2. Locate and open the `requirements.txt` file.
3. Change the version of the `requests` library to `2.19.1`.
4. Commit the changes to the new branch.
5. Open a pull request (PR) to merge this branch into `main`.

### Step 4: Expected Results

- The Dependency Review action will automatically run and check your project's dependencies.
- The PR should fail due to a known vulnerability in the `requests` dependency version `2.19.1`.

## Conclusion

By using the Dependency Review action, you can automatically detect vulnerabilities and license issues in your project dependencies before merging them into the production branch. This practice helps maintain code quality and ensures security compliance.
