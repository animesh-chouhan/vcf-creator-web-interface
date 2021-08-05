#!/bin/sh
pipenv shell
pipenv uninstall vcf_creator
pipenv install vcf_creator

# Update requirements.txt
pip freeze > requirements.txt