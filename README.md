# 📊 Data Engineering Tutorials

Welcome to the **Data Engineering Tutorials** repository! This collection provides practical, hands-on examples focusing on **Data Orchestration** using Apache Airflow and **Data Processing/Machine Learning** using PySpark.

This repository is designed for data engineers, data scientists, and developers looking to master the fundamentals of building robust data pipelines.

---

## 🛠️ Technology Stack

| Category | Technology | Files Included | Purpose |
| :--- | :--- | :--- | :--- |
| **Orchestration** | **Apache Airflow** | `dag_*.py`, `our_first_dag.py`, `create_dag_python_operator.py` | Building, scheduling, and managing data workflows (DAGs). |
| **Data Processing/ML** | **PySpark, MLlib** | `tutorial.ipynb`, `test.csv` | Hands-on data manipulation, transformation, and building a linear regression model. |
| **Dependencies** | **Python, pip** | `requirements.txt` | Defines all necessary Python packages and specific versions. |
| **Database** | **PostgreSQL** | `dag_with_postgres_operator.py` | Demonstrates integration with a PostgreSQL database. |

---

## 🧭 Airflow DAG Examples (Orchestration)

The following Directed Acyclic Graphs (DAGs) illustrate various core concepts in Apache Airflow:

| File Name | Concept Demonstrated | Key Features |
| :--- | :--- | :--- |
| `our_first_dag.py` | **Basic Workflow & Dependencies** | Defines a simple DAG with three BashOperators and demonstrates setting task dependencies (`task1 >> [task2, task3]`). |
| `create_dag_python_operator.py` | **Python Operator & XComs** | Uses the `PythonOperator` to execute custom Python logic and showcases **XComs** for passing data (first name, last name, age) between tasks. |
| `dag_with_task_flow_api.py` | **TaskFlow API (Decorators)** | Illustrates the modern, simplified way to define tasks and dependencies using the `@dag` and `@task` decorators, which implicitly handles XComs. |
| `dag_with_cron_expression.py` | **Custom Scheduling** | Schedules a DAG using a specific **Cron expression** (`0 3 * * Tue`) to run every Tuesday at 3:00 AM. |
| `dag_with_catchup_and_backfill.py` | **Catchup and Backfill** | Demonstrates the `catchup=False` parameter to prevent Airflow from running missed scheduled intervals upon initial deployment. |
| `dag_with_postgres_operator.py` | **Database Integration** | Uses the `SQLExecuteQueryOperator` (a common SQL operator) to perform DDL/DML operations (CREATE, INSERT, DELETE) against a PostgreSQL connection (`postgres_localhost`). |
| `dag_with_python_dependencies.py` | **External Dependencies** | Shows how to ensure external Python libraries (specifically **scikit-learn**) are available within a task environment. |

---

## 🔢 PySpark and ML Tutorial

* **`tutorial.ipynb`**: This Jupyter Notebook contains a hands-on tutorial for data analysis and machine learning using **PySpark**. It covers setting up a Spark Session, preparing data, performing **feature vectorization**, and training a **Linear Regression** model using PySpark's MLlib package.
* **`test.csv`**: This CSV file contains sample employee data (`name`, `age`, `experience`, `department`, `salary`) used as the dataset within the `tutorial.ipynb` notebook.

---

## ⚙️ Setup and Installation

To run these tutorials, you'll need Python, pip, and access to an Airflow environment and/or a Jupyter environment with PySpark installed.

### Prerequisites

1.  **Python 3.x**
2.  **Apache Airflow** (for running the DAGs)
3.  **Docker/Virtual Environment** (recommended for dependency isolation)

### 1. Install Dependencies

Install the required Python packages defined in the `requirements.txt` file:

```bash
# custom_requirements.txt content includes:
# scikit-learn==1.7.2
# matplotlib==3.8.4
# SQLAlchemy<2.0 (Note: This specific downgrade is often needed for compatibility with older Airflow/FAB configurations)

pip install -r requirements.txt
```
__

## 🧑‍💻 Author
**Rushil Shah**  
📫 [LinkedIn](https://linkedin.com/in/rushilshahh)
💼 Portfolio
