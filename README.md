# selenium-pytest

This is simple project to showcase how to write automation test case with pytest, Selenium WebDriver and WebDriver Manager. I also used
pytest-xdist as parallel execution.

Pre-requisites:
- Have Python > =3.9
- Have pip3 >= 21.0
- Have pipenv >= 9.0


Setup:
- Run: pipenv install to install dependencies
- Run: pipenv run python -m pytest to run all tests in sequence.
- Run: pipenv run python -m pytest -n 3 to run the test in parallel with 3 threads.


Other things to be improved:
- HTML report
