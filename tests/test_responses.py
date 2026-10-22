import unittest

import project2


class MatchingTests(unittest.TestCase):
    def test_does_not_match_substrings(self):
        # "this" contains "hi" but must not trigger the greeting.
        self.assertEqual(project2.get_response("what is this"), project2.FALLBACK)

    def test_matches_whole_phrase(self):
        self.assertEqual(project2.get_response("hello"), project2.RESPONSES["hello"])

    def test_longest_phrase_wins(self):
        self.assertEqual(
            project2.get_response("how are you doing"),
            project2.RESPONSES["how are you"],
        )

    def test_negation_beats_sentiment(self):
        self.assertEqual(
            project2.get_response("I am not happy"),
            project2.RESPONSES["not happy"],
        )

    def test_empty_input_falls_back(self):
        self.assertEqual(project2.get_response("   "), project2.FALLBACK)

    def test_greeting_boundaries(self):
        self.assertEqual(project2.greeting_for_hour(0), "Good Morning")
        self.assertEqual(project2.greeting_for_hour(12), "Good Afternoon")
        self.assertEqual(project2.greeting_for_hour(18), "Good Evening")


if __name__ == "__main__":
    unittest.main()
