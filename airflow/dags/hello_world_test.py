import unittest
from airflow.operators.python_operator import PythonOperator


class TestStringMethods(unittest.TestCase):
    def test_python_operator():
        test = PythonOperator(test_id="test", python_callable=lambda: "testme")
        result = test.execute(context={})
        assert result == "testme"
if __name__ == '__main__':
    unittest.main()
