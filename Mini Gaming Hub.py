import random
import time
import msvcrt  # works on Windows for instant key detection

# ---------- TIC TAC TOE GAME ----------
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def empty_positions(board):
    return [i for i, val in enumerate(board) if val == " "]

def player_move(board, player):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in range(9) and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Enter a valid number between 1-9.")

def computer_move(board, computer, player):
    print("Computer is thinking...")
    time.sleep(1)
    # Unbeatable logic (computer always wins)
    for move in empty_positions(board):
        board_copy = board[:]
        board_copy[move] = computer
        if check_winner(board_copy, computer):
            board[move] = computer
            return
    for move in empty_positions(board):
        board_copy = board[:]
        board_copy[move] = player
        if check_winner(board_copy, player):
            board[move] = computer
            return
    if board[4] == " ":
        board[4] = computer
        return
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        board[random.choice(corners)] = computer
        return
    sides = [i for i in [1,3,5,7] if board[i] == " "]
    if sides:
        board[random.choice(sides)] = computer
        return

def play_tic_tac_toe():
    board = [" "] * 9
    print("\n🎮 Welcome to Tic Tac Toe!")
    user = input("Choose your mark (X or O): ").upper()
    while user not in ["X", "O"]:
        user = input("Invalid choice. Choose 'X' or 'O': ").upper()
    computer = "O" if user == "X" else "X"
    print(f"You are '{user}' and Computer is '{computer}'\n")
    turn = "User"
    while True:
        print_board(board)
        if turn == "User":
            player_move(board, user)
            if check_winner(board, user):
                print_board(board)
                print("You won... oh wait, that’s not supposed to happen 😅")
                break
            turn = "Computer"
        else:
            computer_move(board, computer, user)
            if check_winner(board, computer):
                print_board(board)
                print("Computer wins! 😎")
                break
            turn = "User"
        if " " not in board:
            print_board(board)
            print("It's a draw (but how did you survive?) 😏")
            break


# ---------- STONE PAPER SCISSORS GAME ----------
def normalize_choice(choice):
    c = choice.lower().strip()
    if c.startswith("s") and not c.startswith("sc"):  # s, st, sto, stone
        return "stone"
    elif c.startswith("p"):  # p, pa, pap, pape, paper
        return "paper"
    elif c.startswith("sc"):  # sc, sci, scis, scissor
        return "scissors"
    else:
        return None

def play_stone_paper_scissors():
    print("\n✊🖐✌ Welcome to Stone Paper Scissors (3 Rounds)!")
    choices = ["stone", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    for round_no in range(1, 4):
        print(f"\n🕹️ Round {round_no} of 3")
        user_choice = None
        while not user_choice:
            raw = input("Choose Stone, Paper, or Scissors: ")
            user_choice = normalize_choice(raw)
            if not user_choice:
                print("Invalid input, try again (like 's', 'p', 'sc').")
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 😄")
            user_score += 1
        else:
            print("Computer wins this round! 😎")
            comp_score += 1
        print(f"\n🏆 SCOREBOARD after Round {round_no}")
        print(f"You: {user_score} | Computer: {comp_score}")
    print("\n=============================")
    print("🎯 FINAL RESULT:")
    if user_score > comp_score:
        print("You Win the Match! 🥳")
    elif comp_score > user_score:
        print("Computer Wins the Match! 🤖")
    else:
        print("It's a Draw Match! 😅")
    print("=============================")
    again = input("\nDo you want to play Stone Paper Scissors again? (y/n): ").lower()
    if again == "y":
        play_stone_paper_scissors()


# ---------- REACTION TIMER GAME ----------
def play_reaction_timer():
    print("\n⚡ Welcome to Reaction Timer Game!")
    print("Instructions:")
    print("Wait for the word 'GO!' to appear, then press any key as FAST as possible.")
    print("If you press before 'GO!' appears, you lose the round.")
    input("\nPress ENTER to start...")

    delay = random.uniform(2, 5)
    print("\nGet Ready...")
    time.sleep(delay)

    print("GO! ⏱️")
    start_time = time.time()
    while not msvcrt.kbhit():
        pass
    msvcrt.getch()  # capture the key press
    reaction_time = time.time() - start_time
    print(f"\nYour reaction time: {reaction_time:.3f} seconds")

    if reaction_time < 0.2:
        print("⚡ Lightning fast! Incredible reflexes!")
    elif reaction_time < 0.4:
        print("🔥 Great job! You’re quick!")
    elif reaction_time < 0.6:
        print("🙂 Decent reaction time.")
    else:
        print("🐢 Bit slow... Try again to beat your score!")

    again = input("\nDo you want to play the Reaction Timer again? (y/n): ").lower()
    if again == "y":
        play_reaction_timer()


# ---------- MAIN MENU ----------
def main_menu():
    while True:
        print("\n---------------------------------")
        print("🎮  Choose your game:")
        print("1️⃣  Tic Tac Toe")
        print("2️⃣  Stone Paper Scissors")
        print("3️⃣  Reaction Timer Game")
        print("4️⃣  Quit")
        print("---------------------------------")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            play_tic_tac_toe()
        elif choice == "2":
            play_stone_paper_scissors()
        elif choice == "3":
            play_reaction_timer()
        elif choice == "4":
            print("Thanks for playing! Goodbye 👋")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# ---------- START PROGRAM ----------
if __name__ == "__main__":
    print("✨ Welcome to Sangam’s Mini Game Hub ✨")
    main_menu()
