import sqlite3
from datetime import datetime


class Storage:
    def __init__(self, db_path="pythonflow.db"):
        self.db_path = db_path
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS task_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dag_name TEXT NOT NULL,
                    task_name TEXT NOT NULL,
                    state TEXT NOT NULL,
                    attempt INTEGER NOT NULL,
                    error TEXT,
                    created_at TEXT NOT NULL
                )
                """
            )

    def record_task_run(
        self,
        dag_name,
        task_name,
        state,
        attempt,
        error=None
    ):
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO task_runs (
                    dag_name,
                    task_name,
                    state,
                    attempt,
                    error,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    dag_name,
                    task_name,
                    state,
                    attempt,
                    error,
                    datetime.utcnow().isoformat()
                )
            )

    def get_history(self):
        with self._connect() as conn:
            cursor = conn.execute(
                """
                SELECT dag_name, task_name, state, attempt, error, created_at
                FROM task_runs
                ORDER BY id DESC
                LIMIT 20
                """
            )

            return cursor.fetchall()
