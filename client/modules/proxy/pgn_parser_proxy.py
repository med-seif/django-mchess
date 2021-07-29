from pgn_parser import parser, pgn
import re

pieces = ['R', 'N', 'Q', 'K', 'B']

def parse(data: str):
    result = parser.parse(data, actions=pgn.Actions())
    formatted_game_moves = []

    def get_move_color(move):
        if str(move.white):
            return 'white'
        return 'black'

    def get_piece(move):
        san = get_san(move)
        if san in ['O-O', 'O-O-O']:
            return 'c'
        first_letter = san[0]
        if first_letter in pieces:
            return first_letter
        return 'P'

    def get_clk(move):
        comment = move.__getattribute__(get_move_color(move)).comment
        finds = re.findall(r"(\d+:\d+:\d+(\.\d+)?)", comment)
        return finds[0][0]

    def get_san(move):
        return move.__getattribute__(get_move_color(move)).san

    def get_number(move):
        return move.move_number

    def get_is_take(move):
        if 'x' in get_san(move):
            return 1
        return 0

    def get_is_check(move):
        if '+' in get_san(move):
            return 1
        return 0

    def get_is_checkmate(move):
        if '#' in get_san(move):
            return 1
        return 0

    for m in result.movetext:
        formatted_game_moves.append({
            'move': str(m),
            'color': get_move_color(m)[0],
            'piece': get_piece(m),
            'clk': get_clk(m),
            'number': get_number(m),
            'san': get_san(m),
            'is_take': get_is_take(m),
            'is_check': get_is_check(m),
            'is_checkmate': get_is_checkmate(m),
        })
    result.formatted_moves = formatted_game_moves
    return result


#parse("[Event \"Live Chess\"]\n[Site \"Chess.com\"]\n[Date \"2021.07.04\"]\n[Round \"-\"]\n[White \"Seiftn\"]\n[Black \"elizabethlonehvid\"]\n[Result \"0-1\"]\n[CurrentPosition \"3r3k/1pQ5/p3R1pb/4p1qp/5r2/5B2/PPP2P1P/1K2R3 w - -\"]\n[Timezone \"UTC\"]\n[ECO \"B21\"]\n[ECOUrl \"https://www.chess.com/openings/Sicilian-Defense-Smith-Morra-Gambit-2...cxd4-3.Qxd4-Nc6\"]\n[UTCDate \"2021.07.04\"]\n[UTCTime \"20:29:24\"]\n[WhiteElo \"973\"]\n[BlackElo \"998\"]\n[TimeControl \"600\"]\n[Termination \"elizabethlonehvid won on time\"]\n[StartTime \"20:29:24\"]\n[EndDate \"2021.07.04\"]\n[EndTime \"20:45:00\"]\n[Link \"https://www.chess.com/game/live/19169727355\"]\n\n1. e4 {[%clk 0:10:00]} 1... c5 {[%clk 0:09:58.7]} 2. d4 {[%clk 0:09:58.3]} 2... cxd4 {[%clk 0:09:57.1]} 3. Qxd4 {[%clk 0:09:49.3]} 3... Nc6 {[%clk 0:09:56]} 4. Qd3 {[%clk 0:09:37.5]} 4... e6 {[%clk 0:09:44.4]} 5. Nf3 {[%clk 0:09:20.4]} 5... g6 {[%clk 0:09:42]} 6. e5 {[%clk 0:08:36.3]} 6... Bg7 {[%clk 0:09:39.4]} 7. Bf4 {[%clk 0:08:18.4]} 7... Nge7 {[%clk 0:09:36.2]} 8. Nc3 {[%clk 0:08:00.8]} 8... O-O {[%clk 0:09:25.9]} 9. O-O-O {[%clk 0:07:57.7]} 9... a6 {[%clk 0:09:21.8]} 10. Ng5 {[%clk 0:07:39.1]} 10... Nxe5 {[%clk 0:08:57.1]} 11. Bxe5 {[%clk 0:07:33.6]} 11... Bxe5 {[%clk 0:08:55.3]} 12. Qe3+ {[%clk 0:07:05.8]} 12... Bg7# {[%clk 0:08:43.7]} 13. Qh3 {[%clk 0:06:40.3]} 13... h5 {[%clk 0:08:37.5]} 14. g4 {[%clk 0:06:31]} 14... Bh6 {[%clk 0:08:03.1]} 15. Qh4 {[%clk 0:05:50.9]} 15... f6 {[%clk 0:07:44.6]} 16. Ne4 {[%clk 0:05:12.4]} 16... fxg5 {[%clk 0:07:20.8]} 17. Nxg5 {[%clk 0:05:02.7]} 17... Kg7 {[%clk 0:07:11.1]} 18. Kb1 {[%clk 0:04:42.5]} 18... Nd5 {[%clk 0:06:52.6]} 19. Bc4 {[%clk 0:03:46.3]} 19... Qxg5 {[%clk 0:06:48.6]} 20. Qg3 {[%clk 0:03:01]} 20... Rf4 {[%clk 0:06:03.2]} 21. Bxd5 {[%clk 0:02:15.8]} 21... Rxg4 {[%clk 0:05:54.7]} 22. Qc3+ {[%clk 0:02:08.5]} 22... e5 {[%clk 0:05:41.2]} 23. Rhe1 {[%clk 0:01:22.8]} 23... d6 {[%clk 0:05:38.2]} 24. Bf3 {[%clk 0:01:02]} 24... Rf4 {[%clk 0:05:16.5]} 25. Rxd6 {[%clk 0:00:33.1]} 25... Be6 {[%clk 0:05:02.1]} 26. Rxe6 {[%clk 0:00:18.9]} 26... Rd8 {[%clk 0:04:45.4]} 27. Qc7+ {[%clk 0:00:11.9]} 27... Kh8 {[%clk 0:04:38.2]} 0-1\n")
