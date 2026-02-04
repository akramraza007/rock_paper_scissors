import random
import time

def play_rps():
    item_list = ["Rock", "Paper", "Scissor"]
    win_map = {"Rock": "Scissor", "Paper": "Rock", "Scissor": "Paper"}
    
    user_score = 0
    comp_score = 0
    tie_score = 0

    print("\n🎮 Welcome to Rock, Paper, Scissor Pro!")
    
    while True:
        print("\n--- MENU ---")
        print("1. Play a Round 🕹️")
        print("2. View Scores 📊")
        print("3. Reset Scores 🔄")
        print("4. Exit 🚪")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            user_move = input("Enter Rock, Paper, or Scissor: ").strip().capitalize()
            
            if user_move not in item_list:
                print("❌ Invalid move! Please check your spelling.")
                continue

            comp_move = random.choice(item_list)
            
            print("🤖 Computer is thinking...")
            time.sleep(0.8)
            print(f"Result: {user_move} vs {comp_move}")

            if user_move == comp_move:
                print("🤝 It's a Tie!")
                tie_score += 1
            elif win_map[user_move] == comp_move:
                print(f"🎉 You Win! {user_move} beats {comp_move}.")
                user_score += 1
            else:
                print(f"💀 Computer Wins! {comp_move} beats {user_move}.")
                comp_score += 1

        elif choice == '2':
            print(f"\n🏆 --- SCOREBOARD ---")
            print(f"👤 User Score: {user_score}")
            print(f"🤖 Comp Score: {comp_score}")
            print(f"🤝 Ties: {tie_score}")
            print("---------------------")

        elif choice == '3':
            user_score = comp_score = tie_score = 0
            print("✨ Scores cleared successfully!")

        elif choice == '4':
            confirm = input("Are you sure you want to exit the game? (y/n): ").lower()
            if confirm == 'y':
                print("Thanks for playing the game...👋")
                break
        else:
            print("❌ Invalid selection. Please choose 1, 2, 3, or 4.")
play_rps()