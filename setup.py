import setuptools
from pip._internal.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.requirement) for ir in install_reqs]

setuptools.setup(
    name="AVIP-spring-2021",
    version="0.0.1",
    author="Lev Marder",
    author_email="asertolpas@gmail.com",
    description="A small example package",
    package_dir={"": "."},
    install_requires=reqs,
    python_requires=">=3.9",
)
