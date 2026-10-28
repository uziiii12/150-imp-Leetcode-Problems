class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        k = len(s1)

        for right in range(len(s2)):
            window_count[ord(s2[right]) - ord('a')] += 1

            if right >= k:
                window_count[ord(s2[right - k]) - ord('a')] -= 1

            if s1_count == window_count:
                return True

        return False