
#from random import choice
import random
from collections.abc import MutableSet



class TooShortError(ValueError):
        "Raised when the length of the word is too small"
        pass

class TooLongError(ValueError):
        "Raised when the length of the word is too long"
        pass

class NotLettersError(ValueError):
        "Raised when the word has anything other than captial letters A-Z"
        pass

class WordleWords(MutableSet):

        def __init__(self, letters):
                '''To initilize the instances of class wordle words.
                   initializes an empty set of words and the length of each word.
                   Returns:- none.'''
                self._words = set()
                self._letters = letters

        def __contains__(self, word):
                '''To check whether the word is in the self._words.
                   Returns:- True/False.'''
                return word in self._words

        def __iter__(self):
                '''To iterate over words.
                   Returns:- An iterator over words.'''
                return iter(self._words)

        def __len__(self):
                '''Returns:- Number of words in a set.'''
                return len(self._words)

        def add(self, word):
                '''add(self,word)-takes one parameter which is words.
                   Adds each of those words to self._words based on certain conditions.
                   Returns:- None.'''
                self.check_word(word)
                self._words.add(word)
        
        def discard(self, word):
                '''discard(self,word)-takes one parameter which is word.
                   Discards each of those words from self._words.
                   Returns:- None. '''
                self._words.discard(word)


        def load_file(self, filename):
                '''load_file(self,filename) - takes the file to be opened which contains the words.
                   Taking each of those words and adding them into self._words by using add(self,words).
                   Returns:- None.'''
                with open(filename,"r") as fileopen:
                        contents = fileopen.readlines()
                        fileopen.close()
                
                for each_word in contents:
                        each_word = each_word.rstrip()
                        if self._letters == len(each_word):
                                self.add((each_word).upper())

        def check_word(self, word):
                '''check_words(self,word) - takes one parameter which is word.
                   check that word for three conditions mentioned below and based on that add them to self._words.
                   Raises error if word is not according to the condition.
                   Returns:- None'''
                if len(word) < self._letters:
                        raise TooShortError("The word is too short!")
                elif len(word) > self._letters:
                        raise TooLongError("The word is too long!")
                elif not word.isalpha():
                        raise NotLettersError("The word does not contain anything except A-Z!")

                        
        def letters(self):
                '''Returns:- The size of the letters which each words should be'''
                return self._letters
        
        def copy(self):
                '''Returns:- second WorldeWords instance which contains the same words.'''
                copy_words = WordleWords(self._letters)
                copy_words._words = self._words.copy()
                return copy_words._words


class Guess:
        def __init__(self, guess, answer):
                '''To initialize the instances of guess class which is guess and answer
                Returns:- None'''
                self._guess = guess
                self._answer = answer
        
        def guess(self):
                '''guess(self) - takes the players guess
                   Returns:- player guess'''
                return self._guess
        
        def correct(self):
                '''correct(self) - it checks for correct letters in the guess and combines them in a string
                   returns:- a string containing correct letter guesses'''
                b_string = "_"*len(self._answer)
                for index in range(len(self._answer)):
                        if self._guess[index] == self._answer[index]:
                                b_string = b_string[:index] + self._answer[index] + b_string[index+1:]
                return b_string
                        
        def misplaced(self):
                '''misplaced(self) - checks for misplaced letters in self._guess
                   Returns:- a string containing sorted misplaced letters''' 
                # First block removes all elements which are at the right position. 
                length = len(self._answer)
                element_1 = self._guess
                element_2 = self._answer
                for index in range(length):
                        if element_1[index] == element_2[index]:
                                element_1 = element_1[:index]+"_"+element_1[index+1:]
                                element_2 = element_2[:index]+"_"+element_2[index+1:]
                # Second block checks for misplaced elements from the new strings.
                a_string = ""               
                index = 0
                for each_element in  element_1:
                        if (each_element in  element_2) and (each_element != "_"):
                                if (each_element != element_2[index]):
                                        if (element_1.count(each_element) < element_2.count(each_element)):
                                                if each_element not in a_string:
                                                        count = element_1.count(each_element)
                                                        a_string = (each_element*count) + a_string
                                        elif (element_1.count(each_element) > element_2.count(each_element)):
                                                if each_element not in a_string: 
                                                        count = element_2.count(each_element)
                                                        a_string = (each_element*count) + a_string
                                        else:
                                                a_string = each_element + a_string
                        index += 1
                return "".join(sorted(a_string))     

        def wrong(self):
                '''wrong(self) - checks for wrong letters in self._guess
                   Returns:- a string containing sorted wrong letters'''
                a_string = ""
                for each_element in self._guess:
                        if each_element not in self._answer:
                                a_string = each_element + a_string
                        if (each_element not in a_string):  
                                if (each_element in self._answer) and ((self.guess()).count(each_element) > self._answer.count(each_element)):
                                        a_string = each_element + a_string
                return "".join(sorted(a_string))
        
        def is_win(self):
                '''is_win(self) - checks for the conditions where guess is equal to answer
                   Returns:- True/False'''
                if self.guess() == self._answer:
                        return True
                else:
                        return False


class Wordle:

        def __init__(self, words):
                '''Initializes the instances of wordle which is a random word and number of guesses
                   Returns:- None'''
                self._words = random.choice(list(words))
                self._count = 0

        def guesses(self):
                '''Returns:- the number of guesses which player made'''
                return self._count 

        def guess(self, guessed):
                '''Returns:- the guess word'''
                guess = Guess(guessed,self._words)
                self._count += 1
                return guess