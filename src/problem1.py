"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and ruoqing.  April 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# DONE: 2.  READ the code of the  Rect  class below.
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement at least 2 tests of the  problem1  function.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    # Test 1:
    print('Test 1:')
    print('  Testing the return value:')
    rectangles = [Rect(5, 4), Rect(3, 5), Rect(7, 9)]
    expected = 20 + 15 + 63
    actual = problem1(rectangles)
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print()

    # Test 2:
    print('Test 2:')
    print('  Testing the return value:')
    rectangles = [Rect(8, 4), Rect(6, 5), Rect(7, 4)]
    expected = 32 + 30 + 28
    actual = problem1(rectangles)
    print("    Expected:", expected)
    print("    Actual:  ", actual)
    print()


def problem1(rectangles):
    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    area = 0
    for k in range(len(rectangles)):
        area = area + rectangles[k].w * rectangles[k].h
    return area

    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()