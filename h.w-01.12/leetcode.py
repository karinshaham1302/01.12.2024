# You are given a large integer represented as an integer array digits, where each digits[i]
# is the ith digit of the integer. The digits are ordered from most significant to least
# significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.


# class Solution:
#    def plusOne(self, digits: List[int]) -> List[int]:


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Given a large integer represented as a list of digits, increments the integer by one.

        This function directly adds 1 to the rightmost digit (least significant digit) of the
        number represented by the list of digits.

        The function assumes that the digits list will not have leading zeros and that the
        digits are all less than 9.

        Param:
        digits (List[int]): A list of digits representing the large integer.

        Returns:
        List[int]: The resulting list of digits after adding one to the integer.
         Example:
        Input: [1, 2, 3]
        Output: [1, 2, 4]

        Input: [4,3,2,1]
        Output: [4,3,2,2]
        """
        digits[-1] += 1
        return digits


result = plusOne([1, 2, 3])
print(result)


# לדעתי הטריק בשאלה הזו זה כשהמספר גדול מ- 9 אך לצערי לא הצלחתי לפתור..
# אודה אם תענה על זה בשיעור
