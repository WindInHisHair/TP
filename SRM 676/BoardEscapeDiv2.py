# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BoardEscapeDiv2:
    def testPos(self, s, i,j, c):
        if i >= 0 and i < len(s) and j >=0 and j < len(s[0]):
            if s[i][j] == c:
                return True
            else:
                return False
        else:
            return False

    def canMove(self, s, i,j):

        if i <0 or j < 0 or i >= len(s) or j >= len(s[0]):
            return False
        else:
            if s[i][j] == '#':
                return False
            else:
                return True


    def findWinner(self, s, k):
        
        foundT= False
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == 'T':

                    if self.testPos(s, i+1,j, 'E') or self.testPos(s, i-1, j, 'E') or self.testPos(s, i,j+1, 'E') or self.testPos(s, i, j-1, 'E'):
                        return 'Alice'

                    if not(self.canMove(s, i+1,j) or self.canMove(s, i-1, j) or self.canMove(s, i, j+1) or self.canMove(s, i, j-1)):
                        return 'Bob'

                    foundT = True
                    break

            if foundT:
                break

        if k %2 == 0:
            return 'Bob'
        else:
            return 'Alice'



# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(s, k, __expected):
    startTime = time.time()
    instance = BoardEscapeDiv2()
    exception = None
    try:
        __result = instance.findWinner(s, k);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("BoardEscapeDiv2 (550 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BoardEscapeDiv2.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            s = []
            for i in range(0, int(f.readline())):
                s.append(f.readline().rstrip())
            s = tuple(s)
            k = int(f.readline().rstrip())
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(s, k, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1450455756
    PT, TT = (T / 60.0, 75.0)
    points = 550 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
