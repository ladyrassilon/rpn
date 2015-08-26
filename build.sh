pip install pylint pep8 nose
pep8 rpn tests > pep8_report.txt
python setup.py nosetests --with-xunit --with-coverage --cover-package rpn --cover-erase --cover-xml --cover-branch --cover-html
pylint -f parseable -d I0011,R0801 rpn | tee pylint.out
