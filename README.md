[![GitHub Actions saucedemo](https://github.com/ivanovajulika/RedRover/actions/workflows/action.yml/badge.svg)](https://github.com/Elvorob/Saucedemo/actions)
# ***SAUCEDEMO***

[Click Website](https://www.saucedemo.com/) 


[<img src="https://www.saucedemo.com/static/media/Login_Bot_graphic.20658452.png" width="140" height="140">](https://www.saucedemo.com/)
- [Как работать с репозиторием?](#some-inst)
- [Pytest inf](#some-pytest)
- [Poetry](#some-poetry)
- [Python html report](#some-html)
- [Allure](#some-allure)
- [Creat Allure single HTML file builder](#some-allure-html-file)


# **Как работать с репозиторием?:** <a name="some-inst"></a>
<img src="https://www.press-store.net/_pu/0/29765718.jpg" width="60" height="60"> 

[Ссылка на инструкцию](https://docs.google.com/document/d/1-eqVnOTsdPmREaV7frzYSc0VGnU-3FhHAfutOBCzdCw/edit?usp=sharing)

# Pytest INFO:<a name="some-pytest"></a>

> ***Do not forget check your tests with black and flake8 befor pushing***

### **pytest flags**
    -s - prints desired output (pytest -s test_file_name)
    
    -v - shows test process' percentage (pytest -v test_file_name)
    
    -m - allows to run tests with specific marks (pytest -m mark_title test_file_name)

### **pytest-xdist**

##### *Запускает несколько тестов одновременно* 

    pytest -n auto OR pytest -n 5( any number)

# POETRY<a name="some-poetry"></a> 
#### WEB с дополнительной информацией &middot;[![poetry](https://img.shields.io/badge/poetry-website-brightgreen.svg?style=flat-square)](https://python-poetry.org/docs/)
  
### *Running all tests in the project with poetry:*
  
    poetry run pytest 
  
### *Running test by name with poetry:*
  
    poetry run pytest test_name.py 
  
### *Shou setups and PASSED/FAILED^*
  
    poetry run pytest test_name.py --setup-show -sv 
   
# PYTHON_HTML_REPORT <a name="some-html"></a>
#### WEB с дополнительной информацией &middot;[![pytest-html](https://img.shields.io/badge/pyhtml-website-brightgreen.svg?style=flat-square)](https://pytest-html.readthedocs.io/en/latest/user_guide.html)

### *How add python-html reports*:
  
    poetry add pytest -html

### ***Start:***
  
    poetry run pytest Tests/test_name.py --html=report/report.html --self-contained-html
    
### right click to file > open in browser or in finder  
### report.html - the name of the file, it can be anything  

# ALLURE <a name="some-allure"></a>
#### WEB с дополнительной информацией &middot;[![WEB-SITE](https://img.shields.io/badge/allure-website-brightgreen.svg?style=flat-square)](https://docs.qameta.io/allure/#_pytest)
  
### ***Create allure:***
  
###### Создаст отчет по всем тестам:
  
    pytest --alluredir=/allure
  
###### Создаст отчет по  указанному тесту:
  
    pytest имя теста --alluredir=/allure
  
### ***Create report html:***
     
    allure serve
    
-exmpl(allure serve <C:\allure>)
  
### ***Creating a report from an existing one allure:***
  
    allure generate <директория где лежит отчет>
  
-exmpl (allure generate C:\allure)
  
# Creat Allure single HTML file builder<a name="some-allure-html-file"></a>
-создает файл `complete.html`
  
    allure-combine ./allure-report
  
-delete  `sinon.js` и `server.js`
  
### ***Open allure report:***
  
    allure open <directory>  

### ***Clean allure report:***
  
    allure report clean 

### ***Change directory:***

    allure generate old directory-o new directory
