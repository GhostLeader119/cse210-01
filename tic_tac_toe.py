def game_center():
    #main control function
    def player_select():
        player_1 = input('PLayer one\nEnter your name: ')
        player_2 = input('\nPLayer two\nEnter your name: ')
        print(f'Welcome {player_1}, {player_2}')
        return player_1,player_2

    def game_setup():
        #Initilizes game board
        #[A1] [A2] [A3]
        #[B1] [B2] [B3]
        #[C1] [C2] [C3]
        game_board = {}
        options = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        for items in options:
            game_board[items] = items
        return game_board

    def run_game(game_board,player_1,player_2):

        def game_display(data):
            #game_board = dictionary lines, sub_dictionaries
            print()
            boxes = []
            count = 0

            for line in data:
                offer = data[line]

                boxes.append(offer)

                count += 1
                if count == 3:
                    print('[' + boxes[0] + ']' + '[' + boxes[1] + ']' + '[' + boxes[2] + ']')
                    boxes = []
                    count = 0
            print()
            return

        def victory_check(game_board):
            #[A1] [A2] [A3]
            #[B1] [B2] [B3]
            #[C1] [C2] [C3]
            A1 = game_board['A1']
            A2 = game_board['A2']
            A3 = game_board['A3']
            B1 = game_board['B1']
            B2 = game_board['B2']
            B3 = game_board['B3']
            C1 = game_board['C1']
            C2 = game_board['C2']
            C3 = game_board['C3']
            if A1 == B2 and B2 == C3:
                victory = A1
                status = False
            elif A3 == B2 and B2 == C1:
                victory = A3
                status = False
            elif A1 == A2 and A2 == A3:
                victory = A1
                status = False
            elif B1 == B2 and B2 == B3:
                victory = B1
                status = False
            elif C1 == C2 and C2 == C3:
                victory = C1
                status = False
            elif A1 == B1 and B1 == C1:
                victory = A1
                status = False
            elif A2 == B2 and B2 == C2:
                victory = A2
                status = False
            elif A3 == B3 and B3 == C3:
                victory = A3
                status = False
            else:
                victory = 'N'
                status = True
            return status,victory

        status = True
        victory = 'N'
        tic = 0
        while status:

            
            game_display(game_board)

            while True:
                option = input(f'[x] {player_1} choose a tile: ')

                if option in game_board:
                    game_board[option] = 'X'
                    tic += 1
                    break
                else:
                    print('Enter valid entry\n')
            
            game_display(game_board)
            status,victory = victory_check(game_board)
            if tic == 9:
                return victory
            elif victory != 'N':
                return victory
            
            while True:
                option = input(f'[O] {player_2} choose a tile: ')
                if option in game_board:
                    game_board[option] = 'O'
                    tic += 1
                    break
                else:
                    print('Enter valid entry\n')

            status,victory = victory_check(game_board)
            if tic == 9:
                return victory
            elif victory != 'N':
                return victory

        return victory


    Status = True    
    while Status:
        game_board = game_setup()
        print('Welcome to Tic-Tac-Toe please enter the names of both players:\n')
        player_1,player_2 = player_select()
        victory = run_game(game_board,player_1,player_2)
        if victory == 'N':
            print('\nGame draw!\n')
        elif victory == 'X':
            print(f'\n{player_1} wins!\n')
        elif victory == 'O':
            print(f'\n{player_2} wins!\n')
        
        while True:
            try:
                select = input('Would you like to play again? Y/N ').upper()
                if select == 'N' or select == 'NO':
                    Status = False
                    break
                elif select == 'Y' or select == 'YES':
                    Status = True
                    break
                else:
                    print('Enter a valid input.')
            except ValueError:
                print('Invalid input cought by error catcher...')

game_center()