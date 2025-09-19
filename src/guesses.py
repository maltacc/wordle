# class for assigning guesses 
from colors import Color
from collections import defaultdict

def validateGuess(guess: str, word: str) -> list[str]: 
    # have a map of letter -> set(indices)
    # if a letter in guess doesn't exist in the word, assign it to be grey
    # if a letter is used multiple times, match both instances by removing the 
    # correctly matched idx each time
    n = len(word)
    mp = defaultdict(set)

    # build char to index map
    for i in range(n): 
        mp[word[i]].add(i)

    colors = [Color.GREY] * n
    for i in range(n): 
        if guess[i] == word[i]: 
            colors[i] = Color.GREEN
            mp[word[i]].remove(i)
        elif guess[i] in mp:
            colors[i] = Color.YELLOW
    
    return colors

if __name__ == "__main__":
    print(validateGuess("apple", "allee"))
    # should return [GREEN, GREY, GREY, YELLOW, GREEN]
    print(validateGuess("BEARY", "ABBEY"))
    # should return [YELLOW, YELLOW, YELLOW, GREY, GREEN]