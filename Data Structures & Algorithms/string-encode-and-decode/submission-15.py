class Solution:

    def encode(self, strs: List[str]) -> str:

        return "/".join(strs) if len(strs) != 0 else None

    def decode(self, s: str) -> List[str]:

        if s != None:
            return s.split("/")
        else:
            return []