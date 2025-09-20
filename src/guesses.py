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
    
    # edge case: multiple instance of a letter are in guess but fewer 
    # instances are in word. Soln: do two passes of marking to remove 
    # correct guesses first, then for each character correctly guessed but not 
    # in the right position, decrement the count 
    
    # First pass: mark all exact matches (GREEN) and remove them from available letters
    for i in range(n): 
        if guess[i] == word[i]: 
            colors[i] = Color.GREEN
            mp[word[i]].remove(i)
    
    # Second pass: mark misplaced letters (YELLOW) only if they're still available
    for i in range(n):
        if colors[i] == Color.GREY and guess[i] in mp and len(mp[guess[i]]) > 0:
            colors[i] = Color.YELLOW
            # Remove one instance of this letter from available letters
            mp[guess[i]].pop()
    
    return colors

if __name__ == "__main__":
    for i in range(6): 
        guess = input("Enter your guess with no spaces: ")
        if len(guess) != 5: 
            print("Guess must be 5 letters long")
            continue
        print(validateGuess(guess.upper(), "LATER"))
        
    # print(validateGuess("apple", "allee"))
    # # should return [GREEN, GREY, GREY, YELLOW, GREEN]
    # print(validateGuess("BEARY", "ABBEY"))
    # # should return [YELLOW, YELLOW, YELLOW, GREY, GREEN]
    print(validateGuess("TESTS", "LATER"))