from setuptools import setup

setup(
  name = "do_username",
  version = "1.0.0",
  packages = ["do_username"],
  entry_points= {
    "console_scripts": [
      "do_username = do_username.__main__:main"
    ]
  }
)
