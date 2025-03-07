name: Bug Report
description: Report a bug to help us improve
title: "Bug: "
labels: [bug]

body:
- type: markdown
  attributes:
    value: >
      
        Thank you for opening this issue!

        If you're new to CellGeometry, consider the following options first:

        - reading the CellGeometry documentation: https://bioshapelab.github.io/cellGeometry
        - searching our existing issue tracker for a similar issue (https://github.com/bioshapelab/CellGeometry/issues) to see if
          your problem has already been reported.
    
- type: textarea
  attributes:
    label: Describe the bug
    description: |
      A clear and concise description of the bug.
  validations:
    required: false
- type: textarea
  attributes:
    label: Steps/Code to Reproduce
    description: |
      Describe clearly and concisely the steps to ensure that it can be reproduced and potentially fixed:
        - Any commands you ran
        - What module is affected if you know
        - Include a minimal, reproducible example (https://stackoverflow.com/help/minimal-reproducible-example), if possible.
    placeholder: |
      ```
      Sample code to reproduce the problem
      ```
  validations:
    required: true
- type: textarea
  attributes:
    label: Expected Behaviour
    description: >
      A clear and concise description of what you expected to happen.
    placeholder: >
      Example: No error is thrown.
  validations:
    required: true
- type: textarea
  attributes:
    label: Actual Behaviour
    description: |
      Please paste or describe the results you observe instead of the expected behaviour. 
      If you observe an error, please paste the error message including the **full traceback** of the exception. 
    placeholder: >
      Please paste or specifically describe the actual output or traceback.
  validations:
    required: true
- type: textarea
  attributes:
    label: Your environment
    render: shell
    description: |
      - CellGeometry version tested on:
      - Operating system and architecture:
  validations:
    required: true
- type: markdown
  attributes:
    value: >
      Thanks for contributing 🎉!
