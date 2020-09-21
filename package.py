
name = "jinja2"

description = "A very fast and expressive template engine."

version = "2.11.2"

requires = [
    "markupsafe-0.23+"
]

variants = []


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
