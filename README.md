# Pylint

### USAGE
    pylint source.py
#### Get Errors & Warnings
    pylint -rn source.py
#### To Get Errors
    pylint -E source.py
#### To Disable Warning
    pylint -rn -d unused-variable source.py
    >> pylint -d missing-docstring example\ex3_fail.py
    or
    pylint -rn -d W06012 source.py
    >> pylint -d C0111 -d C0103 example\ex3_fail.py
#### To Use Configuration File
1. pylintrc in the current working directory
2. .pylintrc in the current working directory
3. The file named by environment variable PYLINTRC
4. if you have a home directory which isn’t /root:
    1. .pylintrc in your home directory
    2. .config/pylintrc in your home directory
5. /etc/pylintrc

##### Auto generation
    pylint --generate-rcfile > ~/.pylintrc

### Pylint Git-hook
#### Setup
    pip install git-pylint-commit-hook
#### Git-hook
    # project_root/.git/hooks/pre-commit
    # #!/usr/bin/env bash
    git-pylint-commit-hook
#### Config
- Settings are loaded by default from the .pylintrc file in the root of your repo.
```
[pre-commit-hook]
command=custom_pylint
params=--rcfile=/path/to/another/pylint.rc
limit=8.0
```
    
    
*참조
 - [Pylint 1.6.0 docs](https://docs.pylint.org/en/1.6.0/run.html)
 - [Pylint pdf](https://buildmedia.readthedocs.org/media/pdf/pylint/latest/pylint.pdf)


# Flake8
### USAGE
    flake8 [options] directory|file
### IGNORE
    flake8 --ignore E24,W504 directory|file
### SELECT
    flake8 --select E123,W503 directory|file
### Config
    project_root에서 setup.cfg, tox.ini, .flake8 파일을 사용할수있다.
    
```
[flake8]

ignore = E501, E402, E261

exclude = .git, __pycache__

count = True
```

### Githook
- 커밋 전에 실행되는 pre-commit에서 Lint 하는 작업
    ```
    flake8 --install-hook git
    ```
- 위 명령어를 통해 자동으로 pre-commit 설정을 할수있다.
#### 설정
- strict
```
Lint의 결과에 에러메세지가 하나라도있으면, 커밋 취소 (default false)
git config --bool flake8.strict true
```
- lazy
```
index에 올라간 코드만 검사. (default false)
git config --bool flake8.lazy true
```
*참조
- [Flake8 Github](https://github.com/PyCQA/flake8)
- [Flake8 설명 blog](https://tech.songyunseop.com/post/2017/05/lint-with-flake8/)

# Coverage
## Usage
    coverage <command> [options] [args]
    
### Commands
    annotate    적용 결과로 소스파일에 주석을 작성.
    combine     다른 머신이나 프로세스와 결합할 수 있음.
    erase       이전 결과값 삭제
    help        Get help on using coverage.py.
    html        Create an HTML report.
    report      Report coverage stats on modules.
    run         Run a Python program and measure code execution.
    xml         Create an XML report of coverage results.

### 예제
    coverage run source.py
    coverage report (-m)
    coverage html
    coverage xml
    