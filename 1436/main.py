class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict(paths)
        start = paths[0][0]
        while True:
            next = d.get(start)
            if next:
                start = next
            else:
                return start  