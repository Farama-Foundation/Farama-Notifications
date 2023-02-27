import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Farama-Notifications",
    version="0.0.4",
    author="Jordan Terry",
    author_email="Jkterry@farama.org",
    description="Notifications for all Farama Foundation maintained libraries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Farama-Foundation/Farama-Notifications",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["farama_notifications"],
)
