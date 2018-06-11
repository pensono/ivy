
import unittest
import os.path
from ivy import ivy_module as im
from ivy import ivy_compiler as ic
from ivy import ivy_utils as iu


class TestCompileErrors(unittest.TestCase):
    def test_tokenization_error(self):
        self.error_location_test('tokenization_error.ivy', 2, 10)

    def test_tokenization_error_beginning(self):
        self.error_location_test('tokenization_error_beginning.ivy', 2, 1)

    def test_tokenization_error_end(self):
        self.error_location_test('tokenization_error_end.ivy', 2, 10)

    def test_syntax_error(self):
        self.error_location_test('syntax_error.ivy', 3, 15)

    def test_syntax_error_beginning(self):
        self.error_location_test('syntax_error_beginning.ivy', 3, 1)

    def test_arity_error(self):
        self.error_location_test('arity_error.ivy', 5, 12)

    def test_unknown_symbol(self):
        self.error_location_test('unknown_symbol.ivy', 5, 15)

    def test_tabs(self):
        self.error_location_test('tabs.ivy', 3, 5)

    def error_location_test(self, filename, line, column):
        prog_filename = os.path.join(os.path.dirname(__file__), 'compile_errors', filename)

        def make_assertions(e):
            self.assertEquals(e.source_location.line, line)
            self.assertEquals(e.source_location.column, column)

        with im.Module():
            try:
                ic.ivy_new(prog_filename)
            except iu.ErrorList as e:
                make_assertions(e.errors[0])
                return
            except iu.IvyError as e:
                make_assertions(e)
                return
        self.assertTrue(False)  # No errors, spike the test


if __name__ == '__main__':
    unittest.main()