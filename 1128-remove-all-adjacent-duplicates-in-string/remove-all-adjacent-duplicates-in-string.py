
class Solution:
    def removeDuplicates(self, s: str) -> str:

        n = len(s)
        st = []

        for i in range(n):

            if not st:
                st.append(s[i])
                continue

            if st[-1] == s[i]:
                st.pop()
                continue

            st.append(s[i])

        return "".join(st)