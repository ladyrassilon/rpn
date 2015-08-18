from setuptools import setup

with open("README.rst") as readme_file:
    long_description = readme_file.read()


setup(name="RPyN",
    version="0.1",
    packages=["rpn",],
    license="GNU GPL v3.0",
    description="Evaluates a given Reverse Polish Notation",
    author="Gemma Hentsch",
    author_email="contact@halfapenguin.com",
    install_requires=[
        
    ],
    test_requires=[
        "mock(>=1.0.1)", 
        "coverage(>=3.7.1)",
        "nose(>=1.3.4)",
    ],
    long_description=long_description,
    test_suite="nose.collector",
    url="https://github.com/zooeysoftware/rpn",
    keywords = ["rpn", "math", "formula"],
    download_url="https://github.com/zooeysoftware/rpn/archive/",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ]
)