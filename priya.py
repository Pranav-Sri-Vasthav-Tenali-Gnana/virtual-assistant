import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import tkinter
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning darling !")
        print("Good morning darling \U0001F60D")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon honey !")

    else:
        speak("Good Evening love !")
        print("Good evening darling \U0001F60D")
        namee = 1
        namee = ("priya")
        speak("thanks for choosing me")


def usrname():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome Master")
    speak(uname)
    columns = shutil.get_terminal_size().columns


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        audio = r.listen(source)
        r.pause_threshold = 1.5

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()

    while True:

        query = takeCommand().lower()

        if "priya" in query or "hey priya" in query or "khul ja sim sim" in query:
            wishMe()
            usrname()
            speak("How can i Help you")

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open music' in query or "open song" in query:
            speak("which song")
            print("which song")
            song = takeCommand()
            speak("Here you go with music")
            webbrowser.open("https://www.jiosaavn.com/search/" + song + "")

        elif 'the time' in query:
            strTime = datetime.datetime.now()
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            namee = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            namee = takeCommand()
            speak("Thanks for naming me")

        elif 'exit' in query:
            speak("Love you babe..............,come back soon")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I was created by pranav ")
        

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'games' in query:
            speak("multiplayer or single player")
            print("multiplayer or single player")
            a = takeCommand()
        elif 'multiplayer' in query:
            speak("tic tac toe")
            print("1.tic_tac_toe")
            speak("dots and boxes")
            print("2.dots and boxes")
            speak("tron")
            print("3.tron")
            speak("pong")
            print("4.pong")

        elif "single player" in query:
            speak("simonsays")
            print("1.simonsays")
            speak("memory")
            print("2.memory")
            speak("guess")
            print("3.guess")
            speak("snake")
            print("4.snake")
            speak("pico")
            print("5.pico")
            speak("fidget")
            print("6.fidget")
            speak("cannon")
            print("7.cannon")
            speak("tiles")
            print("8.tiles")
            speak("pacman")
            print("9.pacman")
            speak("rock paper scissors")
            print("10.rock paper scissors")
        elif 'tic tac toe' in query:
            speak('have fun')
            from tkinter import *
            import numpy as np

            size_of_board = 600
            symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
            symbol_thickness = 50
            symbol_X_color = '#EE4035'
            symbol_O_color = '#0492CF'
            Green_color = '#7BC043'

            class Tic_Tac_Toe():
                # ------------------------------------------------------------------
                # Initialization Functions:
                # ------------------------------------------------------------------
                def __init__(self):
                    self.window = Tk()
                    self.window.title('Tic-Tac-Toe')
                    self.canvas = Canvas(
                        self.window, width=size_of_board, height=size_of_board)
                    self.canvas.pack()
                    # Input from user in form of clicks
                    self.window.bind('<Button-1>', self.click)

                    self.initialize_board()
                    self.player_X_turns = True
                    self.board_status = np.zeros(shape=(3, 3))

                    self.player_X_starts = True
                    self.reset_board = False
                    self.gameover = False
                    self.tie = False
                    self.X_wins = False
                    self.O_wins = False

                    self.X_score = 0
                    self.O_score = 0
                    self.tie_score = 0

                def mainloop(self):
                    self.window.mainloop()

                def initialize_board(self):
                    for i in range(2):
                        self.canvas.create_line(
                            (i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

                    for i in range(2):
                        self.canvas.create_line(
                            0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

                def play_again(self):
                    self.initialize_board()
                    self.player_X_starts = not self.player_X_starts
                    self.player_X_turns = self.player_X_starts
                    self.board_status = np.zeros(shape=(3, 3))

                # ------------------------------------------------------------------
                # Drawing Functions:
                # The modules required to draw required game based object on canvas
                # ------------------------------------------------------------------

                def draw_O(self, logical_position):
                    logical_position = np.array(logical_position)
                    # logical_position = grid value on the board
                    # grid_position = actual pixel values of the center of the grid
                    grid_position = self.convert_logical_to_grid_position(
                        logical_position)
                    self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                            outline=symbol_O_color)

                def draw_X(self, logical_position):
                    grid_position = self.convert_logical_to_grid_position(
                        logical_position)
                    self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                            fill=symbol_X_color)
                    self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                            grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                            fill=symbol_X_color)

                def display_gameover(self):

                    if self.X_wins:
                        self.X_score += 1
                        text = 'Winner: Player 1 (X)'
                        color = symbol_X_color
                    elif self.O_wins:
                        self.O_score += 1
                        text = 'Winner: Player 2 (O)'
                        color = symbol_O_color
                    else:
                        self.tie_score += 1
                        text = 'Its a tie'
                        color = 'gray'

                    self.canvas.delete("all")
                    self.canvas.create_text(
                        size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

                    score_text = 'Scores \n'
                    self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                            text=score_text)

                    score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
                    score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
                    score_text += 'Tie                    : ' + \
                        str(self.tie_score)
                    self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                            text=score_text)
                    self.reset_board = True

                    score_text = 'Click to play again \n'
                    self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                            text=score_text)

                # ------------------------------------------------------------------
                # Logical Functions:
                # The modules required to carry out game logic
                # ------------------------------------------------------------------

                def convert_logical_to_grid_position(self, logical_position):
                    logical_position = np.array(logical_position, dtype=int)
                    return (size_of_board / 3) * logical_position + size_of_board / 6

                def convert_grid_to_logical_position(self, grid_position):
                    grid_position = np.array(grid_position)
                    return np.array(grid_position // (size_of_board / 3), dtype=int)

                def is_grid_occupied(self, logical_position):
                    if self.board_status[logical_position[0]][logical_position[1]] == 0:
                        return False
                    else:
                        return True

                def is_winner(self, player):

                    player = -1 if player == 'X' else 1

                    # Three in a row
                    for i in range(3):
                        if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                            return True
                        if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                            return True

                    # Diagonals
                    if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                        return True

                    if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                        return True

                    return False

                def is_tie(self):

                    r, c = np.where(self.board_status == 0)
                    tie = False
                    if len(r) == 0:
                        tie = True

                    return tie

                def is_gameover(self):
                    # Either someone wins or all grid occupied
                    self.X_wins = self.is_winner('X')
                    if not self.X_wins:
                        self.O_wins = self.is_winner('O')

                    if not self.O_wins:
                        self.tie = self.is_tie()

                    gameover = self.X_wins or self.O_wins or self.tie

                    if self.X_wins:
                        print('X wins')
                    if self.O_wins:
                        print('O wins')
                    if self.tie:
                        print('Its a tie')

                    return gameover

                def click(self, event):
                    grid_position = [event.x, event.y]
                    logical_position = self.convert_grid_to_logical_position(
                        grid_position)

                    if not self.reset_board:
                        if self.player_X_turns:
                            if not self.is_grid_occupied(logical_position):
                                self.draw_X(logical_position)
                                self.board_status[logical_position[0]
                                                  ][logical_position[1]] = -1
                                self.player_X_turns = not self.player_X_turns
                        else:
                            if not self.is_grid_occupied(logical_position):
                                self.draw_O(logical_position)
                                self.board_status[logical_position[0]
                                                  ][logical_position[1]] = 1
                                self.player_X_turns = not self.player_X_turns

                        # Check if game is concluded
                        if self.is_gameover():
                            self.display_gameover()
                            # print('Done')
                    else:  # Play Again
                        self.canvas.delete("all")
                        self.play_again()
                        self.reset_board = False

            game_instance = Tic_Tac_Toe()
            game_instance.mainloop()
        elif 'dots and boxes' in query:
            speak('have fun')
            from tkinter import *
            import numpy as np

            size_of_board = 600
            number_of_dots = 6
            symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
            symbol_thickness = 50
            dot_color = '#7BC043'
            player1_color = '#0492CF'
            player1_color_light = '#67B0CF'
            player2_color = '#EE4035'
            player2_color_light = '#EE7E77'
            Green_color = '#7BC043'
            dot_width = 0.25*size_of_board/number_of_dots
            edge_width = 0.1*size_of_board/number_of_dots
            distance_between_dots = size_of_board / (number_of_dots)

            class Dots_and_Boxes():
                # ------------------------------------------------------------------
                # Initialization functions
                # ------------------------------------------------------------------
                def __init__(self):
                    self.window = Tk()
                    self.window.title('Dots_and_Boxes')
                    self.canvas = Canvas(
                        self.window, width=size_of_board, height=size_of_board)
                    self.canvas.pack()
                    self.window.bind('<Button-1>', self.click)
                    self.player1_starts = True
                    self.refresh_board()
                    self.play_again()

                def play_again(self):
                    self.refresh_board()
                    self.board_status = np.zeros(
                        shape=(number_of_dots - 1, number_of_dots - 1))
                    self.row_status = np.zeros(
                        shape=(number_of_dots, number_of_dots - 1))
                    self.col_status = np.zeros(
                        shape=(number_of_dots - 1, number_of_dots))

                    # Input from user in form of clicks
                    self.player1_starts = not self.player1_starts
                    self.player1_turn = not self.player1_starts
                    self.reset_board = False
                    self.turntext_handle = []

                    self.already_marked_boxes = []
                    self.display_turn_text()

                def mainloop(self):
                    self.window.mainloop()

                # ------------------------------------------------------------------
                # Logical Functions:
                # The modules required to carry out game logic
                # ------------------------------------------------------------------

                def is_grid_occupied(self, logical_position, type):
                    r = logical_position[0]
                    c = logical_position[1]
                    occupied = True

                    if type == 'row' and self.row_status[c][r] == 0:
                        occupied = False
                    if type == 'col' and self.col_status[c][r] == 0:
                        occupied = False

                    return occupied

                def convert_grid_to_logical_position(self, grid_position):
                    grid_position = np.array(grid_position)
                    position = (grid_position-distance_between_dots /
                                4)//(distance_between_dots/2)

                    type = False
                    logical_position = []
                    if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
                        r = int((position[0]-1)//2)
                        c = int(position[1]//2)
                        logical_position = [r, c]
                        type = 'row'
                        # self.row_status[c][r]=1
                    elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
                        c = int((position[1] - 1) // 2)
                        r = int(position[0] // 2)
                        logical_position = [r, c]
                        type = 'col'

                    return logical_position, type

                def mark_box(self):
                    boxes = np.argwhere(self.board_status == -4)
                    for box in boxes:
                        if list(box) not in self.already_marked_boxes and list(box) != []:
                            self.already_marked_boxes.append(list(box))
                            color = player1_color_light
                            self.shade_box(box, color)

                    boxes = np.argwhere(self.board_status == 4)
                    for box in boxes:
                        if list(box) not in self.already_marked_boxes and list(box) != []:
                            self.already_marked_boxes.append(list(box))
                            color = player2_color_light
                            self.shade_box(box, color)

                def update_board(self, type, logical_position):
                    r = logical_position[0]
                    c = logical_position[1]
                    val = 1
                    if self.player1_turn:
                        val = - 1

                    if c < (number_of_dots-1) and r < (number_of_dots-1):
                        self.board_status[c][r] += val

                    if type == 'row':
                        self.row_status[c][r] = 1
                        if c >= 1:
                            self.board_status[c-1][r] += val

                    elif type == 'col':
                        self.col_status[c][r] = 1
                        if r >= 1:
                            self.board_status[c][r-1] += val

                def is_gameover(self):
                    return (self.row_status == 1).all() and (self.col_status == 1).all()

                # ------------------------------------------------------------------
                # Drawing Functions:
                # The modules required to draw required game based object on canvas
                # ------------------------------------------------------------------

                def make_edge(self, type, logical_position):
                    if type == 'row':
                        start_x = distance_between_dots/2 + \
                            logical_position[0]*distance_between_dots
                        end_x = start_x+distance_between_dots
                        start_y = distance_between_dots/2 + \
                            logical_position[1]*distance_between_dots
                        end_y = start_y
                    elif type == 'col':
                        start_y = distance_between_dots / 2 + \
                            logical_position[1] * distance_between_dots
                        end_y = start_y + distance_between_dots
                        start_x = distance_between_dots / 2 + \
                            logical_position[0] * distance_between_dots
                        end_x = start_x

                    if self.player1_turn:
                        color = player1_color
                    else:
                        color = player2_color
                    self.canvas.create_line(
                        start_x, start_y, end_x, end_y, fill=color, width=edge_width)

                def display_gameover(self):
                    player1_score = len(np.argwhere(self.board_status == -4))
                    player2_score = len(np.argwhere(self.board_status == 4))

                    if player1_score > player2_score:
                        # Player 1 wins
                        text = 'Winner: Player 1 '
                        color = player1_color
                    elif player2_score > player1_score:
                        text = 'Winner: Player 2 '
                        color = player2_color
                    else:
                        text = 'Its a tie'
                        color = 'gray'

                    self.canvas.delete("all")
                    self.canvas.create_text(
                        size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

                    score_text = 'Scores \n'
                    self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                            text=score_text)

                    score_text = 'Player 1 : ' + str(player1_score) + '\n'
                    score_text += 'Player 2 : ' + str(player2_score) + '\n'
                    # score_text += 'Tie                    : ' + str(self.tie_score)
                    self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                            text=score_text)
                    self.reset_board = True

                    score_text = 'Click to play again \n'
                    self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                            text=score_text)

                def refresh_board(self):
                    for i in range(number_of_dots):
                        x = i*distance_between_dots+distance_between_dots/2
                        self.canvas.create_line(x, distance_between_dots/2, x,
                                                size_of_board-distance_between_dots/2,
                                                fill='gray', dash=(2, 2))
                        self.canvas.create_line(distance_between_dots/2, x,
                                                size_of_board-distance_between_dots/2, x,
                                                fill='gray', dash=(2, 2))

                    for i in range(number_of_dots):
                        for j in range(number_of_dots):
                            start_x = i*distance_between_dots+distance_between_dots/2
                            end_x = j*distance_between_dots+distance_between_dots/2
                            self.canvas.create_oval(start_x-dot_width/2, end_x-dot_width/2, start_x+dot_width/2,
                                                    end_x+dot_width/2, fill=dot_color,
                                                    outline=dot_color)

                def display_turn_text(self):
                    text = 'Next turn: '
                    if self.player1_turn:
                        text += 'Player1'
                        color = player1_color
                    else:
                        text += 'Player2'
                        color = player2_color

                    self.canvas.delete(self.turntext_handle)
                    self.turntext_handle = self.canvas.create_text(size_of_board - 5*len(text),
                                                                   size_of_board-distance_between_dots/8,
                                                                   font="cmr 15 bold", text=text, fill=color)

                def shade_box(self, box, color):
                    start_x = distance_between_dots / 2 + \
                        box[1] * distance_between_dots + edge_width/2
                    start_y = distance_between_dots / 2 + \
                        box[0] * distance_between_dots + edge_width/2
                    end_x = start_x + distance_between_dots - edge_width
                    end_y = start_y + distance_between_dots - edge_width
                    self.canvas.create_rectangle(
                        start_x, start_y, end_x, end_y, fill=color, outline='')

                def display_turn_text(self):
                    text = 'Next turn: '
                    if self.player1_turn:
                        text += 'Player1'
                        color = player1_color
                    else:
                        text += 'Player2'
                        color = player2_color

                    self.canvas.delete(self.turntext_handle)
                    self.turntext_handle = self.canvas.create_text(size_of_board - 5*len(text),
                                                                   size_of_board-distance_between_dots/8,
                                                                   font="cmr 15 bold", text=text, fill=color)

                def click(self, event):
                    if not self.reset_board:
                        grid_position = [event.x, event.y]
                        logical_positon, valid_input = self.convert_grid_to_logical_position(
                            grid_position)
                        if valid_input and not self.is_grid_occupied(logical_positon, valid_input):
                            self.update_board(valid_input, logical_positon)
                            self.make_edge(valid_input, logical_positon)
                            self.mark_box()
                            self.refresh_board()
                            self.player1_turn = not self.player1_turn

                            if self.is_gameover():
                                # self.canvas.delete("all")
                                self.display_gameover()
                            else:
                                self.display_turn_text()
                    else:
                        self.canvas.delete("all")
                        self.play_again()
                        self.reset_board = False

            game_instance = Dots_and_Boxes()
            game_instance.mainloop()
        elif "tron" in query:
            from turtle import *
            from freegames import square, vector
            print("player 1 controls:       player 2 controls:")
            print("for up 'a'                for up 'j'")
            print("for down 'd'               for down 'l'")

            p1xy = vector(-100, 0)
            p1aim = vector(4, 0)
            p1body = set()

            p2xy = vector(100, 0)
            p2aim = vector(-4, 0)
            p2body = set()

            def inside(head):
                "Return True if head inside screen."
                return -200 < head.x < 200 and -200 < head.y < 200

            def draw():
                "Advance players and draw game."
                p1xy.move(p1aim)
                p1head = p1xy.copy()

                p2xy.move(p2aim)
                p2head = p2xy.copy()

                if not inside(p1head) or p1head in p2body:
                    print('Player blue wins!')
                    return

                if not inside(p2head) or p2head in p1body:
                    print('Player red wins!')
                    return

                p1body.add(p1head)
                p2body.add(p2head)

                square(p1xy.x, p1xy.y, 3, 'red')
                square(p2xy.x, p2xy.y, 3, 'blue')
                update()
                ontimer(draw, 50)

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            listen()
            onkey(lambda: p1aim.rotate(90), 'a')
            onkey(lambda: p1aim.rotate(-90), 'd')
            onkey(lambda: p2aim.rotate(90), 'j')
            onkey(lambda: p2aim.rotate(-90), 'l')
            draw()
            done()

        elif "rock paper scissors" in query:
            from random import randint

            # create a list of play options
            t = ["Rock", "Paper", "Scissors"]

            # assign a random play to the computer
            computer = t[randint(0, 2)]

            # set player to False
            player = False

            while player == False:
                # set player to True
                player = input("Rock, Paper, Scissors?")
                if player == computer:
                    print("Tie!")
                elif player == "Rock":
                    if computer == "Paper":
                        print("You lose!", computer, "covers", player)
                    else:
                        print("You win!", player, "smashes", computer)
                elif player == "Paper":
                    if computer == "Scissors":
                        print("You lose!", computer, "cut", player)
                    else:
                        print("You win!", player, "covers", computer)
                elif player == "Scissors":
                    if computer == "Rock":
                        print("You lose...", computer, "smashes", player)
                    else:
                        print("You win!", player, "cut", computer)
                elif player == "exit":
                    break
                else:
                    print("That's not a valid play. Check your spelling!")
                # player was set to True, but we want it to be False so the loop continues
                player = False
                computer = t[randint(0, 2)]

        elif "simonsays" in query:
            from random import choice
            from time import sleep
            from turtle import *
            from freegames import floor, square, vector

            pattern = []
            guesses = []
            tiles = {
                vector(0, 0): ('red', 'dark red'),
                vector(0, -200): ('blue', 'dark blue'),
                vector(-200, 0): ('green', 'dark green'),
                vector(-200, -200): ('yellow', 'khaki'),
            }

            def grid():
                "Draw grid of tiles."
                square(0, 0, 200, 'dark red')
                square(0, -200, 200, 'dark blue')
                square(-200, 0, 200, 'dark green')
                square(-200, -200, 200, 'khaki')
                update()

            def flash(tile):
                "Flash tile in grid."
                glow, dark = tiles[tile]
                square(tile.x, tile.y, 200, glow)
                update()
                sleep(0.5)
                square(tile.x, tile.y, 200, dark)
                update()
                sleep(0.5)

            def grow():
                "Grow pattern and flash tiles."
                tile = choice(list(tiles))
                pattern.append(tile)

                for tile in pattern:
                    flash(tile)

                print('Pattern length:', len(pattern))
                guesses.clear()

            def tap(x, y):
                "Respond to screen tap."
                onscreenclick(None)
                x = floor(x, 200)
                y = floor(y, 200)
                tile = vector(x, y)
                index = len(guesses)

                if tile != pattern[index]:
                    exit()

                guesses.append(tile)
                flash(tile)

                if len(guesses) == len(pattern):
                    grow()

                onscreenclick(tap)

            def start(x, y):
                "Start game."
                grow()
                onscreenclick(tap)

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            grid()
            onscreenclick(start)
            done()

        elif "memory" in query:
            from random import *
            from turtle import *
            from freegames import path

            car = path('car.gif')
            tiles = list(range(32)) * 2
            state = {'mark': None}
            hide = [True] * 64

            def square(x, y):
                "Draw white square with black outline at (x, y)."
                up()
                goto(x, y)
                down()
                color('black', 'white')
                begin_fill()
                for count in range(4):
                    forward(50)
                    left(90)
                end_fill()

            def index(x, y):

                return int((x + 200) // 50 + ((y + 200) // 50) * 8)

            def xy(count):
                "Convert tiles count to (x, y) coordinates."
                return (count % 8) * 50 - 200, (count // 8) * 50 - 200

            def tap(x, y):
                "Update mark and hidden tiles based on tap."
                spot = index(x, y)
                mark = state['mark']

                if mark is None or mark == spot or tiles[mark] != tiles[spot]:
                    state['mark'] = spot
                else:
                    hide[spot] = False
                    hide[mark] = False
                    state['mark'] = None

            def draw():
                "Draw image and tiles."
                clear()
                goto(0, 0)
                shape(car)
                stamp()

                for count in range(64):
                    if hide[count]:
                        x, y = xy(count)
                        square(x, y)

                mark = state['mark']

                if mark is not None:
                    x, y = xy(mark)
                    up()
                    goto(x + 2, y)
                    color('black')
                    write(tiles[mark], font=('Arial', 30, 'normal'))

                update()
                ontimer(draw, 100)

            shuffle(tiles)
            setup(420, 420, 370, 0)
            addshape(car)
            hideturtle()
            tracer(False)
            onscreenclick(tap)
            draw()
            done()

        elif "guess" in query:
            from random import randint

            start = 0
            end = 100
            value = randint(start, end)

            print("I'm thinking of a number between", start, "and", end)

            guess = None

            while guess != value:

                text = input("Guess the number: ")

                try:
                    guess = int(text)
                except:
                    print("Whoops! Be sure the number contains only digits.")
                    continue

                if guess < value:
                    print("Higher.")
                elif guess > value:
                    print("Lower.")

            print("Congratulations! You guessed the right answer:", value)

        elif "snake" in query:
            from tkinter import *
            import random
            import time
            import numpy as np
            from PIL import ImageTk, Image

            # Define useful parameters
            size_of_board = 600
            rows = 10
            cols = 10
            DELAY = 100
            snake_initial_length = 3
            symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
            symbol_thickness = 2
            RED_COLOR = "#EE4035"
            BLUE_COLOR = "#0492CF"
            Green_color = "#7BC043"

            BLUE_COLOR_LIGHT = '#67B0CF'
            RED_COLOR_LIGHT = '#EE7E77'

            class SnakeAndApple:
                # ------------------------------------------------------------------
                # Initialization Functions:
                # ------------------------------------------------------------------
                def __init__(self):
                    self.window = Tk()
                    self.window.title("Snake-and-Apple")
                    self.canvas = Canvas(
                        self.window, width=size_of_board, height=size_of_board)
                    self.canvas.pack()
                    # Input from user in form of clicks and keyboard
                    self.window.bind("<Key>", self.key_input)
                    self.window.bind("<Button-1>", self.mouse_input)
                    self.play_again()
                    self.begin = False

                def initialize_board(self):
                    self.board = []
                    self.apple_obj = []
                    self.old_apple_cell = []

                    for i in range(rows):
                        for j in range(cols):
                            self.board.append((i, j))

                    for i in range(rows):
                        self.canvas.create_line(
                            i * size_of_board / rows, 0, i * size_of_board / rows, size_of_board,
                        )

                    for i in range(cols):
                        self.canvas.create_line(
                            0, i * size_of_board / cols, size_of_board, i * size_of_board / cols,
                        )

                def initialize_snake(self):
                    self.snake = []
                    self.crashed = False
                    self.snake_heading = "Right"
                    self.last_key = self.snake_heading
                    self.forbidden_actions = {}
                    self.forbidden_actions["Right"] = "Left"
                    self.forbidden_actions["Left"] = "Right"
                    self.forbidden_actions["Up"] = "Down"
                    self.forbidden_actions["Down"] = "Up"
                    self.snake_objects = []
                    for i in range(snake_initial_length):
                        self.snake.append((i, 0))

                def play_again(self):
                    self.canvas.delete("all")
                    self.initialize_board()
                    self.initialize_snake()
                    self.place_apple()
                    self.display_snake(mode="complete")
                    self.begin_time = time.time()

                def mainloop(self):
                    while True:
                        self.window.update()
                        if self.begin:
                            if not self.crashed:
                                self.window.after(
                                    DELAY, self.update_snake(self.last_key))
                            else:
                                self.begin = False
                                self.display_gameover()

                # ------------------------------------------------------------------
                # Drawing Functions:
                # The modules required to draw required game based object on canvas
                # ------------------------------------------------------------------
                def display_gameover(self):
                    score = len(self.snake)
                    self.canvas.delete("all")
                    score_text = "Scores \n"

                    # put gif image on canvas
                    # pic's upper left corner (NW) on the canvas is at x=50 y=10

                    self.canvas.create_text(
                        size_of_board / 2,
                        3 * size_of_board / 8,
                        font="cmr 40 bold",
                        fill=Green_color,
                        text=score_text,
                    )
                    score_text = str(score)
                    self.canvas.create_text(
                        size_of_board / 2,
                        1 * size_of_board / 2,
                        font="cmr 50 bold",
                        fill=BLUE_COLOR,
                        text=score_text,
                    )
                    time_spent = str(
                        np.round(time.time() - self.begin_time, 1)) + 'sec'
                    self.canvas.create_text(
                        size_of_board / 2,
                        3 * size_of_board / 4,
                        font="cmr 20 bold",
                        fill=BLUE_COLOR,
                        text=time_spent,
                    )
                    score_text = "Click to play again \n"
                    self.canvas.create_text(
                        size_of_board / 2,
                        15 * size_of_board / 16,
                        font="cmr 20 bold",
                        fill="gray",
                        text=score_text,
                    )

                def place_apple(self):
                    # Place apple randomly anywhere except at the cells occupied by snake
                    unoccupied_cels = set(self.board) - set(self.snake)
                    self.apple_cell = random.choice(list(unoccupied_cels))
                    row_h = int(size_of_board / rows)
                    col_w = int(size_of_board / cols)
                    x1 = self.apple_cell[0] * row_h
                    y1 = self.apple_cell[1] * col_w
                    x2 = x1 + row_h
                    y2 = y1 + col_w
                    self.apple_obj = self.canvas.create_rectangle(
                        x1, y1, x2, y2, fill=RED_COLOR_LIGHT, outline=BLUE_COLOR,
                    )

                def display_snake(self, mode=""):
                    # Remove tail from display if it exists
                    if self.snake_objects != []:
                        self.canvas.delete(self.snake_objects.pop(0))
                    if mode == "complete":
                        for i, cell in enumerate(self.snake):
                            # print(cell)
                            row_h = int(size_of_board / rows)
                            col_w = int(size_of_board / cols)
                            x1 = cell[0] * row_h
                            y1 = cell[1] * col_w
                            x2 = x1 + row_h
                            y2 = y1 + col_w
                            self.snake_objects.append(
                                self.canvas.create_rectangle(
                                    x1, y1, x2, y2, fill=BLUE_COLOR, outline=BLUE_COLOR,
                                )
                            )
                    else:
                        # only update head
                        cell = self.snake[-1]
                        row_h = int(size_of_board / rows)
                        col_w = int(size_of_board / cols)
                        x1 = cell[0] * row_h
                        y1 = cell[1] * col_w
                        x2 = x1 + row_h
                        y2 = y1 + col_w
                        self.snake_objects.append(
                            self.canvas.create_rectangle(
                                x1, y1, x2, y2, fill=BLUE_COLOR, outline=RED_COLOR,
                            )
                        )
                        if self.snake[0] == self.old_apple_cell:
                            self.snake.insert(0, self.old_apple_cell)
                            self.old_apple_cell = []
                            tail = self.snake[0]
                            row_h = int(size_of_board / rows)
                            col_w = int(size_of_board / cols)
                            x1 = tail[0] * row_h
                            y1 = tail[1] * col_w
                            x2 = x1 + row_h
                            y2 = y1 + col_w
                            self.snake_objects.insert(
                                0,
                                self.canvas.create_rectangle(
                                    x1, y1, x2, y2, fill=BLUE_COLOR, outline=RED_COLOR
                                ),
                            )
                        self.window.update()

                # ------------------------------------------------------------------
                # Logical Functions:
                # The modules required to carry out game logic
                # ------------------------------------------------------------------
                def update_snake(self, key):
                    # Check if it hit the wall or its own body
                    tail = self.snake[0]
                    head = self.snake[-1]
                    if tail != self.old_apple_cell:
                        self.snake.pop(0)
                    if key == "Left":
                        self.snake.append((head[0] - 1, head[1]))
                    elif key == "Right":
                        self.snake.append((head[0] + 1, head[1]))
                    elif key == "Up":
                        self.snake.append((head[0], head[1] - 1))
                    elif key == "Down":
                        self.snake.append((head[0], head[1] + 1))

                    head = self.snake[-1]
                    if (
                            head[0] > cols - 1
                            or head[0] < 0
                            or head[1] > rows - 1
                            or head[1] < 0
                            or len(set(self.snake)) != len(self.snake)
                    ):
                        # Hit the wall / Hit on body
                        self.crashed = True
                    elif self.apple_cell == head:
                        # Got the apple
                        self.old_apple_cell = self.apple_cell
                        self.canvas.delete(self.apple_obj)
                        self.place_apple()
                        self.display_snake()
                    else:
                        self.snake_heading = key
                        self.display_snake()

                def check_if_key_valid(self, key):
                    valid_keys = ["Up", "Down", "Left", "Right"]
                    if key in valid_keys and self.forbidden_actions[self.snake_heading] != key:
                        return True
                    else:
                        return False

                def mouse_input(self, event):
                    self.play_again()

                def key_input(self, event):
                    if not self.crashed:
                        key_pressed = event.keysym
                        # Check if the pressed key is a valid key
                        if self.check_if_key_valid(key_pressed):
                            # print(key_pressed)
                            self.begin = True
                            self.last_key = key_pressed

            game_instance = SnakeAndApple()
            game_instance.mainloop()

        elif "pico" in query:
            from random import sample, shuffle

            digits = 3
            guesses = 20

            print('I am thinking of a', digits, 'digit number.')
            print('Try to guess what it is.')
            print('Here are some clues:')
            print('When I say:    That means:')
            print('  pico         One digit is correct but in the wrong position.')
            print('  fermi        One digit is correct and in the right position.')
            print('  bagels       No digit is correct.')
            print('There are no repeated digits in the number.')

            # Create a random number.

            letters = sample('0123456789', digits)

            if letters[0] == '0':
                letters.reverse()

            number = ''.join(letters)

            print('I have thought up a number.')
            print('You have', guesses, 'guesses to get it.')

            counter = 1

            while True:
                print('Guess #', counter)
                guess = input()

                if len(guess) != digits:
                    print('Wrong number of digits. Try again!')
                    continue

                # Create the clues.

                clues = []

                for index in range(digits):
                    if guess[index] == number[index]:
                        clues.append('fermi')
                    elif guess[index] in number:
                        clues.append('pico')

                shuffle(clues)

                if len(clues) == 0:
                    print('bagels')
                else:
                    print(' '.join(clues))

                counter += 1

                if guess == number:
                    print('You got it!')
                    break

                if counter > guesses:
                    print('You ran out of guesses. The answer was', number)
                    break

        elif "fidget" in query:
            from turtle import *

            state = {'turn': 0}

            def spinner():
                "Draw fidget spinner."
                clear()
                angle = state['turn'] / 10
                right(angle)
                forward(100)
                dot(120, 'red')
                back(100)
                right(120)
                forward(100)
                dot(120, 'green')
                back(100)
                right(120)
                forward(100)
                dot(120, 'blue')
                back(100)
                right(120)
                update()

            def animate():
                "Animate fidget spinner."
                if state['turn'] > 0:
                    state['turn'] -= 1

                spinner()
                ontimer(animate, 20)

            def flick():
                "Flick fidget spinner."
                state['turn'] += 10

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            width(20)
            onkey(flick, 'space')
            listen()
            animate()
            done()

        elif "cannon" in query:

            from random import randrange
            from turtle import *
            from freegames import vector

            ball = vector(-200, -200)
            speed = vector(0, 0)
            targets = []

            def tap(x, y):
                "Respond to screen tap."
                if not inside(ball):
                    ball.x = -199
                    ball.y = -199
                    speed.x = (x + 200) / 25
                    speed.y = (y + 200) / 25

            def inside(xy):
                "Return True if xy within screen."
                return -200 < xy.x < 200 and -200 < xy.y < 200

            def draw():
                "Draw ball and targets."
                clear()

                for target in targets:
                    goto(target.x, target.y)
                    dot(20, 'blue')

                if inside(ball):
                    goto(ball.x, ball.y)
                    dot(6, 'red')

                update()

            def move():
                "Move ball and targets."
                if randrange(40) == 0:
                    y = randrange(-150, 150)
                    target = vector(200, y)
                    targets.append(target)

                for target in targets:
                    target.x -= 0.5

                if inside(ball):
                    speed.y -= 0.35
                    ball.move(speed)

                dupe = targets.copy()
                targets.clear()

                for target in dupe:
                    if abs(target - ball) > 13:
                        targets.append(target)

                draw()

                for target in targets:
                    if not inside(target):
                        return

                ontimer(move, 50)

            setup(420, 420, 370, 0)
            hideturtle()
            up()
            tracer(False)
            onscreenclick(tap)
            move()
            done()

        elif "tiles" in query:

            from random import *
            from turtle import *
            from freegames import floor, vector

            tiles = {}
            neighbors = [
                vector(100, 0),
                vector(-100, 0),
                vector(0, 100),
                vector(0, -100),
            ]

            def load():
                "Load tiles and scramble."
                count = 1

                for y in range(-200, 200, 100):
                    for x in range(-200, 200, 100):
                        mark = vector(x, y)
                        tiles[mark] = count
                        count += 1

                tiles[mark] = None

                for count in range(1000):
                    neighbor = choice(neighbors)
                    spot = mark + neighbor

                    if spot in tiles:
                        number = tiles[spot]
                        tiles[spot] = None
                        tiles[mark] = number
                        mark = spot

            def square(mark, number):
                "Draw white square with black outline and number."
                up()
                goto(mark.x, mark.y)
                down()

                color('black', 'white')
                begin_fill()
                for count in range(4):
                    forward(99)
                    left(90)
                end_fill()

                if number is None:
                    return
                elif number < 10:
                    forward(20)

                write(number, font=('Arial', 60, 'normal'))

            def tap(x, y):
                "Swap tile and empty square."
                x = floor(x, 100)
                y = floor(y, 100)
                mark = vector(x, y)

                for neighbor in neighbors:
                    spot = mark + neighbor

                    if spot in tiles and tiles[spot] is None:
                        number = tiles[mark]
                        tiles[spot] = number
                        square(spot, number)
                        tiles[mark] = None
                        square(mark, None)

            def draw():
                "Draw all tiles."
                for mark in tiles:
                    square(mark, tiles[mark])
                update()

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            load()
            draw()
            onscreenclick(tap)
            done()

        elif "pacman" in query:

            from random import choice
            from turtle import *
            from freegames import floor, vector

            state = {'score': 0}
            path = Turtle(visible=False)
            writer = Turtle(visible=False)
            aim = vector(5, 0)
            pacman = vector(-40, -80)
            ghosts = [
                [vector(-180, 160), vector(5, 0)],
                [vector(-180, -160), vector(0, 5)],
                [vector(100, 160), vector(0, -5)],
                [vector(100, -160), vector(-5, 0)],
            ]
            tiles = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]

            def square(x, y):
                "Draw square using path at (x, y)."
                path.up()
                path.goto(x, y)
                path.down()
                path.begin_fill()

                for count in range(4):
                    path.forward(20)
                    path.left(90)

                path.end_fill()

            def offset(point):
                "Return offset of point in tiles."
                x = (floor(point.x, 20) + 200) / 20
                y = (180 - floor(point.y, 20)) / 20
                index = int(x + y * 20)
                return index

            def valid(point):
                "Return True if point is valid in tiles."
                index = offset(point)

                if tiles[index] == 0:
                    return False

                index = offset(point + 19)

                if tiles[index] == 0:
                    return False

                return point.x % 20 == 0 or point.y % 20 == 0

            def world():
                "Draw world using path."
                bgcolor('black')
                path.color('blue')

                for index in range(len(tiles)):
                    tile = tiles[index]

                    if tile > 0:
                        x = (index % 20) * 20 - 200
                        y = 180 - (index // 20) * 20
                        square(x, y)

                        if tile == 1:
                            path.up()
                            path.goto(x + 10, y + 10)
                            path.dot(2, 'white')

            def move():
                "Move pacman and all ghosts."
                writer.undo()
                writer.write(state['score'])

                clear()

                if valid(pacman + aim):
                    pacman.move(aim)

                index = offset(pacman)

                if tiles[index] == 1:
                    tiles[index] = 2
                    state['score'] += 1
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)

                up()
                goto(pacman.x + 10, pacman.y + 10)
                dot(20, 'yellow')

                for point, course in ghosts:
                    if valid(point + course):
                        point.move(course)
                    else:
                        options = [
                            vector(5, 0),
                            vector(-5, 0),
                            vector(0, 5),
                            vector(0, -5),
                        ]
                        plan = choice(options)
                        course.x = plan.x
                        course.y = plan.y

                    up()
                    goto(point.x + 10, point.y + 10)
                    dot(20, 'red')

                update()

                for point, course in ghosts:
                    if abs(pacman - point) < 20:
                        return

                ontimer(move, 100)

            def change(x, y):
                "Change pacman aim if valid."
                if valid(pacman + vector(x, y)):
                    aim.x = x
                    aim.y = y

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            writer.goto(160, 160)
            writer.color('white')
            writer.write(state['score'])
            listen()
            onkey(lambda: change(5, 0), 'Right')
            onkey(lambda: change(-5, 0), 'Left')
            onkey(lambda: change(0, 5), 'Up')
            onkey(lambda: change(0, -5), 'Down')
            world()
            move()
            done()

        elif 'pong' in query:

            from random import choice, random
            from turtle import *
            from freegames import vector
            print("player 1 controls:       player 2 controls:")
            print("for up 'w'                for up 'i'")
            print("for down 's'               for down 'k'")

            def value():
                "Randomly generate value between (-5, -3) or (3, 5)."
                return (3 + random() * 2) * choice([1, -1])

            ball = vector(0, 0)
            aim = vector(value(), value())
            state = {1: 0, 2: 0}

            def move(player, change):
                "Move player position by change."
                state[player] += change

            def rectangle(x, y, width, height):
                "Draw rectangle at (x, y) with given width and height."
                up()
                goto(x, y)
                down()
                begin_fill()
                for count in range(2):
                    forward(width)
                    left(90)
                    forward(height)
                    left(90)
                end_fill()

            def draw():

                clear()
                rectangle(-200, state[1], 10, 50)
                rectangle(190, state[2], 10, 50)

                ball.move(aim)
                x = ball.x
                y = ball.y

                up()
                goto(x, y)
                dot(10)
                update()

                if y < -200 or y > 200:
                    aim.y = -aim.y

                if x < -185:
                    low = state[1]
                    high = state[1] + 50

                    if low <= y <= high:
                        aim.x = -aim.x
                    else:
                        return

                if x > 185:
                    low = state[2]
                    high = state[2] + 50

                    if low <= y <= high:
                        aim.x = -aim.x
                    else:
                        return

                ontimer(draw, 50)

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            listen()
            onkey(lambda: move(1, 20), 'w')
            onkey(lambda: move(1, -20), 's')
            onkey(lambda: move(2, 20), 'i')
            onkey(lambda: move(2, -20), 'k')
            draw()
            done()

        elif "calculator" in query:
            from tkinter import*
            import math
            import parser
            import tkinter.messagebox

            root = Tk()
            root.title("Scientific Calculator")
            root.configure(background="Powder blue")
            root.resizable(width=False, height=False)
            root.geometry("480x624+20+20")

            """root1=TK()
            root1.title("Conversion")
            root1.configure(background="Gray")
            root1.resizable(width=False, height=False)
            root1.geometry("944x624+20+20")
            """
            calc = Frame(root)
            calc.grid()

            class Calc():
                def __init__(self):
                    self.total = 0
                    self.current = ""
                    self.input_value = True
                    self.check_sum = False
                    self.op = ""
                    self.result = False

                def numberEnter(self, num):
                    self.result = False
                    firstnum = txtDisplay.get()
                    secondnum = str(num)
                    if self.input_value:
                        self.current = secondnum
                        self.input_value = False
                    else:
                        if secondnum == '.':
                            if secondnum in firstnum:
                                return
                        self.current = firstnum+secondnum
                    self.display(self.current)

                def sum_of_total(self):
                    self.result = True
                    self.current = float(self.current)
                    if self.check_sum == True:
                        self.valid_function()
                    else:
                        self.total = float(txtDisplay.get())

                def valid_function(self):
                    if self.op == "add":
                        self.total += self.current
                    if self.op == "sub":
                        self.total -= self.current
                    if self.op == "multi":
                        self.total *= self.current
                    if self.op == "divide":
                        self.total /= self.current
                    if self.op == "mod":
                        self.total %= self.current
                    if self.op == "inv":
                        self.total = 1/self.current
                    self.input_value = True
                    self.check_sum = False
                    self.display(self.total)

                def operation(self, op):
                    self.current = float(self.current)
                    if self.check_sum:
                        self.valid_function()
                    elif not self.result:
                        self.total = self.current
                        self.input_value = True
                    self.check_sum = True
                    self.op = op
                    self.result = False

                def Clear_Entry(self):
                    self.result = False
                    self.current = "0"
                    self.display(0)
                    self.input_value = True

                def all_Clear_Entry(self):
                    self.Clear_Entry()
                    self.total = 0

                def tanh(self):
                    self.reult = False
                    self.current = math.tanh(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def tan(self):
                    self.reult = False
                    self.current = math.tan(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def sinh(self):
                    self.reult = False
                    self.current = math.sinh(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def sin(self):
                    self.reult = False
                    self.current = math.sin(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def log(self):
                    self.reult = False
                    self.current = math.log(float(txtDisplay.get()))
                    self.display(self.current)

                def exp(self):
                    self.reult = False
                    self.current = math.exp(float(txtDisplay.get()))
                    self.display(self.current)

                def mathsPM(self):
                    self.reult = False
                    self.current = -(float(txtDisplay.get()))
                    self.display(self.current)

                def squared(self):
                    self.reult = False
                    self.current = math.sqrt(float(txtDisplay.get()))
                    self.display(self.current)

                def cos(self):
                    self.reult = False
                    self.current = math.cos(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def cosh(self):
                    self.reult = False
                    self.current = math.cosh(
                        math.radians(float(txtDisplay.get())))
                    self.display(self.current)

                def display(self, value):
                    txtDisplay.delete(0, END)
                    txtDisplay.insert(0, value)

                def pi(self):
                    self.reult = False
                    self.current = math.pi
                    self.display(self.current)

                def tau(self):
                    self.reult = False
                    self.current = math.tau
                    self.display(self.current)

                def e(self):
                    self.reult = False
                    self.current = math.e
                    self.display(self.current)

                def acosh(self):
                    self.result = False
                    self.current = math.acosh(float(txtDisplay.get()))
                    self.display(self.current)

                def asinh(self):
                    self.result = False
                    self.current = math.asinh(float(txtDisplay.get()))
                    self.display(self.current)

                def expm1(self):
                    self.result = False
                    self.current = math.expm1(float(txtDisplay.get()))
                    self.display(self.current)

                def lgamma(self):
                    self.result = False
                    self.current = math.lgamma(float(txtDisplay.get()))
                    self.display(self.current)

                def degrees(self):
                    self.result = False
                    self.current = math.degrees(float(txtDisplay.get()))
                    self.display(self.current)

                def log2(self):
                    self.result = False
                    self.current = math.log2(float(txtDisplay.get()))
                    self.display(self.current)

                def log10(self):
                    self.result = False
                    self.current = math.log10(float(txtDisplay.get()))
                    self.display(self.current)

                def log1p(self):
                    self.result = False
                    self.current = math.log1p(float(txtDisplay.get()))
                    self.display(self.current)
            """    def inv(self):
                    self.result=False
                    self.current=math
                    self.display(self.current)
                def perc(self):
                    self.result=False
                    self.current=(float(txtDisplay.get())/100
                    self.display(self.current)
                def expo(self):
                    self.result=False
                    self.current=
                    self.display(self.current)
                def square(self):
                    self.result=False
                    self.current=(float(txtDisplay.get())*(float(txtDisplay.get())
                    self.display(self.current)
                def 

            """

            added_value = Calc()
            txtDisplay = Entry(calc, relief=SUNKEN, font=(
                'arial', 20, 'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
            txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
            txtDisplay.insert(0, "0")
            numberpad = "789456123"
            i = 0
            btn = []
            for j in range(2, 5):
                for k in range(3):
                    btn.append(Button(calc, width=6, height=2, font=(
                        'arial', 20, 'bold'), bd=4, text=numberpad[i]))
                    btn[i].grid(row=j, column=k, pady=1)
                    btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(
                        x)
                    i += 1
            btnClear = Button(calc, text=chr(67), width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
            btnAllClear = Button(calc, text=chr(67)+chr(69), width=6, height=2, font=('arial', 20, 'bold'),
                                 bd=4, bg="powder blue", command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)

            btnSq = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                           bg="powder blue", command=added_value.squared).grid(row=1, column=2, pady=1)
            btnAdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="powder blue", command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

            btnSub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="powder blue", command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
            btnMult = Button(calc, text="×", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                             bg="powder blue", command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

            btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="powder blue", command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)
            btnZero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                             bg="powder blue", command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

            btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="powder blue", command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
            btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'),
                           bd=4, bg="powder blue", command=added_value.mathsPM).grid(row=5, column=2, pady=1)

            btnEquals = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                               bg="powder blue", command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

            # ===================Scientific Calculator====================================================================================================================================================

            btnPi = Button(calc, text='π', width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.pi).grid(row=1, column=4, pady=1)
            btnCos = Button(calc, text="cos", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.cos).grid(row=1, column=5, pady=1)

            btnTan = Button(calc, text="tan", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.tan).grid(row=1, column=6, pady=1)
            btnSin = Button(calc, text="sin", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.sin).grid(row=1, column=7, pady=1)

            btn2Pi = Button(calc, text='2π', width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.tau).grid(row=2, column=4, pady=1)
            btnCosh = Button(calc, text="cosh", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.cosh).grid(row=2, column=5, pady=1)

            btnTanh = Button(calc, text="tanh", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.tanh).grid(row=2, column=6, pady=1)
            btnSinh = Button(calc, text="sinh", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.sinh).grid(row=2, column=7, pady=1)

            btnLog = Button(calc, text='log', width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log).grid(row=3, column=4, pady=1)
            btninv = Button(calc, text="Inv", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="gray", command=lambda: added_value.operation("inv")).grid(row=3, column=5, pady=1)

            btnMod = Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'),
                            bd=4, command=lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)
            btnE = Button(calc, text="e", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.e).grid(row=3, column=7, pady=1)

            btnLog2 = Button(calc, text='log2', width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log2).grid(row=4, column=4, pady=1)
            btnDeg = Button(calc, text="deg", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.degrees).grid(row=4, column=5, pady=1)

            btnAcosh = Button(calc, text="acosh", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.acosh).grid(row=4, column=6, pady=1)
            btnAsinh = Button(calc, text="asinh", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="gray", command=added_value.asinh).grid(row=4, column=7, pady=1)

            btnLog10 = Button(calc, text='log10', width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log10).grid(row=5, column=4, pady=1)
            btnLog1p = Button(calc, text="log1p", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log1p).grid(row=5, column=5, pady=1)

            btnExpm1 = Button(calc, text="expm1", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.expm1).grid(row=5, column=6, pady=1)
            btnLgamma = Button(calc, text="lgamma", width=6, height=2, font=(
                'arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.lgamma).grid(row=5, column=7, pady=1)

            # ===============================Display Text======================================================================================================================================

            lblDisplay = Label(calc, text="Scientific Calculator", font=(
                'arial', 30, 'bold'), justify=CENTER)
            lblDisplay.grid(row=0, column=4, columnspan=4)

            lblDisplay = Label(calc, text="Do u r math babe", font=(
                'arial', 30, 'bold'), justify=CENTER)
            lblDisplay.grid(row=6, column=0, columnspan=4)

            # =======================Menu and function===========================================================

            def iExit():
                iExit = tkinter.messagebox.askyesno(
                    "Scientific Calculator", "Confirm if you want to exit")
                if iExit > 0:
                    root.destroy()
                    return

            def Scientific():
                root.resizable(width=False, height=False)
                root.geometry("944x624+20+20")

            def Standard():
                root.resizable(width=False, height=False)
                root.geometry("480x624+20+20")
            """
            def Volume():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Length():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")
                
            def W_M():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Temp():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Energy():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Area():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Speed():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Time():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Power():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Data():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Pressure():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")

            def Angle():
                root1.resizable(width=False, height=False)
                root1.geometry("944x624+20+20")
            """

            menubar = Menu(calc)

            filemenu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label="File", menu=filemenu)
            filemenu.add_command(label="Standadrd", command=Standard)
            filemenu.add_command(label="Scientific", command=Scientific)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=iExit)

            """
            conversionmenu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label = "Converter", menu=conversionmenu)
            conversionmenu.add_command(label = "Volume", command=Volume)
            conversionmenu.add_command(label = "Length", command=Length)
            conversionmenu.add_command(label = "Weight and Mass", command=W_M)
            conversionmenu.add_command(label = "Temperature", command=Temp)
            conversionmenu.add_command(label = "Energy", command=Energy)
            conversionmenu.add_command(label = "Area", command=Area)
            conversionmenu.add_command(label = "Speed", command=Speed)
            conversionmenu.add_command(label = "Time", command=Time)
            conversionmenu.add_command(label = "Power", command=Power)
            conversionmenu.add_command(label = "Data", command=Data)
            conversionmenu.add_command(label = "Pressure", command=Pressure)
            conversionmenu.add_command(label = "Angle", command=Angle)

            """

            """editmenu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label = "Edit", menu=editmenu)
            editmenu.add_command(label = "Cut")
            editmenu.add_command(label = "Copy")
            editmenu.add_separator()
            editmenu.add_command(label = "Paste")

            helpmenu = Menu(menubar, tearoff=0)
            menubar.add_cascade(label = "Help", menu=helpmenu)
            helpmenu.add_command(label = "View Help")
            """

            # ====================Main Loop=============================================================================

            root.config(menu=menubar)
            root.mainloop()

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to the group P S P G . further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\pranav\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif 'news' in query:

            import bs4
            from bs4 import BeautifulSoup as soup
            from urllib.request import urlopen

            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()

            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item")
            speak("here are some top news from google")
            # Print news title, url and publish date
            for news in news_list:
                print(news.title.text)
                print(news.link.text)
                print(news.pubDate.text)
                print("-"*60)

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "grouppspg Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('groupp.txt', 'w')

        elif "show note" in query:
            speak("Showing Notes")
            file = open("groupp.txt", "r")
            print(file.read())
            speak(file.read())

        elif "relax" in query:
            import turtle
            turtle.speed(0)
            turtle.bgcolor("black")
            for i in range(1000):
                for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
                    turtle.color(colours)
                    turtle.pensize(2)
                    turtle.left(12)
                    turtle.forward(200)
                    turtle.left(90)
                    turtle.forward(200)
                    turtle.left(90)
                    turtle.forward(200)
                    turtle.left(90)
                    turtle.forward(200)
                    turtle.left(90)

            turtle.done()

        elif "weather" in query:

            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            webbrowser.open("https://www.google.com/search?sxsrf=ALeKk01417bVqCLZLv0hmdYy-BGy8b1cgQ%3A1605794346999&ei=Knq2X7OxPOqC4-EPjrCq-A4&q=weather+" + city_name + "&oq=weather+" + city_name +
                            "&gs_lcp=CgZwc3ktYWIQAzIHCAAQFBCHAjICCAAyBggAEAcQHjIGCAAQBxAeMgIIADIGCAAQBxAeMgcIABAUEIcCMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgcIABBHELADOgcIIxDJAxAnOgYIABAWEB46BwgjEOoCECc6CggjELACECcQnQI6CAgAEAgQBxAeOggIABAHEAUQHlDw8-IBWPKn4wFg6LHjAWgCcAB4BIAB3QKIAZcOkgEHMC43LjEuMZgBAKABAaoBB2d3cy13aXqwAQrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwiz7omN4o7tAhVqwTgGHQ6YCu8Q4dUDCA0&uact=5")

        elif "translate" in query:
            speak("from language")
            print("from language")
            From_language = takeCommand()
            speak("to language")
            print("to language")
            to_language = takeCommand()
            speak("matter")
            print("matter")
            matter = takeCommand()
            webbrowser.open("https://www.google.com/search?sxsrf=ALeKk00yc6LD-mFUcT2ZF-HYfdrVSKVnxg%3A1605802390751&ei=lpm2X6e3LZCo9QOVtIP4DQ&q=translate+" + From_language + "+to+" + to_language + "+" + matter + "&oq=translate+" + From_language + "+to+" + to_language +
                            "+" + matter + "&gs_lcp=CgZwc3ktYWIQAzIJCAAQyQMQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoFCAAQyQM6AggAOgcIABAUEIcCUNHEHVjazh1gotgdaABwAHgAgAG8AYgB_QSSAQMwLjSYAQCgAQGqAQdnd3Mtd2l6yAEIuAECwAEB&sclient=psy-ab&ved=0ahUKEwin2tGIgI_tAhUQVH0KHRXaAN8Q4dUDCA0&uact=5")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(namee)

        elif "find ip" in query:
            import socket as s
            speak("tell the website name for the ip address")
            print("Tell the website name for the ip address")
            a = takeCommand()
            host = a
            print(f'ip of {host} is {s.gethostbyname(host)}')
            speak(f'ip of {host} is {s.gethostbyname(host)}')

        elif "will you be my gf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("I'll ditch u careful")

        elif "explore sky" in query:
            speak("have a nice space tour")
            print("have a nice space tour")
            webbrowser.open("https://www.google.co.in/sky/")

        elif "explore mars" in query:
            speak("have a nice mars tour")
            print("have a nice mars tour")
            webbrowser.open("https://www.google.co.in/mars/")

        elif "explore sun" in query:
            speak("have a nice sun tour")
            print("have a nice sun tour")
            webbrowser.open("https://www.google.co.in/sun/")

        elif "explore earth" in query:
            print("have a nice earth tour")
            speak("have a nice earth tour")
            webbrowser.open("https://www.google.com/intl/en_in/earth/")

        elif "explore moon" in query:
            print("have a nice moon tour")
            speak("have a nice moon tour")
            webbrowser.open("https://www.google.co.in/moon/")

        elif "a p o d" in query:
            print("enjoy the pic")
            speak("enjoy the pic")
            webbrowser.open("https://apod.nasa.gov/apod/astropix.html")

        elif "alarm" in query:
            import datetime

            alarm_hour = int(input("Set hour: "))
            alarm_minutes = int(input("Set minutes: "))
            am_pm = input("am or pm? ")

            print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

            if am_pm == 'pm' or 'Pm':
                alarm_hour += 12

            elif alarm_hour == 12 and am_pm == 'am':
                alarm_hour -= 12

            else:
                pass

            while True:

                if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

                    print("\nIt's the time!")
                    speak("alarm")
                    speak("alarm")
                    speak("alarm")
                    speak("alarm")
                    speak("alarm")
                    speak("alarm")
                    break
