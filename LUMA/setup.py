from setuptools import setup, find_packages

setup(
    name="luma-lang",
    version="0.1.0",
    author="TuNombre",
    description="LUMA: Lenguaje de programación cognitivo-emocional",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    python_requires=">=3.9",
    packages=find_packages(include=['luma', 'luma.*']),
    install_requires=[
        "lark-parser>=1.1.2",
        "sexpdata>=0.0.3",
        "typing-extensions>=4.0.0"
    ],
    extras_require={
        'dev': [
            "pytest>=7.0",
            "mypy>=0.910",
            "black>=21.0"
        ],
        'debug': [
            "ipython>=8.0",
            "rich>=10.0"
        ],
        'profile': [
            "pyinstrument>=3.0"
        ],
        'speed': [
            "mypyc>=0.9"
        ]
    },
    entry_points={
        'console_scripts': [
            'luma=luma.cli.main:app',
            'luma-parse=luma_parser.cli:main'
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    project_urls={
        "Source": "https://github.com/tuusuario/luma-lang",
    }
)