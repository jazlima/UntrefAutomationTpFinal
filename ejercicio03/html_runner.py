import unittest
from HtmlTestRunner import HTMLTestRunner

test_suite = unittest.TestLoader().discover('tests')
runner = HTMLTestRunner(output='test-reports', report_title='Pruebas de Saucelab', combine_reports = True)
try:
    runner.run(test_suite)
except:
    print('Falta algo')