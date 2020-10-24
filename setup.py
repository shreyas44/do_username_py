from setuptools import setup

setup(
  name = "do_username",
  version = "1.0.0",
  packages = ["do_username"],
  license = "MIT",
  author = "Shreyas",
  author_email = "shreyas.sreenivasa@gmail.com",
  url = "https://github.com/shreyas44/do_username_py",
  entry_points= {
    "console_scripts": [
      "do_username = do_username.__main__:main"
    ]
  }
)
