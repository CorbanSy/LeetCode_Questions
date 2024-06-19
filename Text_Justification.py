class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            # Check if adding the new word exceeds the max width
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line, current_length = [], 0

            current_line.append(word)
            current_length += len(word)

        # Left-justify the last line
        result.append(' '.join(current_line).ljust(maxWidth))

        return result