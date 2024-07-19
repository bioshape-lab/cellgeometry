![Asset 5](https://github.com/bioshape-lab/cells/assets/22850980/344f448f-84a9-4f06-8527-8ddec210fb31)


[![Docker](https://github.com/amilworks/cells/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/amilworks/cells/actions/workflows/docker-publish.yml)[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8322532.svg)](https://doi.org/10.5281/zenodo.8322532)


[[__`CellGeometry App`__]](https://cellgeometry.ece.ucsb.edu)
[[__`Docs`__]](https://geometric-intelligence.github.io/cellgeometry/)

A web-based application for Cell Shape Analysis.




https://github.com/bioshape-lab/cellgeometry/assets/22850980/cc1b4952-7195-4107-b37b-cf8a826e3800



:link: __Table of Contents__
- [Project Description](#-project-description)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 📝 Project Description 

This project focuses on the analysis and comparison of biological cell shapes using elastic metrics implemented in Geomstats. The shapes of biological cells are determined by various processes and biophysical forces, which play a crucial role in cellular functions. By utilizing quantitative measures that reflect cellular morphology, this project aims to leverage large-scale biological cell image data for morphological studies.

The analysis of cell shapes has significant applications in various domains. One notable application is the accurate classification and discrimination of cancer cell lines treated with different drugs. Measures of irregularity and spreading of cells can provide valuable insights for understanding the effects of drug treatments.

## 🎯 Features

- Quantitative analysis and comparison of biological cell shapes using Geomstats.
- Utilization of elastic metrics implemented in Geomstats for shape analysis.
- Calculation of measures reflecting cellular morphology, facilitating in-depth characterization of cell shapes.
- Leveraging large-scale biological cell image data for comprehensive morphological studies.
- Framework for optimal matching, deforming, and comparing cell shapes using geodesics and geodesic distances.
- Visualization of cellular shape variations, aiding in the interpretation and communication of analysis results.
- User-friendly Streamlit app interface for seamless analysis, visualization, and interaction with biological cell data.
- Comprehensive set of tools and methods, empowering researchers and scientists in cellular biology to gain insights and make discoveries.


## ⚙️ Installation

To install and set up the Streamlit app, follow these steps:

1. Clone the repository:

   ```bash
   gh repo clone bioshape-lab/cells
   ```

2. Navigate to the project directory:

   ```bash
   cd cells/cells/streamlit
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source env/bin/activate
     ```

5. Install project dependencies using Poetry:

   ```bash
   poetry install
   ```

   This command reads the `pyproject.toml` file, resolves dependencies, and installs them into the virtual environment.

6. Run the Streamlit app:

   ```bash
   streamlit run Hello.py
   ```

   The Streamlit app should now be running locally. Open your web browser and visit `http://localhost:8501` to access the app.

> __Note:__ Make sure you have Python and Poetry installed on your machine before following these steps. The `pyproject.yaml` file should contain the necessary dependencies and their versions, enabling Poetry to manage the installation process effectively.


## 🚀 Usage

To use the Streamlit app, follow these steps:

1. Make sure you have completed the installation steps mentioned in the [Installation](#-installation) section.

2. Ensure that the virtual environment is activated:

   - For Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source env/bin/activate
     ```

3. Run the Streamlit app:

   ```bash
   streamlit run Hello.py
   ```

4. Once the app is running, it will display a local URL, such as `http://localhost:8501`.

5. Open your web browser and visit the provided URL to access the Streamlit app.

6. Interact with the app's user interface to explore and analyze the biological cell shapes.

7. Customize the parameters, select different options, or upload your own data to observe the impact on the analysis and visualization of cell shapes.

8. View the results and visualizations presented by the app, which may include statistical summaries, plots, or interactive displays.

9. Experiment with different features and functionalities of the app to gain insights into the morphological characteristics of the cells.

10. To stop the app, press `Ctrl+C` in the terminal or command prompt where it is running.


## 🤝 Contributing

We welcome and appreciate contributions to enhance the functionality and features of this Streamlit app. To contribute, please follow these guidelines:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your contribution: `git checkout -b feature/your-feature-name`.
3. Make your changes and ensure that the app is still functioning properly.
4. Commit your changes: `git commit -m "Add your commit message here"`.
5. Push to the branch: `git push origin feature/your-feature-name`.
6. Open a pull request, providing a clear description of your changes and their purpose.
7. Our team will review the pull request and provide feedback and suggestions if needed.
8. Once the pull request is approved, it will be merged into the main branch.

### Guidelines for Contributions

- Follow the coding style and conventions used in the existing codebase.
- Ensure your code is well-documented, with clear comments and explanations where necessary.
- Write unit tests for new features or modifications to ensure the stability of the app.
- Keep your pull requests focused on a specific feature or bug fix to facilitate review.
- Be respectful and considerate towards others when discussing and addressing feedback.

By contributing to this Streamlit app, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

Thank you for considering contributing to this app. Your contributions are highly valued and help improve the overall quality and user experience of the app.

## 📄 License 

This project is licensed under the MIT License - see the LICENSE file for details.

The MIT License is a permissive open-source license that allows you to use, modify, and distribute the code in both commercial and non-commercial projects. It provides you with the freedom to adapt the software to your needs, while also offering some protection against liability. It is one of the most commonly used licenses in the open-source community.

## :raised_hands: Acknowledgments 

This project is extremely grateful for the guidance of Professor Nina Miolane and the members of BioShape lab for their feedback/invaluable discussions.

This project is conducted in the context of the [UCSB Data-Driven Biology (DDB)](https://ddb.bioengineering.ucsb.edu/) program under the grant NSF NRT Award Number: 2125644. This project is partially funded by the NSF CAREER grant 2240158.


## ❓ Frequently Asked Questions

<details>
  <summary>Click to expand/collapse</summary>

### Q1: What is Poetry?

A1: Poetry is a dependency and package management tool for Python projects. It simplifies the management of project dependencies and helps with package installation, versioning, and resolution. It also provides features for creating virtual environments and publishing packages.

### Q2: Why did you choose Poetry for package management?

A2: We chose Poetry for package management because of its robust features and ease of use. Poetry simplifies the process of managing dependencies, ensuring consistent package versions across different environments, and allows for efficient package installation and updates.

### Q3: How do I install Poetry?

A3: To install Poetry, you can follow the official installation instructions provided in the [Poetry documentation](https://python-poetry.org/docs/#installation). It supports different operating systems, including Windows, macOS, and Linux.

### Q4: How do I manage project dependencies with Poetry?

A4: Poetry provides a simple and intuitive way to manage project dependencies. You can define your project's dependencies in the `pyproject.toml` file using the `[tool.poetry.dependencies]` section. Poetry handles dependency resolution and installation automatically when you run `poetry install`. You can also manage additional dependencies such as development and testing packages.

### Q5: Can I use other package managers with Streamlit?

A5: Yes, you can use other package managers like pip or conda with Streamlit. Streamlit is compatible with different package management systems, and you can use your preferred package manager to install and manage dependencies. However, if you're using Poetry for your project, it is recommended to stick with it for consistency and to ensure proper management of dependencies.

### Q6: How do I deploy my Streamlit app with Poetry?

A6: Deploying a Streamlit app with Poetry involves a few steps. First, ensure you have a proper deployment environment set up, such as a cloud-based service or hosting platform. Then, create a deployment configuration file, such as a `Dockerfile`, that includes the necessary instructions to install project dependencies using Poetry. Finally, follow the deployment instructions provided by your hosting platform to deploy your Streamlit app with the required dependencies.

### Q7: How do I update my project dependencies with Poetry?

A7: To update your project dependencies using Poetry, you can run `poetry update` command. This command updates your project's dependencies to their latest compatible versions as specified in the `pyproject.toml` file. Poetry resolves and installs the updated dependencies automatically, ensuring compatibility and consistency.

### Q8: Can I share my Poetry-based Streamlit app with others?

A8: Yes, you can share your Poetry-based Streamlit app with others. Ensure that you include the necessary files, such as the `pyproject.toml` and `poetry.lock`, which contain the dependency information. You can also provide instructions on how to set up and run the app, including the steps to install Poetry and run `poetry install` to install the dependencies.

### Q9: Where can I find more information about Poetry?

A9: You can find more information about Poetry, including detailed documentation and examples, on the official Poetry website: [python-poetry.org](https://python-poetry.org/). The documentation provides in-depth guidance on various aspects of using Poetry for package management.

### Q10: Can I contribute to the project and suggest improvements?

A10: Absolutely! Contributions and suggestions are welcome. Please refer to the [Contributing](#-contributing) section of this README for guidelines on how to contribute to the project. We appreciate your support!

</details>




## Troubleshooting 

Include a troubleshooting section that addresses common issues or errors that users may encounter. Provide solutions or workarounds to help users resolve these problems on their own.

## Related Projects 

If there are related projects or repositories that users may find useful or interesting, list them here with a brief description.


