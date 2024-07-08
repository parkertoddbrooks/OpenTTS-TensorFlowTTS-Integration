from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="opentts-tensorflowtts-integration",
    version="0.1.0",
    author="Parker Todd Brooks",
    author_email="foo@foo.com",
    description="A library integrating OpenTTS with TensorFlow TTS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parkertoddbrooks/OpenTTS-TensorFlowTTS-Integration",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow>=2.4.0",
        "numpy>=1.19.2",
        "librosa>=0.8.0",
        "soundfile>=0.10.3",
        "tqdm>=4.50.0",
        # Add other dependencies here
    ],
    extras_require={
        "dev": ["pytest", "flake8", "black"],
    },
)
