python setup.py nosetests --with-xunit --with-coverage --cover-package rpn --cover-erase --cover-xml --cover-branch --cover-html
pip install pylint
pylint -f parseable -d I0011,R0801 rpn | tee pylint.out
