import unittest

class TestNormalizeCompanyName(unittest.TestCase):

    def test_softsol_lowercase(self):
        self.assertEqual(
            normalize_company_name("CAF softsol"),
            "CAF SoftSol Pvt Ltd."
        )

    def test_solution_format(self):
        self.assertEqual(
            normalize_company_name("CAF solution"),
            "CAF SoftSol Pvt Ltd."
        )

    def test_full_company_name(self):
        self.assertEqual(
            normalize_company_name("CAF softSolution IndiaPvt Limited"),
            "CAF SoftSol India Pvt Ltd."
        )

    def test_empty_string(self):
        self.assertEqual(
            normalize_company_name(""),
            "Company Name Not Available"
        )

    def test_none_value(self):
        self.assertEqual(
            normalize_company_name(None),
            "Company Name Not Available"
        )


if __name__ == "__main__":
    unittest.main()
