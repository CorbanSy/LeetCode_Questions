class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            {},
            {'blank': 1, 'sign': 2, 'digit': 3, 'dot': 4},
            {'digit': 3, 'dot': 4},
            {'digit': 3, 'dot': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}
        ]
        
        current_state = 1
        for char in s:
            if char == ' ':
                char_type = 'blank'
            elif char in ['+', '-']:
                char_type = 'sign'
            elif char in '0123456789':
                char_type = 'digit'
            elif char == '.':
                char_type = 'dot'
            elif char in ['e', 'E']:
                char_type = 'e'
            else:
                return False
            
            if char_type not in state[current_state]:
                return False
            current_state = state[current_state][char_type]
        
        if current_state in [3, 5, 8, 9]:
            return True
        return False