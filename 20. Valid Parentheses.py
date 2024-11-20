class Solution:
    def isValid(self, s: str) -> bool:
        parans_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        st = []
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in '[({(':
                st.append(char)
            else:
                if not st:
                    return False

                top_ele = st[-1]
                if top_ele != parans_map[char]:
                    return False
                st.pop()
        return True if len(st) == 0 else False
