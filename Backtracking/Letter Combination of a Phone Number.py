class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappingList = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        outputDict = {}

        for digit in digits:
            currentLetters = mappingList[digit]

            # if outputDict is empty, we need to first put in 1 empty combi
            if not outputDict:
                outputDict = {""}

            newOutputDict = {}
            for combi in outputDict:
                # For each combination in the outputDict (ad, be, cf)
                for letter in currentLetters:
                    newCombi = (
                        combi + letter
                    )  # We merge the new letter (adp, adq, adr, ads)
                    newOutputDict[newCombi] = True

            outputDict = newOutputDict

        # Change it to an array
        outputArray = []
        for combi in outputDict:
            outputArray.append(combi)

        return outputArray
