import unittest

from src.context_loader import load_context


class ContextLoaderTests(unittest.TestCase):
    def test_default_loads_project_and_user_only(self) -> None:
        sources = load_context()
        labels = [label for label, _ in sources]
        self.assertEqual(labels, ["Project memory", "User memory"])

    def test_dynamic_context_is_opt_in(self) -> None:
        sources = load_context(include_dynamic=True)
        labels = [label for label, _ in sources]
        self.assertEqual(
            labels,
            ["Project memory", "User memory", "Dynamic task context"],
        )

    def test_project_memory_mentions_no_q_learning_claim(self) -> None:
        sources = dict(load_context())
        self.assertIn("Q-learning is a later task", sources["Project memory"])


if __name__ == "__main__":
    unittest.main()
