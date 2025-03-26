from setuptools import find_packages, setup

setup(
    name="pomodoro",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pomodoro=app.run:entrypoint"]},
    install_requires=[req.strip() for req in open("requirements/requirements.txt").readlines()],
)
