from typing import List
class Solution:
    ## my solution
    # using for loop and list append
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies) - extraCandies
        li = []
        for i in range(len(candies)):
            if candies[i] >= limit:
                li.append(True)
            else:
                li.append(False)

        return li

        #other solution
    def otherSolution(self, candies: List[int], extraCandies: int) -> List[bool]:
        limit = max(candies)-extraCandies
        return ([ True if candy >= limit else False for candy in candies])


    def ohterKidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy+extraCandies >= maxCandies for candy in candies]

    # it is important making code readable and checking time and space complexity
    #
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high_enough = max(candies) - extraCandies
        result = []
        for num in candies:
            if num >= high_enough:
                result.append(num)
        return result
