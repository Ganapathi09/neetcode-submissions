class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtract(curr,openC , closeC):
            if len(curr) == 2*n:
                result.append(curr)
                return
            if openC < n:
                backtract(curr + "(" , openC +1,closeC)

            if closeC < openC:
                backtract(curr + ")" , openC ,closeC + 1)   

        backtract("",0,0)
        return result               