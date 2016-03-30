#!/bin/bash
wget https://github.com/sympy/sympy/releases/download/sympy-1.0/sympy-1.0.tar.gz
tar -xvzf sympy-1.0.tar.gz
cd sympy-1.0/
python setup.py develop
cd ../
pip install pylint pep8 nose
pep8 rpn tests > pep8_report.txt
python setup.py nosetests --with-xunit --with-coverage --cover-package rpn --cover-erase --cover-xml --cover-branch --cover-html
pylint -f parseable -d I0011,R0801 rpn | tee pylint.out
rm -rf sympy-1.0
rm sympy-1.0.tar.gz