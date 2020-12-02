import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="automated_accessibility_testing",  # Replace with your own username
    version="0.0.15",
    author="Romeu Carvalho Antunes",
    author_email="romeu.antunes@outlook.com",
    description="package with the intention of automating accessibility tests for django web development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TCC2-Romeu/Pacote-Pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["beautifulsoup4 ~= 4.9", "py-w3c ~= 0.3", "joblib ~= 0.17"],
    extras_require={"django": ["django ~= 2.2"]},
)
