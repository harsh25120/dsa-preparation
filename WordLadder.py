from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}

        while level and endWord not in parents:
            nextLevel = defaultdict(list)

            for word in level:
                if word in wordSet:
                    wordSet.remove(word)

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i + 1:]

                        if newWord in wordSet:
                            nextLevel[newWord].append(word)

            level = nextLevel.keys()

            for word, prevs in nextLevel.items():
                parents[word].extend(prevs)

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        if endWord in parents:
            dfs(endWord, [endWord])

        return res