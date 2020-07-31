# Solution

class FirstUnique:

    def __init__(self, nums: List[int]):
        # Initialize a dict which remembers the order in which items are added
        self.uniques = {}
        # Initialize a 'duplicates' set to remember and quickly check if a number is unique
        self.duplicates = set()
        
        # Populate the 'uniques' dict and 'duplicates' set with the initialization values 
        for num in nums:
            if num in self.duplicates:
                if num in self.uniques:
                    del self.uniques[num]
            else:
                self.uniques[num] = 0
                self.duplicates.add(num)
                

    def showFirstUnique(self) -> int:
        # Return the first key in the 'uniques' dict such a value exists, otherwise -1
        return next(iter(self.uniques.keys())) if self.uniques else -1

    
    def add(self, value: int) -> None:
        # If we have already added the value, we will remove it from the uniques dict
        if value in self.duplicates:
            if value in self.uniques:
                del self.uniques[value]
        # If the value has not been added before, we add it to 'uniques' and 'duplicates'
        else:
            self.uniques[value] = 0
            self.duplicates.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
