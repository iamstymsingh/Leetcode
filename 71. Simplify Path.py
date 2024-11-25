class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        if not path:
            return "/"
            
        for piece in path.split('/'):
            if piece == '.' or piece == '':
                continue
            elif piece == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(piece)

        canonical_path = ""
        while stack:
            canonical_path = "/" + stack.pop() + canonical_path
        return canonical_path if canonical_path else '/'