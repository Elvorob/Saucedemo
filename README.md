# Saucedemo
Сайт https://www.saucedemo.com/

Инструкция как работать с репозиторием:
https://docs.google.com/document/d/1-eqVnOTsdPmREaV7frzYSc0VGnU-3FhHAfutOBCzdCw/edit?usp=sharing

*Do not forget check your tests with black and flake8 befor pushing*

**pytest flags**
- -s - prints desired output (pytest -s test_file_name)
- -v - shows test process' percentage (pytest -v test_file_name)
- -m - allows to run tests with specific marks (pytest -m mark_title test_file_name)

**pytest-xdist**

Запускает несколько тестов одновременно //  
pytest -n auto OR pytest -n 5( any number)


**pytest-html**

pytest <name of test> --html=report/report.html --self-contained-html //  
right click to file > open in browser or in finder //  
report.html - the name of the file, it can be anything //  

**Poetry**
  
  - poetry run pytest (running all tests in the project with poetry)
  - poetry run pytest test_name.py (running test by name with poetry)
  - poetry run pytest test_name.py --setup-show -sv (shou setups and PASSED/FAILED)
