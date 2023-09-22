class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = abs(x)
        return int(math.sqrt(x))