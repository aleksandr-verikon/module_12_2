from run_and_tur import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    def tearDown(self):
        pass

    def test_beg1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        finishers = tournament.start()
        TournamentTest.all_results[1] = finishers
        self.assertTrue(finishers[2].name == "Ник")  # Исправлено на 1 место

    def test_beg2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        finishers = tournament.start()
        TournamentTest.all_results[2] = finishers
        self.assertTrue(finishers[2].name == "Ник")

    def test_beg3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        TournamentTest.all_results[3] = finishers
        self.assertTrue(finishers[3].name == "Ник")


if __name__ == "__main__":
    unittest.main()

