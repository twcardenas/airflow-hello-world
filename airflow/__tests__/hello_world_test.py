import unittest
from airflow.models import DagBag
from airflow.operators.python_operator import PythonOperator


class TestHelloWorld(unittest.TestCase):
    def test_python_operator(self):
        dag_bag = DagBag(include_examples=False)
        assert not dag_bag.import_errors
        assert not dag_bag.dags

        for dag_id, dag in dag_bag.dags.items():
            assert dags.tags

        dag = dag_bag.get_dag(dag_id='exampleShouldFail')
        assert len(dag_bag.import_errors) == 0, "No Import Failures"
        assert dag is not None
    def test_python_operator(self):
        test = PythonOperator(task_id="test", python_callable=lambda: "testme")
        result = test.execute(context={})
        assert result == "testme"
if __name__ == '__main__':
    unittest.main()
