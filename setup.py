
import setuptools

def load_requirements():
    try:
        with open("requirements.txt") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("WARNING: requirements.txt not found")
        return []
    
setuptools.setup(
    name="BSMhighPT2023",
    version="1.0",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=load_requirements(),
    include_package_data=True
)
